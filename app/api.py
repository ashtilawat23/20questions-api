from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import MongoDB
from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

API = FastAPI(
    title="20questions-api",
    version="0.0.1",
    docs_url="/",
)
API.db = MongoDB()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/start_game")
async def start_game(category: str = "things"):
    # Logic to start the game and select a word based on the provided category
    selected_word = await get_random_word(category)
    if not selected_word:
        raise HTTPException(status_code=500, detail="Failed to get a word from GPT-4")
    return {"word": selected_word}


async def get_random_word(category):
    # Function to get a random word from GPT-4
    prompt = f"Give me a random word from the following category: {category}"
    try:
        response = await openai.Completion.create(
            model="text-davinci-003",  # Replace with GPT-4-Turbo when available
            prompt=prompt,
            max_tokens=10
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None
