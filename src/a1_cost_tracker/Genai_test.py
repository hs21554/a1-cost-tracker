import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
MODEL = "gemini-3.5-flash-lite"
Genai_Key = os.getenv("Genai_API_Key")
client = genai.Client(api_key=Genai_Key) # reads GEMINI_API_KEY
resp = client.models.generate_content(model=MODEL, contents="My Name is Huzaifa and i am very happy to be a part of IEC Agentic AI Class.")
print(resp.text)
print(resp.usage_metadata.prompt_token_count, resp.usage_metadata.candidates_token_count)