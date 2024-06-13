# Reddit Comment Analysis: Understanding Public Sentiment

## Introduction

This project delves into the fascinating world of Reddit comments, employing sentiment analysis techniques to unearth the underlying emotions and opinions expressed by users. By analyzing Reddit data, we can gain valuable insights into public opinion trends, user satisfaction levels, and emotional responses to various topics.

## Research Questions

This project aims to answer the following key questions:

1. **User Motivations:** Can we identify the primary reasons driving users to post on Reddit?
2. **Trending Topics:** Can we pinpoint the most discussed topics and keywords within a specific timeframe?
3. **Sentiment Analysis:** Can we analyze the sentiment and opinions expressed in individual Reddit posts?

## Data Collection

We've meticulously scraped post and comment data for the month of July from the r/Nepal subreddit. This data encompasses three fields:

- **title:** The title of the post.
- **selftext:** The main text content of the post.
- **comments:** An array of associated comments for the post.

The data is stored in the `ScrapedData/posts.json` file. We leveraged the Python Reddit API to facilitate data collection.

## Data Cleaning

To ensure optimal analysis, we meticulously cleaned the collected data, removing unwanted characters and HTML tags during the scraping process. Additionally, during model training, we performed targeted stopword removal to further refine the data for analysis.

## Answering the Research Questions

**1. User Motivations**

To shed light on user motivations, we utilized a Large Language Model (LLM) to analyze the top 60 posts from July. This analysis yielded the following insights:

- **Frustration** emerged as the most prevalent emotion behind Reddit posts (60 posts).
- **Help Seeking** followed closely (10 posts).
- Posts focused on **Sharing and Nostalgia** (7 each) held equal weight.
- **Warnings** (6 posts) and **Exposures** (4 posts) aimed to alert others.
- A smaller number of posts expressed **Appreciation** (3 posts) and **Confusion** (3 posts).

These findings are stored in the `ScrapedData/intent.json` file, accompanied by a visually informative bar chart located in `static/bar_graph_top_10.png`.

**2. Trending Topics**

By examining the titles of the top 60 posts from July, we pinpointed trending topics and keywords. We have generated a word cloud to visualize the most frequently used words during this period:

- **Sirohiya**: This suggests a potential debate surrounding the arrest of the owner of Kantipur Media House.
- **Balen**: The word cloud highlights discussions related to the unconventional work methods of Kathmandu Metropolitan's Mayor.
- Other prominent topics include **job**, **gang violence**, and **pollution**.

The word cloud generated from this analysis is available in the `static/wordcloud.png` file.

**3. Sentiment Analysis**

To analyze sentiment within specific posts, we inferred our trained model. This model delves into the potential toxicity levels of Nepali Reddit comments, providing an understanding of how toxic comments might be within different posts.

## Model Details

**Data Source:**

- The model was trained on the `jigsaw-toxic-comment-classification-challenge` dataset from Kaggle (https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge), located in the `Dataset` directory.

**Model Characteristics:**

- **Framework:** TensorFlow (please specify the version)
- **Type:** Multi-class classification model
- **Location:** Saved in the `Models` directory

**Inference Process:**

- **Input Data:** User-provided Reddit posts are retrieved from the `ScrapedData/posts.json` file (JSON format).
- **Process:** The trained model is used to infer sentiment from the posts.

## Using the Project

**Requirements (Optional):**

If you intend to run the project locally, install the necessary dependencies:

    ```bash
    pip install -r requirements.txt

# Preparation:

To ensure compatibility with the trained model, your Reddit post data must be formatted in the same way as the training data. Refer to the data preparation script (potentially in data.ipynb or a separate script) for specific formatting instructions.

# Execution:

Once your Reddit post data is prepared and dependencies are installed (if applicable), run the main inference script (main.py) to analyze sentiment within your data. This script will leverage the trained model to infer sentiment for each post.

# Notebooks
For a deeper understanding of the project's components, explore the provided Jupyter Notebooks:

  1. Train.ipynb: This notebook holds the code for training the sentiment analysis model. This is crucial as it details the model's architecture and training process.
  2. data.ipynb (Optional): This notebook focuses on determining user intent within Reddit posts. If you're interested in analyzing user motivations beyond sentiment, this notebook provides valuable insights. The results of this analysis are saved in intent.json.
  3. post_sentiment.ipynb (Optional): If you're exploring cluster analysis techniques to group comments based on similar sentiment or topics, this notebook might be relevant. It delves into the process of performing cluster analysis on the comments.
