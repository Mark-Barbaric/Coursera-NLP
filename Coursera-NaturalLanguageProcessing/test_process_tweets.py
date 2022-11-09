import text_preprocessing
import numpy as np
from nltk import twitter_samples

all_positive_tweets=twitter_samples.strings('positive_tweets.json')

def test_remove_hyperlinks():
    tweet1 = "#mbarbari https://this-is-me.com i love this"
    cleaned_tweet = text_preprocessing.remove_hyperlinks_and_twitter_styles(tweet1)
    assert cleaned_tweet == "mbarbari  i love this"

def test_tokenize_tweet():
    tweet1 = "#mbarbari i an loving this website https://this-is-me!!!. True love :) :) ;)"
    tokenized_tweet = text_preprocessing.process_tweet(tweet1)
    assert(tokenized_tweet == ['mbarbari', 'love', 'websit', 'true', 'love', ':)', ':)', ';)'])

def test_build_frequecies():
    tweet1 = all_positive_tweets[0]
    labels = np.append(np.ones(5), np.zeros(5))
    freq = text_preprocessing.build_word_frequencies(tweet1, labels)