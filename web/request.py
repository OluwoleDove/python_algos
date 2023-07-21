import requests

# The URL of your Flask application endpoint for determine_palindrome
url = 'http://127.0.0.1:5000/determine_palindrome'

# JSON data to send in the request body
data = {
    'palindrome': 'level'
}

# Headers specifying the content type as JSON
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Check the response
if response.status_code == 200:
    result = response.json()
    print(result)  # Output: "level is a palindrome"
else:
    print(f"Error: {response.status_code} - {response.text}")
