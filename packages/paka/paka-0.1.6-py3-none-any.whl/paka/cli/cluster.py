from __future__ import annotations

from typing import List

import click
import typer

from paka.cli.utils import load_cluster_manager
from paka.k8s.utils import remove_crd_finalizers
from paka.k8s.utils import update_kubeconfig as merge_update_kubeconfig
from paka.logger import logger

cluster_app = typer.Typer()


@cluster_app.command()
def up(
    cluster_config: str = typer.Option(
        "",
        "--file",
        "-f",
        help="Path to the cluster config file. The cluster config file is a "
        "YAML file that contains the configuration of the cluster",
    ),
    update_kubeconfig: bool = typer.Option(
        False,
        "--update-kubeconfig",
        "-u",
        help="Updates the default kubeconfig file (~/.kube/config) to include"
        "the connection details of the newly created Kubernetes cluster"
        "This allows kubectl to communicate with the new cluster.",
    ),
) -> None:
    """
    Creates or updates a Kubernetes cluster based on the provided configuration.
    """
    cluster_manager = load_cluster_manager(cluster_config)
    cluster_manager.create()
    if update_kubeconfig:
        logger.info("Updating kubeconfig...")
        merge_update_kubeconfig()
        logger.info("Successfully updated kubeconfig.")


@cluster_app.command()
def down(
    cluster_config: str = typer.Option(
        "",
        "--file",
        "-f",
        help="Path to the cluster config file. The cluster config file is a "
        "YAML file that contains the configuration of the cluster",
    ),
    yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Automatic yes to prompts. Use this option to bypass the confirmation "
        "prompt and directly proceed with the operation.",
    ),
) -> None:
    """
    Tears down the Kubernetes cluster, removing all associated resources and data.
    """
    if yes or click.confirm(
        f"Are you sure you want to proceed with the operation? Please note that "
        "all resources and data will be permanently deleted.",
        default=False,
    ):
        # Sometime finalizers might block CRD deletion, so we need to force delete those.
        # This is best effort and might not work in all cases.
        # TODO: better way to handle this
        crds = [
            "scaledobjects.keda.sh",
            "routes.serving.knative.dev",
            "ingresses.networking.internal.knative.dev",
        ]

        for crd in crds:
            try:
                remove_crd_finalizers(crd)
            except Exception as e:
                pass

        cluster_manager = load_cluster_manager(cluster_config)
        cluster_manager.destroy()


@cluster_app.command()
def preview(
    cluster_config: str = typer.Option(
        "",
        "--file",
        "-f",
        help="Path to the cluster config file. The cluster config file is a "
        "YAML file that contains the configuration of the cluster",
    ),
    policy_packs: List[str] = typer.Option(
        [],
        "--policy-pack",
        "-p",
        help="Path to the policy pack.",
    ),
) -> None:
    """
    Previews the changes that will be applied to the cloud resources.
    """
    cluster_manager = load_cluster_manager(cluster_config)
    if policy_packs:
        cluster_manager.preview(policy_packs=policy_packs)
    else:
        cluster_manager.preview()


@cluster_app.command()
def refresh(
    cluster_config: str = typer.Option(
        "",
        "--file",
        "-f",
        help="Path to the cluster config file. The cluster config file is a "
        "YAML file that contains the configuration of the cluster",
    ),
) -> None:
    """
    Synchronize the local cluster state with the state in the cloud.
    """
    cluster_manager = load_cluster_manager(cluster_config)
    cluster_manager.refresh()
