# Azure AKS Deployment Guide - AI Powered Investor Intelligence Platform

## Overview

This document explains how to deploy the application from a local machine to Azure Kubernetes Service (AKS).

Deployment Flow:

```text
Local Application
    ↓
Docker Image
    ↓
Azure Container Registry (ACR)
    ↓
Azure Kubernetes Service (AKS)
    ↓
Azure PostgreSQL
    ↓
Public Load Balancer
    ↓
Application URL
```

---

# Step 1: Build Docker Image

Build the Docker image locally.

```bash
docker build -t invint .
```

Verify image creation.

```bash
docker images
```

Expected Output:

```text
REPOSITORY    TAG
invint        latest
```

---

# Step 2: Run Docker Locally

Run the container locally.

```bash
docker run -p 8000:8000 invint
```

Open browser:

```text
http://localhost:8000
```

Verify:

* Application loads successfully
* Dashboard renders
* PDF upload works
* Chatbot works

Stop container:

```bash
Ctrl + C
```

---

# Step 3: Login to Azure

Authenticate with Azure.

```bash
az login
```

Verify subscription.

```bash
az account show
```

---

# Step 4: Login to Azure Container Registry (ACR)

Login using Azure CLI.

```bash
az acr login --name invintelligence
```

Alternative login using username/password.

Retrieve credentials.

```bash
az acr credential show --name invintelligence
```

Login manually.

```bash
docker login invintelligence.azurecr.io
```

Provide:

```text
Username: invintelligence
Password: <acr-password>
```

Expected Output:

```text
Login Succeeded
```

---

# Step 5: Tag Docker Image

Tag local image for ACR.

```bash
docker tag invint:latest invintelligence.azurecr.io/invint:v1
```

Verify image.

```bash
docker images
```

Expected Output:

```text
invintelligence.azurecr.io/invint    v1
```

---

# Step 6: Push Docker Image to ACR

Push image.

```bash
docker push invintelligence.azurecr.io/invint:v1
```

Verify image push.

```bash
az acr repository list --name invintelligence --output table
```

---

# Step 7: Connect to AKS

Download cluster credentials.

```bash
az aks get-credentials --resource-group rg-inv-intelligence --name inv-intelligence-aks --overwrite-existing
```

Verify connection.

```bash
kubectl get nodes
```

Expected Output:

```text
STATUS
Ready
```

---

# Step 8: Verify AKS Can Access ACR

Attach ACR to AKS.

```bash
az aks update --resource-group rg-inv-intelligence --name inv-intelligence-aks --attach-acr invintelligence
```

Verify access.

```bash
az aks check-acr --resource-group rg-inv-intelligence --name inv-intelligence-aks --acr invintelligence
```

Expected Output:

```text
Your cluster can pull images from invintelligence.azurecr.io!
```

---

# Step 9: Create Image Pull Secret

If AKS cannot pull images directly from ACR, create a Docker Registry Secret.

Retrieve ACR credentials.

```bash
az acr credential show --name invintelligence
```

Create secret.

```bash
kubectl create secret docker-registry acr-secret \
  --docker-server=invintelligence.azurecr.io \
  --docker-username=invintelligence \
  --docker-password=<acr-password>
```

Configure default service account to use the secret.

```bash
kubectl patch serviceaccount default -p "{\"imagePullSecrets\": [{\"name\": \"acr-secret\"}]}"
```

---

# Step 10: Deploy Application

Create deployment.

```bash
kubectl create deployment invint --image=invintelligence.azurecr.io/invint:v1
```

Verify deployment.

```bash
kubectl get deployments
```

Expected Output:

```text
NAME     READY
invint   1/1
```

---

# Step 11: Monitor Pod Startup

List pods.

```bash
kubectl get pods
```

Watch pod startup.

```bash
kubectl get pods -w
```

Expected Output:

```text
STATUS
Running
```

---

# Step 12: View Application Logs

Current logs.

```bash
kubectl logs <pod-name>
```

Example:

```bash
kubectl logs invint-xxxxxxxxxx-yyyyy
```

Follow logs in real time.

```bash
kubectl logs -f <pod-name>
```

View previous container logs.

```bash
kubectl logs <pod-name> --previous
```

Describe pod.

```bash
kubectl describe pod <pod-name>
```

---

# Step 13: Expose Application

Create public Load Balancer.

```bash
kubectl expose deployment invint --type=LoadBalancer --port=80 --target-port=8000
```

Verify service.

```bash
kubectl get svc
```

Expected Output:

```text
NAME     TYPE           EXTERNAL-IP
invint   LoadBalancer   20.xxx.xxx.xxx
```

---

# Step 14: Access Application

Open browser.

```text
http://<external-ip>
```

Example:

```text
http://20.xxx.xxx.xxx
```

---

# Common Troubleshooting Commands

List Nodes

```bash
kubectl get nodes
```

List Pods

```bash
kubectl get pods
```

List Services

```bash
kubectl get svc
```

List Deployments

```bash
kubectl get deployments
```

Describe Deployment

```bash
kubectl describe deployment invint
```

Describe Pod

```bash
kubectl describe pod <pod-name>
```

View Logs

```bash
kubectl logs <pod-name>
```

Follow Logs

```bash
kubectl logs -f <pod-name>
```

Restart Deployment

```bash
kubectl rollout restart deployment invint
```

Delete Deployment

```bash
kubectl delete deployment invint
```

Delete Service

```bash
kubectl delete service invint
```

Delete Secret

```bash
kubectl delete secret acr-secret
```

Delete All Resources

```bash
kubectl delete all --all
```

---

# AKS Cluster Operations

List AKS Clusters

```bash
az aks list --output table
```

Get AKS Credentials

```bash
az aks get-credentials --resource-group rg-inv-intelligence --name inv-intelligence-aks --overwrite-existing
```

Delete AKS Cluster

```bash
az aks delete --resource-group rg-inv-intelligence --name inv-intelligence-aks --yes --no-wait
```

Verify Deletion

```bash
az aks list --output table
```

---

# ACR Operations

List Registries

```bash
az acr list --output table
```

Show Registry Details

```bash
az acr show --name invintelligence
```

Show Registry Credentials

```bash
az acr credential show --name invintelligence
```

Delete Registry

```bash
az acr delete --name invintelligence --resource-group rg-inv-intelligence --yes
```

---

# Production Enhancements

The current deployment is functional and suitable for demonstrations and development purposes.

Typical production enhancements include:

* GitHub Actions CI/CD
* Azure Key Vault Integration
* HTTPS / SSL Certificates
* Custom Domain
* NGINX Ingress Controller
* Monitoring and Logging
* Horizontal Pod Autoscaling
* Application Authentication
* Private Networking
* WAF Protection

These enhancements can be implemented incrementally as part of future deployment improvements.
