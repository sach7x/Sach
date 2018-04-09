

```python
#3 data observations
#CBS has the most positive overall compound tweet polarity as of 4/8/2018
#CNN has the most negative overall compound tweet polarity, followed by Fox News, as of 4/8/2018
#NYT has the most neutral overall compound tweet polarity, as of 4/8/2018
```


```python
# Dependencies
import tweepy
import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
```


```python
# Target Account
target_user = "@BBC"

# YOUR CODE HERE
n_results = 100
counter = 1
sentiments_bbc = []
for status in tweepy.Cursor(api.user_timeline, id=target_user, tweet_mode="extended").items(n_results):
    tweet=status._json
    results=analyzer.polarity_scores(tweet["full_text"])
    pos = results['pos']
    neg = results['neg']
    neu = results['neu']
    compound = results['compound']
    tweets_ago = counter
    
    sentiments_bbc.append({
                      "Compound" : compound,
                      "Positive" : pos,
                      "Negative" : neg,
                      "Neutral" : neu,
                      "Tweets Ago": counter})
    counter+=1
    
sentiments_bbc
```




    [{'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 1},
     {'Compound': 0.4939,
      'Negative': 0.0,
      'Neutral': 0.686,
      'Positive': 0.314,
      'Tweets Ago': 2},
     {'Compound': 0.25,
      'Negative': 0.088,
      'Neutral': 0.765,
      'Positive': 0.147,
      'Tweets Ago': 3},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 4},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 5},
     {'Compound': -0.2263,
      'Negative': 0.106,
      'Neutral': 0.894,
      'Positive': 0.0,
      'Tweets Ago': 6},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 7},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 8},
     {'Compound': -0.2023,
      'Negative': 0.189,
      'Neutral': 0.811,
      'Positive': 0.0,
      'Tweets Ago': 9},
     {'Compound': 0.875,
      'Negative': 0.0,
      'Neutral': 0.607,
      'Positive': 0.393,
      'Tweets Ago': 10},
     {'Compound': 0.2732,
      'Negative': 0.0,
      'Neutral': 0.488,
      'Positive': 0.512,
      'Tweets Ago': 11},
     {'Compound': -0.0772,
      'Negative': 0.058,
      'Neutral': 0.942,
      'Positive': 0.0,
      'Tweets Ago': 12},
     {'Compound': 0.5859,
      'Negative': 0.0,
      'Neutral': 0.787,
      'Positive': 0.213,
      'Tweets Ago': 13},
     {'Compound': 0.3818,
      'Negative': 0.0,
      'Neutral': 0.894,
      'Positive': 0.106,
      'Tweets Ago': 14},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 15},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 16},
     {'Compound': 0.6369,
      'Negative': 0.0,
      'Neutral': 0.792,
      'Positive': 0.208,
      'Tweets Ago': 17},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.783,
      'Positive': 0.217,
      'Tweets Ago': 18},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.748,
      'Positive': 0.252,
      'Tweets Ago': 19},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 20},
     {'Compound': -0.7269,
      'Negative': 0.405,
      'Neutral': 0.523,
      'Positive': 0.072,
      'Tweets Ago': 21},
     {'Compound': 0.6515,
      'Negative': 0.0,
      'Neutral': 0.581,
      'Positive': 0.419,
      'Tweets Ago': 22},
     {'Compound': 0.6908,
      'Negative': 0.0,
      'Neutral': 0.769,
      'Positive': 0.231,
      'Tweets Ago': 23},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 24},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 25},
     {'Compound': -0.5719,
      'Negative': 0.222,
      'Neutral': 0.778,
      'Positive': 0.0,
      'Tweets Ago': 26},
     {'Compound': 0.0018,
      'Negative': 0.129,
      'Neutral': 0.703,
      'Positive': 0.168,
      'Tweets Ago': 27},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 28},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 29},
     {'Compound': 0.69,
      'Negative': 0.0,
      'Neutral': 0.749,
      'Positive': 0.251,
      'Tweets Ago': 30},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 31},
     {'Compound': -0.6966,
      'Negative': 0.15,
      'Neutral': 0.85,
      'Positive': 0.0,
      'Tweets Ago': 32},
     {'Compound': -0.8658,
      'Negative': 0.338,
      'Neutral': 0.662,
      'Positive': 0.0,
      'Tweets Ago': 33},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 34},
     {'Compound': 0.34,
      'Negative': 0.0,
      'Neutral': 0.906,
      'Positive': 0.094,
      'Tweets Ago': 35},
     {'Compound': 0.4588,
      'Negative': 0.0,
      'Neutral': 0.769,
      'Positive': 0.231,
      'Tweets Ago': 36},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 37},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 38},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.894,
      'Positive': 0.106,
      'Tweets Ago': 39},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 40},
     {'Compound': -0.1531,
      'Negative': 0.124,
      'Neutral': 0.78,
      'Positive': 0.096,
      'Tweets Ago': 41},
     {'Compound': -0.7777,
      'Negative': 0.332,
      'Neutral': 0.621,
      'Positive': 0.047,
      'Tweets Ago': 42},
     {'Compound': 0.6037,
      'Negative': 0.0,
      'Neutral': 0.64,
      'Positive': 0.36,
      'Tweets Ago': 43},
     {'Compound': 0.8126,
      'Negative': 0.0,
      'Neutral': 0.791,
      'Positive': 0.209,
      'Tweets Ago': 44},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 45},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 46},
     {'Compound': 0.5499,
      'Negative': 0.282,
      'Neutral': 0.332,
      'Positive': 0.385,
      'Tweets Ago': 47},
     {'Compound': -0.5849,
      'Negative': 0.31,
      'Neutral': 0.559,
      'Positive': 0.13,
      'Tweets Ago': 48},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 49},
     {'Compound': -0.4215,
      'Negative': 0.171,
      'Neutral': 0.741,
      'Positive': 0.088,
      'Tweets Ago': 50},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 51},
     {'Compound': 0.2023,
      'Negative': 0.0,
      'Neutral': 0.899,
      'Positive': 0.101,
      'Tweets Ago': 52},
     {'Compound': 0.8617,
      'Negative': 0.0,
      'Neutral': 0.689,
      'Positive': 0.311,
      'Tweets Ago': 53},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 54},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 55},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 56},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 57},
     {'Compound': 0.25,
      'Negative': 0.0,
      'Neutral': 0.905,
      'Positive': 0.095,
      'Tweets Ago': 58},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 59},
     {'Compound': 0.4579,
      'Negative': 0.067,
      'Neutral': 0.779,
      'Positive': 0.154,
      'Tweets Ago': 60},
     {'Compound': -0.6908,
      'Negative': 0.176,
      'Neutral': 0.824,
      'Positive': 0.0,
      'Tweets Ago': 61},
     {'Compound': 0.7096,
      'Negative': 0.0,
      'Neutral': 0.629,
      'Positive': 0.371,
      'Tweets Ago': 62},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 63},
     {'Compound': -0.765,
      'Negative': 0.32,
      'Neutral': 0.68,
      'Positive': 0.0,
      'Tweets Ago': 64},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 65},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 66},
     {'Compound': 0.0028,
      'Negative': 0.118,
      'Neutral': 0.724,
      'Positive': 0.159,
      'Tweets Ago': 67},
     {'Compound': 0.4588,
      'Negative': 0.0,
      'Neutral': 0.75,
      'Positive': 0.25,
      'Tweets Ago': 68},
     {'Compound': -0.2263,
      'Negative': 0.112,
      'Neutral': 0.888,
      'Positive': 0.0,
      'Tweets Ago': 69},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 70},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 71},
     {'Compound': 0.4215,
      'Negative': 0.0,
      'Neutral': 0.797,
      'Positive': 0.203,
      'Tweets Ago': 72},
     {'Compound': 0.6027,
      'Negative': 0.0,
      'Neutral': 0.843,
      'Positive': 0.157,
      'Tweets Ago': 73},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 74},
     {'Compound': 0.2023,
      'Negative': 0.0,
      'Neutral': 0.924,
      'Positive': 0.076,
      'Tweets Ago': 75},
     {'Compound': 0.3164,
      'Negative': 0.0,
      'Neutral': 0.906,
      'Positive': 0.094,
      'Tweets Ago': 76},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 77},
     {'Compound': -0.128,
      'Negative': 0.091,
      'Neutral': 0.909,
      'Positive': 0.0,
      'Tweets Ago': 78},
     {'Compound': -0.4003,
      'Negative': 0.114,
      'Neutral': 0.886,
      'Positive': 0.0,
      'Tweets Ago': 79},
     {'Compound': -0.2023,
      'Negative': 0.229,
      'Neutral': 0.625,
      'Positive': 0.146,
      'Tweets Ago': 80},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 81},
     {'Compound': 0.7269,
      'Negative': 0.0,
      'Neutral': 0.643,
      'Positive': 0.357,
      'Tweets Ago': 82},
     {'Compound': -0.5994,
      'Negative': 0.262,
      'Neutral': 0.738,
      'Positive': 0.0,
      'Tweets Ago': 83},
     {'Compound': 0.7906,
      'Negative': 0.0,
      'Neutral': 0.759,
      'Positive': 0.241,
      'Tweets Ago': 84},
     {'Compound': 0.4215,
      'Negative': 0.0,
      'Neutral': 0.763,
      'Positive': 0.237,
      'Tweets Ago': 85},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 86},
     {'Compound': -0.1531,
      'Negative': 0.062,
      'Neutral': 0.938,
      'Positive': 0.0,
      'Tweets Ago': 87},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 88},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 89},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 90},
     {'Compound': -0.296,
      'Negative': 0.121,
      'Neutral': 0.879,
      'Positive': 0.0,
      'Tweets Ago': 91},
     {'Compound': 0.636,
      'Negative': 0.0,
      'Neutral': 0.729,
      'Positive': 0.271,
      'Tweets Ago': 92},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 93},
     {'Compound': 0.1531,
      'Negative': 0.0,
      'Neutral': 0.897,
      'Positive': 0.103,
      'Tweets Ago': 94},
     {'Compound': 0.34,
      'Negative': 0.0,
      'Neutral': 0.902,
      'Positive': 0.098,
      'Tweets Ago': 95},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.891,
      'Positive': 0.109,
      'Tweets Ago': 96},
     {'Compound': 0.25,
      'Negative': 0.0,
      'Neutral': 0.929,
      'Positive': 0.071,
      'Tweets Ago': 97},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 98},
     {'Compound': -0.5423,
      'Negative': 0.209,
      'Neutral': 0.791,
      'Positive': 0.0,
      'Tweets Ago': 99},
     {'Compound': 0.6486,
      'Negative': 0.0,
      'Neutral': 0.739,
      'Positive': 0.261,
      'Tweets Ago': 100}]




