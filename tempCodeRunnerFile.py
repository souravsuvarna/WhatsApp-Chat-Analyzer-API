url = "http://127.0.0.1:8000/chat-percentage"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_percenatge_of_chats = response.json()

    # Process the JSON data as needed
    print(json_data_percenatge_of_chats)
else:
    print("Error:", response.status_code)
    
print("Success")