from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, field_validator, model_validator
from ruamel.yaml import YAML

from paka.utils import to_yaml


def validate_size(v: str, error_message: str = "Invalid size format") -> str:
    """
    Validates the format of the size field.

    Args:
        v (str): The value of the size field.
        error_message (str, optional): The error message to raise if the format of the input value is invalid. Defaults to "Invalid size format".

    Returns:
        str: The input value if validation is successful.

    Raises:
        ValueError: If the format of the input value is invalid. The error message is specified by the `error_message` parameter.
    """
    if not re.match(r"^\d+(Mi|Gi)$", v):
        raise ValueError(error_message)
    return v


class ResourceRequest(BaseModel):
    """
    Represents the resource request for a container.

    Attributes:
        cpu (str): The amount of CPU to request.
        memory (str): The amount of memory to request.
        gpu (Optional[int]): The number of GPUs to request. Defaults to None.
    """

    cpu: str
    memory: str
    gpu: Optional[int] = None

    @field_validator("cpu", mode="before")
    def validate_cpu(cls, v: str) -> str:
        """
        Validates the format of the cpu field.

        Args:
            v (str): The value of the cpu field.

        Returns:
            str: The input value if validation is successful.

        Raises:
            ValueError: If the format of the input value is invalid.
        """
        if not re.match(r"^\d+(m)?$", v):
            raise ValueError("Invalid CPU format")
        return v

    @field_validator("memory", mode="before")
    def validate_memory(cls, v: str) -> str:
        """
        Validates the format of the memory field.

        Args:
            v (str): The value of the memory field.

        Returns:
            str: The input value if validation is successful.

        Raises:
            ValueError: If the format of the input value is invalid.
        """
        return validate_size(v, "Invalid memory format")

    @field_validator("gpu")
    def validate_gpu(cls, v: Optional[int]) -> Optional[int]:
        """
        Validates the value of the gpu field.

        Args:
            v (Optional[int]): The value of the gpu field.

        Returns:
            Optional[int]: The input value if validation is successful.

        Raises:
            ValueError: If the value is less than 0.
        """
        if v is not None and v < 0:
            raise ValueError("GPU count cannot be less than 0")
        return v


class AwsGpuNode(BaseModel):
    """
    Represents a configuration for an AWS GPU node.

    Attributes:
        diskSize (int): The size of the disk for the GPU node in GB.
    """

    diskSize: int


class GcpGpuNode(BaseModel):
    """
    Represents a Google Cloud Platform GPU node.

    Attributes:
        imageType (str): The type of image used for the GPU node.
        acceleratorType (str): The type of accelerator used for the GPU node.
        acceleratorCount (int): The number of accelerators attached to the GPU node.
        diskType (str): The type of disk used for the GPU node.
        diskSize (int): The size of the disk attached to the GPU node in GB.
    """

    imageType: str
    acceleratorType: str
    acceleratorCount: int
    diskType: str
    diskSize: int


class CloudNode(BaseModel):
    """
    Represents a node in the cloud cluster.

    Attributes:
        nodeType (str): The type of the node.
        diskSize (int): The size of the disk attached to the node in GB.
        awsGpu (Optional[AwsGpuNode]): The AWS GPU node configuration, if applicable.
        gcpGpu (Optional[GcpGpuNode]): The GCP GPU node configuration, if applicable.
    """

    nodeType: str
    diskSize: int = 20
    awsGpu: Optional[AwsGpuNode] = None
    gcpGpu: Optional[GcpGpuNode] = None

    @model_validator(mode="before")
    def validate_gpu(
        cls, values: Dict[str, Union[AwsGpuNode, GcpGpuNode]]
    ) -> Dict[str, Union[AwsGpuNode, GcpGpuNode]]:
        if values.get("awsGpu") and values.get("gcpGpu"):
            raise ValueError("At most one of awsGpu or gcpGpu can exist")
        return values


class Runtime(BaseModel):
    """
    Represents a runtime for a model.

    Attributes:
        image (str): The Docker image to use for the runtime.
        command (List[str], optional): The command to run in the Docker container.
    """

    image: str
    command: Optional[List[str]] = None


class Model(BaseModel):
    """
    Represents a model.

    Attributes:
        hfRepoId (str, optional): The HuggingFace repository ID for the model.
        files (List[str], optional): The list of files to include from the repository. Defaults to all files ("*").
        useModelStore (bool, optional): Whether to save the model to a model store, such as s3. Defaults to True.
    """

    hfRepoId: Optional[str] = None
    files: List[str] = ["*"]

    useModelStore: bool = True


