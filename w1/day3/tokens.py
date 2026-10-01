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

prompt1="Hi"
prompt2="explain time travel in detail"
prompt3="write a 1000 word essay on ai era"
prompt=[prompt1,prompt2,prompt3]

for i in prompt:
    message_i={
        "role":role,
        "content": i
    }
    messages=[message_i]
    response=client.chat.completions.create(model=model,messages=messages,max_tokens=50)    # tokens limit

    # answer=response.choices[0].message.content
    usage=response.usage
    print(usage.prompt_tokens,usage.completion_tokens,usage.prompt_tokens+usage.completion_tokens,response.choices[0].finish_reason)