```python
#print(json.dumps(tweet, indent=4, sort_keys=True))
bbc_name = tweet['user']['name']
sentiments_bbc_df = pd.DataFrame(sentiments_bbc)
sentiments_bbc_df['Media Source'] = bbc_name
sentiments_bbc_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>Media Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>1</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.4939</td>
      <td>0.000</td>
      <td>0.686</td>
      <td>0.314</td>
      <td>2</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.2500</td>
      <td>0.088</td>
      <td>0.765</td>
      <td>0.147</td>
      <td>3</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>4</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>5</td>
      <td>BBC</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Target Account
target_user = "@CBS"

# YOUR CODE HERE
n_results = 100
counter = 1
sentiments_cbs = []
for status in tweepy.Cursor(api.user_timeline, id=target_user, tweet_mode="extended").items(n_results):
    tweet=status._json
    results=analyzer.polarity_scores(tweet["full_text"])
    pos = results['pos']
    neg = results['neg']
    neu = results['neu']
    compound = results['compound']
    tweets_ago = counter
    
    sentiments_cbs.append({
                      "Compound" : compound,
                      "Positive" : pos,
                      "Negative" : neg,
                      "Neutral" : neu,
                      "Tweets Ago": counter})
    counter+=1
    
sentiments_cbs
```




    [{'Compound': 0.6467,
      'Negative': 0.0,
      'Neutral': 0.72,
      'Positive': 0.28,
      'Tweets Ago': 1},
     {'Compound': 0.7345,
      'Negative': 0.0,
      'Neutral': 0.85,
      'Positive': 0.15,
      'Tweets Ago': 2},
     {'Compound': 0.5562,
      'Negative': 0.0,
      'Neutral': 0.86,
      'Positive': 0.14,
      'Tweets Ago': 3},
     {'Compound': 0.4199,
      'Negative': 0.0,
      'Neutral': 0.92,
      'Positive': 0.08,
      'Tweets Ago': 4},
     {'Compound': 0.8313,
      'Negative': 0.0,
      'Neutral': 0.799,
      'Positive': 0.201,
      'Tweets Ago': 5},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 6},
     {'Compound': 0.4199,
      'Negative': 0.0,
      'Neutral': 0.924,
      'Positive': 0.076,
      'Tweets Ago': 7},
     {'Compound': 0.4389,
      'Negative': 0.0,
      'Neutral': 0.928,
      'Positive': 0.072,
      'Tweets Ago': 8},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 9},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 10},
     {'Compound': 0.3164,
      'Negative': 0.0,
      'Neutral': 0.959,
      'Positive': 0.041,
      'Tweets Ago': 11},
     {'Compound': 0.6964,
      'Negative': 0.0,
      'Neutral': 0.883,
      'Positive': 0.117,
      'Tweets Ago': 12},
     {'Compound': 0.6597,
      'Negative': 0.0,
      'Neutral': 0.759,
      'Positive': 0.241,
      'Tweets Ago': 13},
     {'Compound': -0.3875,
      'Negative': 0.082,
      'Neutral': 0.88,
      'Positive': 0.038,
      'Tweets Ago': 14},
     {'Compound': 0.8217,
      'Negative': 0.0,
      'Neutral': 0.844,
      'Positive': 0.156,
      'Tweets Ago': 15},
     {'Compound': 0.7568,
      'Negative': 0.0,
      'Neutral': 0.712,
      'Positive': 0.288,
      'Tweets Ago': 16},
     {'Compound': 0.8495,
      'Negative': 0.0,
      'Neutral': 0.634,
      'Positive': 0.366,
      'Tweets Ago': 17},
     {'Compound': 0.4926,
      'Negative': 0.0,
      'Neutral': 0.803,
      'Positive': 0.197,
      'Tweets Ago': 18},
     {'Compound': -0.3182,
      'Negative': 0.095,
      'Neutral': 0.905,
      'Positive': 0.0,
      'Tweets Ago': 19},
     {'Compound': -0.25,
      'Negative': 0.133,
      'Neutral': 0.867,
      'Positive': 0.0,
      'Tweets Ago': 20},
     {'Compound': 0.6239,
      'Negative': 0.0,
      'Neutral': 0.911,
      'Positive': 0.089,
      'Tweets Ago': 21},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 22},
     {'Compound': 0.7096,
      'Negative': 0.0,
      'Neutral': 0.877,
      'Positive': 0.123,
      'Tweets Ago': 23},
     {'Compound': 0.807,
      'Negative': 0.0,
      'Neutral': 0.659,
      'Positive': 0.341,
      'Tweets Ago': 24},
     {'Compound': 0.1513,
      'Negative': 0.051,
      'Neutral': 0.884,
      'Positive': 0.065,
      'Tweets Ago': 25},
     {'Compound': 0.7783,
      'Negative': 0.0,
      'Neutral': 0.788,
      'Positive': 0.212,
      'Tweets Ago': 26},
     {'Compound': 0.7351,
      'Negative': 0.0,
      'Neutral': 0.854,
      'Positive': 0.146,
      'Tweets Ago': 27},
     {'Compound': 0.4199,
      'Negative': 0.0,
      'Neutral': 0.938,
      'Positive': 0.062,
      'Tweets Ago': 28},
     {'Compound': 0.6688,
      'Negative': 0.0,
      'Neutral': 0.891,
      'Positive': 0.109,
      'Tweets Ago': 29},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 30},
     {'Compound': 0.6239,
      'Negative': 0.0,
      'Neutral': 0.903,
      'Positive': 0.097,
      'Tweets Ago': 31},
     {'Compound': 0.3818,
      'Negative': 0.068,
      'Neutral': 0.8,
      'Positive': 0.133,
      'Tweets Ago': 32},
     {'Compound': 0.296,
      'Negative': 0.0,
      'Neutral': 0.95,
      'Positive': 0.05,
      'Tweets Ago': 33},
     {'Compound': 0.508,
      'Negative': 0.0,
      'Neutral': 0.88,
      'Positive': 0.12,
      'Tweets Ago': 34},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 35},
     {'Compound': 0.7959,
      'Negative': 0.0,
      'Neutral': 0.786,
      'Positive': 0.214,
      'Tweets Ago': 36},
     {'Compound': 0.807,
      'Negative': 0.0,
      'Neutral': 0.799,
      'Positive': 0.201,
      'Tweets Ago': 37},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 38},
     {'Compound': 0.5754,
      'Negative': 0.053,
      'Neutral': 0.802,
      'Positive': 0.145,
      'Tweets Ago': 39},
     {'Compound': 0.5399,
      'Negative': 0.0,
      'Neutral': 0.801,
      'Positive': 0.199,
      'Tweets Ago': 40},
     {'Compound': -0.34,
      'Negative': 0.185,
      'Neutral': 0.7,
      'Positive': 0.115,
      'Tweets Ago': 41},
     {'Compound': 0.7003,
      'Negative': 0.0,
      'Neutral': 0.791,
      'Positive': 0.209,
      'Tweets Ago': 42},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 43},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 44},
     {'Compound': 0.7184,
      'Negative': 0.0,
      'Neutral': 0.667,
      'Positive': 0.333,
      'Tweets Ago': 45},
     {'Compound': 0.9451,
      'Negative': 0.0,
      'Neutral': 0.58,
      'Positive': 0.42,
      'Tweets Ago': 46},
     {'Compound': 0.6239,
      'Negative': 0.0,
      'Neutral': 0.909,
      'Positive': 0.091,
      'Tweets Ago': 47},
     {'Compound': 0.8697,
      'Negative': 0.0,
      'Neutral': 0.765,
      'Positive': 0.235,
      'Tweets Ago': 48},
     {'Compound': 0.4939,
      'Negative': 0.0,
      'Neutral': 0.686,
      'Positive': 0.314,
      'Tweets Ago': 49},
     {'Compound': 0.8997,
      'Negative': 0.0,
      'Neutral': 0.645,
      'Positive': 0.355,
      'Tweets Ago': 50},
     {'Compound': 0.6514,
      'Negative': 0.0,
      'Neutral': 0.907,
      'Positive': 0.093,
      'Tweets Ago': 51},
     {'Compound': 0.7081,
      'Negative': 0.066,
      'Neutral': 0.623,
      'Positive': 0.311,
      'Tweets Ago': 52},
     {'Compound': 0.636,
      'Negative': 0.0,
      'Neutral': 0.819,
      'Positive': 0.181,
      'Tweets Ago': 53},
     {'Compound': 0.4588,
      'Negative': 0.0,
      'Neutral': 0.933,
      'Positive': 0.067,
      'Tweets Ago': 54},
     {'Compound': 0.5106,
      'Negative': 0.0,
      'Neutral': 0.918,
      'Positive': 0.082,
      'Tweets Ago': 55},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 56},
     {'Compound': 0.5562,
      'Negative': 0.0,
      'Neutral': 0.826,
      'Positive': 0.174,
      'Tweets Ago': 57},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 58},
     {'Compound': 0.7845,
      'Negative': 0.072,
      'Neutral': 0.619,
      'Positive': 0.309,
      'Tweets Ago': 59},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 60},
     {'Compound': 0.6514,
      'Negative': 0.0,
      'Neutral': 0.787,
      'Positive': 0.213,
      'Tweets Ago': 61},
     {'Compound': 0.1867,
      'Negative': 0.0,
      'Neutral': 0.92,
      'Positive': 0.08,
      'Tweets Ago': 62},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 63},
     {'Compound': 0.6166,
      'Negative': 0.0,
      'Neutral': 0.845,
      'Positive': 0.155,
      'Tweets Ago': 64},
     {'Compound': 0.8402,
      'Negative': 0.0,
      'Neutral': 0.75,
      'Positive': 0.25,
      'Tweets Ago': 65},
     {'Compound': 0.296,
      'Negative': 0.0,
      'Neutral': 0.901,
      'Positive': 0.099,
      'Tweets Ago': 66},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 67},
     {'Compound': 0.6514,
      'Negative': 0.0,
      'Neutral': 0.829,
      'Positive': 0.171,
      'Tweets Ago': 68},
     {'Compound': 0.7088,
      'Negative': 0.0,
      'Neutral': 0.763,
      'Positive': 0.237,
      'Tweets Ago': 69},
     {'Compound': -0.4939,
      'Negative': 0.157,
      'Neutral': 0.766,
      'Positive': 0.077,
      'Tweets Ago': 70},
     {'Compound': 0.6514,
      'Negative': 0.0,
      'Neutral': 0.806,
      'Positive': 0.194,
      'Tweets Ago': 71},
     {'Compound': 0.6115,
      'Negative': 0.0,
      'Neutral': 0.734,
      'Positive': 0.266,
      'Tweets Ago': 72},
     {'Compound': 0.6696,
      'Negative': 0.0,
      'Neutral': 0.892,
      'Positive': 0.108,
      'Tweets Ago': 73},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.857,
      'Positive': 0.143,
      'Tweets Ago': 74},
     {'Compound': 0.539,
      'Negative': 0.0,
      'Neutral': 0.899,
      'Positive': 0.101,
      'Tweets Ago': 75},
     {'Compound': 0.2244,
      'Negative': 0.0,
      'Neutral': 0.917,
      'Positive': 0.083,
      'Tweets Ago': 76},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 77},
     {'Compound': 0.4926,
      'Negative': 0.0,
      'Neutral': 0.883,
      'Positive': 0.117,
      'Tweets Ago': 78},
     {'Compound': 0.1275,
      'Negative': 0.092,
      'Neutral': 0.795,
      'Positive': 0.113,
      'Tweets Ago': 79},
     {'Compound': 0.784,
      'Negative': 0.0,
      'Neutral': 0.853,
      'Positive': 0.147,
      'Tweets Ago': 80},
     {'Compound': 0.8658,
      'Negative': 0.0,
      'Neutral': 0.553,
      'Positive': 0.447,
      'Tweets Ago': 81},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 82},
     {'Compound': 0.91,
      'Negative': 0.0,
      'Neutral': 0.675,
      'Positive': 0.325,
      'Tweets Ago': 83},
     {'Compound': 0.6688,
      'Negative': 0.0,
      'Neutral': 0.889,
      'Positive': 0.111,
      'Tweets Ago': 84},
     {'Compound': -0.2023,
      'Negative': 0.23,
      'Neutral': 0.619,
      'Positive': 0.15,
      'Tweets Ago': 85},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 86},
     {'Compound': 0.6705,
      'Negative': 0.0,
      'Neutral': 0.766,
      'Positive': 0.234,
      'Tweets Ago': 87},
     {'Compound': 0.4389,
      'Negative': 0.0,
      'Neutral': 0.915,
      'Positive': 0.085,
      'Tweets Ago': 88},
     {'Compound': 0.4404,
      'Negative': 0.0,
      'Neutral': 0.884,
      'Positive': 0.116,
      'Tweets Ago': 89},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 90},
     {'Compound': 0.91,
      'Negative': 0.0,
      'Neutral': 0.658,
      'Positive': 0.342,
      'Tweets Ago': 91},
     {'Compound': 0.7096,
      'Negative': 0.0,
      'Neutral': 0.803,
      'Positive': 0.197,
      'Tweets Ago': 92},
     {'Compound': 0.4215,
      'Negative': 0.033,
      'Neutral': 0.892,
      'Positive': 0.075,
      'Tweets Ago': 93},
     {'Compound': -0.6981,
      'Negative': 0.21,
      'Neutral': 0.79,
      'Positive': 0.0,
      'Tweets Ago': 94},
     {'Compound': 0.4547,
      'Negative': 0.092,
      'Neutral': 0.749,
      'Positive': 0.159,
      'Tweets Ago': 95},
     {'Compound': 0.8591,
      'Negative': 0.0,
      'Neutral': 0.462,
      'Positive': 0.538,
      'Tweets Ago': 96},
     {'Compound': 0.4885,
      'Negative': 0.151,
      'Neutral': 0.615,
      'Positive': 0.234,
      'Tweets Ago': 97},
     {'Compound': 0.5994,
      'Negative': 0.0,
      'Neutral': 0.822,
      'Positive': 0.178,
      'Tweets Ago': 98},
     {'Compound': 0.7717,
      'Negative': 0.0,
      'Neutral': 0.675,
      'Positive': 0.325,
      'Tweets Ago': 99},
     {'Compound': 0.7177,
      'Negative': 0.0,
      'Neutral': 0.8,
      'Positive': 0.2,
      'Tweets Ago': 100}]




