# 🤖 Enterprise Multi-AI Agent Systems

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/LangGraph-Orchestration-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

## 🌟 The Vision
> **"Orchestrating Intelligence at Scale."**
> A production-grade, cloud-native Multi-AI Agent ecosystem built using **LangGraph** & **LangChain**, supercharged by **Groq (LPU)** for lightning-fast inference and **Tavily** for real-time web intelligence. Experience a full-stack solution with **FastAPI** backends, **Streamlit** frontends, and a rigorous **DevSecOps** pipeline (Jenkins, SonarQube, Docker) deployed on **AWS ECS Fargate**.

---

## 🚀 Interactive UI Experience (Sequential Tour)

This application is organized into 5 specialized modules, each designed for a premium user experience:

### 🎮 1. Demo Project (The AI Workspace)
*   **Persona Customization**: Switch between *Research Assistant*, *Python Developer*, *Data Analyst*, or define a *Custom Identity*.
*   **Groq-Powered Chat**: Experience near-instantaneous responses (Llama 3.1) with real-time streaming.
*   **Quick Start Swarm**: One-click buttons to trigger agentic flows for Blog Posts, Health Advice, Travel Planning, or Debugging.
*   **Smart Controls**: Integrated "Send" and "Clear" workflow for seamless conversation management.

### 📖 2. About Project (The Implementation Workflow)
*   **Implementation Steps**: A step-by-step technical journey from *Data Ingestion* to *AWS Cloud Deployment*.
*   **Strategic Vision**: Understand the "Why" behind using a multi-agent swarm over single-prompt LLMs.

### 🔧 3. Tech Stack (The Visual Engine)
*   **Technology Cards**: Hover-interactive cards displaying our core stack (AI Core, Application, DevOps).
*   **SonarQube Dashboard**: A dedicated guide to our code quality standards, highlighting how we manage *Bugs*, *Vulnerabilities*, and *Smells*.

### 🏗️ 4. System Architecture (The Logic Flow)
*   **Workflow Explorer**: A direct visualization of the information pipeline: *User Query -> API Gateway -> LangGraph Orchestrator -> Collaborative Agents*.
*   **Component Deep Dive**: Technical expanders for the **Agent Swarm** logic and **External Memory** systems.
*   **Gallery**: Collection of architectural diagrams showing the end-to-end data flow.

---

## 📐 System Architecture Visualization

### 🔄 System Workflow & Orchestration
This diagram explains the high-level orchestration of user requests through the multi-agent graph.
![System Workflow](Multi+AI+Agent+Workflow.png)

### 🧩 Multi-Agent Interaction Loop
The system utilizes a complex cyclic graph to manage state and agent transitions.
![Agent Interaction Loop](Archi_Diagram/Screenshot%202025-12-29%20095148.png)

### 🚀 Deployment Architecture
The platform is containerized and deployed on AWS using a robust CI/CD pipeline.
![Deployment Architecture](Archi_Diagram/Screenshot%202025-12-29%20095214.png)

---

### 📋 5. System Logs (Live Monitoring)
*   **Analytics Dashboard**: Visual metric cards for *Info Events*, *Errors*, and *Warnings*.
*   **Live Feed**: A color-coded, scrollable log viewer to track every decision the AI agents make.
*   **Downloadable Diagnostics**: Secure local downloading of system history for offline analysis.

---

## 🛠️ Deep Tech Stack & Ecosystem

### 🧠 AI & Orchestration
*   **LangGraph**: Cyclic graph-based state machine for complex agentic loops.
*   **Groq LPU**: Specialized hardware for the world's fastest LLM inference.
*   **Tavily Search**: AI-native search engine designed for perfect RAG retrieval.
*   **LangChain**: The glue connecting tools, models, and memory.

### 🌐 Full-Stack Application
*   **FastAPI**: Asynchronous, high-performance REST API backend.
*   **Streamlit**: Modern, reactive frontend with custom CSS/JS premium styling.
*   **Pydantic**: Robust data validation and settings management.

### ☁️ DevOps & Cloud Mastery
*   **Docker**: Fully containerized environment for consistent deployment.
*   **Jenkins**: Automated CI/CD pipelines for testing and delivery.
*   **SonarQube**: Static Application Security Testing (SAST) and code quality gating.
*   **AWS ECS Fargate**: Serverless, scalable container orchestration in the cloud.

---

## ⚙️ Setting Up Your Local Environment

Follow these sequential steps to get the system running locally:

### 1. Repository Setup
```bash
git clone https://github.com/Ratnesh-181998/Enterprise-Multi-AI-Agent-Systems-.git
cd Enterprise-Multi-AI-Agent-Systems-
```

### 2. Environment Configuration
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 3. Dependency Installation
```bash
# It is recommended to use a virtual environment
python -m venv venv
source venv/bin/activate # windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Launch the System
```bash
# Start the Streamlit Dashboard
streamlit run Multi_Agent_streamlit_app.py
```

---

## 📞 Connect with the Developer

### **RATNESH KUMAR SINGH**
*Data Scientist (AI/ML Engineer) | 4+ Years Experience*

| Platform | Link |
| :--- | :--- |
| **🌐 Portfolio** | [Live Demo App](https://appudtzei3tyyttd6xjhwur.streamlit.app/) |
| **📧 Email** | [rattudacsit2021gate@gmail.com](mailto:rattudacsit2021gate@gmail.com) |
| **💼 LinkedIn** | [ratneshkumar1998](https://www.linkedin.com/in/ratneshkumar1998/) |
| **🐙 GitHub** | [Ratnesh-181998](https://github.com/Ratnesh-181998) |
| **📱 Mobile** | +91-947-XXXX-46 |

---

## 📄 LICENSE & Compliance
This project is licensed under the **MIT License**. It embraces open-source collaboration while maintaining enterprise-level security and quality standards.

> **Note on Large Files**: This repository uses **Git LFS** (Large File Storage) for high-resolution architecture diagrams and serialized model states.

---
<p align="center">Made with ❤️ for the AI Community</p>
