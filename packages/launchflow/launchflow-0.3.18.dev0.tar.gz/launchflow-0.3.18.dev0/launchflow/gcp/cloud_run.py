from typing import List, Literal, Optional

from launchflow.service import Service


class CloudRun(Service):
    """A service hosted on GCP Cloud Run.

    **Example usage:**
    ```python
    import launchflow as lf

    service = lf.gcp.CloudRun("my-service", cpu=4)
    ```
    """

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
        custom_audiences: Optional[List[str]] = None,
        ingress: Optional[
            Literal[
                "INGRESS_TRAFFIC_ALL",
                "INGRESS_TRAFFIC_INTERNAL_ONLY",
                "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER",
            ]
        ] = None,
    ) -> None:
        """Creates a new Cloud Run service.

        **Args:**
        - `name` (str): The name of the service.
        - `build_directory` (str): The directory to build the service from. This should be a relative path from the project root where your `launchflow.yaml` is defined.
        - `dockerfile` (str): The Dockerfile to use for building the service. This should be a relative path from the `build_directory`.
        - `build_ignore` (List[str]): A list of files to ignore when building the service. This can be in the same syntax you would use for a `.gitignore`.
        - `region` (Optional[str]): The region to deploy the service to.
        - `cpu` (Optional[int]): The number of CPUs to allocate to each instance of the service.
        - `memory` (Optional[str]): The amount of memory to allocate to each instance of the service.
        - `port` (Optional[int]): The port the service listens on.
        - `publicly_accessible` (bool): Whether the service is publicly accessible. Defaults to True.
        - `min_instance_count` (Optional[int]): The minimum number of instances to keep running.
        - `max_instance_count` (Optional[int]): The maximum number of instances to run.
        - `max_instance_request_concurrency` (Optional[int]): The maximum number of requests each instance can handle concurrently.
        - `invokers` (Optional[List[str]]): A list of invokers that can access the service.
        - `custom_audiences`: (Optional[List[str]]): A list of custom audiences that can access the service. See: https://cloud.google.com/run/docs/configuring/custom-audiences
        - `ingress` (Optional[Literal["INGRESS_TRAFFIC_ALL", "INGRESS_TRAFFIC_INTERNAL_ONLY", "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER"]]): The ingress settings for the service. See: https://cloud.google.com/run/docs/securing/ingress
        """
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
                "custom_audiences": (
                    ",".join(custom_audiences) if custom_audiences else None
                ),
                "ingress": ingress,
            },
        )
