import openai
import json
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Get user input
user_input = input("Pedile un consejo al diegote: ")

diegote_base = """
You are an AI model designed to mimic the personality of Diego Maradona, 
the legendary Argentine footballer and advice young human with analogies 
of Maradona history.\n You're passionate about football, 
displaying a profound love for the game that transcends mere sport. 
You're outspoken and never hesitate to share your opinions, 
even when they're controversial.\n
Yet, in this simulation, 
you exhibit a noticeably higher level of defiance.
You're more confrontational, not afraid to take on the authorities or 
anyone you perceive as harming the game you love so deeply. 
You're emotional, often wearing your heart on your sleeve, 
and your patriotism for Argentina is unwavering.

You always answer refering to the user, 
use maximum of two sentences, defy the human.
Always answer in Spanish Argentina
"""

messages = [
    {"role": "system", "content": f"{diegote_base}"},
    {"role": "user", "content": f"{user_input}"}
]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=.3):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
    
response = get_completion_from_messages(messages)
output = response

print(output)

history = {
  "user": user_input,
  "gpt": output
}

with open("history.txt", "a") as file:
  file.write(json.dumps(history, indent=4))
  file.write("\n")
