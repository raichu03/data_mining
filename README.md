# data_mining

## Introduction
This project focuses on leveraging sentiment analysis techniques to examine Reddit posts, aiming to understand the underlying sentiments expressed by users. By applying sentiment analysis to Reddit data, we can uncover insights into public opinion trends, user satisfaction, and emotional responses to various subjects.

## Three Questions we are trying to answer
* Can we determine the underlying reasons motivating users to post on Reddit?
* Can we determine the trending topics and keywords over a specific period of time?
* Can we analyse the sentiment and opinion of people on specific posts?

## Data Collection
We have scraped post and comments data form the subreddit r/Nepal of the month of july. The data contains three fields **title**, **selftext** and **comments**. It is stored in ```ScrapedData/posts.json``` file. We have used the reddit API in python to scrape the necessary data.



## Data Cleaning
There were lot of noise in the collected data. We removed most of the noise or unwanted characters form the dataset during the time of data collection. Task involved removing special characters, html tags. During the process of modelling we also performed spot word removal according to our need. 

## Answering our Questions

1. *Can we determine the underlying reasons motivating users to post on Reddit?*

To answer this question we took the help of LLM analyse the 60 top posts of this months. We feed them in the LLM to analyse them and found the following stats:
- frustration: 60
- help: 10
- sharing and nostalgia: 7 each
- warning: 6
- expose: 4
- apperation and confusion: 3

From above data we can determine that most of the posts made are showing frustration towards some system and iis followed by the posts asking for help. Similarly post discussing about sharing some advice and unlocking old memories are both at same level. Warning others user and exposing some truth are also there followed by post apperaciting and sharing confusion.

The analysis data of post intent is saved in ```ScrapedData/intent.json``` file and its bar graph is in ```static/bar_graph_top_10.png``` file

2. *Can we determine the trending topics and keywords over a specific period of time?*

To answer this question we have analised the the title of top 60 posts of this months. We have built world cloud to see the most used words this monts.

- From the world could we found out that one of the most used words are **Sirohiya** who is Owner of **Knatipur Media House**. It shows that resent arrest of him might have sparked some debete on the reddit page over the time of month.

- Next most owrd used word is **Balen** who is Mayor or **Kathmandu metropolitian**. There were lot of discussion aobut his working methods, which is little unconventional.

- There were also lot of other topics like **job**, **gang voilence**, **pollution** etc.

We have provided the word cloud result in ```static/wordcloud.png``` file

3. *Can we analyse the sentiment and opinion of people on specific posts?*