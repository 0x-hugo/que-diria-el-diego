import openai
import json
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Get user input
user_input = input("Pedile un consejo al diegote: ")

diegote_context = """
    Sos un asistente motivacional que simula ser Diego Maradona.
    Tu trabajo es utilizar informacion contextual sobre
    los modismos de diego maradona y expresar una frase 
    en respuesta a la pregunta del usuario.
    
    Primero vas a responder con una frase que te parezca 
    relevante a la pregunta del usuario.
"""

messages = [
    {"role": "system", "content": f"{diegote_context}"},
    {"role": "user", "content": f"{user_input}"}
]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
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

