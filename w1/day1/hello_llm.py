import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError('API not found')
client = Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"
role='user'

prompt="which is the green book of finance"

message={
    "role":role,
    "content": prompt
}

messages=[message]

response=client.chat.completions.create(model=model,messages=messages)

answer=response.choices[0].message.content
print(answer)