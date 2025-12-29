import streamlit as st
import requests
import json
import os
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Multi AI Agent System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium design
st.markdown("""
<style>
    /* Enhanced Multi-Color Theme */
    :root {
        --primary-gold: #FFD700;
        --secondary-gold: #FFC800;
        --accent-blue: #2874f0;
        --accent-green: #2ecc71;
        --accent-orange: #ff9f43;
        --accent-purple: #9b59b6;
        --accent-cyan: #00d4ff;
        --background-dark: #141E30; 
        --card-bg: rgba(36, 59, 85, 0.6); 
        --text-light: #ecf0f1; 
        --text-dim: #bdc3c7;   
        --hover-glow: rgba(46, 204, 113, 0.6);
    }
    
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }

    strong, b {
        color: var(--primary-gold);
        font-weight: 700;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 3px solid var(--accent-green);
    }

    h1 { color: var(--accent-cyan) !important; text-shadow: 0 0 40px rgba(0, 212, 255, 0.6); }
    h2 { color: var(--accent-blue) !important; }
    h3 { color: var(--accent-green) !important; }
    
    .stCard {
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.9) 0%, rgba(37, 43, 59, 0.9) 100%);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(40, 116, 240, 0.2);
        border: 2px solid rgba(40, 116, 240, 0.3);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        color: #ffffff;
        border-radius: 25px;
        font-weight: 700;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(155, 89, 182, 0.6);
    }

    /* Chat Styling */
    .user-message {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-cyan) 100%);
        padding: 15px; border-radius: 15px; margin: 10px 0 10px 20%; color: white;
    }
    .bot-message {
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.95) 0%, rgba(42, 49, 66, 0.95) 100%);
        padding: 15px; border-radius: 15px; margin: 10px 20% 10px 0; border: 1px solid var(--accent-green); color: white;
    }
</style>
""", unsafe_allow_html=True)

# Helper for absolute paths
def get_abs_path(relative_path):
    return os.path.abspath(relative_path)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='background: #ffffff; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #2874f0;'>
        <h2 style='color: #2874f0; margin: 0;'>🤖 Multi AI Agent</h2>
        <p style='color: #666; font-size: 0.9rem; font-weight: bold;'>ADVANCED ORCHESTRATION</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.2) 0%, rgba(40, 116, 240, 0.2) 100%); 
                padding: 15px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.4);'>
        <p style='margin: 5px 0; color: #00d4ff; font-weight: 600;'>Ratnesh Kumar Singh</p>
        <p style='margin: 5px 0; font-size: 0.9rem;'>
            🔗 <a href='https://github.com/Ratnesh-181998' style='color: #2874f0; text-decoration: none;'>GitHub</a> | 
            <a href='https://www.linkedin.com/in/ratneshkumar1998/' style='color: #9b59b6; text-decoration: none;'>LinkedIn</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Project Info")
    st.info("A powerful Multi-Agent System using Groq LLMs and Tavily Search.")

