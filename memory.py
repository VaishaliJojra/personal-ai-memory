from mem0 import Memory
import logging
logging.getLogger("mem0").setLevel(logging.ERROR)


config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "personal_ai_memory",
            "embedding_model_dims": 768,
            "path": "./data",
        }
    },

    "llm": {
        "provider": "ollama",
        "config": {
            "model": "qwen2.5:0.5b",
            "ollama_base_url": "http://localhost:11434",
        }
    },

    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",
            "ollama_base_url": "http://localhost:11434",
        }
    }
}


memory = Memory.from_config(config)


def add_memory(user_id, text):
    memory.add(
        text,
        user_id=user_id,
        infer=False
    )


def search_memory(user_id, query):
    results = memory.search(
        query,
        filters={"user_id": user_id}
    )

    return results
