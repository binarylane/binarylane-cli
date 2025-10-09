from __future__ import annotations

from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.types import Unset

from binarylane.console.commands.api import post_v2_servers

if TYPE_CHECKING:
    from http import HTTPStatus

    from binarylane.client import Client
    from binarylane.models.create_server_response import CreateServerResponse
    from binarylane.models.validation_problem_details import ValidationProblemDetails


class Command(post_v2_servers.Command):
    """Server create command with preference defaults

    This wraps the auto-generated server create command to inject
    user-configured default values from preferences.
    """

    def run(self, args: List[str]) -> None:
        """Override run to inject config defaults into args before parsing"""
        if args == [self.CHECK]:
            return super().run(args)

        # Inject CLI defaults for required parameters
        ctx = self._context
        modified_args = list(args)

        if "--size" not in modified_args and ctx.default_size:
            modified_args.extend(["--size", ctx.default_size])
        if "--image" not in modified_args and ctx.default_image:
            modified_args.extend(["--image", str(ctx.default_image)])
        if "--region" not in modified_args and ctx.default_region:
            modified_args.extend(["--region", ctx.default_region])

        super().run(modified_args)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, CreateServerResponse, ValidationProblemDetails]]:
        """Override request to inject config defaults for optional parameters"""
        # First, inject defaults into request body
        body = request.json_body  # type: ignore[attr-defined]
        ctx = self._context

        # Optional parameters with config defaults
        if isinstance(getattr(body, "backups", Unset), type(Unset)):
            if ctx.default_backups is not None:
                body.backups = ctx.default_backups

        if isinstance(getattr(body, "ssh_keys", Unset), type(Unset)):
            if ctx.default_ssh_keys:
                body.ssh_keys = [key.strip() for key in ctx.default_ssh_keys.split(",")]

        if isinstance(getattr(body, "user_data", Unset), type(Unset)):
            if ctx.default_user_data:
                body.user_data = ctx.default_user_data

        if isinstance(getattr(body, "port_blocking", Unset), type(Unset)):
            if ctx.default_port_blocking is not None:
                body.port_blocking = ctx.default_port_blocking

        if isinstance(getattr(body, "password", Unset), type(Unset)):
            if ctx.default_password:
                body.password = ctx.default_password

        if isinstance(getattr(body, "vpc_id", Unset), type(Unset)):
            if ctx.default_vpc:
                try:
                    body.vpc_id = int(ctx.default_vpc)
                except ValueError:
                    pass  # Let lookup mechanism handle it

        # Now call parent's request with modified body
        return super().request(client, request)
