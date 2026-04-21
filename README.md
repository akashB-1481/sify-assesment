# sify-assesment

Microservices-based application deployed using Docker and Kubernetes with Nginx frontend, Flask backend, Redis cache, persistent storage, and monitoring via Prometheus &amp; Grafana.

# 🚀 Kubernetes Microservices Deployment Lab

## 📌 Project Overview

This project demonstrates the deployment of a **microservices-based application** using **Docker and Kubernetes**.

The application consists of:

- **Frontend**: Nginx (serves UI and routes requests)
- **Backend**: Flask API (handles business logic)
- **Cache**: Redis (in-memory data store)
- **Storage**: Persistent Volume for data durability
- **Monitoring**: Prometheus & Grafana

---

## 🏗️ Architecture

```
User → Ingress / NodePort → Nginx → Backend API → Redis → Persistent Storage
```

---

## 🐳 Part 1: Docker Setup

### Features

- Custom Nginx Docker image
- Flask-based backend API
- Redis integration
- Multi-container setup using Docker Compose

### Validation

- Access frontend via browser
- API call through `/api`
- Redis counter increments per request

---

## ☸️ Part 2: Kubernetes Deployment

### Core Components

- **Deployment**
  - Nginx (3 replicas)
  - Backend (2 replicas)

- **StatefulSet**
  - Redis (with persistent identity)

- **Services**
  - ClusterIP (internal communication)
  - NodePort (external access)

---

## ⚙️ Configuration Management

- **ConfigMap**
  - Stores application configuration (e.g., environment variables)

- **Secret**
  - Stores sensitive data (e.g., passwords)

---

## 💾 Storage

- Persistent Volume Claim (PVC)
- Mounted into backend for data persistence
- Data remains intact even after pod restarts

---

## ❤️ Health Checks

- **Liveness Probe**
  - Restarts unhealthy containers

- **Readiness Probe**
  - Controls traffic flow to pods

---

## 🔄 Deployment Strategy

- Rolling updates for zero downtime
- Rollback support using Kubernetes commands

---

## 📊 Monitoring

- Prometheus for metrics collection
- Grafana for visualization dashboards

---

## 🌐 Networking

- **Ingress Controller**
  - Routes traffic:
    - `/` → Frontend
    - `/api` → Backend

---

## 🧠 Advanced Kubernetes Concepts

- **StatefulSet** for Redis
- **DaemonSet** for logging agents
- **NodeSelector** for scheduling
- **Taints & Tolerations** for node control

---

## 📁 Project Structure

```
k8s-microservices-lab/
│
├── docker/
│   ├── nginx/
│   ├── backend/
│   └── docker-compose.yml
│
├── k8s/
│   ├── deployments/
│   ├── services/
│   ├── ingress/
│   ├── config/
│   ├── storage/
│   └── monitoring/
│
└── README.md
```

---

## ✅ Key Learnings

- Containerization using Docker
- Multi-container communication
- Kubernetes core concepts (Pod, Deployment, Service)
- Configuration and secret management
- Persistent storage handling
- Application health monitoring
- Production-style deployment strategies

---

## 📅 Timeline

- Assignment Start: 21-Apr-2026
- Submission Deadline: 27-Apr-2026

---

## 👨‍💻 Author

Akash B
Platform Engineering | DevOps Enthusiast

---

## 📌 Notes

This project is built as part of a Kubernetes hands-on assessment and focuses on practical implementation of real-world deployment scenarios.
