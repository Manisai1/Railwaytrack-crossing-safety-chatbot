Railway Track Safety Chatbot
An AI-powered chatbot designed to provide accurate, real-time railway safety information using LLMs and retrieval-based techniques. Built during the AI for Good Hackathon 2025, this system focuses on delivering validated and context-aware responses for railway safety scenarios.

🧠 Overview
This project uses a combination of:

Retrieval-Augmented Generation (RAG)

Large Language Models (LLMs)

Structured prompt engineering

to ensure that responses are reliable, grounded, and relevant to railway safety use cases.

⚙️ Architecture
User Query → Retrieval System → Context Injection → LLM → Validated Response
🔹 Components
User Interface (Streamlit)
Simple and interactive UI for asking queries.

Retriever (RAG Pipeline)
Fetches relevant safety information from preloaded data.

LLM Layer (OpenAI / Groq)
Generates responses based on retrieved context.

Validation Layer
Ensures responses are accurate and aligned with safety guidelines.

🔥 Key Features
✅ Domain-specific chatbot for railway safety

✅ Context-aware responses using RAG

✅ Multi-model support (OpenAI, Groq)

✅ Structured prompt engineering for accuracy

✅ Fast and interactive UI using Streamlit

✅ Designed and deployed under hackathon constraints

🛠 Tech Stack
Language: Python

Frameworks: LangChain, Streamlit

LLMs: OpenAI, Groq

Vector Store: ChromaDB (or similar)

Concepts: RAG, Prompt Engineering, NLP



OpenAI / Groq API Key

