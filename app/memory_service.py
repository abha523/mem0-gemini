from .config import get_memory

memory = get_memory()

def recall(query: str, user_id: str, top_k: int = 5) -> list[str]:
    # Use filters={'user_id': user_id} as required by mem0 v2.x
    result = memory.search(query=query, filters={"user_id": user_id}, top_k=top_k)
    return [m["memory"] for m in result.get("results", [])]

def remember(user_msg: str, assistant_msg: str, user_id: str) -> None:
    messages = [
        {"role": "user", "content": user_msg},
        {"role": "assistant", "content": assistant_msg},
    ]
    memory.add(messages, user_id=user_id)
