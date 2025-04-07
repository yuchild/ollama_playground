#!usr/bin/env python3

import ollama

# Initalizathe Ollama client
client = ollama.Client()

# Define the model and input prompt
model = "llama2"
prompt = "Write a python funtion to add two numbers"

response = client.generate(model=model, prompt=prompt)

# Print the response
print("Response from Ollama:")
print(response.response)