# Professional Badge at Top
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("")  # Empty space for alignment

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2874f0 0%, #9b59b6 100%); 
                padding: 6px 12px; border-radius: 6px; 
                box-shadow: 0 2px 8px rgba(40, 116, 240, 0.4);
                border: 1px solid rgba(155, 89, 182, 0.3);
                text-align: center;
                margin-bottom: 10px;'>
        <p style='margin: 0; color: #ffffff; font-weight: 700; font-size: 0.7rem; line-height: 1.5;'>
            <strong>Ratnesh Kumar Singh</strong><br>
            Data Scientist (AI/ML) | 4+ Yrs
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown("""
<div style='text-align: center; padding: 15px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 12px; margin-bottom: 15px; border: 2px solid rgba(40, 116, 240, 0.4);'>
<div style='display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 8px; flex-wrap: wrap;'>
<h1 style='color: #00d4ff; margin: 0; font-size: 1.8rem; font-weight: 800; text-shadow: 0 0 15px rgba(0, 212, 255, 0.5); letter-spacing: 1px; line-height: 1;'>
MULTI AI AGENT SYSTEMS
</h1>
</div>
<p style='font-size: 1.0rem; color: #e8e8e8; font-weight: 500; margin: 0; letter-spacing: 0.5px;'>
🤖 Advanced Multi-Agent Orchestration using LangGraph & Groq
</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎬 Demo Project", 
    "📖 About Project", 
    "🔧 Tech Stack",
    "🏗️ System Architecture", 
    "📋 System Logs"
])

# --- TAB 1: DEMO ---
with tab1:
    st.header("🤖 Live Agent Demo")
    
    # Welcome Container
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                padding: 15px; border-radius: 12px; border: 1px solid rgba(40, 116, 240, 0.2); margin-bottom: 20px;
                border-left: 5px solid #00d4ff;'>
        <h3 style='color: #00d4ff; margin: 0 0 5px 0;'>👋 Welcome to the Ratnesh AI Agent Workspace</h3>
        <p style='color: #e8e8e8; margin: 0; font-size: 0.95rem;'>
            Configure your specialized AI agent and start collaborating! 
            Enable <b>Web Search</b> to give your agent access to real-time information.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Configuration (Collapsible for cleaner UI)
    with st.expander("⚙️ Agent Configuration & Settings", expanded=True):
        c1, c2 = st.columns([1, 1])
        with c1:
            # Enhanced Agent Identity Selection
            agent_role_selected = st.selectbox(
                "Select AI Agent Identity:", 
                ["Research Assistant", "Python Developer", "Data Scientist", "Market Analyst", "Content Writer", "Medical Researcher", "Travel Planner", "Custom..."],
                help="Choose a specialized role or creating your own."
            )
            
            if agent_role_selected == "Custom...":
                agent_name = st.text_input("Enter Custom Agent Name:", value="General Assistant")
            else:
                agent_name = agent_role_selected

            model = st.selectbox("Select AI Model:", [
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant",
                "mixtral-8x7b-32768"
            ], help="Choose the brain for your agent. Llama 3 70B is best for complex tasks.")
        with c2:
            st.write("") # Spacer
            st.write("")
            allow_search = st.checkbox("Enable Web Search (Tavily)", value=True, help="Allows the agent to browse the internet for up-to-date info.")
            
    # Chat History Container
    chat_container = st.container()
    
    # Quick Action Buttons
    # Quick Action Buttons
    st.markdown("### 🚀 Quick Starts & Sample Queries")
    
    # Row 1
    q1, q2, q3, q4 = st.columns(4)
    if q1.button("📰 AI News", use_container_width=True, help="Find latest AI developments"):
        st.session_state.messages.append({"role": "user", "content": "Search for the latest breaking news in Artificial Intelligence and summarize top 3 headlines."})
    if q2.button("🐍 Py Script", use_container_width=True, help="Generate Python code"):
         st.session_state.messages.append({"role": "user", "content": "Write a Python script to visualize stock data using matplotlib."})
    if q3.button("📊 Stocks", use_container_width=True, help="Analyze market trends"):
        st.session_state.messages.append({"role": "user", "content": "What is the current performance of major tech stocks like NVDA, AAPL, and MSFT?"})
    if q4.button("� Explain", use_container_width=True, help="Explain complex topics"):
        st.session_state.messages.append({"role": "user", "content": "Explain the concept of Quantum Computing to a 10-year-old."})

    # Row 2
    q5, q6, q7, q8 = st.columns(4)
    if q5.button("✍️ Writer", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Write a professional blog post about 'The Future of Agentic AI' with distinct sections."})
    if q6.button("🏥 Health", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Search for recent peer-reviewed studies on the benefits of intermittent fasting."})
    if q7.button("🌍 Travel", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Plan a 3-day itinerary for a trip to Tokyo, Japan, focusing on food and technology."})
    if q8.button("🐛 Debug", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "I have a Python list index out of range error. Explain why this happens and how to fix it with examples."})

    # Display Chat
    with chat_container:
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if not st.session_state.messages:
             st.info("Start the conversation by typing a message below or using a Quick Start button above!")

        for msg in st.session_state.messages:
            role_class = "user-message" if msg["role"] == "user" else "bot-message"
            role_icon = "👤" if msg["role"] == "user" else "🤖"
            
            # Custom display names
            display_name = "Ratnesh AI Assistant" if msg["role"] == "assistant" else "You"
            
            # Basic timestamp simulation (optional enhancement)
            time_str = datetime.now().strftime("%H:%M") 
            
            st.markdown(f"""
            <div class='{role_class}'>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                    <strong>{role_icon} {display_name}</strong>
                    <span style="font-size: 0.7rem; opacity: 0.7;">{time_str}</span>
                </div>
                {msg['content']}
            </div>
            """, unsafe_allow_html=True)

    # Input Area
    st.markdown("---")
    
    # Custom Input Layout
    input_col, btn_col1, btn_col2 = st.columns([8, 1.5, 1.5])
    
    with input_col:
        # User input field
        query = st.text_input("Message:", label_visibility="collapsed", placeholder="💬 Type your message here...", key="user_query_input")

    with btn_col1:
        # Submit/Enter Button
        enter_pressed = st.button("📤 Send", use_container_width=True, type="primary")

    with btn_col2:
        # Clear Conversation Button
        clear_pressed = st.button("🧹 Clear", use_container_width=True, type="primary")
    
    if clear_pressed:
        st.session_state.messages = []
        st.rerun()
    
    # Handle Input (From Text Input or Quick Buttons)
    if enter_pressed and query:
        st.session_state.messages.append({"role": "user", "content": query})
    elif query and "quick_query" in st.session_state: # Handle quick button injection if needed, though they append directly
        pass 
    
    # Logic to handle if a quick button was pressed (they append directly to messages)
    # The original code appended to messages immediately.
    # We just need to check if we need to run the backend.
    
    # Trigger Backend Call if last message is User
    # We use a flag or check if the last message is new/unanswered
    # Simple check: if last message is user, call backend.
    
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        last_user_query = st.session_state.messages[-1]["content"]
        
        # Call Backend
        API_URL = "http://127.0.0.1:9999/chat"
        payload = {
            "model_name": model,
            "system_prompt": agent_name,
            "messages": [last_user_query],
            "allow_search": allow_search
        }
        
        try:
            with st.spinner(f"🤖 {agent_name} is thinking & searching..."):
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    ans = response.json().get("response", "No response")
                    st.session_state.messages.append({"role": "assistant", "content": ans})
                    st.rerun()
                else:
                    st.error(f"Backend Error: {response.text}")
        except Exception as e:
            st.error(f"Connection Failed: {str(e)}")

# --- TAB 2: ABOUT ---
with tab2:
    st.header("📖 About The Project")
    st.markdown("""
    ### 🚀 Overview
    This project demonstrates a robust **Multi-AI Agent System** tailored for complex reasoning and real-time information retrieval. 
    It bridges the gap between static LLM knowledge and dynamic world information using **Tavily Search**.

    ### ✨ Key Features
    *   **Orchestration**: Built on **LangGraph** for stateful, cyclical agentic workflows.
    *   **Search**: Integrated **Tavily API** for high-precision, AI-optimized web search.
    *   **Models**: Powered by **Groq's LPU** inference engine for near-instant responses using Llama 3.
    *   **Architecture**: Fully containerized with Docker, deployed via AWS ECS Fargate.
    
    ### 🎯 Use Cases
    1.  **Market Research**: Fetch and synthesize latest news.
    2.  **Code Assistant**: Debug and research documentation simultaneously.
    3.  **Fact Checking**: Verify claims against live web sources.

    ---
    ### 🛠️ Step-by-Step Implementation Workflow

    #### **Step 1: Define the Problem**
    Modern AI applications must be accurate, scalable, and maintainable. Single-LLM systems struggle with complex reasoning. This project addresses this by building a **Multi-AI Agent system** with strict **code quality** and **CI/CD** automation.

    #### **Step 2: High-Level Architecture**
    *   **Frontend**: Streamlit (User Interface)
    *   **Backend**: FastAPI
    *   **AI Engine**: LangChain + LangGraph (Multi-Agent)
    *   **Search**: Tavily (Online Context)
    *   **Inference**: Groq (Fast LLM Support)
    *   **Quality**: SonarQube
    *   **CI/CD**: Jenkins -> Docker -> AWS ECS Fargate

    #### **Step 3: Build the Multi-Agent AI System**
    Instead of a monolithic model, we use specialized agents:
    *   **Search Agent**: Uses Tavily for real-time data.
    *   **Reasoning Agent**: Processes search results using Groq.
    *   **Answer Agent**: Formulates user-friendly responses.
    *   **LangGraph**: Orchestrates flow and manages state.

    #### **Step 4: Backend APIs with FastAPI**
    Exposes REST endpoints to trigger the agent workflow. Ensures high performance and async support for valid real-time interaction.

    #### **Step 5: Frontend with Streamlit**
    Provides an interactive UI for instant feedback, prototyping, and stakeholder demos.

    #### **Step 6: Containerization (Docker)**
    Ensures environment consistency across Dev, Test, and Prod. Packages API, Agents, and dependencies into a single portable image.

    #### **Step 7: Code Quality (SonarQube)**
    *   **Bugs**: Detects logical errors.
    *   **Code Smells**: Identifies bad practices (e.g., long functions).
    *   **Duplication**: Promotes modular, reusable code.

    #### **Step 8: Automate CI/CD (Jenkins)**
    Automates fetching code, running analysis, building Docker images, and deploying to AWS. Removes human error from the release process.

    #### **Step 9: Cloud Deployment (AWS ECS Fargate)**
    Serverless container execution for auto-scaling and reduced infrastructure management.

    #### **Step 10: Version Control (GitHub)**
    Acts as the source of truth and triggers the CI/CD pipeline upon code changes.

    ---
    **One-Line Summary:**  
    *“I built a cloud-native Multi-AI Agent system using LangGraph and LangChain, powered by Groq LLMs and Tavily search, with FastAPI and Streamlit, containerized using Docker, quality-checked with SonarQube, automated via Jenkins, and deployed on AWS ECS Fargate.”*
    """)

# --- TAB 3: TECH STACK ---
with tab3:
    st.header("🔧 Technology Stack")
    
    # 1. Visual Tech Stack Display
    st.markdown("### 🛠️ Core Technologies")
    
    st.markdown("""
    <style>
    .tech-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        transition: transform 0.3s ease;
    }
    .tech-card:hover {
        transform: translateY(-5px);
        border-color: #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.subheader("🧠 AI & Logic")
        st.markdown("""
        <div class="tech-card">
            <strong>Groq</strong><br><span style="font-size:0.8em; color:#bbb;">Ultra-fast LLM Inference Engine</span>
        </div>
        <div class="tech-card">
            <strong>LangGraph</strong><br><span style="font-size:0.8em; color:#bbb;">Agentic AI Orchestration</span>
        </div>
        <div class="tech-card">
            <strong>LangChain</strong><br><span style="font-size:0.8em; color:#bbb;">Generative AI Framework</span>
        </div>
        <div class="tech-card">
            <strong>Tavily</strong><br><span style="font-size:0.8em; color:#bbb;">AI-Optimized Search Tool</span>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.subheader("� Application")
        st.markdown("""
        <div class="tech-card">
            <strong>Streamlit</strong><br><span style="font-size:0.8em; color:#bbb;">Interactive Frontend UI</span>
        </div>
        <div class="tech-card">
            <strong>FastAPI</strong><br><span style="font-size:0.8em; color:#bbb;">High-Perf Backend APIs</span>
        </div>
        <div class="tech-card">
            <strong>Python</strong><br><span style="font-size:0.8em; color:#bbb;">Core Programming Language</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.subheader("🚀 DevOps & Cloud")
        st.markdown("""
        <div class="tech-card">
            <strong>Docker</strong><br><span style="font-size:0.8em; color:#bbb;">Containerization</span>
        </div>
        <div class="tech-card">
            <strong>Jenkins</strong><br><span style="font-size:0.8em; color:#bbb;">CI/CD Pipelines</span>
        </div>
        <div class="tech-card">
            <strong>AWS ECS Fargate</strong><br><span style="font-size:0.8em; color:#bbb;">Serverless Cloud Deployment</span>
        </div>
        <div class="tech-card">
            <strong>SonarQube</strong><br><span style="font-size:0.8em; color:#bbb;">Code Quality & Security</span>
        </div>
         <div class="tech-card">
            <strong>GitHub</strong><br><span style="font-size:0.8em; color:#bbb;">Source Code Management</span>
        </div>
        """, unsafe_allow_html=True)

    # Detailed Tech Stack List
    st.markdown("### 🔍 Detailed Tech Breakdown")
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px;">
        <ul style="list-style-type: none; padding-left: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>1. Groq:</strong> LLM Inference Engine for speed.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>2. Tavily:</strong> Online Search Tool for real-time validation.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>3. LangChain:</strong> Generative AI Framework to interact with LLMs.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>4. LangGraph:</strong> Agentic AI Framework to make AI Agents.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>5. FastAPI:</strong> To build backend APIs for handling user requests.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>6. Streamlit:</strong> To make UI or frontend of the app.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>7. Docker:</strong> For containerization of the app during deployment.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>8. SonarQube:</strong> Code quality evaluator (Bugs, Security, Bad Practices).</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>9. Jenkins:</strong> For making CI/CD pipelines.</li>
            <li style="margin-bottom: 15px; padding-bottom: 5px; border-bottom: 1px solid rgba(255,255,255,0.05);"><strong>10. AWS ECS Fargate:</strong> Serverless compute engine to run app on cloud.</li>
            <li style="margin-bottom: 0;"><strong>11. GitHub:</strong> Source Code Management (SCM) system.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # 2. SonarQube Deep Dive (Interactive)
    st.subheader("🛡️ Code Quality Focus: SonarQube")
    st.info("We use SonarQube to ensure our codebase remains clean, secure, and maintainable.")
    
    sq_col1, sq_col2, sq_col3 = st.columns(3)
    with sq_col1:
        with st.expander("🐛 1. Bugs", expanded=True):
            st.write("Detects logical errors and dead code that breaks the app.")
            st.code("""
# Example Dead Code
if msg == "hi":
    print("Hi")
elif msg == "hi": # Unreachable!
    print("Hi 2nd")
            """, language="python")

    with sq_col2:
        with st.expander("🤢 2. Code Smells", expanded=True):
            st.write("Identifies bad practices like massive functions (300+ lines).")
            st.markdown("**Solution:** Split into `func1`, `func2`, `func3`.")
            st.success("✅ Benefits: Readability & Easier Analysis")

    with sq_col3:
        with st.expander("♻️ 3. Duplication", expanded=True):
            st.write("Finds repeated blocks of code across `app.py`, `main.py`, etc.")
            st.warning("⚠️ Reduces maintainability if not fixed.")

    st.markdown("---")



# --- TAB 4: SYSTEM ARCHITECTURE ---
with tab4:
    st.subheader("🏗️ Architecture Diagram")
    
    # 1. Architecture Visuals (Preserved)
    img_locations = [
        os.path.join(os.getcwd(), "CODE", "Multi+AI+Agent+Workflow.png"),
        os.path.join(os.getcwd(), "Multi+AI+Agent+Workflow.png"),
        os.path.join(os.getcwd(), "Screenshot 2025-12-29 095100.png")
    ]
    
    img_shown = False
    for img_path in img_locations:
        if os.path.exists(img_path):
            st.image(img_path, caption="System Workflow", use_container_width=True)
            img_shown = True
            break
    
    if not img_shown:
        st.error("Architecture image not found in standard locations.")

    st.markdown("---")

    # 2. Key Workflow Steps (Static Display)
    st.markdown("### 🔄 System Workflow breakdown")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**1. User Query**\n\nFrontend (Streamlit) packages user prompt into JSON.")
    with c2:
        st.warning("**2. API Gateway**\n\nFastAPI handles validation & auth.")
    with c3:
        st.error("**3. Orchestration**\n\nLangGraph directs flow based on intent.")

    c4, c5 = st.columns([1.5, 1.5])
    with c4:
        st.success("**4. Collaborative Agents**\n\nSearch (Tavily) + Reasoning (Llama-3) + Answer Agents.")
    with c5:
        st.info("**5. Response Delivery**\n\nFinal output stream returned to UI.")

    st.markdown("---")

    # 3. Component Deep Dive (New)
    st.markdown("### 🧩 Technical Components")
    ac1, ac2 = st.columns(2)
    
    with ac1:
        with st.expander("🐝 Agent Swarm (LangGraph)", expanded=False):
            st.write("""
            The core intelligence is managed by **LangGraph**, which defines a cyclic graph:
            1.  **Nodes**: Represent agents (Search, Reasoner).
            2.  **Edges**: Define the transition logic.
            3.  **State**: Shared context passed between agents.
            """)
            
    with ac2:
        with st.expander("💾 External Memory & Search", expanded=False):
            st.write("""
            To prevent hallucinations, we use **RAG (Retrieval-Augmented Generation)** principles:
            - **Tavily API**: Fetches real-time, high-quality search results.
            - **Context Window**: Properly managed to fit within LLM limits.
            """)

    st.markdown("---")
    st.subheader("📸 Additional Architecture Diagrams")
    
    # Relative path for portable deployment
    archi_dir = os.path.join(os.getcwd(), "Archi_Diagram")

    # Mapping filenames to descriptive titles/content
    image_metadata = {
        "Screenshot 2025-12-29 094816.png": "Integrated Tech Stack: Groq, Tavily, LangGraph & Docker",
        "Screenshot 2025-12-29 095100.png": "Agentic Workflow Construction: Input -> Orchestration -> Output",
        "Screenshot 2025-12-29 095126.png": "Backend Request Flow: FastAPI & LangChain Integration",
        "Screenshot 2025-12-29 095148.png": "Multi-Agent Interaction Loop: Researcher, Router & Generator",
        "Screenshot 2025-12-29 095214.png": "System Deployment Architecture: Containerization & Cloud",
        "Screenshot 2025-12-29 095240.png": "Real-time Search Integration Strategy",
        "Screenshot 2025-12-29 095303.png": "UI Chat Conversation"
    }
    
    if os.path.exists(archi_dir):
        archi_files = sorted([f for f in os.listdir(archi_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        if archi_files:
            for file_name in archi_files:
                img_path = os.path.join(archi_dir, file_name)
                
                # Get description or fallback to a clean name
                title_text = image_metadata.get(file_name, f"Architecture Diagram: {file_name}")
                
                # Display Content Line & Image
                st.markdown(f"#### 📌 {title_text}")
                st.image(img_path, caption=title_text, use_container_width=True)
                st.markdown("---")
        else:
             st.info("No additional architecture images found in the folder.")
    else:
        st.warning(f"Architecture folder not found at: {archi_dir}")

# --- TAB 5: SYSTEM LOGS ---
with tab5:
    st.header("📋 System Logs")
    st.markdown("Monitor the internal state, debug information, and execution logs of the Multi-Agent System.")

    # 1. Controls & File Selection
    col_refresh, col_file = st.columns([1, 3])
    with col_refresh:
        if st.button("🔄 Refresh Logs", use_container_width=True):
            st.rerun()
            
    # 2. Log File Viewer & Parsing
    # Use absolute path based on script location for better cloud compatibility
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "logs")
    
    # Ensure logs directory exists to prevent "not found" errors
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
        
    if os.path.exists(log_dir):
        log_files = sorted(os.listdir(log_dir), reverse=True)
        if log_files:
            with col_file:
                selected_log = st.selectbox("Select Log File:", log_files, index=0, label_visibility="collapsed")
            
            log_path = os.path.join(log_dir, selected_log)
            
            # File Metadata
            try:
                file_stats = os.stat(log_path)
                file_size_kb = file_stats.st_size / 1024
                # FIX: datetime is imported as 'from datetime import datetime', so use datetime.fromtimestamp directly
                mod_time = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            except Exception as e:
                mod_time = "Unknown"
                file_size_kb = 0
            
            st.caption(f"📅 Last Modified: **{mod_time}** | 📦 Size: **{file_size_kb:.2f} KB**")

            # Parse Log Content
            log_lines = []
            info_count = 0
            error_count = 0
            warning_count = 0
            
            with open(log_path, "r", encoding='utf-8', errors='ignore') as f:
                raw_lines = f.readlines()
                for line in raw_lines:
                    line = line.strip()
                    if not line: continue
                    
                    # Basic classification based on keywords
                    level = "INFO"
                    if "ERROR" in line.upper(): 
                        level = "ERROR"
                        error_count += 1
                    elif "WARNING" in line.upper(): 
                        level = "WARNING"
                        warning_count += 1
                    elif "SUCCESS" in line.upper(): 
                        level = "SUCCESS"
                        info_count += 1 # Treat success as info category for stats
                    else:
                        info_count += 1
                        
                    log_lines.append({"content": line, "level": level})

            # --- FLIPKART STYLE UI ---
            st.markdown("---")
            
            # Summary Metrics
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f"""
                <div style='background: rgba(46, 204, 113, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2ecc71; text-align: center;'>
                    <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>INFO EVENTS</h4>
                    <p style='color: #2ecc71; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{info_count}</p>
                </div>
                """, unsafe_allow_html=True)
            with m2:
                err_color = "#e74c3c" if error_count > 0 else "#95a5a6"
                st.markdown(f"""
                <div style='background: rgba(231, 76, 60, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid {err_color}; text-align: center;'>
                    <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>ERRORS</h4>
                    <p style='color: {err_color}; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{error_count}</p>
                </div>
                """, unsafe_allow_html=True)
            with m3:
                warn_color = "#f39c12" if warning_count > 0 else "#95a5a6"
                st.markdown(f"""
                <div style='background: rgba(243, 156, 18, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid {warn_color}; text-align: center;'>
                    <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>WARNINGS</h4>
                    <p style='color: {warn_color}; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{warning_count}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")

            # Filters & Download
            c_filter, c_down = st.columns([3, 1])
            with c_filter:
                level_filter = st.multiselect(
                    "🔽 Filter Logs by Level", 
                    ["INFO", "WARNING", "ERROR", "SUCCESS"], 
                    default=["INFO", "WARNING", "ERROR", "SUCCESS"]
                )
            
            with c_down:
                 st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True) 
                 st.download_button(
                    label="📥 Download",
                    data="\n".join([l["content"] for l in log_lines]),
                    file_name=selected_log,
                    mime="text/plain",
                    use_container_width=True
                )

            # Styled Scrollable Log Feed
            st.markdown("### 📜 Log Feed")
            log_container = st.container(height=500)
            
            with log_container:
                if log_lines:
                    # Show latest at bottom for file logs? usually files are top-to-bottom. 
                    # User might prefer latest (bottom of file) at top of view? 
                    # Let's show in reverse order (newest first) as it is usually more useful.
                    for log in reversed(log_lines):
                        if log['level'] in level_filter:
                            msg = log['content']
                            if log['level'] == 'ERROR':
                                st.error(msg, icon="🚨")
                            elif log['level'] == 'WARNING':
                                st.warning(msg, icon="⚠️")
                            elif log['level'] == 'SUCCESS':
                                st.success(msg, icon="✅")
                            else:
                                st.info(msg, icon="ℹ️")
                else:
                    st.info("📭 Log file is empty.")

        else:
            st.info("No log files found in logs directory.")
    else:
        st.error(f"Logs directory not found: {log_dir}")

st.markdown("---")

# Footer container
st.markdown("""
<div style='text-align: center; padding: 20px 20px 10px 20px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 10px; border-top: 2px solid #2874f0;'>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>🤖 Multi AI Agent System</p>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>Built with ❤️ by Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer 4+Years Exp)</p>
    <p style='font-size: 0.9rem; color: #e8e8e8; margin-bottom: 5px;'>Powered by LangGraph, LangChain, Groq, Tavily, and Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Social links using Streamlit columns (inside the visual footer area)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://github.com/Ratnesh-181998" target="_blank" style="text-decoration: none; color: #2874f0; font-size: 1.1rem; font-weight: 600;">🔗 GitHub</a></p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="mailto:rattudacsit2021gate@gmail.com" style="text-decoration: none; color: #26a65b; font-size: 1.1rem; font-weight: 600;">📧 Email</a></p>', unsafe_allow_html=True)

with col4:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://www.linkedin.com/in/ratneshkumar1998/" target="_blank" style="text-decoration: none; color: #0077b5; font-size: 1.1rem; font-weight: 600;">💼 LinkedIn</a></p>', unsafe_allow_html=True)

# Close the visual footer
st.markdown("""
<div style='height: 10px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 0 0 10px 10px; border-bottom: 2px solid #2874f0; margin-top: -10px;'></div>
""", unsafe_allow_html=True)
