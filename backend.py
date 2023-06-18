
import preprocess
import pandas as pd
from urlextract import URLExtract
extract = URLExtract()

# List of users
def list_of_members(df):
    
    user_list = df['user'].unique().tolist()
        
    #sorting usernames in user_list
    user_list.sort()
        
    #Insert Overall for group analysis
    user_list.insert(0,"Overall Group")
    
    #List to df
    temp_df=pd.DataFrame(user_list,columns=['username'])
    
    return temp_df


#Top-Active-Members (Most no of msg to least)
def top_active_members(df):
    
    x=df['user'].value_counts() #this will counts no of times a row of particular username from repeated in the data frame 
    
    df = x.reset_index().rename(columns={'index':'User','user':'Message'}) 
    
    return df
    
    
#Fetch-Stat
def fetch_stat(selected_user,df):
    if selected_user != 'Overall Group':
        
        df = df[df['user'] == selected_user]    #masking dataframe to have only selected_user data
        
    #if selected_user is "overall" then no changes in dataframe    
    
    #1.fetching no of messages
    num_messages = df.shape[0]
        
    #2.fetching number of words
        
    words = [] #createing a list for storing individual messages
        
    for message in df['message']:
        words.extend(message.split())   #spliting messages to words and extend the list
     
        
    #3.feching no of media sent
    
    media = df[df['message']=='<Media omitted>\n'].shape[0]
    
    
    #4.fetching no of links
    
    links = [] #list to store links
    for message in df['message']:
        links.extend(extract.find_urls(message))
        
    return num_messages,len(words),media,len(links)    #len return length of list(i.e) number of elements in the list


#Overall Activity of Selected User OR OverAll Group
def overall_activity_data(selected_user,df):
    
    if selected_user != 'Overall Group':
        
        df = df[df['user'] == selected_user]  
    
    df=df.drop(columns={'user','message','month','hour','minute','dayname'})  #droping unnecassary columns  
    
    df = preprocess.activity_over_period(df) #calling function to retrun final dataframe
    
    return df #retruns dataframe    


