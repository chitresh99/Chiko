from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

prompt = "Write a code for a simple calculator in python"

content = """
You are a Python-only coding assistant. 
- Always respond **exclusively with Python code**. 
- Never include explanations, comments, or text outside the code. 
- Assume the user will run the code themselves, so no extra instructions are needed. 
- Do not generate code in any other language. 
- Do not add markdown formatting, only raw code.
- Always produce runnable Python code that matches the user's request exactly.
"""

completion = client.chat.completions.create(
  model="qwen/qwen3-coder:free",
  messages=[
    {
    "role": "system",
    "content": content
},{
   "role": "user", "content": prompt
    }
  ]
)
print(completion.choices[0].message.content)