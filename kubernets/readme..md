# Kubernetes 3-Tier Application (Production-Ready Design)

## 📌 Overview

This project demonstrates a **3-tier application deployment in Kubernetes** with a production-style architecture:

- **Frontend** → Nginx
- **Backend** → Flask API
- **Database** → Redis

The setup follows best practices including:

- Namespace isolation
- Service-based communication
- Environment variable configuration
- Scalable and modular design

---

## 🏗️ Architecture

```
Internet / Client
        │
        ▼
Ingress / NodePort
        │
        ▼
[ Nginx - frontend-ns ]
        │
        ▼
flask-service.backend-ns
        │
        ▼
[ Flask - backend-ns ]
        │
        ▼
redis-service.db-ns
        │
        ▼
[ Redis - db-ns ]
```

---

## 📂 Namespaces

| Layer    | Namespace   |
| -------- | ----------- |
| Frontend | frontend-ns |
| Backend  | backend-ns  |
| Database | db-ns       |

---

## 🌐 Service Discovery & DNS

Kubernetes uses internal DNS for communication between services.

### 🔹 DNS Format

```
<service-name>.<namespace>.svc.cluster.local
```

### 🔹 Examples

| Service       | DNS Name                  |
| ------------- | ------------------------- |
| nginx-service | nginx-service.frontend-ns |
| flask-service | flask-service.backend-ns  |
| redis-service | redis-service.db-ns       |

---

## 🔗 Cross-Namespace Communication

### ✅ Nginx → Flask

```
proxy_pass http://flask-service.backend-ns:5000;
```

### ✅ Flask → Redis

```
redis-service.db-ns:6379
```

---

## ⚙️ Environment Variables

Avoid hardcoding values inside code or Docker images.

### Example (Flask Deployment)

```yaml
env:
  - name: REDIS_HOST
    value: redis-service.db-ns
```

---

## 🐳 Docker Best Practices

- Keep Docker images **generic**
- Do NOT hardcode:
  - Service names
  - IPs
  - Environment-specific configs

### ❌ Bad Practice

```
redis_host = "redis-service"
```

### ✅ Good Practice

Use environment variables:

```
redis_host = os.getenv("REDIS_HOST")
```

---

## 🔧 Kubernetes Components Used

- Deployment
- Service (ClusterIP / NodePort)
- Namespace
- ConfigMap (for configs like Nginx)
- Environment Variables
- (Planned) Ingress
- (Planned) Persistent Volumes

---

## 🧪 Debugging Tips

### Check pods

```bash
kubectl get pods -A
```

### Check services

```bash
kubectl get svc -A
```

### Test DNS inside cluster

```bash
kubectl exec -it <pod> -n <namespace> -- sh
nslookup flask-service.backend-ns
```

---

## 🚀 Future Enhancements

- Ingress Controller (Nginx / AWS ALB)
- Persistent Volume for Redis
- Helm Charts
- Horizontal Pod Autoscaling
- Secrets management
- CI/CD integration

---

## 🎯 Key Learnings

- Kubernetes **Service = Stable communication layer**
- DNS-based service discovery is critical
- Namespaces enable **logical isolation**
- Never couple application config with container image

---

## 📌 Summary

This project demonstrates how to design a **scalable, production-ready Kubernetes application** using:

- Multi-namespace architecture
- Service-based communication
- Clean configuration management

---

## 👨‍💻 Author

Akash B
