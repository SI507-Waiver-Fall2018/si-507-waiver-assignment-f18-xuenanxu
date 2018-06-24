# Name: Xuenan Xu
# uniqname: xuenanxu
# UMID: 35069066

# these should be the only imports you need
import tweepy
import nltk
import json
import sys
import re
from nltk.corpus import stopwords
from collections import Counter


# write your code here
# usage should be python3 part1.py <username> <num_tweets>

#input <username> and <num_tweets> from terminal
username = sys.argv[1]
num_tweets = sys.argv[2]

# Twitter API credentials
consumer_key = "NshTkl12iN403rwAMPIKe6QNm"
consumer_secret = "T1strmb5m8Cov3f82iWR9ECJA3AEfe8VvsdAhEN3Ay4mMxucnd"
access_key = "953558126611050501-dYcUAljPmJDGZpNwBWnMfpC4jXFbVCl"
access_secret = "cSMJ9zXfAxStS0cVmkguhRSuHb73Cm2Chb1wkL5RrPYIo"

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# initial request for user tweets
api = tweepy.API(auth)
user_tweets = api.user_timeline(id = username, num = num_tweets, tweet_mode = "extended")

# create corpus for user tweets
corpus = ""
for tweet in user_tweets:
    corpus += tweet.full_text + " "

tokens = nltk.word_tokenize(corpus)

# get rid of stopwords
stopWords = set(stopwords.words('english'))
stopWords.update(['http','https','RT'])

cleared_tokens = []
for w in tokens:
    if w not in stopWords and re.match("[a-zA-Z]", w):
        cleared_tokens.append(w)

tagged_tokens = nltk.pos_tag(cleared_tokens)

# create list of verbs, nouns and adj
tweet_tokens_verb = []
tweet_tokens_noun = []
tweet_tokens_adj = []
for (token,tagger) in tagged_tokens:
    if tagger.startswith('VB'):
        tweet_tokens_verb.append(token)
    elif tagger.startswith('NN'):
        tweet_tokens_noun.append(token)
    elif tagger.startswith('JJ'):
        tweet_tokens_adj.append(token)

# define functions for picking the top five words
def top_five(cleared_tokens):
	tweet_tokens_freq = Counter(cleared_tokens)
	top_five_words = tweet_tokens_freq.most_common(5)
	return top_five_words

def output_string(top_five_words):
	common_word = ""
	for token in top_five_words:
		common_word += token[0]+"("+str(token[1])+") "
	return common_word

# get the top five verb, noun and adj
top_verb = top_five(tweet_tokens_verb)
top_noun = top_five(tweet_tokens_noun)
top_adj = top_five(tweet_tokens_adj)

# number of the original tweets
original_tweets = api.user_timeline(id = username,num = num_tweets,include_rts = False,tweet_mode='extended')

# number of the original tweets that are favourited
fav = 0
for tweet in original_tweets:
    fav += tweet.favorite_count

# number of the original tweets that are retweeted
retweet = 0
for tweet in original_tweets:
    retweet += tweet.retweet_count


# final output

# save the top five noun to csv
noun_data = open('noun_data.csv','w')
noun_data.write("Noun,Number\n")
words = re.findall('\w+', output_string(top_noun))
for i,j in zip(words[0::2],words[1::2]):
   noun_data.write(i + "," + j + "\n")

# print output
def output():
	print("USER:", username)
	print("TWEETS ANALYZED:", num_tweets)
	print("VERBS:", output_string(top_verb))
	print("NOUNS:", output_string(top_noun))
	print("ADJECTIVES:", output_string(top_adj))
	print("ORIGINAL TWEETS:", len(original_tweets))
	print( "TIMES FAVORITED (ORIGINAL TWEETS ONLY:)", fav)
	print("TIMES FAVORITED (ORIGINAL TWEETS ONLY:)", retweet)

output()