```python
cbs_name = tweet['user']['name']
sentiments_cbs_df = pd.DataFrame(sentiments_cbs)
sentiments_cbs_df['Media Source'] = cbs_name
sentiments_cbs_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>Media Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.6467</td>
      <td>0.0</td>
      <td>0.720</td>
      <td>0.280</td>
      <td>1</td>
      <td>CBS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.7345</td>
      <td>0.0</td>
      <td>0.850</td>
      <td>0.150</td>
      <td>2</td>
      <td>CBS</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.5562</td>
      <td>0.0</td>
      <td>0.860</td>
      <td>0.140</td>
      <td>3</td>
      <td>CBS</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.4199</td>
      <td>0.0</td>
      <td>0.920</td>
      <td>0.080</td>
      <td>4</td>
      <td>CBS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.8313</td>
      <td>0.0</td>
      <td>0.799</td>
      <td>0.201</td>
      <td>5</td>
      <td>CBS</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Target Account
target_user = "@CNN"

# YOUR CODE HERE
n_results = 100
counter = 1
sentiments_cnn = []
for status in tweepy.Cursor(api.user_timeline, id=target_user, tweet_mode="extended").items(n_results):
    tweet=status._json
    results=analyzer.polarity_scores(tweet["full_text"])
    pos = results['pos']
    neg = results['neg']
    neu = results['neu']
    compound = results['compound']
    tweets_ago = counter
    
    sentiments_cnn.append({
                      "Compound" : compound,
                      "Positive" : pos,
                      "Negative" : neg,
                      "Neutral" : neu,
                      "Tweets Ago": counter})
    counter+=1
    
sentiments_cnn
```




    [{'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 1},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 2},
     {'Compound': -0.7906,
      'Negative': 0.368,
      'Neutral': 0.632,
      'Positive': 0.0,
      'Tweets Ago': 3},
     {'Compound': -0.4019,
      'Negative': 0.137,
      'Neutral': 0.863,
      'Positive': 0.0,
      'Tweets Ago': 4},
     {'Compound': 0.5859,
      'Negative': 0.0,
      'Neutral': 0.759,
      'Positive': 0.241,
      'Tweets Ago': 5},
     {'Compound': -0.5719,
      'Negative': 0.236,
      'Neutral': 0.764,
      'Positive': 0.0,
      'Tweets Ago': 6},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 7},
     {'Compound': -0.9062,
      'Negative': 0.357,
      'Neutral': 0.643,
      'Positive': 0.0,
      'Tweets Ago': 8},
     {'Compound': -0.5106,
      'Negative': 0.275,
      'Neutral': 0.604,
      'Positive': 0.121,
      'Tweets Ago': 9},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 10},
     {'Compound': -0.3818,
      'Negative': 0.178,
      'Neutral': 0.822,
      'Positive': 0.0,
      'Tweets Ago': 11},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 12},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 13},
     {'Compound': 0.6369,
      'Negative': 0.0,
      'Neutral': 0.704,
      'Positive': 0.296,
      'Tweets Ago': 14},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.828,
      'Positive': 0.172,
      'Tweets Ago': 15},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 16},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 17},
     {'Compound': 0.34,
      'Negative': 0.218,
      'Neutral': 0.446,
      'Positive': 0.337,
      'Tweets Ago': 18},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.861,
      'Positive': 0.139,
      'Tweets Ago': 19},
     {'Compound': 0.7717,
      'Negative': 0.0,
      'Neutral': 0.642,
      'Positive': 0.358,
      'Tweets Ago': 20},
     {'Compound': -0.6249,
      'Negative': 0.389,
      'Neutral': 0.611,
      'Positive': 0.0,
      'Tweets Ago': 21},
     {'Compound': -0.3818,
      'Negative': 0.13,
      'Neutral': 0.797,
      'Positive': 0.072,
      'Tweets Ago': 22},
     {'Compound': -0.4215,
      'Negative': 0.177,
      'Neutral': 0.823,
      'Positive': 0.0,
      'Tweets Ago': 23},
     {'Compound': -0.7845,
      'Negative': 0.259,
      'Neutral': 0.676,
      'Positive': 0.065,
      'Tweets Ago': 24},
     {'Compound': 0.2023,
      'Negative': 0.0,
      'Neutral': 0.878,
      'Positive': 0.122,
      'Tweets Ago': 25},
     {'Compound': -0.5719,
      'Negative': 0.236,
      'Neutral': 0.764,
      'Positive': 0.0,
      'Tweets Ago': 26},
     {'Compound': -0.3818,
      'Negative': 0.204,
      'Neutral': 0.68,
      'Positive': 0.116,
      'Tweets Ago': 27},
     {'Compound': 0.5859,
      'Negative': 0.0,
      'Neutral': 0.863,
      'Positive': 0.137,
      'Tweets Ago': 28},
     {'Compound': 0.34,
      'Negative': 0.218,
      'Neutral': 0.446,
      'Positive': 0.337,
      'Tweets Ago': 29},
     {'Compound': -0.4588,
      'Negative': 0.25,
      'Neutral': 0.75,
      'Positive': 0.0,
      'Tweets Ago': 30},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 31},
     {'Compound': -0.7717,
      'Negative': 0.427,
      'Neutral': 0.573,
      'Positive': 0.0,
      'Tweets Ago': 32},
     {'Compound': -0.4019,
      'Negative': 0.197,
      'Neutral': 0.803,
      'Positive': 0.0,
      'Tweets Ago': 33},
     {'Compound': 0.6588,
      'Negative': 0.0,
      'Neutral': 0.785,
      'Positive': 0.215,
      'Tweets Ago': 34},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 35},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 36},
     {'Compound': -0.6124,
      'Negative': 0.417,
      'Neutral': 0.583,
      'Positive': 0.0,
      'Tweets Ago': 37},
     {'Compound': 0.0258,
      'Negative': 0.164,
      'Neutral': 0.667,
      'Positive': 0.17,
      'Tweets Ago': 38},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 39},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 40},
     {'Compound': 0.1316,
      'Negative': 0.128,
      'Neutral': 0.699,
      'Positive': 0.172,
      'Tweets Ago': 41},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 42},
     {'Compound': -0.8834,
      'Negative': 0.442,
      'Neutral': 0.558,
      'Positive': 0.0,
      'Tweets Ago': 43},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 44},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 45},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 46},
     {'Compound': 0.5574,
      'Negative': 0.071,
      'Neutral': 0.706,
      'Positive': 0.224,
      'Tweets Ago': 47},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 48},
     {'Compound': -0.6249,
      'Negative': 0.389,
      'Neutral': 0.611,
      'Positive': 0.0,
      'Tweets Ago': 49},
     {'Compound': -0.7351,
      'Negative': 0.238,
      'Neutral': 0.762,
      'Positive': 0.0,
      'Tweets Ago': 50},
     {'Compound': -0.6597,
      'Negative': 0.268,
      'Neutral': 0.732,
      'Positive': 0.0,
      'Tweets Ago': 51},
     {'Compound': -0.6124,
      'Negative': 0.25,
      'Neutral': 0.75,
      'Positive': 0.0,
      'Tweets Ago': 52},
     {'Compound': -0.4215,
      'Negative': 0.149,
      'Neutral': 0.851,
      'Positive': 0.0,
      'Tweets Ago': 53},
     {'Compound': -0.4767,
      'Negative': 0.129,
      'Neutral': 0.871,
      'Positive': 0.0,
      'Tweets Ago': 54},
     {'Compound': 0.2023,
      'Negative': 0.128,
      'Neutral': 0.698,
      'Positive': 0.174,
      'Tweets Ago': 55},
     {'Compound': -0.5122,
      'Negative': 0.202,
      'Neutral': 0.798,
      'Positive': 0.0,
      'Tweets Ago': 56},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 57},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.764,
      'Positive': 0.236,
      'Tweets Ago': 58},
     {'Compound': -0.2023,
      'Negative': 0.167,
      'Neutral': 0.725,
      'Positive': 0.109,
      'Tweets Ago': 59},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.918,
      'Positive': 0.082,
      'Tweets Ago': 60},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 61},
     {'Compound': -0.0258,
      'Negative': 0.097,
      'Neutral': 0.811,
      'Positive': 0.093,
      'Tweets Ago': 62},
     {'Compound': -0.6249,
      'Negative': 0.175,
      'Neutral': 0.825,
      'Positive': 0.0,
      'Tweets Ago': 63},
     {'Compound': -0.6808,
      'Negative': 0.221,
      'Neutral': 0.697,
      'Positive': 0.082,
      'Tweets Ago': 64},
     {'Compound': -0.8519,
      'Negative': 0.249,
      'Neutral': 0.751,
      'Positive': 0.0,
      'Tweets Ago': 65},
     {'Compound': 0.2023,
      'Negative': 0.0,
      'Neutral': 0.942,
      'Positive': 0.058,
      'Tweets Ago': 66},
     {'Compound': 0.3804,
      'Negative': 0.046,
      'Neutral': 0.852,
      'Positive': 0.102,
      'Tweets Ago': 67},
     {'Compound': -0.4019,
      'Negative': 0.091,
      'Neutral': 0.909,
      'Positive': 0.0,
      'Tweets Ago': 68},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 69},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.803,
      'Positive': 0.197,
      'Tweets Ago': 70},
     {'Compound': -0.8402,
      'Negative': 0.205,
      'Neutral': 0.795,
      'Positive': 0.0,
      'Tweets Ago': 71},
     {'Compound': 0.5096,
      'Negative': 0.071,
      'Neutral': 0.762,
      'Positive': 0.167,
      'Tweets Ago': 72},
     {'Compound': 0.0772,
      'Negative': 0.0,
      'Neutral': 0.966,
      'Positive': 0.034,
      'Tweets Ago': 73},
     {'Compound': -0.7096,
      'Negative': 0.237,
      'Neutral': 0.648,
      'Positive': 0.115,
      'Tweets Ago': 74},
     {'Compound': 0.6486,
      'Negative': 0.0,
      'Neutral': 0.798,
      'Positive': 0.202,
      'Tweets Ago': 75},
     {'Compound': 0.128,
      'Negative': 0.082,
      'Neutral': 0.818,
      'Positive': 0.1,
      'Tweets Ago': 76},
     {'Compound': -0.4019,
      'Negative': 0.109,
      'Neutral': 0.891,
      'Positive': 0.0,
      'Tweets Ago': 77},
     {'Compound': 0.4404,
      'Negative': 0.0,
      'Neutral': 0.83,
      'Positive': 0.17,
      'Tweets Ago': 78},
     {'Compound': -0.9136,
      'Negative': 0.458,
      'Neutral': 0.542,
      'Positive': 0.0,
      'Tweets Ago': 79},
     {'Compound': -0.3182,
      'Negative': 0.082,
      'Neutral': 0.872,
      'Positive': 0.046,
      'Tweets Ago': 80},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 81},
     {'Compound': -0.1531,
      'Negative': 0.132,
      'Neutral': 0.769,
      'Positive': 0.099,
      'Tweets Ago': 82},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 83},
     {'Compound': 0.128,
      'Negative': 0.116,
      'Neutral': 0.741,
      'Positive': 0.143,
      'Tweets Ago': 84},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.87,
      'Positive': 0.13,
      'Tweets Ago': 85},
     {'Compound': 0.0258,
      'Negative': 0.174,
      'Neutral': 0.645,
      'Positive': 0.181,
      'Tweets Ago': 86},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 87},
     {'Compound': -0.8402,
      'Negative': 0.205,
      'Neutral': 0.795,
      'Positive': 0.0,
      'Tweets Ago': 88},
     {'Compound': -0.1531,
      'Negative': 0.132,
      'Neutral': 0.769,
      'Positive': 0.099,
      'Tweets Ago': 89},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 90},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 91},
     {'Compound': -0.3818,
      'Negative': 0.224,
      'Neutral': 0.776,
      'Positive': 0.0,
      'Tweets Ago': 92},
     {'Compound': -0.8271,
      'Negative': 0.314,
      'Neutral': 0.686,
      'Positive': 0.0,
      'Tweets Ago': 93},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 94},
     {'Compound': 0.5994,
      'Negative': 0.0,
      'Neutral': 0.62,
      'Positive': 0.38,
      'Tweets Ago': 95},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 96},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 97},
     {'Compound': -0.8271,
      'Negative': 0.303,
      'Neutral': 0.697,
      'Positive': 0.0,
      'Tweets Ago': 98},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 99},
     {'Compound': -0.9022,
      'Negative': 0.268,
      'Neutral': 0.732,
      'Positive': 0.0,
      'Tweets Ago': 100}]