class ModelGroup(BaseModel):
    """
    Represents a group of VMs that serve the inference for a specific type of model.

    Attributes:
        name (str): The name of the model group.
        minInstances (int): The minimum number of instances to provision.
        maxInstances (int): The maximum number of instances to provision.
        model (Optional[Model]): The model to deploy in the model group. If None, runtime image is responsible for loading the model.
        runtime (Runtime): The runtime for the model group.
    """

    name: str
    minInstances: int
    maxInstances: int

    model: Optional[Model] = None
    runtime: Runtime

    @model_validator(mode="before")
    def check_instances_num(cls, values: Dict[str, int]) -> Dict[str, int]:
        min_instances, max_instances = values.get("minInstances"), values.get(
            "maxInstances"
        )
        if min_instances and max_instances and max_instances < min_instances:
            raise ValueError(
                "maxInstances must be greater than or equal to minInstances"
            )
        return values

    @field_validator("minInstances", mode="before")
    def validate_min_instances(cls, v: int) -> int:
        """
        Validates the value of the minInstances field. Spinning up 1 model group instance is heavy.
        No scaling down to 0 for now.

        Args:
            v (int): The value of the minInstances field.

        Returns:
            int: The input value if validation is successful.

        Raises:
            ValueError: If the value of the input value is invalid.
        """
        if v <= 0:
            raise ValueError("minInstances must be greater than 0")
        return v


class Trigger(BaseModel):
    type: str
    metadata: Dict[str, str]


class CloudModelGroup(ModelGroup, CloudNode):
    """
    Represents a group of cloud models.

    This class inherits from both the `ModelGroup` and `CloudNode` classes.

    Attributes:
        resourceRequest (Optional[ResourceRequest]): The resource request for the model group, specifying the amount of CPU and memory to request.

    Inherited Attributes:
        name (str): The name of the model group.
        minInstances (int): The minimum number of instances to provision for the model group.
        maxInstances (int): The maximum number of instances to provision for the model group.
        nodeType (str): The type of the node.
    """

    # TODO: make required for HPA to work
    resourceRequest: Optional[ResourceRequest] = None

    autoScaleTriggers: Optional[List[Trigger]] = None
    """
    Triggers for autoscaling the model group. Trigger are not strongly typed, so we use a list of dictionaries to represent them.
    For example:

    autoScaleTriggers=[
        # CPU trigger example
        Trigger(
            type="cpu",
            metadata={
                "type": "Utilization",
                "value": "70"
            }
        ),
        # Prometheus trigger example
        Trigger(
            type="prometheus",
            metadata={
                "serverAddress": "http://prometheus-operated.default.svc.cluster.local",
                "metricName": "http_requests_total",
                "threshold": "100",
                "query": "sum(rate(http_requests_total{job=\"example-job\"}[2m]))"
            }
        )
    ]
    """


class ClusterConfig(BaseModel):
    """
    Represents the configuration for a cluster.

    Attributes:
        name (str): The name of the cluster.
        region (str): The default region for the cluster.
        namespace (str, optional): The namespace in which the cluster is deployed. Defaults to 'default'.
        nodeType (str): The type of nodes in the cluster.
        minNodes (int): The minimum number of nodes in the cluster.
        maxNodes (int): The maximum number of nodes in the cluster.
        logRetentionDays (int, optional): The number of days to retain log entries. Defaults to 14.
    """

    name: str
    region: str

    namespace: str = "default"

    nodeType: str
    minNodes: int
    maxNodes: int

    logRetentionDays: int = 14


class CloudVectorStore(CloudNode):
    """
    Represents a cloud vector store.

    Attributes:
        replicas (int): The number of replicas for the vector store. Defaults to 1.
        storage_size (str): The size of the storage of one node for the vector store. Defaults to "10Gi".
        resourceRequest (Optional[ResourceRequest]): The resource request for the vector store, specifying the amount of CPU and memory to request.

    Inherited Attributes:
        nodeType (str): The type of the node.

    Methods:
        validate_storage_size: Validates the format of the storage_size field.
    """

    replicas: int = 1
    storage_size: str = "10Gi"
    resourceRequest: Optional[ResourceRequest] = None

    @field_validator("storage_size", mode="before")
    def validate_storage_size(cls, v: str) -> str:
        """
        Validates the format of the storage_size field.

        Args:
            v (str): The value of the storage_size field.

        Returns:
            str: The input value if validation is successful.

        Raises:
            ValueError: If the format of the input value is invalid.
        """
        return validate_size(v, "Invalid storage size format")

    @field_validator("replicas", mode="before")
    def validate_replicas(cls, v: int) -> int:
        """
        Validates the value of the replicas field.

        Args:
            v (int): The value of the replicas field.

        Returns:
            int: The input value if validation is successful.

        Raises:
            ValueError: If the value of the input value is invalid.
        """
        if v <= 0:
            raise ValueError("replicas must be greater than 0")
        return v


