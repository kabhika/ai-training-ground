import requests
import json

# Target Endpoint (Simulating an AI API endpoint)
url = "https://jsonplaceholder.typicode.com/posts"

# Headers tell the server what kind of data we are sending
headers = {
    "Content-Type": "application/json"
}

# The Payload: This is exactly how you will structure a prompt for an LLM later
payload = {
    "title": "AI Transition Progress",
    "body": "Completed Day 1. Executing Day 2 accelerated session.",
    "userId": 99
}

print("Sending POST Request (Simulating an AI Prompt submission)...")
# Notice we are using requests.post() instead of .get()
response = requests.post(url, headers=headers, json=payload)

# 201 is the HTTP status code for "Created" (Successful POST)
if response.status_code == 201:
    print("Successfully posted data!\n")
    print("Server responded with the created object:")
    print(json.dumps(response.json(), indent=4)) # indent=4 makes JSON readable
else:
    print(f"Failed to post data. Status code: {response.status_code}")