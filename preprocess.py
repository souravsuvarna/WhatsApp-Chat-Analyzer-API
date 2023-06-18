import re
import json
import pandas as pd

def process(data):
    
    pattern = '\d{1,2}\/\d{1,2}\/\d{2,4},\s\d{1,2}:\d{1,2}?\s?\w{1,2}\s-\s'
    
    messages = re.split(pattern,data)[1:]
    
    dates = re.findall(pattern,data)
    
    ##DataFrame
    
    
    df = pd.DataFrame({'user_message':messages, 'message_date':dates})

    pat = '\d{1,2}\/\d{1,2}\/\d{2,4},\s\d{1,2}:\d{1,2}\s\w{1,2}\s-\s'

    p1 = '\d{2}\/\d{2}\/\d{2,4},\s\d{1,2}:\d{2}\u202f(?:am|pm)\s-\s'

    p2 = '\d{1,2}\/\d{1,2}\/\d{4},\s\d{1,2}:\d{2}\s-\s'

    p3 = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

    if re.match(p1,dates[1]):
        
        df['message_date']= pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
        
    elif re.match(p2,dates[1]):
        
        df['message_date']= pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')
        
    elif re.match(p3,dates[1]):
        df['message_date']= pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M:%S - ')

    elif re.match(pat,dates[1]):
        
        df['message_date']= pd.to_datetime(df['message_date'], format='%m/%d/%y, %I:%M %p - ')
        
        
    else:
        
        
        df['message_date']= pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')


    df.rename(columns={'message_date': 'date'}, inplace=True)
    
   
   
    
    # sperating users and messages

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:#username
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
        
    df['user'] = users
    df['message'] = messages
    df.drop(columns = ['user_message'], inplace = True )
    
    
    
    
    
    #Year
    df['year'] = df['date'].dt.year
    
    
    #Month
    df['month'] = df['date'].dt.month_name()

    
    #Day
    df['day'] = df['date'].dt.day
    
    
    #hour
    df['hour'] = df['date'].dt.hour
    
    
    #Minute
    df['minute'] = df['date'].dt.minute
    
    df['month_num']=df['date'].dt.month
    
    df = df.drop('date', axis=1)
    
    #Removing rows of group_notifications as they not needed
    df=df[df['user']!='group_notification']
    
    return df

