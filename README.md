# 🧠 AIgentOps — Open Source AI Agent Orchestration on Kubernetes

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Kubernetes](https://img.shields.io/badge/k8s-ready-green)
![CI/CD](https://img.shields.io/github/actions/workflow/status/<your-org>/aigentops/deploy.yml)

## 📌 What is AIgentOps?

**AIgentOps** is a fully open-source, self-hostable platform to **deploy, manage, and monitor AI agents** (LLMs, RAG pipelines, embeddings, vector databases, and frontend UIs) using **Kubernetes and modern DevOps best practices** — all without relying on cloud services or proprietary tools.

Whether you’re running AI workloads at the edge, in a secure on-prem cluster, or across hybrid infrastructure, AIgentOps gives you a **modular, GitOps-native, production-ready system** to bring AI to your environment.

---

## 🎯 Why are we building AIgentOps?

AI is evolving fast, but deploying LLMs, agents, and RAG pipelines in production is still a **manual, fragmented, and cloud-centric** process. We need:

- ✅ **Cloud-neutral infrastructure**: Self-hosted, not locked to AWS/GCP/Azure  
- ✅ **Composable architecture**: Pick and swap components (LangChain, FastAPI, Weaviate, Qdrant, MinIO, etc.)  
- ✅ **Secure and auditable deployments**: Secrets managed via SealedSecrets, GitOps tracked rollouts  
- ✅ **Scalable, monitored stacks**: Built-in metrics, logs, and alerting  
- ✅ **Infrastructure as Code**: Easily replicate environments across clusters  

> 🛠️ We are DevOps engineers and architects who believe AI deployments should be **as automatable and repeatable** as building a microservice.

---

## 🧱 Key Features

- 🌐 **Kubernetes-Native AI Agent Deployment** (LangChain/FastAPI)
- 📊 **Built-in Observability**: Prometheus, Grafana, Loki
- 🔐 **Secure Secrets Management**: Bitnami SealedSecrets
- 📦 **Fully OSS Stack**: No proprietary SaaS or cloud lock-in
- 📥 **Vector DB Integration**: Qdrant or Weaviate
- 🗃️ **Embeddings Storage**: MinIO (S3-compatible)
- 🚀 **CI/CD Pipelines**: GitHub Actions + Helmfile + Kubernetes
- 🛑 **Rollback-ready**: Helm versioning, GitOps sync
- 🛡️ **Auth Gateway**: NestJS with JWT-based auth
- 🧪 **Modular Architecture**: Deploy API, UI, agent, DB separately or together

---

## 🖼️ System Overview

```mermaid
flowchart TD
  subgraph DevOps CI/CD
    GH[GitHub Actions]
    HR[Helmfile]
    TF[OpenTofu]
  end

  subgraph Core Services
    UI[Next.js UI]
    API[NestJS Gateway]
    AGENT[LangChain/FastAPI Agent]
    VDB[Qdrant]
    POSTGRES[PostgreSQL]
    STORAGE[MinIO]
  end

  subgraph Platform Layer
    K8S[Kubernetes]
    HELM[Helm + Helmfile]
    METRICS[Prometheus + Grafana]
    LOGS[Loki + Grafana Logs]
    SECRETS[SealedSecrets]
  end

  GH --> HR --> HELM --> K8S
  API --> AGENT --> VDB
  API --> POSTGRES
  UI --> API
  AGENT --> STORAGE
  K8S --> METRICS
  K8S --> LOGS
  K8S --> SECRETS


Tech stack 
-----------
| Layer        | Tools                           |
| ------------ | ------------------------------- |
| Platform     | Kubernetes (k3s or kubeadm)     |
| CI/CD        | GitHub Actions, Helmfile        |
| AI Agent     | FastAPI, LangChain              |
| UI           | Next.js                         |
| API Gateway  | NestJS with JWT Auth            |
| Vector DB    | Qdrant / Weaviate               |
| Storage      | MinIO                           |
| DB           | PostgreSQL (Bitnami Helm Chart) |
| Monitoring   | Prometheus, Grafana, Loki       |
| Secrets Mgmt | SealedSecrets (Bitnami)         |
```


