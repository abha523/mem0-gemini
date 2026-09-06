import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
CHAT_MODEL = "gemini-3.1-flash-lite"

def generate_reply(user_msg: str, memories: list[str]) -> str:
    memory_block = "\n".join(f"- {m}" for m in memories) or "No memories yet."
    system_instruction = (
        "You are a helpful assistant with long-term memory of this user.\n"
        f"Known facts about the user:\n{memory_block}\n"
        "Use them naturally. Don't mention that you have a memory system."
    )
    
    response = client.models.generate_content(
        model=CHAT_MODEL,
        contents=user_msg,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=[{"google_search": {}}],
        ),
    )
    return response.text
