import os
from dotenv import load_dotenv
from mem0 import Memory

load_dotenv()

MEM0_CONFIG = {
    "llm": {
        "provider": "gemini",
        "config": {
            "model": "gemini-3.1-flash-lite",
            "api_key": os.environ["GOOGLE_API_KEY"],
            "temperature": 0.2,
            "max_tokens": 2000,
        },
    },
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "models/gemini-embedding-001",
            "api_key": os.environ["GOOGLE_API_KEY"],
            "embedding_dims": 768,
            "output_dimensionality": 768,
        },
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "mem0_gemini",
            "path": "./qdrant_data",
            "embedding_model_dims": 768,
        },
    },
}

def get_memory() -> Memory:
    return Memory.from_config(MEM0_CONFIG)
