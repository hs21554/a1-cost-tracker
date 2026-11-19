from groq import Groq
import os   
from dotenv import load_dotenv
load_dotenv()
MODEL = "openai/gpt-oss-120b"
Groq_Key= os.getenv("Groq_Key")
client = Groq(api_key=Groq_Key) # reads GROQ_API_KEY
resp = client.chat.completions.create(model=MODEL,
messages=[{"role": "user", "content": "My Name is Huzaifa and i am very happy to be a part of IEC Agentic AI Class."}])
print(resp.choices[0].message.content)
print(resp.usage.prompt_tokens, resp.usage.completion_tokens)