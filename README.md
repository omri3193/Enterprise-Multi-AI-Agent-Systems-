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

### 🔄 1. High-Level System Workflow
Overview of the orchestration logic and main components.
![System Workflow](Multi+AI+Agent+Workflow.png)

### 🧩 2. Agentic Workflow Construction
Detailed design of Input, Orchestration, and Output stages.
![Agentic Workflow](Archi_Diagram/Screenshot%202025-12-29%20095100.png)

### 🛰️ 3. Backend Integration Flow
How FastAPI, LangChain, and Groq communicate.
![Backend Integration](Archi_Diagram/Screenshot%202025-12-29%20095126.png)

### 🐝 4. Multi-Agent Interaction Loop
The core cyclic graph logic for Research, Routing, and Generation.
![Agent Interaction Loop](Archi_Diagram/Screenshot%202025-12-29%20095148.png)

### �️ 5. Integrated Tech Stack
Visual representation of the toolset: Groq, Tavily, LangGraph, and Docker.
![Tech Stack](Archi_Diagram/Screenshot%202025-12-29%20094816.png)

### �🚀 6. Deployment & Cloud Architecture
Containerization strategy and AWS Cloud infrastructure.
![Deployment Architecture](Archi_Diagram/Screenshot%202025-12-29%20095214.png)

### 🔍 7. Real-time Search & Search Strategy
Tavily integration and RAG retrieval mechanisms.
![Search Strategy](Archi_Diagram/Screenshot%202025-12-29%20095240.png)

---

### 📋 5. System Logs (Live Monitoring)
*   **Analytics Dashboard**: Visual metric cards for *Info Events*, *Errors*, and *Warnings*.
*   **Live Feed**: A color-coded, scrollable log viewer to track every decision the AI agents make.
*   **Downloadable Diagnostics**: Secure local downloading of system history for offline analysis.

---

## 🛠️ Core Technology Stack

### 🧠 AI & Intelligent Orchestration
- **Groq (Llama 3.1)**: State-of-the-art LLM inference engine providing near-zero latency for real-time agent reasoning.
- **LangGraph**: Used to build complex, stateful multi-agent workflows with cyclic graph logic.
- **LangChain**: The foundational framework for LLM abstraction, tool integration, and prompt management.
- **Tavily Search**: Advanced search engine specialized for LLM retrieval and real-time fact-checking.

### 🌐 Full-Stack Application
- **FastAPI**: High-performance, asynchronous Python backend for handling agent orchestration and API requests.
- **Streamlit**: Interactive and premium frontend dashboard with custom CSS-glassmorphism styling.
- **Pydantic**: Robust data validation and settings management.

### 🚀 DevOps, Cloud & LLMOps
- **Docker**: Used for standardizing application environments via containerization.
- **Jenkins**: Orchestrating automated CI/CD pipelines from commit to cloud deployment.
- **SonarQube**: Static Application Security Testing (SAST) and code quality gating.
- **AWS ECS Fargate**: Serverless, scalable container orchestration in the cloud.
- **GitHub**: Source Code Management (SCM) and version control.

---

## 🛡️ Code Quality & Security Standards (SonarQube)

To ensure enterprise-grade reliability, the project integrates **SonarQube** for continuous code inspection and quality assurance.

### 🔍 Key Checks Performed:
*   **Bug Detection**: Identifying logic errors and "Dead Code" (redundant conditions) before they reach production.
*   **Code Smells**: Flagging technical debt (e.g., complex 300+ line methods) for refactoring to maintain maintainability.
*   **Code Duplication**: Detecting repetitive blocks across `app.py`, `main.py`, etc., to enforce **DRY** (Don't Repeat Yourself) principles.
*   **Security Vulnerabilities**: Scanning for sensitive credential leaks and insecure coding patterns.

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
