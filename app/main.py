from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .memory_service import recall, remember, memory
from .chat_service import generate_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    memories = recall(req.message, req.user_id)
    reply = generate_reply(req.message, memories)
    remember(req.message, reply, req.user_id)
    return {"reply": reply, "memories_used": memories}

@app.get("/memories/{user_id}")
def get_memories(user_id: str):
    return memory.get_all(user_id=user_id)

@app.delete("/memories/{user_id}")
def clear_memories(user_id: str):
    memory.delete_all(user_id=user_id)
    return {"status": "cleared"}
