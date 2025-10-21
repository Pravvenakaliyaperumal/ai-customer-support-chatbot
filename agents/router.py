from agents.claude_agent import ask_claude
from agents.gemini_agent import ask_gemini
from utils.prompt_manager import build_prompt

def handle_query(user_message: str) -> str:
    # Basic routing: factual → Gemini, conversational → Claude
    if any(word in user_message.lower() for word in ["price", "schedule", "details", "duration"]):
        prompt = build_prompt(user_message, context_type="factual")
        return ask_gemini(prompt)
    else:
        prompt = build_prompt(user_message, context_type="conversational")
        return ask_claude(prompt)
