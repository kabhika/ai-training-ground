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