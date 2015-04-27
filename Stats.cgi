#!/usr/bin/python
from birdy.twitter import UserClient
from urlparse import urlparse
import cgi


print "Content-type: text/html\n\n"

print "This Page Works!   "

'''These Are to get your OAUTH things'''
form = cgi.FieldStorage()
#OAUTH_TOKEN = str(form.getlist("oauth_token")[0])
OAUTH_VERIFIER = str(form.getlist("oauth_verifier")[0])

#print 'oauth token', OAUTH_TOKEN
print 'Your OAUTH_VERIFIER is: ',OAUTH_VERIFIER , '    '




CONSUMER_KEY = 'yvLZFbUtoy3Jmfz3rbSvYPKtE'
CONSUMER_SECRET = 'H4cg9Dv3J8hPfh7CUEaKWNxi8pzGeTK5eyJJNl39QAn4hPzk8f'
CALLBACK_URL = 'https://tweet-karma-cgisburne.c9.io/Stats.cgi'

client = UserClient(CONSUMER_KEY, CONSUMER_SECRET)
token = client.get_authorize_token(CALLBACK_URL)
ACCESS_TOKEN = token.oauth_token
ACCESS_TOKEN_SECRET = token.oauth_token_secret 
print "Your ACCESS_TOKEN_SECRET and ACCESS_TOKEN work!"





#print('<!DOCTYPE html><html lang="en-us"><head><meta charset="utf-8"><title>Twitter Karma</title><link type="text/css" rel="stylesheet" href="Style.CSS" media="screen"></head><body><p>' + str(OAUTH_TOKEN) + str(' ') + str(OAUTH_VERIFIER) + '</p></body></html>')

client = UserClient(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
                    
print "redefining your client worked!"

token = client.get_access_token(OAUTH_VERIFIER)

print "You have retrieved your final token!"

client.api.statuses.user_timeline.get()


print "You have made an api request!"