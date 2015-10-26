#!/usr/bin/env python
# -*- coding:utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
# from search import SearchTweets

sched = BlockingScheduler()
# search_tweets = SearchTweets()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    # search_tweets.fetch_tweet()
    print 'hello'

sched.start()
