# kube_connector
from fastapi import FastAPI, HTTPException
from kubernetes import client, config
from starlette.concurrency import run_in_threadpool

app = FastAPI()

config.load_kube_config()

class KubeResourceHandler:
    def __init__(self, api_client, create_method):
        """initializes the api client"""
        self.api_client = api_client
        self.create_method = create_method

    async def apply_resource(self, manifest: dict):
        try:
            await run_in_threadpool(self.create_method, namespace=manifest["metadata"]["namespace"], body=manifest)
            return {"status": f"{self.__class__.__name__} created successfully in backend."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

class PodHandler(KubeResourceHandler):
    def __init__(self):
        super().__init__(api_client=client.CoreV1Api(), create_method=client.CoreV1Api().create_namespaced_pod)

class DeploymentHandler(KubeResourceHandler):
    def __init__(self):
        super().__init__(api_client=client.AppsV1Api(), create_method=client.AppsV1Api().create_namespaced_deployment)

@app.post("/apply-pod/")
async def apply_pod(manifest: dict):
    """Applies pod to cluster"""
    handler = PodHandler()
    return await handler.apply_resource(manifest)

@app.post("/apply-deployment/")
async def apply_deployment(manifest: dict):
    handler = DeploymentHandler()
    return await handler.apply_resource(manifest)