```python
cnn_name = tweet['user']['name']
sentiments_cnn_df = pd.DataFrame(sentiments_cnn)
sentiments_cnn_df['Media Source'] = cnn_name
sentiments_cnn_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>Media Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>1</td>
      <td>CNN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>2</td>
      <td>CNN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.7906</td>
      <td>0.368</td>
      <td>0.632</td>
      <td>0.000</td>
      <td>3</td>
      <td>CNN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.4019</td>
      <td>0.137</td>
      <td>0.863</td>
      <td>0.000</td>
      <td>4</td>
      <td>CNN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.5859</td>
      <td>0.000</td>
      <td>0.759</td>
      <td>0.241</td>
      <td>5</td>
      <td>CNN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Target Account
target_user = "@FoxNews"

# YOUR CODE HERE
n_results = 100
counter = 1
sentiments_foxnews = []
for status in tweepy.Cursor(api.user_timeline, id=target_user, tweet_mode="extended").items(n_results):
    tweet=status._json
    results=analyzer.polarity_scores(tweet["full_text"])
    pos = results['pos']
    neg = results['neg']
    neu = results['neu']
    compound = results['compound']
    tweets_ago = counter
    
    sentiments_foxnews.append({
                      "Compound" : compound,
                      "Positive" : pos,
                      "Negative" : neg,
                      "Neutral" : neu,
                      "Tweets Ago": counter})
    counter+=1
    
sentiments_foxnews
```




    [{'Compound': 0.8658,
      'Negative': 0.033,
      'Neutral': 0.722,
      'Positive': 0.245,
      'Tweets Ago': 1},
     {'Compound': -0.5574,
      'Negative': 0.081,
      'Neutral': 0.919,
      'Positive': 0.0,
      'Tweets Ago': 2},
     {'Compound': 0.2732,
      'Negative': 0.067,
      'Neutral': 0.815,
      'Positive': 0.119,
      'Tweets Ago': 3},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 4},
     {'Compound': 0.7906,
      'Negative': 0.0,
      'Neutral': 0.733,
      'Positive': 0.267,
      'Tweets Ago': 5},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 6},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.894,
      'Positive': 0.106,
      'Tweets Ago': 7},
     {'Compound': 0.7184,
      'Negative': 0.0,
      'Neutral': 0.812,
      'Positive': 0.188,
      'Tweets Ago': 8},
     {'Compound': 0.3818,
      'Negative': 0.0,
      'Neutral': 0.898,
      'Positive': 0.102,
      'Tweets Ago': 9},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 10},
     {'Compound': -0.296,
      'Negative': 0.099,
      'Neutral': 0.901,
      'Positive': 0.0,
      'Tweets Ago': 11},
     {'Compound': 0.8316,
      'Negative': 0.0,
      'Neutral': 0.794,
      'Positive': 0.206,
      'Tweets Ago': 12},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 13},
     {'Compound': 0.2263,
      'Negative': 0.0,
      'Neutral': 0.863,
      'Positive': 0.137,
      'Tweets Ago': 14},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.769,
      'Positive': 0.231,
      'Tweets Ago': 15},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 16},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 17},
     {'Compound': -0.4019,
      'Negative': 0.278,
      'Neutral': 0.722,
      'Positive': 0.0,
      'Tweets Ago': 18},
     {'Compound': -0.3199,
      'Negative': 0.092,
      'Neutral': 0.853,
      'Positive': 0.055,
      'Tweets Ago': 19},
     {'Compound': -0.5484,
      'Negative': 0.146,
      'Neutral': 0.793,
      'Positive': 0.06,
      'Tweets Ago': 20},
     {'Compound': 0.3818,
      'Negative': 0.0,
      'Neutral': 0.852,
      'Positive': 0.148,
      'Tweets Ago': 21},
     {'Compound': -0.9277,
      'Negative': 0.418,
      'Neutral': 0.582,
      'Positive': 0.0,
      'Tweets Ago': 22},
     {'Compound': 0.7783,
      'Negative': 0.0,
      'Neutral': 0.702,
      'Positive': 0.298,
      'Tweets Ago': 23},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.892,
      'Positive': 0.108,
      'Tweets Ago': 24},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 25},
     {'Compound': -0.6324,
      'Negative': 0.147,
      'Neutral': 0.853,
      'Positive': 0.0,
      'Tweets Ago': 26},
     {'Compound': 0.3818,
      'Negative': 0.0,
      'Neutral': 0.833,
      'Positive': 0.167,
      'Tweets Ago': 27},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 28},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 29},
     {'Compound': -0.8555,
      'Negative': 0.308,
      'Neutral': 0.579,
      'Positive': 0.113,
      'Tweets Ago': 30},
     {'Compound': 0.4404,
      'Negative': 0.0,
      'Neutral': 0.879,
      'Positive': 0.121,
      'Tweets Ago': 31},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 32},
     {'Compound': -0.4767,
      'Negative': 0.22,
      'Neutral': 0.78,
      'Positive': 0.0,
      'Tweets Ago': 33},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.924,
      'Positive': 0.076,
      'Tweets Ago': 34},
     {'Compound': -0.5994,
      'Negative': 0.194,
      'Neutral': 0.725,
      'Positive': 0.081,
      'Tweets Ago': 35},
     {'Compound': 0.5707,
      'Negative': 0.0,
      'Neutral': 0.862,
      'Positive': 0.138,
      'Tweets Ago': 36},
     {'Compound': -0.6765,
      'Negative': 0.209,
      'Neutral': 0.791,
      'Positive': 0.0,
      'Tweets Ago': 37},
     {'Compound': -0.3566,
      'Negative': 0.058,
      'Neutral': 0.942,
      'Positive': 0.0,
      'Tweets Ago': 38},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.881,
      'Positive': 0.119,
      'Tweets Ago': 39},
     {'Compound': 0.7906,
      'Negative': 0.0,
      'Neutral': 0.843,
      'Positive': 0.157,
      'Tweets Ago': 40},
     {'Compound': 0.25,
      'Negative': 0.12,
      'Neutral': 0.679,
      'Positive': 0.201,
      'Tweets Ago': 41},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 42},
     {'Compound': -0.8271,
      'Negative': 0.209,
      'Neutral': 0.791,
      'Positive': 0.0,
      'Tweets Ago': 43},
     {'Compound': -0.8126,
      'Negative': 0.54,
      'Neutral': 0.46,
      'Positive': 0.0,
      'Tweets Ago': 44},
     {'Compound': 0.296,
      'Negative': 0.095,
      'Neutral': 0.714,
      'Positive': 0.19,
      'Tweets Ago': 45},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 46},
     {'Compound': -0.3612,
      'Negative': 0.2,
      'Neutral': 0.8,
      'Positive': 0.0,
      'Tweets Ago': 47},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 48},
     {'Compound': -0.0258,
      'Negative': 0.205,
      'Neutral': 0.548,
      'Positive': 0.247,
      'Tweets Ago': 49},
     {'Compound': -0.3182,
      'Negative': 0.126,
      'Neutral': 0.874,
      'Positive': 0.0,
      'Tweets Ago': 50},
     {'Compound': -0.3818,
      'Negative': 0.206,
      'Neutral': 0.794,
      'Positive': 0.0,
      'Tweets Ago': 51},
     {'Compound': -0.6908,
      'Negative': 0.217,
      'Neutral': 0.783,
      'Positive': 0.0,
      'Tweets Ago': 52},
     {'Compound': -0.4019,
      'Negative': 0.162,
      'Neutral': 0.838,
      'Positive': 0.0,
      'Tweets Ago': 53},
     {'Compound': 0.8271,
      'Negative': 0.0,
      'Neutral': 0.565,
      'Positive': 0.435,
      'Tweets Ago': 54},
     {'Compound': 0.5707,
      'Negative': 0.0,
      'Neutral': 0.871,
      'Positive': 0.129,
      'Tweets Ago': 55},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 56},
     {'Compound': -0.765,
      'Negative': 0.306,
      'Neutral': 0.694,
      'Positive': 0.0,
      'Tweets Ago': 57},
     {'Compound': -0.7506,
      'Negative': 0.314,
      'Neutral': 0.686,
      'Positive': 0.0,
      'Tweets Ago': 58},
     {'Compound': 0.5106,
      'Negative': 0.0,
      'Neutral': 0.732,
      'Positive': 0.268,
      'Tweets Ago': 59},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 60},
     {'Compound': -0.6705,
      'Negative': 0.31,
      'Neutral': 0.69,
      'Positive': 0.0,
      'Tweets Ago': 61},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.847,
      'Positive': 0.153,
      'Tweets Ago': 62},
     {'Compound': 0.296,
      'Negative': 0.066,
      'Neutral': 0.819,
      'Positive': 0.115,
      'Tweets Ago': 63},
     {'Compound': -0.7482,
      'Negative': 0.298,
      'Neutral': 0.608,
      'Positive': 0.094,
      'Tweets Ago': 64},
     {'Compound': -0.1531,
      'Negative': 0.118,
      'Neutral': 0.882,
      'Positive': 0.0,
      'Tweets Ago': 65},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.73,
      'Positive': 0.27,
      'Tweets Ago': 66},
     {'Compound': -0.5423,
      'Negative': 0.241,
      'Neutral': 0.759,
      'Positive': 0.0,
      'Tweets Ago': 67},
     {'Compound': -0.4019,
      'Negative': 0.209,
      'Neutral': 0.678,
      'Positive': 0.113,
      'Tweets Ago': 68},
     {'Compound': -0.4019,
      'Negative': 0.162,
      'Neutral': 0.838,
      'Positive': 0.0,
      'Tweets Ago': 69},
     {'Compound': -0.4939,
      'Negative': 0.352,
      'Neutral': 0.494,
      'Positive': 0.154,
      'Tweets Ago': 70},
     {'Compound': -0.1027,
      'Negative': 0.134,
      'Neutral': 0.746,
      'Positive': 0.119,
      'Tweets Ago': 71},
     {'Compound': -0.4404,
      'Negative': 0.162,
      'Neutral': 0.838,
      'Positive': 0.0,
      'Tweets Ago': 72},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 73},
     {'Compound': -0.4767,
      'Negative': 0.156,
      'Neutral': 0.767,
      'Positive': 0.077,
      'Tweets Ago': 74},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.898,
      'Positive': 0.102,
      'Tweets Ago': 75},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 76},
     {'Compound': -0.9538,
      'Negative': 0.464,
      'Neutral': 0.536,
      'Positive': 0.0,
      'Tweets Ago': 77},
     {'Compound': 0.7184,
      'Negative': 0.0,
      'Neutral': 0.812,
      'Positive': 0.188,
      'Tweets Ago': 78},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 79},
     {'Compound': -0.2023,
      'Negative': 0.122,
      'Neutral': 0.878,
      'Positive': 0.0,
      'Tweets Ago': 80},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 81},
     {'Compound': 0.4767,
      'Negative': 0.068,
      'Neutral': 0.769,
      'Positive': 0.163,
      'Tweets Ago': 82},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.902,
      'Positive': 0.098,
      'Tweets Ago': 83},
     {'Compound': -0.802,
      'Negative': 0.396,
      'Neutral': 0.604,
      'Positive': 0.0,
      'Tweets Ago': 84},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 85},
     {'Compound': -0.3612,
      'Negative': 0.053,
      'Neutral': 0.947,
      'Positive': 0.0,
      'Tweets Ago': 86},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 87},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.848,
      'Positive': 0.152,
      'Tweets Ago': 88},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 89},
     {'Compound': -0.9201,
      'Negative': 0.283,
      'Neutral': 0.672,
      'Positive': 0.045,
      'Tweets Ago': 90},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 91},
     {'Compound': 0.5707,
      'Negative': 0.0,
      'Neutral': 0.871,
      'Positive': 0.129,
      'Tweets Ago': 92},
     {'Compound': -0.6486,
      'Negative': 0.306,
      'Neutral': 0.694,
      'Positive': 0.0,
      'Tweets Ago': 93},
     {'Compound': -0.2023,
      'Negative': 0.153,
      'Neutral': 0.847,
      'Positive': 0.0,
      'Tweets Ago': 94},
     {'Compound': -0.5574,
      'Negative': 0.087,
      'Neutral': 0.913,
      'Positive': 0.0,
      'Tweets Ago': 95},
     {'Compound': -0.7964,
      'Negative': 0.18,
      'Neutral': 0.82,
      'Positive': 0.0,
      'Tweets Ago': 96},
     {'Compound': -0.802,
      'Negative': 0.188,
      'Neutral': 0.812,
      'Positive': 0.0,
      'Tweets Ago': 97},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 98},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 99},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.719,
      'Positive': 0.281,
      'Tweets Ago': 100}]




