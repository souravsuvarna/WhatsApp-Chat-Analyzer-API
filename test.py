import requests,json

# 1.Upload
url = "http://127.0.0.1:8086/upload"

with open("mscs.txt", "rb") as file:
    # Create a dictionary to hold the file data
    files = {"file": file}

    # Make a POST request to the API endpoint with the file
    response = requests.post(url, files=files)
    
json_data = response.json()

# Check if the request was successful (status code 200)
if response.status_code == 200:
     # Process the JSON data as needed
    print(json_data)
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")



# 2.Group-Members
url = "http://127.0.0.1:8086/group-members"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_group = response.json()

    # Process the JSON data as needed
    print(json_data_group)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#3.Top Users
url = "http://127.0.0.1:8086/top-active-members"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_top_active_users = response.json()

    # Process the JSON data as needed
    print(json_data_top_active_users)
    
    print("Success")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")




# 4.Fetch Stats

url = "http://127.0.0.1:8086/fetch-stats"

username="Overall Group"

payload = {
    "data": json_data,
    "username": username
}

response = requests.post(url,json=payload)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_fetch_stat = response.json()

    # Process the JSON data as needed
    print(json_data_fetch_stat)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#5. Overall Activity of Selected User or Overall Group

url = "http://127.0.0.1:8086/overall-activity"

username="Overall Group"

payload = {
    "data": json_data,
    "username": username
}
response = requests.post(url,json=payload)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_overall_activity = response.json()

    # Process the JSON data as needed
    print(json_data_overall_activity)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#6.Percentages of chats done by user

url = "http://127.0.0.1:8086/chat-percentage"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_percenatge_of_chats = response.json()

    # Process the JSON data as needed
    print(json_data_percenatge_of_chats)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")




#7. Monthly Activity

url = "http://127.0.0.1:8086/monthly-activity"

username="Overall Group"

payload = {
    "data": json_data,
    "username": username
}
response = requests.post(url,json=payload)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_monthly_activity = response.json()

    # Process the JSON data as needed
    print(json_data_monthly_activity)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#8.Weekly Activity

url = "http://127.0.0.1:8086/weekly-activity"

username="Overall Group"

payload = {
    "data": json_data,
    "username": username
}
response = requests.post(url,json=payload)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_weekly_activity = response.json()

    # Process the JSON data as needed
    print(json_data_weekly_activity)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#9.Daily Activity

url = "http://127.0.0.1:8086/daily-activity"

username="Overall Group"

payload = {
    "data": json_data,
    "username": username
}
response = requests.post(url,json=payload)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_daily_activity = response.json()

    # Process the JSON data as needed
    print(json_data_daily_activity)
    
    print("Success")
else:
    print("Error:", response.status_code)
    
    print("Fail")
    

#10.Media shared per user

url = "http://127.0.0.1:8086/media-shared"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_media_shared = response.json()

    # Process the JSON data as needed
    print(json_data_media_shared)
    
    print("Success")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")
    


#11.Emoji shared per user

url = "http://127.0.0.1:8086/emoji-shared"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_emoji_shared = response.json()

    # Process the JSON data as needed
    print(json_data_emoji_shared)
    
    print("Success")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")
    
