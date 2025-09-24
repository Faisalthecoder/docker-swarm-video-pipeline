# 🎥 Docker Swarm Video Pipeline

This project is a **distributed video processing pipeline** built with **Docker Swarm**.  
It includes a backend API, worker service, message queue, frontend, and NGINX reverse proxy.  
Deployed with **Swarm services** for scalability and fault tolerance.  

---

## 🚀 Features
- **API Service** → Accepts video processing requests (Python + Flask/FastAPI).
- **Worker Service** → Processes jobs asynchronously from a message queue.
- **Queue (Redis/RabbitMQ)** → Handles background task scheduling.
- **Frontend** → Simple UI for submitting and tracking jobs.
- **NGINX** → Reverse proxy to expose services under your domain (`aitrack.tech`).

---

## 🛠️ Requirements
- Docker `>= 20.x`
- Docker Swarm initialized
- Git

---

## 📦 Clone the Repo
```bash
git clone git@github.com:faisalthecoder/docker-swarm-video-pipeline.git
cd docker-swarm-video-pipeline

