import re
import string
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

import sys, os
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,here)

def remove_hyperlinks_and_twitter_styles(tweet):
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks    
    tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)
    return tweet


def process_tweet(tweet):

    clean_tweet = remove_hyperlinks_and_twitter_styles(tweet)
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
    reduce_len=True)
    tweet_tokens = tokenizer.tokenize(clean_tweet)

    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')

    tweets_clean = []

    for word in tweet_tokens:
        if (word not in stopwords_english and
        word not in string.punctuation):
            stem_word = stemmer.stem(word)
            tweets_clean.append(stem_word)

    return tweets_clean  

def build_word_frequencies(tweets, labels):
    
    freqs = {}
    yslist = np.squeeze(labels.tolist())

    for label, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, label)

            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1
    

    return freqs