class Job(BaseModel):
    """
    Represents a job cluster configuration.

    Attributes:
        broker_storage_size (str): The size of the storage for the broker. Defaults to "10Gi".
    """

    enabled: bool = False

    broker_storage_size: str = "10Gi"

    @field_validator("broker_storage_size", mode="before")
    def validate_broker_storage_size(cls, v: str) -> str:
        """
        Validates the format of the broker_storage_size field.

        Args:
            v (str): The value of the storage_size field.

        Returns:
            str: The input value if validation is successful.

        Raises:
            ValueError: If the format of the input value is invalid.
        """
        return validate_size(v, "Invalid storage size format")


class Prometheus(BaseModel):
    enabled: bool = False

    storage_size: str = "10Gi"
    grafana: bool = False
    alertmanager: bool = False
    kube_api_server: bool = False
    kubelet: bool = False
    kube_controller_manager: bool = False
    core_dns: bool = False
    kube_etcd: bool = False
    kube_scheduler: bool = False
    kube_proxy: bool = False
    kube_state_metrics: bool = False
    node_exporter: bool = False
    thanos_ruler: bool = False

    @field_validator("storage_size", mode="before")
    def validate_storage_size(cls, v: str) -> str:
        """
        Validates the format of the storage_size field.

        Args:
            v (str): The value of the storage_size field.

        Returns:
            str: The input value if validation is successful.

        Raises:
            ValueError: If the format of the input value is invalid.
        """
        return validate_size(v, "Invalid storage size format")


class Tracing(BaseModel):
    """Represents the configuration for tracing."""

    enabled: bool = False

    autoScalingEnabled: bool = False

    zipkinHelmSettings: Optional[Dict[str, Any]] = None
    """https://github.com/openzipkin/zipkin-helm"""


class CloudConfig(BaseModel):
    """
    Represents the configuration for the cloud environment.

    Attributes:
        cluster (ClusterConfig): The configuration for the Kubernetes cluster.
        modelGroups (List[CloudModelGroup], optional): The list of model groups
            to be deployed in the cloud. If None, no model groups will be deployed. Defaults to None.
        vectorStore (CloudVectorStore, optional): The configuration
            for the vector store in the cloud. If None, the vector store will
            not be provisioned. Defaults to None.
        job (Job, optional): The configuration for the job broker. If None, the
            job broker will not be provisioned. Defaults to None.
        prometheus (Prometheus, optional): The configuration for Prometheus.
            If None, Prometheus will not be provisioned. Defaults to None.
    """

    cluster: ClusterConfig
    modelGroups: Optional[List[CloudModelGroup]] = None
    vectorStore: Optional[CloudVectorStore] = None
    job: Optional[Job] = None

    prometheus: Optional[Prometheus] = None
    tracing: Optional[Tracing] = None

    @field_validator("modelGroups", mode="before")
    def check_model_group(cls, v: List[Any]) -> List[Any]:
        if v is None or len(v) == 0:
            return v
        # Check if there are duplicated model group names
        model_group_names = [dict(group)["name"] for group in v]
        if len(set(model_group_names)) != len(model_group_names):
            raise ValueError("Duplicate model group names are not allowed")
        return v


class Config(BaseModel):
    """
    Configuration class for managing cloud cluster settings.

    Attributes:
        aws (Optional[CloudConfig]): AWS cloud configuration.
        gcp (Optional[CloudConfig]): GCP cloud configuration.

    Methods:
        check_one_field: Validates that exactly one cloud configuration (aws or gcp) is provided.
    """

    aws: Optional[CloudConfig] = None
    gcp: Optional[CloudConfig] = None

    @model_validator(mode="before")
    def check_one_field(cls, values: Dict[str, CloudConfig]) -> Dict[str, CloudConfig]:
        """
        Validates that exactly one cloud configuration is provided.

        Args:
            values (Dict[str, CloudConfig]): Dictionary of field values, where keys are the cloud providers (aws, gcp) and values are the corresponding cloud configurations.

        Returns:
            Dict[str, CloudConfig]: The input values if validation is successful.

        Raises:
            ValueError: If more or less than one cloud configuration is provided.
        """
        non_none_fields = sum(value is not None for value in values.values())
        if non_none_fields != 1:
            raise ValueError("Exactly one cloud configuration must be provided")

        return values


def generate_yaml(config: Config) -> str:
    """
    Generate a YAML string representation of the given config object.

    Args:
        config (Config): The config object to generate YAML from.

    Returns:
        str: The YAML string representation of the config object.
    """
    return to_yaml(config.model_dump(exclude_none=True))


def parse_yaml(yaml_str: str) -> Config:
    """
    Parse a YAML string and return a Config object.

    Args:
        yaml_str (str): The YAML string to parse.

    Returns:
        Config: The parsed Config object.
    """
    yaml = YAML()
    data = yaml.load(yaml_str)
    return Config(**data)
