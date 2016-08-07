import twitter
import sys
import json



consumer_key = 'SXl2ENelBF2BKylMY3qzkB5ku'
consumer_secret = 'hqgMxRHop9egXclUrshXlCC4fuEUp8uDsoVAfpuuxfs7udM9Qf'
access_token = '750884170583400448-aSfH5mHqh4vg1r26Ml36V7J18ve2eum'
access_secret = 'iH6Umr0eC5kvEKgakv1wM0qzEGBP3YSc9f7gQ77q9AfvD'
    
auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)
    
twitter_api = twitter.Twitter(auth=auth)


q = 'Trump'

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

         

dates = []
i=1 



try:
    while i < 10000:
         for tweet in stream:
             dates.append(tweet['created_at'])
             print (i)
             i = i+1 
             break
             
finally:
    

    with open('dates.json', 'a') as outfile:
         json.dump(dates, outfile)


print (len(dates))
