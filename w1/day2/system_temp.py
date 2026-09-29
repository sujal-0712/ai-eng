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

prompt="suggest a name for my food company, a single word name and dont ask for more context"

# system
message_system={
    "role":"system",
    "content": "you are brand manager which suggest name for company"
}

message={
    "role":role,
    "content": prompt
}

messages=[message_system,message]

# temperature range [0,2]


response=client.chat.completions.create(model=model,messages=messages,temperature= 2)

answer=response.choices[0].message.content
print(answer)