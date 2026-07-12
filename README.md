# AI Infrastructure Platform on Kubernetes

**End-to-end AI Infrastructure / MLOps platform** demonstrating **Cloud, DevOps, DevSecOps, Kubernetes, and AI deployment** skills.

## 🚀 Project Overview

This project showcases how to build a production-style AI inference platform using modern cloud-native technologies. It demonstrates the complete workflow from containerization and automated CI/CD pipelines to Kubernetes deployment and security scanning.

The goal is to simulate how real-world AI services are built, deployed, secured, and managed in production.

---

## 🛠️ Tech Stack

| Category               | Technology                                      |
| ---------------------- | ----------------------------------------------- |
| Backend                | FastAPI, scikit-learn                           |
| Programming Language   | Python                                          |
| Containerization       | Docker                                          |
| Container Registry     | GitHub Container Registry (GHCR)                |
| Orchestration          | Kubernetes                                      |
| CI/CD                  | GitHub Actions                                  |
| Security               | Trivy                                           |
| Infrastructure as Code | Terraform *(coming soon)*                       |
| Monitoring             | Prometheus, Grafana *(integration coming soon)* |
| GitOps                 | ArgoCD *(planned)*                              |

---

## 🏗️ Architecture

```text
GitHub
    │
    ▼
GitHub Actions
(Build + Security Scan)
    │
    ▼
Docker Image
    │
    ▼
GitHub Container Registry
    │
    ▼
Kubernetes Cluster
    │
    ▼
FastAPI AI Inference Service
```

---

## 📂 Project Structure

```text
ai-infra-platform/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── terraform/          # Coming soon
└── README.md
```

---

## ⚡ Quick Start

### Clone the repository

```bash
git clone git@github.com:Sntosi/ai-infra-platform.git
cd ai-infra-platform
```

### Create a local Kubernetes cluster

```bash
kind create cluster
```

### Build the Docker image

```bash
docker build -t ai-infra-platform .
```

### Deploy to Kubernetes

```bash
kubectl apply -f kubernetes/
```

### Verify deployment

```bash
kubectl get pods
kubectl get services
```

Access the application using the Kubernetes Service or by port-forwarding the deployment.

---

## ✅ Features Implemented

* AI prediction API using FastAPI
* Docker containerization
* Kubernetes Deployment and Service
* GitHub Actions CI/CD pipeline
* Automated security scanning with Trivy
* Production-style repository structure

---

## 🚧 Roadmap

* Terraform Infrastructure as Code
* AWS deployment
* Prometheus monitoring
* Grafana dashboards
* Loki log aggregation
* Alertmanager notifications
* ArgoCD GitOps deployment
* Horizontal Pod Autoscaling
* Helm charts

---

## 🔐 DevSecOps Highlights

* Shift-left security using Trivy
* Automated CI/CD pipeline
* Containerized application deployment
* Kubernetes-native architecture
* Infrastructure as Code (planned)
* Cloud-native deployment practices

---

## 📸 Screenshots

Screenshots will be added as the project evolves.

* GitHub Actions pipeline
* Trivy security scan
* Kubernetes deployment
* FastAPI prediction endpoint
* Grafana dashboard
* Prometheus metrics

---

## 📚 What I Learned

Through this project I gained practical experience with:

* Docker image creation
* Kubernetes deployments
* GitHub Actions automation
* DevSecOps practices
* AI model serving with FastAPI
* Cloud-native application architecture
* Production-style repository organization

---

## 🎯 Project Goal

This project is part of my journey toward becoming a **Cloud Infrastructure / DevSecOps / AI Infrastructure Engineer** by building production-style projects that reflect real industry workflows and best practices.
