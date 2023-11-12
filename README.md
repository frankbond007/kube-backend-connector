Backend API Documentation
Overview

This backend API, named kube_connector, is designed to interact with a Kubernetes cluster. It provides endpoints to apply pod and deployment resources to the cluster. The API is built using FastAPI and leverages the Kubernetes Python client.
Requirements

    Python 3.6+
    Packages from requirements.txt:
        httpx
        fastapi[all]
        uvicorn
        kubernetes
        juju

Installation

    Install Python dependencies:

    bash

    pip install -r requirements.txt

    Set up your Kubernetes environment:
        Ensure you have kubeconfig configured correctly to connect to your Kubernetes cluster.

Running the Application

Execute the following command to run the server:

bash

uvicorn main:app --reload

API Endpoints
Apply Pod

    URL: /apply-pod/
    Method: POST
    Description: Applies a pod resource to the Kubernetes cluster.
    Request Body:
        Type: application/json
        Content: A JSON object representing the pod manifest.
    Responses:
        200 OK: Pod created successfully.
        500 Internal Server Error: Error details if the pod creation fails.

Apply Deployment

    URL: /apply-deployment/
    Method: POST
    Description: Applies a deployment resource to the Kubernetes cluster.
    Request Body:
        Type: application/json
        Content: A JSON object representing the deployment manifest.
    Responses:
        200 OK: Deployment created successfully.
        500 Internal Server Error: Error details if the deployment creation fails.

Classes
KubeResourceHandler

    Purpose: Abstract base class for handling Kubernetes resources.
    Methods:
        __init__(api_client, create_method): Initializes the handler with a Kubernetes API client and a method for resource creation.
        apply_resource(manifest: dict): Applies the given manifest to the cluster. It's an asynchronous method.

PodHandler

    Inherits From: KubeResourceHandler
    Description: Handles the creation of Pod resources.

DeploymentHandler

    Inherits From: KubeResourceHandler
    Description: Handles the creation of Deployment resources.

Error Handling

    The API uses HTTP status codes to indicate the success or failure of an API request.
    In case of errors during resource application, a 500 Internal Server Error is returned with the error details.

Security and Authentication

    This API currently does not implement authentication and authorization. It is recommended to add security measures as per your requirements.
