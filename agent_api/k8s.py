from kubernetes import client, config
from jinja2 import Template
import os

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../k8s_templates/deployment.yaml")

def deploy_agent(config_data):
    config.load_kube_config()
    with open(TEMPLATE_PATH) as f:
        template = Template(f.read())

    rendered_yaml = template.render(
        name=config_data.name,
        image=config_data.image,
        replicas=config_data.replicas
    )

    k8s_client = client.ApiClient()
    k8s_apps = client.AppsV1Api(k8s_client)

    manifest = client.V1Deployment().from_dict(
        client.ApiClient().deserialize(
            client.ApiClient().sanitize_for_serialization(
                client.ApiClient()._ApiClient__deserialize_model(rendered_yaml, client.V1Deployment)
            ),
            client.V1Deployment
        )
    )

    resp = k8s_apps.create_namespaced_deployment(
        namespace="default",
        body=manifest
    )
    return resp.metadata.name