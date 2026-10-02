import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError('API not found')
client = Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"

class complain(BaseModel):
    name : str
    addres : str
    complain : str

Schema=complain.model_json_schema()
response_format={
    "type": "json_object",
}

system_prompt=f"""
extract the personal information and strictly give in json output {Schema}
"""

message_system = {
    "role":"system",
    "content":system_prompt
}
role='user'

text="""
123 Main Street Hometown, TX 77008
November 12, 2023
Mark Smith
Customer Relations Director
Sofa Showroom
555 Broadway Cityland, KS 66214
Re: Broken sofa.
Order Number: S-7654
Dear Mr. Smith:
On October 1, 2023, I bought a Plush sofa model number 25811 from the Sofa Showroom website. I paid $650 on my credit card for the sofa and delivery. Sofa Showroom delivered the sofa to my home on October 10, 2023.
Unfortunately, your product has not performed well because the sofa is defective. One of the legs broke off on October 30, 2023. The sofa is unsteady and rocks while I sit on it, so it is not comfortable or relaxing. I have not used this sofa in a way that would cause any damage. I filed reports about this problem on the Sofa Showroom's website Customer Service page on November 5 and 8. I left my email and asked someone to contact me, but no one has written back.
To resolve the problem, I would like your company to pick up this sofa, for free, and refund the $650 I paid. I have enclosed copies of my records, including my receipt, delivery invoice, and photos of the broken sofa.
I look forward to your reply and a resolution to my problem. I will wait until December 12, 2023 before I contact my state consumer protection office or get other help.
Please contact me at the above address or by phone at 123-456-7890,
Sincerely,
Jane Doe
Enclosures: Receipt, Delivery invoice, Photos
"""

prompt=f"""
this is a complain letter {text} extract the personal information from it
"""

message={
    "role":role,
    "content": prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)

answer=response.choices[0].message.content
data_file=json.loads(answer)

Complain=complain(**data_file)

print(Complain.complain)