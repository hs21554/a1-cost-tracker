import os
from dotenv import load_dotenv
from google import genai
from groq import Groq
import json
load_dotenv()

#First Genai Model Implementation and Response Back Script
# Step 1: Get Model Name and API Key from Environment Variable
GenaiMODEL = os.getenv("Genai_MODEL")
Genai_Key = os.getenv("Genai_API_Key")
client = genai.Client(api_key=Genai_Key)
print("Genai Model Name")
print(GenaiMODEL)

# Check whether Results.json already exists
results = []
with open("Results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

# Step 2: Loop to take prompt from user and generate response
for i in range(3):
    prompt = input(f"\nEnter your prompt ({i+1}/3): ")
    resp = client.models.generate_content( model=GenaiMODEL,contents=prompt)
    print(resp.text)
    input_tokens1 = resp.usage_metadata.prompt_token_count
    output_tokens1 = resp.usage_metadata.candidates_token_count
    print(f"Input Tokens: {input_tokens1}")
    print(f"Output Tokens: {output_tokens1}")
    input_cost1 = (input_tokens1 * 0.30) / 1_000_000
    output_cost1 = (output_tokens1 * 2.50) / 1_000_000
    total_cost1 = input_cost1 + output_cost1
    print(f"Total cost: ${total_cost1:.6f}\n")
    result = {"Prompt_No": i+1, "Prompt": prompt, "Response": resp.text, "Input_Tokens": input_tokens1, "Output_Tokens": output_tokens1, "Total_Cost": total_cost1}
    results.append(result)

with open("Results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
print("\nGemini results saved successfully!\n")


#First Groq Model Implementation and Response Back Script
# Step 1: Get Model Name and API Key from Environment Variable
GroqMODEL = os.getenv("Groq_MODEL")
Groq_Key= os.getenv("Groq_Key")
client = Groq(api_key=Groq_Key) 
print ("Groq AI Model Response")
print (GroqMODEL)

# Step 2: Loop to take prompt from user and generate response
for i in range (3):
    prompt = input(f"\nEnter your Prompt ({i+1}/3):")
    resp = client.chat.completions.create(model=GroqMODEL,messages=[{"role": "user", "content": prompt}])
    print(resp.choices[0].message.content)
    input_tokens2 = resp.usage.prompt_tokens
    output_tokens2 = resp.usage.completion_tokens
    print(f"Input Tokens: {input_tokens2}")
    print(f"Output Tokens: {output_tokens2}")
    input_cost2 = (input_tokens2 * 0.15) / 1_000_000
    output_cost2 = (output_tokens2 * 0.60) / 1_000_000
    total_cost2 = input_cost2 + output_cost2
    print(f"Total cost: ${total_cost2:.6f}")
    result2 = {"Prompt_No": i+1, "Prompt": prompt, "Response": resp.choices[0].message.content, "Input_Tokens": input_tokens2, "Output_Tokens": output_tokens2, "Total_Cost": total_cost2}
    results.append(result2)

with open("Results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
print("\nGroq results saved successfully!\n")