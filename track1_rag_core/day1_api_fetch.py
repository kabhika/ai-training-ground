import requests
import json

# We are using a free dummy API for practice
url = "https://jsonplaceholder.typicode.com/posts/1"

print("Initiating API Request...")
response = requests.get(url)

if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
    print("Successfully fetched data!\n")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")