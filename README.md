# 🤖 Enterprise Multi-AI Agent Systems

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-orange)](https://langchain-ai.github.io/langgraph/)
[![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"I built a cloud-native Multi-AI Agent system using LangGraph and LangChain, powered by Groq LLMs and Tavily search, with FastAPI and Streamlit, containerized using Docker, quality-checked with SonarQube, automated via Jenkins, and deployed on AWS ECS Fargate."**

---

## 🚀 Project Overview

The **Enterprise Multi-AI Agent System** is a cutting-edge platform designed to bridge the gap between static LLM knowledge and dynamic real-world information. By orchestrating a swarm of specialized AI agents using **LangGraph**, this system creates a robust, cyclic workflow that can Research, Reason, and Respond to complex user queries with high accuracy.

Unlike traditional single-shot LLM applications, this system employs an iteratively refining process where agents collaborate—fetching real-time data via **Tavily**, analyzing it with **Groq's Llama 3**, and synthesizing comprehensive answers.

### 🌟 Key Features
- **Multi-Agent Orchestration**: Specialized agents (Search, Reasoning, Answer) working in a directed cyclic graph.
- **Ultra-Fast Inference**: Powered by **Groq LPU** for near-instantaneous LLM responses.
- **Real-Time Web Search**: Integrated **Tavily API** to minimize hallucinations and provide up-to-date facts.
- **Enterprise Architecture**: Decoupled Frontend (Streamlit) and Backend (FastAPI) for scalability.
- **DevSecOps Pipeline**: Full CI/CD automation with Docker, Jenkins, and SonarQube quality gates.

---

## 💻 User Interface & Experience

The application features a premium, user-friendly **Streamlit** dashboard designed for ease of use and visual appeal.

### 🎬 1. Live Demo Tab
- **Interactive Chat**: A chat interface to interact with the AI Swarm.
- **Quick Starts**: Pre-defined prompts for news, coding, health, and travel to get started instantly.
- **Agent Identity**: Customize the persona of your AI assistant (e.g., Researcher, Coder, Analyst).

### 📖 2. About Project
- **Workflow Explainer**: A detailed breakdown of how the agents collaborate.
- **Use Cases**: Examples of how this system can be applied in real-world scenarios like market research and code debugging.

### 🔧 3. Tech Stack
- **Visual Cards**: Interactive display of the core technologies (Groq, LangChain, Docker, etc.).
- **Code Quality**: Dedicated section explaining SonarQube integration for bug tracking and code smell detection.

### 🏗️ 4. System Architecture
- **Interactive Graphs**: Visual representation of the LangGraph workflow and backend system design.
- **Gallery**: Collection of architectural diagrams showing the end-to-end data flow.

### 📋 5. System Logs
- **Live Monitoring**: Real-time view of system logs (INFO, ERRORS, WARNINGS).
- **Diagnostics**: Indicators for system health and downloadable log files for debugging.

---

## 🛠️ Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **AI Core** | **Groq (Llama 3)** | High-speed LLM Inference Engine |
| | **LangGraph** | Agentic Orchestration & State Management |
| | **LangChain** | LLM Framework & Tooling |
| | **Tavily** | AI-Optimized Web Search Tool |
| **Application** | **Streamlit** | Interactive Frontend UI |
| | **FastAPI** | High-Performance Backend API |
| **DevOps** | **Docker** | Containerization & Portability |
| | **Jenkins** | CI/CD Automation Pipelines |
| | **SonarQube** | Code Quality & Security Analysis |
| | **AWS ECS Fargate** | Serverless Cloud Deployment |
| | **GitHub** | Source Code Management (SCM) |

---

## ⚙️ Project Setup & Installation

### Prerequisites
- Python 3.10+
- Docker (optional, for containerization)
- API Keys: `GROQ_API_KEY`, `TAVILY_API_KEY`

### 1. Local Installation

```bash
# Clone the repository
git clone https://github.com/Ratnesh-181998/Enterprise-Multi-AI-Agent-Systems-.git
cd Enterprise-Multi-AI-Agent-Systems-

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up Environment Variables
# Create a .env file and add your keys:
# GROQ_API_KEY=your_key
# TAVILY_API_KEY=your_key

# Run the Application
streamlit run Multi_Agent_streamlit_app.py
```

### 2. Docker Deployment

```bash
# Build the Docker image
docker build -t multi-ai-agent .

# Run the container
docker run -p 8501:8501 --env-file .env multi-ai-agent
```

---

## 📞 Contact

**RATNESH SINGH**

- 📧 **Email**: [rattudacsit2021gate@gmail.com](mailto:rattudacsit2021gate@gmail.com)
- 💼 **LinkedIn**: [Ratnesh Kumar Singh](https://www.linkedin.com/in/ratneshkumar1998/)
- 🐙 **GitHub**: [Ratnesh-181998](https://github.com/Ratnesh-181998)
- 📱 **Phone**: +91-947XXXXX46

### 🔗 Project Links

- 🌐 **Live Demo**: [Streamlit App](https://agentic-ai-trip-planner-crewai-ykagvec2ng6raotrdaw6sp.streamlit.app/)
- 📖 **Documentation**: [GitHub Wiki](https://github.com/Ratnesh-181998/Enterprise-Multi-AI-Agent-Systemsr-/wiki)
- 🐛 **Issue Tracker**: [GitHub Issues](https://github.com/Ratnesh-181998/Enterprise-Multi-AI-Agent-Systems-/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Ratnesh-181998/Enterprise-Multi-AI-Agent-Systems-/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project handles large files using **Git LFS**. Ensure you have Git LFS installed if you plan to clone and contribute with large assets.