```python
foxnews_name = tweet['user']['name']
sentiments_foxnews_df = pd.DataFrame(sentiments_foxnews)
sentiments_foxnews_df['Media Source'] = foxnews_name
sentiments_foxnews_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>Media Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.8658</td>
      <td>0.033</td>
      <td>0.722</td>
      <td>0.245</td>
      <td>1</td>
      <td>Fox News</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.5574</td>
      <td>0.081</td>
      <td>0.919</td>
      <td>0.000</td>
      <td>2</td>
      <td>Fox News</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.2732</td>
      <td>0.067</td>
      <td>0.815</td>
      <td>0.119</td>
      <td>3</td>
      <td>Fox News</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>4</td>
      <td>Fox News</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.7906</td>
      <td>0.000</td>
      <td>0.733</td>
      <td>0.267</td>
      <td>5</td>
      <td>Fox News</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Target Account
target_user = "@nytimes"

# YOUR CODE HERE
n_results = 100
counter = 1
sentiments_nytimes = []
for status in tweepy.Cursor(api.user_timeline, id=target_user, tweet_mode="extended").items(n_results):
    tweet=status._json
    results=analyzer.polarity_scores(tweet["full_text"])
    pos = results['pos']
    neg = results['neg']
    neu = results['neu']
    compound = results['compound']
    tweets_ago = counter
    
    sentiments_nytimes.append({
                      "Compound" : compound,
                      "Positive" : pos,
                      "Negative" : neg,
                      "Neutral" : neu,
                      "Tweets Ago": counter})
    counter+=1
    
sentiments_nytimes
```




    [{'Compound': -0.2263,
      'Negative': 0.113,
      'Neutral': 0.821,
      'Positive': 0.067,
      'Tweets Ago': 1},
     {'Compound': -0.1531,
      'Negative': 0.065,
      'Neutral': 0.935,
      'Positive': 0.0,
      'Tweets Ago': 2},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 3},
     {'Compound': -0.4588,
      'Negative': 0.107,
      'Neutral': 0.893,
      'Positive': 0.0,
      'Tweets Ago': 4},
     {'Compound': 0.3254,
      'Negative': 0.0,
      'Neutral': 0.896,
      'Positive': 0.104,
      'Tweets Ago': 5},
     {'Compound': -0.4404,
      'Negative': 0.26,
      'Neutral': 0.606,
      'Positive': 0.134,
      'Tweets Ago': 6},
     {'Compound': 0.4019,
      'Negative': 0.0,
      'Neutral': 0.748,
      'Positive': 0.252,
      'Tweets Ago': 7},
     {'Compound': 0.6124,
      'Negative': 0.0,
      'Neutral': 0.792,
      'Positive': 0.208,
      'Tweets Ago': 8},
     {'Compound': -0.6908,
      'Negative': 0.19,
      'Neutral': 0.81,
      'Positive': 0.0,
      'Tweets Ago': 9},
     {'Compound': 0.34,
      'Negative': 0.0,
      'Neutral': 0.893,
      'Positive': 0.107,
      'Tweets Ago': 10},
     {'Compound': 0.2776,
      'Negative': 0.059,
      'Neutral': 0.837,
      'Positive': 0.104,
      'Tweets Ago': 11},
     {'Compound': 0.4215,
      'Negative': 0.0,
      'Neutral': 0.797,
      'Positive': 0.203,
      'Tweets Ago': 12},
     {'Compound': -0.1027,
      'Negative': 0.152,
      'Neutral': 0.742,
      'Positive': 0.106,
      'Tweets Ago': 13},
     {'Compound': 0.2297,
      'Negative': 0.0,
      'Neutral': 0.854,
      'Positive': 0.146,
      'Tweets Ago': 14},
     {'Compound': 0.34,
      'Negative': 0.0,
      'Neutral': 0.821,
      'Positive': 0.179,
      'Tweets Ago': 15},
     {'Compound': 0.7351,
      'Negative': 0.0,
      'Neutral': 0.776,
      'Positive': 0.224,
      'Tweets Ago': 16},
     {'Compound': -0.6124,
      'Negative': 0.267,
      'Neutral': 0.733,
      'Positive': 0.0,
      'Tweets Ago': 17},
     {'Compound': 0.4215,
      'Negative': 0.0,
      'Neutral': 0.877,
      'Positive': 0.123,
      'Tweets Ago': 18},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 19},
     {'Compound': 0.4215,
      'Negative': 0.0,
      'Neutral': 0.877,
      'Positive': 0.123,
      'Tweets Ago': 20},
     {'Compound': -0.8779,
      'Negative': 0.336,
      'Neutral': 0.664,
      'Positive': 0.0,
      'Tweets Ago': 21},
     {'Compound': -0.128,
      'Negative': 0.158,
      'Neutral': 0.842,
      'Positive': 0.0,
      'Tweets Ago': 22},
     {'Compound': -0.3612,
      'Negative': 0.185,
      'Neutral': 0.815,
      'Positive': 0.0,
      'Tweets Ago': 23},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.709,
      'Positive': 0.291,
      'Tweets Ago': 24},
     {'Compound': 0.5719,
      'Negative': 0.0,
      'Neutral': 0.684,
      'Positive': 0.316,
      'Tweets Ago': 25},
     {'Compound': 0.6597,
      'Negative': 0.0,
      'Neutral': 0.769,
      'Positive': 0.231,
      'Tweets Ago': 26},
     {'Compound': 0.8591,
      'Negative': 0.0,
      'Neutral': 0.578,
      'Positive': 0.422,
      'Tweets Ago': 27},
     {'Compound': 0.7964,
      'Negative': 0.0,
      'Neutral': 0.458,
      'Positive': 0.542,
      'Tweets Ago': 28},
     {'Compound': -0.1779,
      'Negative': 0.159,
      'Neutral': 0.841,
      'Positive': 0.0,
      'Tweets Ago': 29},
     {'Compound': -0.6124,
      'Negative': 0.357,
      'Neutral': 0.643,
      'Positive': 0.0,
      'Tweets Ago': 30},
     {'Compound': 0.7579,
      'Negative': 0.0,
      'Neutral': 0.772,
      'Positive': 0.228,
      'Tweets Ago': 31},
     {'Compound': -0.1779,
      'Negative': 0.195,
      'Neutral': 0.637,
      'Positive': 0.167,
      'Tweets Ago': 32},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 33},
     {'Compound': -0.1531,
      'Negative': 0.187,
      'Neutral': 0.659,
      'Positive': 0.154,
      'Tweets Ago': 34},
     {'Compound': 0.3612,
      'Negative': 0.079,
      'Neutral': 0.753,
      'Positive': 0.168,
      'Tweets Ago': 35},
     {'Compound': -0.7717,
      'Negative': 0.427,
      'Neutral': 0.573,
      'Positive': 0.0,
      'Tweets Ago': 36},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 37},
     {'Compound': -0.2023,
      'Negative': 0.118,
      'Neutral': 0.802,
      'Positive': 0.08,
      'Tweets Ago': 38},
     {'Compound': 0.34,
      'Negative': 0.0,
      'Neutral': 0.893,
      'Positive': 0.107,
      'Tweets Ago': 39},
     {'Compound': 0.2732,
      'Negative': 0.0,
      'Neutral': 0.826,
      'Positive': 0.174,
      'Tweets Ago': 40},
     {'Compound': 0.5256,
      'Negative': 0.0,
      'Neutral': 0.825,
      'Positive': 0.175,
      'Tweets Ago': 41},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 42},
     {'Compound': 0.4069,
      'Negative': 0.1,
      'Neutral': 0.779,
      'Positive': 0.121,
      'Tweets Ago': 43},
     {'Compound': -0.2023,
      'Negative': 0.112,
      'Neutral': 0.808,
      'Positive': 0.081,
      'Tweets Ago': 44},
     {'Compound': 0.2732,
      'Negative': 0.0,
      'Neutral': 0.932,
      'Positive': 0.068,
      'Tweets Ago': 45},
     {'Compound': -0.0516,
      'Negative': 0.112,
      'Neutral': 0.787,
      'Positive': 0.101,
      'Tweets Ago': 46},
     {'Compound': 0.7845,
      'Negative': 0.0,
      'Neutral': 0.792,
      'Positive': 0.208,
      'Tweets Ago': 47},
     {'Compound': 0.0231,
      'Negative': 0.168,
      'Neutral': 0.629,
      'Positive': 0.203,
      'Tweets Ago': 48},
     {'Compound': -0.7717,
      'Negative': 0.288,
      'Neutral': 0.712,
      'Positive': 0.0,
      'Tweets Ago': 49},
     {'Compound': -0.7096,
      'Negative': 0.269,
      'Neutral': 0.731,
      'Positive': 0.0,
      'Tweets Ago': 50},
     {'Compound': 0.0772,
      'Negative': 0.055,
      'Neutral': 0.879,
      'Positive': 0.066,
      'Tweets Ago': 51},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 52},
     {'Compound': -0.4767,
      'Negative': 0.129,
      'Neutral': 0.871,
      'Positive': 0.0,
      'Tweets Ago': 53},
     {'Compound': 0.25,
      'Negative': 0.0,
      'Neutral': 0.938,
      'Positive': 0.062,
      'Tweets Ago': 54},
     {'Compound': 0.6369,
      'Negative': 0.0,
      'Neutral': 0.843,
      'Positive': 0.157,
      'Tweets Ago': 55},
     {'Compound': -0.8885,
      'Negative': 0.304,
      'Neutral': 0.696,
      'Positive': 0.0,
      'Tweets Ago': 56},
     {'Compound': -0.8462,
      'Negative': 0.246,
      'Neutral': 0.754,
      'Positive': 0.0,
      'Tweets Ago': 57},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.918,
      'Positive': 0.082,
      'Tweets Ago': 58},
     {'Compound': -0.1027,
      'Negative': 0.152,
      'Neutral': 0.742,
      'Positive': 0.106,
      'Tweets Ago': 59},
     {'Compound': -0.3182,
      'Negative': 0.103,
      'Neutral': 0.897,
      'Positive': 0.0,
      'Tweets Ago': 60},
     {'Compound': -0.8591,
      'Negative': 0.463,
      'Neutral': 0.537,
      'Positive': 0.0,
      'Tweets Ago': 61},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 62},
     {'Compound': 0.2297,
      'Negative': 0.0,
      'Neutral': 0.854,
      'Positive': 0.146,
      'Tweets Ago': 63},
     {'Compound': 0.4685,
      'Negative': 0.0,
      'Neutral': 0.844,
      'Positive': 0.156,
      'Tweets Ago': 64},
     {'Compound': 0.2732,
      'Negative': 0.098,
      'Neutral': 0.711,
      'Positive': 0.191,
      'Tweets Ago': 65},
     {'Compound': 0.4215,
      'Negative': 0.0,
      'Neutral': 0.877,
      'Positive': 0.123,
      'Tweets Ago': 66},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 67},
     {'Compound': -0.34,
      'Negative': 0.194,
      'Neutral': 0.806,
      'Positive': 0.0,
      'Tweets Ago': 68},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 69},
     {'Compound': -0.5574,
      'Negative': 0.143,
      'Neutral': 0.823,
      'Positive': 0.034,
      'Tweets Ago': 70},
     {'Compound': -0.6908,
      'Negative': 0.186,
      'Neutral': 0.814,
      'Positive': 0.0,
      'Tweets Ago': 71},
     {'Compound': -0.4404,
      'Negative': 0.14,
      'Neutral': 0.789,
      'Positive': 0.072,
      'Tweets Ago': 72},
     {'Compound': 0.6124,
      'Negative': 0.0,
      'Neutral': 0.792,
      'Positive': 0.208,
      'Tweets Ago': 73},
     {'Compound': 0.5423,
      'Negative': 0.098,
      'Neutral': 0.721,
      'Positive': 0.18,
      'Tweets Ago': 74},
     {'Compound': -0.6486,
      'Negative': 0.346,
      'Neutral': 0.654,
      'Positive': 0.0,
      'Tweets Ago': 75},
     {'Compound': 0.046,
      'Negative': 0.061,
      'Neutral': 0.838,
      'Positive': 0.101,
      'Tweets Ago': 76},
     {'Compound': -0.9136,
      'Negative': 0.463,
      'Neutral': 0.489,
      'Positive': 0.049,
      'Tweets Ago': 77},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 78},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 79},
     {'Compound': 0.1901,
      'Negative': 0.0,
      'Neutral': 0.951,
      'Positive': 0.049,
      'Tweets Ago': 80},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 81},
     {'Compound': 0.2732,
      'Negative': 0.0,
      'Neutral': 0.826,
      'Positive': 0.174,
      'Tweets Ago': 82},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 83},
     {'Compound': 0.0258,
      'Negative': 0.184,
      'Neutral': 0.628,
      'Positive': 0.188,
      'Tweets Ago': 84},
     {'Compound': -0.4291,
      'Negative': 0.079,
      'Neutral': 0.921,
      'Positive': 0.0,
      'Tweets Ago': 85},
     {'Compound': -0.296,
      'Negative': 0.073,
      'Neutral': 0.927,
      'Positive': 0.0,
      'Tweets Ago': 86},
     {'Compound': -0.3182,
      'Negative': 0.161,
      'Neutral': 0.839,
      'Positive': 0.0,
      'Tweets Ago': 87},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.815,
      'Positive': 0.185,
      'Tweets Ago': 88},
     {'Compound': 0.3612,
      'Negative': 0.0,
      'Neutral': 0.828,
      'Positive': 0.172,
      'Tweets Ago': 89},
     {'Compound': -0.3818,
      'Negative': 0.133,
      'Neutral': 0.867,
      'Positive': 0.0,
      'Tweets Ago': 90},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 91},
     {'Compound': -0.8687,
      'Negative': 0.271,
      'Neutral': 0.729,
      'Positive': 0.0,
      'Tweets Ago': 92},
     {'Compound': -0.9062,
      'Negative': 0.637,
      'Neutral': 0.363,
      'Positive': 0.0,
      'Tweets Ago': 93},
     {'Compound': -0.2263,
      'Negative': 0.147,
      'Neutral': 0.853,
      'Positive': 0.0,
      'Tweets Ago': 94},
     {'Compound': 0.7096,
      'Negative': 0.0,
      'Neutral': 0.742,
      'Positive': 0.258,
      'Tweets Ago': 95},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 96},
     {'Compound': 0.0,
      'Negative': 0.0,
      'Neutral': 1.0,
      'Positive': 0.0,
      'Tweets Ago': 97},
     {'Compound': -0.34,
      'Negative': 0.231,
      'Neutral': 0.769,
      'Positive': 0.0,
      'Tweets Ago': 98},
     {'Compound': 0.5423,
      'Negative': 0.053,
      'Neutral': 0.772,
      'Positive': 0.175,
      'Tweets Ago': 99},
     {'Compound': 0.1531,
      'Negative': 0.0,
      'Neutral': 0.904,
      'Positive': 0.096,
      'Tweets Ago': 100}]




