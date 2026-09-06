# 🧠 Personal AI Memory
![Python Tests](https://github.com/VaishaliJojra/personal-ai-memory/actions/workflows/python-tests.yml/badge.svg)

A lightweight personal AI assistant that can **remember previous conversations and retrieve relevant memories** using completely local AI models.

The project combines **Python, Ollama, Mem0, and Qdrant** to create a privacy-focused conversational assistant that runs locally on a low-resource Windows machine.

## ✨ Features

* 💬 Interactive AI chat through the terminal
* 🧠 Persistent conversation memory
* 🔎 Semantic memory search
* 🤖 Local AI inference using Ollama
* 🔐 No OpenAI API required for the AI responses
* 💾 Local vector storage using Qdrant
* ⚡ Optimized for low-resource systems
* 🐍 Built with Python

## 🏗️ Architecture

```text
User
 │
 ▼
app.py
 │
 ├──────────────► Memory Search
 │                    │
 │                    ▼
 │                  Mem0
 │                    │
 │                    ▼
 │                  Qdrant
 │
 ▼
Ollama
 │
 └── qwen2.5:0.5b
        │
        ▼
     AI Response
        │
        ▼
   Save Conversation
        │
        ▼
      Qdrant
```

### Components

| Component            | Purpose                         |
| -------------------- | ------------------------------- |
| **Python**           | Application logic               |
| **Ollama**           | Runs AI models locally          |
| **Qwen 2.5 0.5B**    | Local conversational model      |
| **Mem0**             | Memory management and retrieval |
| **Qdrant**           | Local vector database           |
| **Nomic Embed Text** | Generates text embeddings       |
| **python-dotenv**    | Loads environment configuration |

## 📁 Project Structure

```text
personal-ai-memory/
│
├── app.py              # Main chat application
├── memory.py           # Memory storage and retrieval
├── config.py           # Environment configuration
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Files excluded from Git
│
├── data/               # Local Qdrant database (not uploaded)
├── .venv/              # Python virtual environment (not uploaded)
└── .env                # Local environment variables (not uploaded)
```

## ⚙️ How It Works

When the user enters a message:

1. The application searches the user's existing memories.
2. Relevant memories are retrieved from the local Qdrant vector database.
3. The retrieved memories are added to the AI prompt.
4. Ollama generates a response using the local Qwen model.
5. The conversation is saved as a new memory.
6. Future conversations can retrieve that information when relevant.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/VaishaliJojra/personal-ai-memory.git
cd personal-ai-memory
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama for Windows from the official Ollama website.

Then download the required models:

```powershell
ollama pull qwen2.5:0.5b
ollama pull nomic-embed-text
```

### 5. Run the application

Make sure Ollama is running, then:

```powershell
python app.py
```

You should see:

```text
Personal AI Memory Assistant
Type 'quit' to exit.
```

## 💬 Example

```text
You: My favorite programming language is Python.

AI: That's great! Python is a versatile language...

You: What is my favorite programming language?

AI: Your favorite programming language is Python.
```

The second response is generated using information retrieved from the assistant's stored memory.

## 🔒 Privacy

This project is designed to keep the AI workflow local.

The project uses:

* Local Ollama models
* Local Qdrant storage
* Local conversation memory

Sensitive configuration such as API keys and the local database are excluded from Git using `.gitignore`.

> Never commit `.env`, API keys, credentials, or other secrets to a public repository.

## ⚡ Performance Optimization

The project was designed with limited hardware resources in mind.

Memory storage uses Mem0's direct storage mode (`infer=False`) to avoid an additional LLM-based memory extraction step for every conversation.

This significantly reduces response time and makes the application more practical on systems with limited RAM.

## 🛠️ Technologies

**Languages**

* Python

**AI / ML**

* Ollama
* Qwen 2.5
* Nomic Embed Text

**Memory / Vector Search**

* Mem0
* Qdrant

**Development**

* Git
* GitHub
* VS Code

## 🔮 Future Improvements

Planned improvements include:

* [ ] Web-based chat interface
* [ ] User authentication
* [ ] Multiple user profiles
* [ ] Better memory organization
* [ ] Memory management interface
* [ ] Automated tests
* [ ] Docker support
* [ ] Performance benchmarking
* [ ] Conversation history interface

## 👩‍💻 Author

**Vaishali Jojra**

B.Tech Information Technology

Interested in Python, AI/ML, data analytics, and software development.

---

⭐ If you find this project interesting, feel free to explore the repository.
