# 🤖 AI Customer Support Chatbot

This project demonstrates an **end-to-end LLM chatbot** that combines reasoning (Claude) and retrieval (Gemini) to deliver smart, context-aware responses for customer support use cases.

### 🧱 Architecture
- Flask API for chat handling
- Hybrid Claude + Gemini agent routing
- Prompt templates for factual vs. conversational tone
- n8n automation workflow for logging/analytics
- JSONL logging with latency tracking

### 🚀 Run Locally
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your_key"
export GEMINI_API_KEY="your_key"
python app.py
