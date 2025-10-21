def build_prompt(user_message: str, context_type: str = "factual") -> str:
    if context_type == "factual":
        system_prompt = "You are a helpful AI assistant providing accurate, structured information."
    else:
        system_prompt = "You are a friendly support assistant that communicates clearly and empathetically."
    
    return f"{system_prompt}\n\nUser: {user_message}\nAssistant:"