```python
nytimes_name = tweet['user']['name']
sentiments_nytimes_df = pd.DataFrame(sentiments_nytimes)
sentiments_nytimes_df['Media Source'] = nytimes_name
sentiments_nytimes_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>Media Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.2263</td>
      <td>0.113</td>
      <td>0.821</td>
      <td>0.067</td>
      <td>1</td>
      <td>The New York Times</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.1531</td>
      <td>0.065</td>
      <td>0.935</td>
      <td>0.000</td>
      <td>2</td>
      <td>The New York Times</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>3</td>
      <td>The New York Times</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.4588</td>
      <td>0.107</td>
      <td>0.893</td>
      <td>0.000</td>
      <td>4</td>
      <td>The New York Times</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.3254</td>
      <td>0.000</td>
      <td>0.896</td>
      <td>0.104</td>
      <td>5</td>
      <td>The New York Times</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_sentiments_df = pd.concat([sentiments_bbc_df, sentiments_cbs_df, sentiments_cnn_df, sentiments_foxnews_df, sentiments_nytimes_df], ignore_index=True)
combined_sentiments_df.head()
combined_sentiments_df.to_csv('NewsMood_SDS.csv')
```


```python
#tried double loop to collect info from all news outlets but code did not work
#news_outlets = ("@BBC", "@CBS", "@CNN", "@FoxNews", "nytimes")
#for outlet in news_outlets:
#    n_tweets = 100
#    compound_list = []
#    positive_list = []
#    negative_list = []
#    neutral_list = []
#    sentiments = []
#    for status in tweepy.Cursor(api.user_timeline, id=outlet, tweet_mode='extended', result_type = 'recent').items(n_tweets):
#        tweet = status._json
        
        #vader analysis
#        results = analyzer.polarity_scores(tweet['full_text'])
#        compound = results['compound']
#        pos = results['pos']
#        neg = results['neg']
#        neu = results['neu']
        
        #add value to arrays
#        compound_list.append(results['compound'])
#        positive_list.append(results['pos'])
#        negative_list.append(results['neg'])
#        neutral_list.append(results['neu'])
#        
#        sentiment = {"News Outlet" : outlet,
#                    "Compound": compound_list,
#                    "Positive": positive_list,
#                     "Negative": negative_list,
#                     "Neutral": neutral_list
#                    }

```


