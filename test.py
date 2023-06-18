import requests,json

# 1.Upload
url = "http://127.0.0.1:8000/upload"

with open("dance.txt", "rb") as file:
    # Create a dictionary to hold the file data
    files = {"file": file}

    # Make a POST request to the API endpoint with the file
    response = requests.post(url, files=files)
    
json_data = response.json()

# Check if the request was successful (status code 200)
if response.status_code == 200:
     # Process the JSON data as needed
    print(json_data)
else:
    print("Error:", response.status_code)
    
print("Success")



# 2.Group-Members
url = "http://127.0.0.1:8000/group-members"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_group = response.json()

    # Process the JSON data as needed
    print(json_data_group)
else:
    print("Error:", response.status_code)
    
print("Success")



#3.Top Users
url = "http://127.0.0.1:8000/top-active-members"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_top_active_users = response.json()

    # Process the JSON data as needed
    print(json_data_top_active_users)
else:
    print("Error:", response.status_code)
    
print("Success")