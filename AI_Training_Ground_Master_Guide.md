# AI Training Ground - Master Knowledge Base

## Day 1: Python Environment & API Communication

### Objective
Set up the local development environment, initialize version control, and establish basic API communication using Python.

### Core Concepts Learned
1. **Virtual Environments (`venv`):** Creating isolated Python environments to prevent library conflicts during AI development.
2. **API Communication:** Using the `requests` library to send GET requests to external endpoints (simulating LLM API calls).
3. **JSON Parsing:** Extracting and handling structured data from an API response.

### Execution Record
* Successfully created a virtual environment.
* Wrote `day1_api_fetch.py` to fetch dummy data from JSONPlaceholder.
* Pushed the initial commit to the GitHub repository.

### Code Snapshot
```python
import requests
import json

url = "[https://jsonplaceholder.typicode.com/posts/1](https://jsonplaceholder.typicode.com/posts/1)"
print("Initiating API Request...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Successfully fetched data!\n")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

---

## Day 2: POST Requests & JSON Payloads (Prompt Architecture)

### Objective
Understand the mechanism of sending data to a server using HTTP POST requests, simulating how prompts are packaged and sent to LLM APIs.

### Core Concepts Learned
1. **POST Method:** Used to send data (payloads) to a server to create or update a resource.
2. **HTTP Headers:** Specifying `"Content-Type": "application/json"` so the receiving server knows how to parse the incoming data.
3. **JSON Payloads:** Structuring Python dictionaries into JSON format to act as the "Prompt" or input data for an API.
4. **Status Code 201:** Recognizing the standard HTTP response for successful resource creation.

### Execution Record
* Wrote `day2_api_post.py` to send a JSON payload.
* Successfully received a `201 Created` response with the assigned ID from the server.