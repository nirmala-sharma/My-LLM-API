from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import ollama
from pydantic import BaseModel

app = FastAPI()

# add this CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# define request bodies
class AskRequest(BaseModel):
    question: str

class SummarizeRequest(BaseModel):
    text: str

class TranslateRequest(BaseModel):
    text: str
    language: str


@app.post("/ask")
def ask(body: AskRequest):
  # check empty string
 if body.question.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")
 try:
    question = body.question
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": f"Answer this: {question}"}]
    )
    return {"answer": response["message"]["content"]}
 except Exception as e:
    raise HTTPException(status_code=500, detail="Ollama is not running. Please start Ollama first.")
 

@app.post("/summarize")
def summarize(body: SummarizeRequest):
    # check empty string
    if body.text.strip() == "":
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": f"Summarize this: {body.text}"}]
        )
        return {"summary": response["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {str(e)}")


@app.post("/translate")
def translate(body: TranslateRequest):
    # check empty strings
    if body.text.strip() == "":
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if body.language.strip() == "":
        raise HTTPException(status_code=400, detail="Language cannot be empty")
    
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": f"Translate this to {body.language}: {body.text}"}]
        )
        return {"translation": response["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {str(e)}")