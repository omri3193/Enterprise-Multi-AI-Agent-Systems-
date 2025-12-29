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
> 
> **Summary:** “I built a cloud-native Multi-AI Agent system using LangGraph and LangChain, powered by Groq LLMs and Tavily search, with FastAPI and Streamlit, containerized using Docker, quality-checked with SonarQube, automated via Jenkins, and deployed on AWS ECS Fargate.”
>
> A production-grade, cloud-native Multi-AI Agent ecosystem built using **LangGraph** & **LangChain**, supercharged by **Groq (LPU)** for lightning-fast inference and **Tavily** for real-time web intelligence. Experience a full-stack solution with **FastAPI** backends, **Streamlit** frontends, and a rigorous **DevSecOps** pipeline (Jenkins, SonarQube, Docker) deployed on **AWS ECS Fargate**.
---
## 🌐🎬 Live Demo
🚀 **Try it now:**
- **Streamlit Profile** - https://share.streamlit.io/user/ratnesh-181998
- **Project Demo** - https://appudtzei3tyyttd6xjhwur.streamlit.app/
---

## � Table of Contents
1. [�🚀 Interactive UI Experience](#-interactive-ui-experience-sequential-tour)
2. [🛠️ Step-by-Step Implementation Workflow](#️-step-by-step-implementation-workflow)
3. [📐 System Architecture Visualization](#-system-architecture-visualization)
4. [🛠️ Core Technology Stack](#️-core-technology-stack)
5. [🛡️ Code Quality & Security Standards](#️-code-quality--security-standards-sonarqube)
6. [⚙️ Setting Up Your Local Environment](#️-setting-up-your-local-environment)
7. [📞 Connect with the Developer](#-connect-with-the-developer)

---

## 🚀 Interactive UI Experience (Sequential Tour)

Experience the application through its five specialized modules:

### 🎮 1. Demo Project (The AI Workspace)
*   **Persona Customization**: Switch between *Research Assistant*, *Python Developer*, *Data Analyst*, or define a *Custom Identity*.
*   **Groq-Powered Chat**: Near-instantaneous responses (Llama 3.1) with real-time streaming.
*   **Quick Start Swarm**: One-click workflows for Blog Posts, Health Advice, Travel Planning, or Debugging.
*   **Smart Controls**: Integrated "Send" and "Clear" workflow for conversation management.

### 📖 2. About Project (The Mission)
*   **Detailed Workflow**: A deep dive into the design philosophy.
*   **Strategic Vision**: Understanding why agents outperform single LLMs for complex reasoning.

### 🔧 3. Tech Stack (The Components)
*   **Visual Interface**: Interactive cards for the core stack.
*   **SonarQube Focus**: Detailed explanation of code health monitoring.

### 🏗️ 4. System Architecture
*   **Workflow Explorer**: Visualization of the information pipeline.
*   **Deep Dive Expanders**: Technical breakdowns of Agent Swarms and Memory.

### 📋 5. System Logs (Live Diagnostics)
*   **Metric Cards**: Real-time counts of *Info*, *Errors*, and *Warnings*.
*   **Scrollable Feed**: Live, color-coded execution logs.

---

## 🛠️ Step-by-Step Implementation Workflow

<details>
<summary><b>Click to expand the technical journey (10 Steps)</b></summary>

### **Step 1: Define the Problem**
Addressing LLM limitations in reasoning and real-time accuracy via multi-agent swarms.

### **Step 2: High-Level Architecture**
Establishing the decoupled Frontend (Streamlit) and Backend (FastAPI) foundation.

### **Step 3: Build the Multi-Agent AI System**
Developing specialized Search, Reasoning, and Answer agents within a LangGraph state machine.

### **Step 4: Backend APIs (FastAPI)**
Creating high-performance asynchronous endpoints for the agent workspace.

### **Step 5: Frontend Experience (Streamlit)**
Designing a premium, reactive user interface with custom CSS.

### **Step 6: Containerization (Docker)**
Packaging the entire ecosystem for production consistency.

### **Step 7: Code quality (SonarQube)**
Integrating automated SAST scans for bugs, smells, and security risks.

### **Step 8: CI/CD Automation (Jenkins)**
Automating the build-test-deploy cycle from code commit to cloud.

### **Step 9: Cloud Deployment (AWS ECS Fargate)**
Orchestrating serverless containers for global scalability.

### **Step 10: Version Control (GitHub)**
Maintaining the source of truth and triggering the DevSecOps pipeline.
</details>

---

## 📐 System Architecture Visualization

### 🔄 1. High-Level System Workflow
![System Workflow](Multi+AI+Agent+Workflow.png)

### 🧩 2. Agentic Workflow Construction
![Agentic Workflow](Archi_Diagram/Screenshot%202025-12-29%20095100.png)

### 🛰️ 3. Backend Integration Flow
![Backend Integration](Archi_Diagram/Screenshot%202025-12-29%20095126.png)

### 🐝 4. Multi-Agent Interaction Loop
![Agent Interaction Loop](Archi_Diagram/Screenshot%202025-12-29%20095148.png)

### � 5. Deployment & Cloud Architecture
![Deployment Architecture](Archi_Diagram/Screenshot%202025-12-29%20095214.png)

---

## 🛠️ Core Technology Stack

| Category | Tools | Description |
| :--- | :--- | :--- |
| **🧠 AI Core** | **Groq, LangGraph, LangChain, Tavily** | Orchestration, Reasoning, and Real-time Intelligence. |
| **🌐 Full-Stack** | **FastAPI, Streamlit, Pydantic** | Performance backend and Premium React-styled UI. |
| **🚀 DevOps** | **Docker, Jenkins, AWS ECS, SonarQube** | CI/CD, Quality gates, and Cloud Scaling. |

---

## 🛡️ Code Quality & Security Standards (SonarQube)

Ensuring **Enterprise-Grade** reliability through continuous inspection:
*   ✅ **Bug Detection**: Logical errors and dead code removal.
*   ✅ **Code Smells**: Technical debt reduction for long-term maintainability.
*   ✅ **DRY Principles**: Eliminating code duplication across the repository.
*   ✅ **Security SAST**: Protection against credential leaks and insecure patterns.

---

## ⚙️ Setting Up Your Local Environment

```bash
# 1. Clone & Enter
git clone https://github.com/Ratnesh-181998/Enterprise-Multi-AI-Agent-Systems-.git
cd Enterprise-Multi-AI-Agent-Systems-

# 2. Virtual Env & Install
python -m venv venv
source venv/bin/activate # windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Environment Config
# Create .env with GROQ_API_KEY & TAVILY_API_KEY

# 4. Launch
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

---

## 📄 LICENSE
MIT License © 2025 | Powered by **Git LFS**

<p align="center">Made with ❤️ for the AI Community</p>
