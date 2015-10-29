#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import time, calendar
import datetime
import locale
import os
import commands

oath_key_dict = {
        "consumer_key"       : os.environ.get('CONSUMER_KEY'),
        "consumer_secret"    : os.environ.get('CONSUMER_SECRET'),
        "access_token"       : os.environ.get('ACCESS_TOKEN'),
        "access_token_secret": os.environ.get('ACCESS_TOKEN_SECRET')
        }

class SearchTweets:

    #取得したTweetの日本時間を取得する
    def tweet_JapanTime(self, created_at):
        standard_time = datetime.datetime.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y')
        japan_time    = standard_time + datetime.timedelta(hours=9)
        return japan_time 

    # 車検 && 辰巳 に関するツイートをディクショナリにして返す
    def fetch_tweet(self):
        searchTweets      = SearchTweets()
        host_current_time = datetime.datetime.now()
        japan_time        = host_current_time 
        six_hours_ago     = host_current_time - datetime.timedelta(hours=6)
        tweets_dic        = {}

        # 辰巳PAの無料車検調べる用
        tweets = searchTweets.tweet_search(
                u"車検 && 辰巳", oath_key_dict
                )

        i = 0
        for tweet_all_data in tweets["statuses"]:
            Created_at       = searchTweets.tweet_JapanTime(tweet_all_data["created_at"])
            tweet_id         = tweet_all_data[u'id_str']
            text             = tweet_all_data[u'text']
            created_at       = tweet_all_data[u'created_at']
            user_id          = tweet_all_data[u'user'][u'id_str']
            user_description = tweet_all_data[u'user'][u'description']
            screen_name      = tweet_all_data[u'user'][u'screen_name']

            # 6時間前までのツイート（つぶやきテキスト）を利用
            if six_hours_ago <= Created_at: 
                tweets_dic[i] = {'text' : text, 'created_at' : Created_at}
                i += 1
            
        tweet_count = len(tweets_dic)
        japan_time = datetime.datetime.now() + datetime.timedelta(hours=9)
        url    = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": u"行ってはダメだ!!!! \n" + japan_time.strftime("%Y/%m/%d %H:%M:%S")}
        if tweet_count > 7 :
            twitter = OAuth1Session(oath_key_dict["consumer_key"],
                                    oath_key_dict["consumer_secret"],
                                    oath_key_dict["access_token"],
                                    oath_key_dict["access_token_secret"])
            if commands.getoutput("cat ./value") == 'True' :
                req = twitter.post(url, params = params)

            commands.getoutput("echo 'False' > ./value");
            return True
        else :
            commands.getoutput("echo 'True' > ./value");
            return False

    def create_oath_session(self, oath_key_dict):
        oath = OAuth1Session(
                oath_key_dict["consumer_key"],
                oath_key_dict["consumer_secret"],
                oath_key_dict["access_token"],
                oath_key_dict["access_token_secret"]
                )
        return oath

    def tweet_search(self, search_word, oath_key_dict):
        searchtweets = SearchTweets()
        url = "https://api.twitter.com/1.1/search/tweets.json?"
        params = {
            "q":           unicode(search_word),
            "lang":        "ja",
            "result_type": "recent",
            "count":       "100"
            }
        oath = searchtweets.create_oath_session(oath_key_dict)
        responce = oath.get(url, params = params)
        if responce.status_code != 200:
            print "Error code: %d" %(responce.status_code)
            return None
        tweets = json.loads(responce.text)
        return tweets

if __name__ == "__main__":
    search_tweets = SearchTweets()
    search_tweets.fetch_tweet()
