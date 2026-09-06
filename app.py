import ollama
from memory import add_memory, search_memory


USER_ID = "user_1"


def chat(user_message):
    # Find relevant memories
    memories = search_memory(USER_ID, user_message)

    # Convert memories into text
    memory_text = "\n".join(
        memory["memory"]
        for memory in memories["results"]
    )

    # Give the AI the memories as context
    prompt = f"""
You are a helpful personal AI assistant.

Here are some things you remember about the user:
{memory_text}

User's new message:
{user_message}
"""

    # Ask Ollama for a response
    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    # Save the conversation as memory
    add_memory(
        USER_ID,
        f"User said: {user_message}\nAssistant replied: {answer}"
    )

    return answer


if __name__ == "__main__":
    print("Personal AI Memory Assistant")
    print("Type 'quit' to exit.\n")

    while True:
        user_message = input("You: ")

        # Ignore empty messages
        if not user_message.strip():
            continue

        # Exit the program
        if user_message.lower() == "quit":
            close_memory()
            break

        answer = chat(user_message)

        print(f"\nAI: {answer}\n")
