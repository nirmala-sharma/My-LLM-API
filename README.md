# 🤖 LLM API — FastAPI + Ollama
> A local AI-powered REST API built with FastAPI and Ollama — no API key, no cost, runs entirely on your machine.

## 💡 About This Project

I built a REST API using FastAPI in Python that integrates with a local AI model through Ollama. The API has three endpoints — `/ask` for answering questions, `/summarize` for summarizing long text, and `/translate` for translating text into any language. I used Pydantic for request validation to make sure the inputs are always clean and correct, and added proper error handling for cases like empty inputs or the AI model not running. I also built a dark mode frontend in plain HTML and JavaScript that connects to the API, so anyone can use it directly from the browser without touching the docs. The whole AI runs locally on the machine using Llama 3.2 through Ollama, so there's no API key or cost involved.

---

## 📌 What This Project Does

This project exposes 3 API endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/ask` | POST | Ask the AI any question |
| `/summarize` | POST | Summarize a long piece of text |
| `/translate` | POST | Translate text to any language |

---

## 🛠️ Tech Stack

- **FastAPI** — Python web framework for building APIs
- **Ollama** — Runs AI models locally on your machine (no API key needed)
- **Llama 3.2** — The AI model used for all 3 endpoints
- **Pydantic** — Data validation for request bodies
- **Uvicorn** — Server to run the FastAPI app

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com) installed on your machine

### Step 1: Clone the project
```bash
git clone <your-repo-url>
cd my-llm-api
```

### Step 2: Create and activate virtual environment
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Step 3: Install dependencies
```bash
pip install fastapi uvicorn ollama pydantic
```

### Step 4: Pull the AI model
```bash
ollama pull llama3.2
```

### Step 5: Run the server
```bash
uvicorn llmapp:app --reload
```

### Step 6: Open the API docs
```
http://127.0.0.1:8000/docs
```

---

## 📮 API Endpoints

### POST `/ask`
Ask the AI any question.

**Request Body:**
```json
{
    "question": "What is Python?"
}
```

**Response:**
```json
{
    "answer": "Python is a high-level programming language..."
}
```

---

### POST `/summarize`
Summarize a long piece of text.

**Request Body:**
```json
{
    "text": "Your long text here..."
}
```

**Response:**
```json
{
    "summary": "A short summary of your text..."
}
```

---

### POST `/translate`
Translate text to any language.

**Request Body:**
```json
{
    "text": "Hello, how are you?",
    "language": "French"
}
```

**Response:**
```json
{
    "translation": "Bonjour, comment allez-vous?"
}
```

---

## ⚠️ Error Handling

The API handles the following errors:

| Error | Status Code | Reason |
|---|---|---|
| Empty fields | `400` | User sent empty text or question |
| Ollama not running | `500` | Ollama service is not started |
| Model not found | `500` | llama3.2 is not downloaded |

---

## 🎨 Frontend UI

A dark mode frontend is included to interact with all 3 endpoints visually.

To use it:
1. Start the FastAPI server first
2. Open `index.html` in your browser
3. Use the tabs to switch between Ask, Summarize and Translate

---

## 📁 Project Structure

```
MY-LLM-API/
├── index.html     # frontend UI
├── llmapp.py      # main application code
├── .gitignore.    # It includes files which are not upload/push to the remote origin
└── README.md      # project documentation
```

---

## 📝 Notes

- Make sure Ollama is running before starting the server
- The AI runs completely locally — no internet or API key needed
- You can test all endpoints directly at `http://127.0.0.1:8000/docs`
