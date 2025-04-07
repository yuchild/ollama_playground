import requests
import json

# Set up base URL for local Ollama API using HTTP instead of HTTPS
url = "http://localhost:8080/api/chat/completions"

# Define payload (your input prompt)
payload = {
    'model': 'ollama/llama2',
    'messages': [{"role": "user", "content": "Write a python script that prints 'Hello, world!'"}],
}

# Send the HTTP POST request with streaming enabled
response = requests.post(url, json=payload, stream=True)

# Check if the request was successful
if response.status_code == 200:
    print("Streaming response from Ollama:")
    # Process the streamed response
    for line in response.iter_lines(decode_unicode=True):
        # Check if the line is not empty
        if line:
            try:
                # Parse each line as a JSON object
                json_data = json.loads(line)
                # Extract and print the assistant's message content
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()  # Ensure the final output is on a new line
else:
    print(f"Request failed with status code: {response.status_code}")
