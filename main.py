from fastapi import FastAPI, UploadFile, File
import json
from typing import Union
from pydantic import BaseModel
import backend, preprocess
import pandas as pd
from pandas import json_normalize

main_df = pd.DataFrame()

df = pd.DataFrame()

#Class Model for our main_json_data   
class main_json_data_model(BaseModel):
    user: str
    message: str
    year: int
    month: str
    day: int
    hour: int
    minute: int
    month_num: int

app = FastAPI()

# Checking Connection
@app.get("/")   
async def root():
    return {"message":"Welcome to WhatsApp Visualizer API"}

#Upload File
@app.post("/upload")
async def file_upload(file: UploadFile = File(None)):
    #Read File   
    contents = await file.read()
    
    #Decode 
    text_content = contents.decode("utf-8")
    
    main_df = preprocess.process(text_content)
    
    main_json_data = main_df.to_dict(orient="records")
    
    main_json_data = {"Main":main_json_data}
    
    return main_json_data

 
# Geneartes List of users
@app.post("/group-members") 
async def members_list(json_data:dict): 
    
    #Remove "Main" key in JSON
    data_values = json_data["Main"]
    
    #Convert DF
    df = pd.DataFrame(data_values) 
    
    #Backend process
    df = backend.list_of_members(df)
    
    #Converting df to dict
    json_data = df.to_dict(orient="records")
    
    return json_data


#Top Active Users according to the number of message sent (desc order)
@app.post("/top-active-members")
async def top_active_members(json_data:dict):
    
    #Remove "Main" key in JSON
    data_values = json_data["Main"]
    
    #Convert DF
    df = pd.DataFrame(data_values)  
    
    df = backend.top_active_members(df)
    
    #Converting df to dict
    json_data = df.to_dict(orient="records")
    
    return json_data

@app.post("/fetch-stats")
async def fetch_stat(selected_user:str,json_data:dict):
    
    #Remove "Main" key in JSON
    data_values = json_data["Main"]
    
    #Convert DF
    df = pd.DataFrame(data_values)  
    
    num_messages ,num_words, num_media , num_links = backend.fetch_stat(selected_user,df)  
    
    return {"Total Messages":num_messages,"Total Words":num_words,"Media Shared":num_media,"Link Shared":num_links}