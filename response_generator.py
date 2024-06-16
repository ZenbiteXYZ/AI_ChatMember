from openai import AsyncOpenAI
import httpx
import os
from dotenv import load_dotenv
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))