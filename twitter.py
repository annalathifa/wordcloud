 # -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:26:01 2019

@author: Anna Lathifa Liani
"""

import tweepy
from tweepy import OAuthHandler

consumer_key = 'SBdKjTESnoGU3oQbYCW36kqrN'
consumer_secret = 'GiXpgKfFacVXncblPv1yHhtyvvJsEsPmfgx6061r0vJas77OBg'
access_token = '129129254-byxgHX7hk09dkiOSm8l8JSduX4EQVplyH5VCZ07X'
access_secret = 'pbusLGmCbT7hLtJpoAZlsU05MuzZC7H0fVXqJRdRVjkGG'

auth = OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token (access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process single status
    print (status.text)
    print ("---------")

print ("=========================================================")
    

target=['karniilyas', 'detikcom', 'korantempo']
for user in target:
    for status in tweepy.Cursor(api.user_timeline, id=user).items(10):
        #Process single status
        print (status.text)
        print ("---------")
    print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

user = api.get_user(id='karniilyas')
print ('Info')
print ('Name:', user.name)
print ('Screen Name:', user.screen_name)
print ('Description:', user.description)
print ('Followers Count:', user.followers_count)


target=['karniilyas', 'mohmahfudmd', 'detikcom', 'kompascom', 'korantempo']
for userid in target:
    user = api.get_user(id=userid)
    print ('Info')
    print ('Name:', user.name)
    print ('Screen Name:', user.screen_name)
    print ('Description:', user.description)
    print ('Followers Count:', user.followers_count)
    print ('Last 20 tweets')
    for status in tweepy.Cursor(api.user_timeline, id=user).items(10):
        print (status.text)
        print ("---------")
