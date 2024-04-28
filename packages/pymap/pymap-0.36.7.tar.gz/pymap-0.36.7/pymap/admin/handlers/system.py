
from __future__ import annotations

from datetime import datetime
from typing import TypeAlias

from grpclib.server import Stream
from pymap.__about__ import __version__ as pymap_version
from pymapadmin.__about__ import __version__ as pymap_admin_version
from pymapadmin.grpc.admin_grpc import SystemBase
from pymapadmin.grpc.admin_pb2 import LoginRequest, LoginResponse, \
    PingRequest, PingResponse
from pysasl.creds.plain import PlainCredentials

from . import BaseHandler

__all__ = ['SystemHandlers']

_LoginStream: TypeAlias = Stream[LoginRequest, LoginResponse]
_PingStream: TypeAlias = Stream[PingRequest, PingResponse]


class SystemHandlers(SystemBase, BaseHandler):
    """The GRPC handlers, executed when an admin request is received. Each
    handler should receive a request, take action, and send the response.

    See Also:
        :class:`grpclib.server.Server`

    """

    async def Login(self, stream: _LoginStream) -> None:
        """Response to a login request. For example::

            $ pymap-admin login

        See ``pymap-admin login --help`` for more options.

        Args:
            stream (:class:`~grpclib.server.Stream`): The stream for the
                request and response.

        """
        request = await stream.recv_message()
        assert request is not None
        bearer_token: str | None = None
        credentials: PlainCredentials | None = None
        if not request.HasField('secret'):
            login_context = self.login_as(stream.metadata, request.authcid)
        else:
            credentials = PlainCredentials(
                request.authcid, request.secret, request.authzid)
            login_context = self.login_with(credentials)
        async with self.catch_errors('Login') as result, \
                login_context as identity:
            expiration: datetime | None = None
            if request.HasField('token_expiration'):
                expiration = datetime.fromtimestamp(request.token_expiration)
            bearer_token = await identity.new_token(expiration=expiration)
        resp = LoginResponse(result=result)
        if bearer_token is not None:
            resp.bearer_token = bearer_token
        await stream.send_message(resp)

    async def Ping(self, stream: _PingStream) -> None:
        """Respond to a ping request. For example::

            $ pymap-admin ping

        See ``pymap-admin ping --help`` for more options.

        Args:
            stream (:class:`~grpclib.server.Stream`): The stream for the
                request and response.

        """
        request = await stream.recv_message()
        assert request is not None
        resp = PingResponse(pymap_version=pymap_version,
                            pymap_admin_version=pymap_admin_version)
        await stream.send_message(resp)
        assert request is not None
