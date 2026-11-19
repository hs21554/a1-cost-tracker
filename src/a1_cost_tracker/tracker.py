import os
from dotenv import load_dotenv
from google import genai
from groq import Groq
load_dotenv()

#Genai Model Implementation
Genai_MODEL = "gemini-3.5-flash-lite"
Genai_Key = os.getenv("Genai_API_Key")
client = genai.Client(api_key=Genai_Key) # reads GEMINI_API_KEY
print ("Genai Model Response")
print (Genai_MODEL)
resp = client.models.generate_content(model=Genai_MODEL, contents="My Name is Huzaifa and i am very happy to be a part of IEC Agentic AI Class.")
print(resp.text)
print(resp.usage_metadata.prompt_token_count, resp.usage_metadata.candidates_token_count)
#Costing Fuctionality
input_tokens1 = resp.usage_metadata.prompt_token_count
output_tokens1 = resp.usage_metadata.candidates_token_count
input_cost1 = (input_tokens1 * 0.30) / 1_000_000
output_cost1 = (output_tokens1 * 2.50) / 1_000_000
total_cost1 = input_cost1 + output_cost1
print(f"Total cost: ${total_cost1:.6f}\n")

# Groq Model Implementation
Groq_MODEL = "openai/gpt-oss-120b"
Groq_Key= os.getenv("Groq_Key")
client = Groq(api_key=Groq_Key) # reads GROQ_API_KEY
print ("Groq AI Model Response")
print (Groq_MODEL)
resp = client.chat.completions.create(model=Groq_MODEL, messages=[{"role": "user", "content": "My Name is Huzaifa and i am very happy to be a part of IEC Agentic AI Class."}])
print(resp.choices[0].message.content)
print(resp.usage.prompt_tokens, resp.usage.completion_tokens)
#Costing Fuctionality
input_tokens2 = resp.usage.prompt_tokens
output_tokens2 = resp.usage.completion_tokens
input_cost2 = (input_tokens2 * 0.15) / 1_000_000
output_cost2 = (output_tokens2 * 0.60) / 1_000_000
total_cost2 = input_cost2 + output_cost2
print(f"Total cost: ${total_cost2:.6f}")