```python
media_outlets = ["CNN", "Fox News", "CBS", "The New York Times", "BBC"]
for media in media_outlets:
    news_companies=combined_sentiments_df[combined_sentiments_df["Media Source"]==media]
    plt.plot(news_companies['Tweets Ago'], news_companies["Compound"], "o",label=media)
#plt.scatter(combined_sentiments_df['Tweets Ago'],combined_sentiments_df['Compound'])
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")
plt.title("Sentiment Analysis of Media Tweets (4/8/2018)")
plt.legend(bbox_to_anchor=(1,1))
plt.grid()
plt.show()
plt.savefig('Sentiment Analysis of Media Tweets.png')
```


![png](output_14_0.png)



    <matplotlib.figure.Figure at 0x29784b07080>



```python
compound_group = combined_sentiments_df.groupby('Media Source').mean()['Compound']
compound_average_df = pd.DataFrame(compound_group)
compound_average_df.reset_index(inplace=True)
compound_average_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Media Source</th>
      <th>Compound</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>0.091370</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CBS</td>
      <td>0.432678</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CNN</td>
      <td>-0.131075</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fox News</td>
      <td>-0.057755</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The New York Times</td>
      <td>-0.004640</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbc_compound = compound_average_df[compound_average_df['Media Source']=='BBC']['Compound']
cbs_compound = compound_average_df[compound_average_df['Media Source']=='CBS']['Compound']
cnn_compound = compound_average_df[compound_average_df['Media Source']=='CNN']['Compound']
foxnews_compound = compound_average_df[compound_average_df['Media Source']=='Fox News']['Compound']
nyt_compound = compound_average_df[compound_average_df['Media Source']=='The New York Times']['Compound']
```


```python
fig, ax = plt.subplots()
BBC = ax.bar('BBC', bbc_compound, color='skyblue')
CBS = ax.bar('CBS', cbs_compound, color='g')
CNN = ax.bar('CNN', cnn_compound, color='r')
Fox = ax.bar('Fox', foxnews_compound, color='b')
NYT = ax.bar('NYT', nyt_compound, color='y')

ax.set_ylabel("Tweet Polarity")
ax.set_title("Overall Media Sentiment Based on Twitter (4/8/2018)")
ax.grid(True)

plt.savefig('Overall Media Sentiment Based on Twitter.png')
```


![png](output_17_0.png)

