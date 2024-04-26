from typing import List, Optional
from launchflow.service import Service


class CloudRun(Service):

    def __init__(
        self,
        name: str,
        dockerfile: str = "Dockerfile",
        build_directory: str = ".",
        build_ignore: List[str] = [],
        region: Optional[str] = None,
        cpu: Optional[int] = None,
        memory: Optional[str] = None,
        port: Optional[int] = None,
        publicly_accessible: bool = True,
        min_instance_count: Optional[int] = None,
        max_instance_count: Optional[int] = None,
        max_instance_request_concurrency: Optional[int] = None,
        invokers: Optional[List[str]] = None,
    ) -> None:
        super().__init__(
            name=name,
            dockerfile=dockerfile,
            product_name="gcp_cloud_run",
            build_directory=build_directory,
            build_ignore=build_ignore,
            create_args={
                "region": region,
                "cpu": cpu,
                "memory": memory,
                "port": port,
                "publicly_accessible": publicly_accessible,
                "min_instance_count": min_instance_count,
                "max_instance_count": max_instance_count,
                "max_instance_request_concurrency": max_instance_request_concurrency,
                "invokers": ",".join(invokers) if invokers else None,
            },
        )
