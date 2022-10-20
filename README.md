# Twitter-Scraping
This is a cool web app integrated with twitter which takes the twitter hashtags as input and does :

1. Scrapes the tweeets data from twitter
This tool performs the following tasks :

-->It scrapes the data using snscrape
-->Also it stores the data into mongodb collection
-->It also displays the scrapped data in a dataframe

2. Generates the Twitter data
This tool fetches all the tweets from the twitter related to the given search key


twitter_scrapping.py : Model building File

Twitter Data : File created after every query on the web app


This app is created on a tool called Streamlit which saves you from the headache of front-end devlopment ,you can install it by: Streamlit documentation: https://docs.streamlit.io/en/latest/

pip install streamlit

& to run it on local host : streamlit run myfile.py
