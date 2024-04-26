from launchflow.context import ctx
from typing import Any, Dict, Optional, List


class Service:

    def __init__(
        self,
        name: str,
        product_name: str,
        create_args: Dict[str, Any],
        dockerfile: str = "Dockerfile",
        build_directory: str = ".",
        build_ignore: List[str] = [],  # type: ignore
    ) -> None:
        self.name = name
        self._product_name = product_name
        self._create_args = create_args
        self._dockerfile = dockerfile
        self._build_directory = build_directory
        self._build_ignore = build_ignore

    async def deploy_async(
        self,
        *,
        project_name: Optional[str] = None,
        environment_name: Optional[str] = None
    ):
        return await ctx.deploy_service_operation_async(
            service_type=self.__class__.__name__,
            product_name=self._product_name,
            create_args=self._create_args,
            dockerfile_path=self._dockerfile,
            build_directory=self._build_directory,
            build_ignore=self._build_ignore,
            service_name=self.name,
            environment_name=environment_name,
            project_name=project_name,
        )

    # TODO: add an sync version of deploy
