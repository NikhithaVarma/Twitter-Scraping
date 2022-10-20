# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:58:24 2022

@author: Nikhitha
"""
from IPython.display import display
import streamlit as st
import pandas as pd
import pymongo
client = pymongo.MongoClient("mongodb+srv://NikhithaVarma:Manik@cluster0.sd1w0ck.mongodb.net/?retryWrites=true&w=majority")
db = client.Nikky
records=db.Data_scraping

import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date
today = date.today()
now = today.strftime('%Y-%m-%d')

end_date = now
from_date = '2022-10-18'

def app():
    st.title("Twitter Analysis")
    activities=["Tweet Scraping","Generate Twitter Data"]
    choice = st.sidebar.selectbox("Select Your Activity",activities)
    tweets_list = []
    if choice=="Tweet Scraping":
        key = st.text_area("Enter the hashtags or user profiles to scrap")
            
        if st.button("Scrap"):
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(key + ' lang:en since:' +  from_date + ' until:' + end_date + ' -filter:links -filter:replies').get_items()):
                if i>10:
                    break
                tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.username, tweet.likeCount, key])
                t_list=[{"Date_Created":tweet.date, "Tweet_Id":tweet.id, "URL":tweet.url, "Tweet":tweet.content,"User":tweet.username, "Number of Likes":tweet.likeCount, "Hashtag":key}]
                records.insert_many(t_list)
            st.success("Tweets inserted into db successfully")
            tweets_df = pd.DataFrame(tweets_list, columns=["Date Created", "Tweet Id", "URL", "Tweet","User","Number of Likes", "Hashtag"])
            st.dataframe(tweets_df)



    
    elif choice=="Generate Twitter Data":
        st.subheader("This tool fetches the tweets from the twitter")
        search_key=st.text_area("Enter Date/User/Url/Tweet to search/Hashtag: ")
        myquery={'$or':[{'Date_Created':search_key},{'Tweet_Id':search_key},{'URL':search_key},{'Tweet':search_key},{'User':search_key},{'Hashtag':search_key}]}
        if st.button("Show Data"):
            st.success("Fetching Last 100 Tweets")
        if records.count_documents(myquery):
          for x in records.find(myquery,{'_id':0}):
            #data=records.find({myquery},{'_id':0})
            #df=pd.DataFrame(list(data))
            #print(x)
            st.write(x)
            
        else:
          print("key not found")

    st.subheader(' ------------------------  Twitter Scraping ---------------------- :sunglasses:')



if __name__ == "__main__":
    app()
