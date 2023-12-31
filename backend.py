
import preprocess
import pandas as pd
from urlextract import URLExtract
import re
import emoji
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


#Percentage of chats per user
def percentage_of_chats(df):
    
    #Return Percentages with index and users columns as default column names where index has username and user has percentage of respective users
    y=(df['user'].value_counts()/df.shape[0])*100 
    
    # converting y to data frame and renaming the columns
    df=y.reset_index().rename(columns = {'index':'User','user':'Percentage'})  
    
    #Roundig to 2 position
    df.Percentage=df.Percentage.round(2)
    
    return df


#Number of messages per month
def monthly_messages(selected_user,df):
    
    if selected_user != 'Overall Group':
        
        df = df[df['user'] == selected_user]  
          
    dfmonth=df['month']
    
    dfmonth=dfmonth.reset_index()
    
    dfmonth.drop(columns={'index'},inplace=True)
    
    dfmonth=dfmonth['month'].value_counts()
    
    dfmonth=dfmonth.reset_index()
    
    dfmonth.rename(columns={'index':'month','month':0},inplace=True)
    
    m_order = ['January', 'February', 'March', 'April', 'May', 'June','July','August','September','October','November','December']
    
    dfmonth['month'] = pd.Categorical(dfmonth['month'], categories=m_order, ordered=True)
    
    dfmonth = dfmonth.sort_values('month')
    
    dfmonth.rename(columns={'month':'Month',0:'Message'},inplace=True)
    
    return dfmonth


#Number of messages per week
def weekly_messages(selected_user,df):
    
    if selected_user != 'Overall Group':
        
        df = df[df['user'] == selected_user] 
        
    dfweek = df['dayname']
    
    dfweek=dfweek.reset_index()
    
    dfweek.drop(columns={'index'},inplace=True)
    
    dfweek=dfweek['dayname'].value_counts()
    
    dfweek=dfweek.reset_index()
    
    dfweek.rename(columns={'index':'Day','dayname':'Message'},inplace=True)
    
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    
    dfweek['Day'] = pd.Categorical(dfweek['Day'], categories=day_order, ordered=True)
    
    dfweek = dfweek.sort_values('Day')
    
    return dfweek


#Number of message sent by hour
def daily_messages(selected_user,df):
    
    if selected_user != 'Overall Group':
        
        df = df[df['user'] == selected_user] 
    
    dftime = df['hour']
    
    dftime=dftime.reset_index()
    
    dftime=dftime['hour'].value_counts()
    
    dftime=dftime.reset_index()
    
    dftime.rename(columns={'index':'Hour','hour':'Message'},inplace=True)
    
    dftime=dftime.sort_values(by='Hour')
    
    return dftime


#Number of media shared by user
def media_shared_per_user(df):
    
    df = df[df['message']=='<Media omitted>\n']
    
    df=df['user'].value_counts().reset_index()
    
    df.rename(columns={'index':'User','user':'Media'},inplace=True)
    
    return df


#Number of emoji shared by user
def emoji_shared_per_user(df):
    
    df.drop(columns={'year','month','day','hour','minute','dayname','month_num'},inplace=True)
    
    df["Emoticons"]=df["message"].apply(lambda x:re.findall(r'[\U0001f600-\U0001f650]', x))
    
    df["Emoticons_count"]=df["message"].apply(lambda x:len(re.findall(r'[\U0001f600-\U0001f650]', x)))
    
    emoji=df.groupby(["user"])["Emoticons_count"].sum().sort_values(ascending=False)
    
    emoji=emoji.reset_index()
    
    emoji.rename(columns={'user':'User','Emoticons_count':'Emoji'},inplace=True)
    
    return emoji


#The late night chat data
def late_night_chats(df):
    
    df=df.loc[(df['hour']>22) | (df['hour']<4)]
    
    df=df['user'].value_counts()
    
    df=df.reset_index()
    
    df.rename(columns={'index':'User','user':'Messages'},inplace=True)
    
    return df 


#The early morning chat data
def early_morning_chats(df):
    
    df=df.loc[(df['hour']>3) & (df['hour']<7)]
    
    df=df['user'].value_counts()
    
    df=df.reset_index()
    
    df.rename(columns={'index':'User','user':'Messages'},inplace=True)
    
    return df  



#Most Shared Emojis

def most_shared_emoji(selected_user,df):
    if selected_user != 'Overall Group':
        df = df[df['user'] == selected_user] 
            
    emojis=[]
    for message in df['message']:
        emojis.extend([c for c in message if emoji.emoji_list(c)])
    s=len(emojis)
                
    if s>0:
                    
        df2 = pd.DataFrame(emojis)

        df2.rename(columns={0:'Emoji'},inplace=True)

        df2 = df2.value_counts().reset_index()
        
        df2.rename(columns={0:'Sent'},inplace=True)

        return df2
    else:
        df2 = pd.DataFrame(columns=['204', 'No Content'])
        
        return df2
