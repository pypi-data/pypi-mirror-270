import pulumi_aws as aws

from paka.config import CloudConfig
from paka.utils import call_once, save_cluster_data


@call_once
def create_container_registry(config: CloudConfig) -> None:
    """
    Create a container registry in AWS ECR for storing Docker images.

    Args:
        config (CloudConfig): The configuration object containing cluster information.

    Returns:
        None
    """
    project = config.cluster.name
    repository = aws.ecr.Repository(
        project,
        force_delete=True,
        image_tag_mutability="MUTABLE",
    )

    # Save the repository URL to the cluster data file
    repository.repository_url.apply(
        lambda url: save_cluster_data(project, "registry", url)
    )
