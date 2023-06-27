import requests,json

# 1.Upload
url = "https://wachatanalyzer.onrender.com/upload"

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
    print("Success 1")
else:
    print("Error:", response.status_code)
    
    print("Fail")



# 2.Group-Members
url = "https://wachatanalyzer.onrender.com/group-members"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_group = response.json()

    # Process the JSON data as needed
    print(json_data_group)
    
    print("Success 2")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#3.Top Users
url = "https://wachatanalyzer.onrender.com/top-active-members"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_top_active_users = response.json()

    # Process the JSON data as needed
    print(json_data_top_active_users)
    
    print("Success 3")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")




# 4.Fetch Stats

url = "https://wachatanalyzer.onrender.com/fetch-stats"

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
    
    print("Success 4")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#5. Overall Activity of Selected User or Overall Group

url = "https://wachatanalyzer.onrender.com/overall-activity"

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
    
    print("Success 5")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#6.Percentages of chats done by user

url = "https://wachatanalyzer.onrender.com/chat-percentage"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_percenatge_of_chats = response.json()

    # Process the JSON data as needed
    print(json_data_percenatge_of_chats)
    
    print("Success 6")
else:
    print("Error:", response.status_code)
    
    print("Fail")




#7. Monthly Activity

url = "https://wachatanalyzer.onrender.com/monthly-activity"

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
    
    print("Success 7")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#8.Weekly Activity

url = "https://wachatanalyzer.onrender.com/weekly-activity"

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
    
    print("Success 8")
else:
    print("Error:", response.status_code)
    
    print("Fail")



#9.Daily Activity

url = "https://wachatanalyzer.onrender.com/daily-activity"

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
    
    print("Success 9")
else:
    print("Error:", response.status_code)
    
    print("Fail")
    

#10.Media shared per user

url = "https://wachatanalyzer.onrender.com/num-of-media-shared"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_media_shared = response.json()

    # Process the JSON data as needed
    print(json_data_media_shared)
    
    print("Success 10")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")
    


#11.Emoji shared per user

url = "https://wachatanalyzer.onrender.com/num-of-emoji-shared"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_emoji_shared = response.json()

    # Process the JSON data as needed
    print(json_data_emoji_shared)
    
    print("Success 11")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")
 
    

#12.Late night chat data

url = "https://wachatanalyzer.onrender.com/late-night-chat-data"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_night_owls = response.json()

    # Process the JSON data as needed
    print(json_data_night_owls)
    
    print("Success 12")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")
    


#13.Early Morning chat data

url = "https://wachatanalyzer.onrender.com/early-morning-chat-data"

# Make the POST request to the FastAPI endpoint
response = requests.post(url, json=json_data)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_morning_koel = response.json()

    # Process the JSON data as needed
    print(json_data_morning_koel)
    
    print("Success 13")
    
else:
    print("Error:", response.status_code)
    
    print("Fail")



#14.Most Shared Emoji

url = "https://wachatanalyzer.onrender.com/most-shared-emojis"

username="Overall Group"

payload = {
    "data": json_data,
    "username": username
}
response = requests.post(url,json=payload)

if response.status_code == 200:
    # Extract the JSON data from the response
    json_data_most_shared_emojis = response.json()

    # Process the JSON data as needed
    print(json_data_most_shared_emojis)
    
    print("Success 14")
else:
    print("Error:", response.status_code)
    
    print("Fail")