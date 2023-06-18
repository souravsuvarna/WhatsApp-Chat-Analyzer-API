import requests

url = "http://127.0.0.1:8000/group_members"

with open("dance.txt", "rb") as file:
    # Create a dictionary to hold the file data
    files = {"file": file}

    # Make a POST request to the API endpoint with the file
    response = requests.post(url, files=files)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the response
    json_data = response.json()

    # Process the JSON data as needed
    print(json_data)
else:
    print("Error:", response.status_code)