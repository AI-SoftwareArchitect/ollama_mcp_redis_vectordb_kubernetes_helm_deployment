# Multi-Agent Control System (MCP) with Ollama & Redis

## Project Overview

This project is designed to create a **Multi-Agent Control System (MCP)** using **Ollama** AI models and **Redis Vector DB**. It includes a **commander agent** that issues commands and a **coder agent** that generates code based on user input. The system is deployed using **Docker**, **Kubernetes**, and **Helm**, with **Vertical Pod Autoscaler (VPA)** in place for automatic resource scaling.

## Key Components

### 1. **Ollama AI Integration**
- Two **Ollama agents**: one for issuing commands and the other for generating code.
- Ollama models used: `deepseek-coder:latest`, `qwen2.5-coder:3b`, etc.

### 2. **Redis Vector DB**
- **Redis** is used to store and retrieve contextual data for the agent’s decision-making process.
- The Redis setup is integrated to handle **embedding** and inference operations.

### 3. **FastAPI & Docker**
- **FastAPI** is used to create the API for communication between agents.
- Docker is used to containerize the entire application for deployment.

### 4. **Kubernetes & Helm**
- The project is deployed on **Kubernetes** with **Helm** charts to manage the deployment and scalability.
- **Vertical Pod Autoscaler (VPA)** ensures dynamic resource allocation based on demand.

## Architecture

![Architecture-High-Level-Design(HLD).png](./Architecture-High-Level-Design(HLD).png)

## Setup

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/mcp-ollama.git](https://github.com/AI-SoftwareArchitect/ollama_mcp_redis_vectordb_kubernetes_helm_deployment.git)
