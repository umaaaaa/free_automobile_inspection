#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# twitter_key = {
#         "consumer_key"       : '3ijyREamIGKZxM6LQEUodZKp5',
#         "consumer_secret"    : 'K1YT2lSkD38vBDz0of9eIQj1tx7KHOqtnmQFoRGVUqMCAd4NwV',
#         "access_token"       : '2587234754-ASltwQEUTGRMKeKSudNPRpAsT3IHbP1mMSt5I7e',
#         "access_token_secret": 'MiUWHQYsUHTSfbCqb1nMMWlTdcUFRPYho9s3CIAvDraHu'
#         }

hoge = os.environ.get('CONSUMER_KEY')
print hoge

# if __name__ == "__main__":
#
#     for env in os.environ:
#         print env
#
#     print "----------------------------------"
#     print os.environ.get("CONSUMER_KEY")
