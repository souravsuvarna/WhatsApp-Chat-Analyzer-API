
import preprocess
import pandas as pd


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
    
    

