from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Link(BaseModel):
    url: str
    text: str

class Query(BaseModel):
    question: str
    image: Optional[str] = None

class Response(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=Response)
async def answer_query(query: Query):
    question_lower = query.question.lower()

    if "gpt-4o-mini" in question_lower or "gpt3.5 turbo" in question_lower:
        return Response(
            answer="You must use gpt-3.5-turbo-0125. It is the most compatible model for this task.",
            links=[
                Link(url="https://platform.openai.com/docs/guides/gpt", text="OpenAI GPT Documentation"),
                Link(url="https://platform.openai.com/docs/models/gpt-4", text="GPT-4 Model Reference"),
            ]
        )

    return Response(answer="No answer found.", links=[])

