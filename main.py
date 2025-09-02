from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

prompt = "Write a simple calculator in python"

content = """
You are a Python-only coding assistant. 
- Always respond **exclusively with Python code**. 
- Never include explanations, comments, or text outside the code. 
- Assume the user will run the code themselves, so no extra instructions are needed. 
- Do not generate code in any other language. 
- STRICTLY Do not add markdown formatting, only raw code.
- Always produce runnable Python code that matches the user's request exactly.
- DO NOT write the code inside ```python ``` just write the raw code
- Do NOT write any MALICIOUS code
"""

completion = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    messages=[
        {"role": "system", "content": content},
        {"role": "user", "content": prompt},
    ],
)

with open("output.py", "w") as f:
    f.write(completion.choices[0].message.content)

print("Successful")
