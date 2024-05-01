from __future__ import annotations

from functools import cached_property
from typing import Any, final

import grpc
import grpc.experimental

from chalk import EnvironmentId
from chalk._gen.chalk.auth.v1.agent_pb2 import CustomClaim
from chalk._gen.chalk.auth.v1.permissions_pb2 import Permission
from chalk._gen.chalk.engine.v1.query_server_pb2_grpc import QueryServiceStub
from chalk._gen.chalk.server.v1.auth_pb2_grpc import AuthServiceStub
from chalk._gen.chalk.server.v1.team_pb2 import CreateServiceTokenRequest, CreateServiceTokenResponse
from chalk._gen.chalk.server.v1.team_pb2_grpc import TeamServiceStub
from chalk.client import ChalkAuthException
from chalk.config.auth_config import load_token
from chalk.utils.grpc import AuthenticatedChalkClientInterceptor, TokenRefresher, UnauthenticatedChalkClientInterceptor


@final
class ChalkGRPCClient:
    def __init__(
        self,
        environment_id: EnvironmentId | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        api_server: str | None = None,
        additional_headers: list[tuple[str, str]] | None = None,
    ):
        additional_headers_nonempty: list[tuple[str, str]] = [] if additional_headers is None else additional_headers
        token_config = load_token(
            client_id=client_id,
            client_secret=client_secret,
            active_environment=environment_id,
            api_server=api_server,
            skip_cache=False,
        )
        if token_config is None:
            raise ChalkAuthException()

        server_host: str = (
            (token_config.apiServer or "api.chalk.ai")
            .removeprefix("https://")
            .removeprefix("http://")
            .removeprefix("www.")
        )

        channel_options: list[tuple[str, str | int]] = [
            ("grpc.max_send_message_length", 1024 * 1024 * 100),  # 100MB
            ("grpc.max_receive_message_length", 1024 * 1024 * 100),  # 100MB
            # https://grpc.io/docs/guides/performance/#python
            (grpc.experimental.ChannelOptions.SingleThreadedUnaryStream, 1),
        ]
        _unauthenticated_server_channel: grpc.Channel = (
            grpc.insecure_channel(
                target=server_host,
                options=channel_options,
            )
            if server_host.startswith("localhost") or server_host.startswith("127.0.0.1")
            else grpc.secure_channel(
                target=server_host,
                credentials=grpc.ssl_channel_credentials(),
                options=channel_options,
            )
        )

        self._auth_stub: AuthServiceStub = AuthServiceStub(
            grpc.intercept_channel(
                _unauthenticated_server_channel,
                UnauthenticatedChalkClientInterceptor(
                    server="go-api",
                    additional_headers=additional_headers_nonempty,
                ),
            )
        )

        token_refresher: TokenRefresher = TokenRefresher(
            auth_stub=self._auth_stub,
            client_id=token_config.clientId,
            client_secret=token_config.clientSecret,
        )

        t = token_refresher.get_token()

        self._environment_id = token_config.activeEnvironment or t.primary_environment
        if self._environment_id is None or self._environment_id == "":
            raise ValueError("No environment specified")

        if self._environment_id not in t.environment_id_to_name:
            lower_env_id = self._environment_id.lower()
            valid = [eid for eid, ename in t.environment_id_to_name.items() if ename.lower() == lower_env_id]
            if len(valid) > 1:
                raise ValueError(f"Multiple environments with name {self._environment_id}: {valid}")
            elif len(valid) == 0:
                raise ValueError(f"No environment with name {self._environment_id}: {t.environment_id_to_name}")
            else:
                self._environment_id = valid[0]

        self._server_channel: grpc.Channel = grpc.intercept_channel(
            _unauthenticated_server_channel,
            AuthenticatedChalkClientInterceptor(
                refresher=token_refresher,
                server="go-api",
                environment_id=self._environment_id,
                additional_headers=additional_headers_nonempty,
            ),
        )

        grpc_url = t.grpc_engines.get(self._environment_id, None)
        self._engine_channel: grpc.Channel | None = (
            None
            if grpc_url is None
            else (
                grpc.intercept_channel(
                    grpc.insecure_channel(
                        target=grpc_url,
                        options=channel_options,
                    )
                    if grpc_url.startswith("localhost") or grpc_url.startswith("127.0.0.1")
                    else grpc.secure_channel(
                        target=grpc_url,
                        credentials=grpc.ssl_channel_credentials(),
                        options=channel_options,
                    ),
                    AuthenticatedChalkClientInterceptor(
                        refresher=token_refresher,
                        environment_id=self._environment_id,
                        server="engine",
                        additional_headers=additional_headers_nonempty,
                    ),
                )
            )
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        self._server_channel.close()
        if self._engine_channel is not None:
            self._engine_channel.close()

    @cached_property
    def _team_stub(self):
        return TeamServiceStub(self._server_channel)

    @cached_property
    def _query_stub(self):
        if self._engine_channel is None:
            raise ValueError(f"No engine channel available for environment {self._environment_id}")
        return QueryServiceStub(self._engine_channel)

    # def online_query(
    #     self,
    #     query: str,
    # ) -> Any:
    #     return self._query_stub.OnlineQueryFeather(
    #         OnlineQueryFeatherRequest(
    #             inputs_feather=None,
    #             body_type=FEATHER_BODY_TYPE_RECORD_BATCHES,
    #         ),
    #     )

    def create_service_token(
        self,
        name: str,
        permissions: list[Permission],
        customer_claims: dict[str, list[str]] | None = None,
    ) -> CreateServiceTokenResponse:
        """Create a service token with a given set of permissions and claims.

        Parameters
        ----------
        name
            The name of your service token.
        permissions
            The permissions that you want your token to have.
        customer_claims
            The customer claims that you want your token to have.
        Returns
        -------
        CreateServiceTokenResponse
            A service token response, including a `client_id` and `client_secret` with
            the specified permissions and customer claims.

        Examples
        --------
        >>> from chalk.client import Permission
        >>> client = ChalkGRPCClient(client_id='test', client_secret='test_secret')
        >>> client.create_service_token(permissions=[Permission.PERMISSION_QUERY_ONLINE])
        """
        return self._team_stub.CreateServiceToken(
            CreateServiceTokenRequest(
                name=name,
                permissions=permissions,
                customer_claims=None
                if customer_claims is None
                else [CustomClaim(key=key, values=values) for key, values in customer_claims.items()],
            )
        )
