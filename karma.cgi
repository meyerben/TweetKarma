#!/usr/bin/python
from birdy.twitter import UserClient
from birdy.twitter import AppClient
import cgi





CONSUMER_KEY = 'yvLZFbUtoy3Jmfz3rbSvYPKtE'
CONSUMER_SECRET = 'H4cg9Dv3J8hPfh7CUEaKWNxi8pzGeTK5eyJJNl39QAn4hPzk8f'
CALLBACK_URL = 'https://tweet-karma-cgisburne.c9.io/Stats.cgi'

client = UserClient(CONSUMER_KEY, CONSUMER_SECRET)
token = client.get_authorize_token(CALLBACK_URL)

ACCESS_TOKEN = token.oauth_token #Don't need this for anything here.
#print ACCESS_TOKEN
ACCESS_TOKEN_SECRET = token.oauth_token_secret # Don't need this for anything
#print ACCESS_TOKEN_SECRET
TOKEN_URL = token.auth_url


URL= str(TOKEN_URL)
print "Status: 301 Moved"
print "Location: %s" % URL
print

#print "Content-type: text/html\n\n"

#print TOKEN_URL




#client = UserClient(CONSUMER_KEY, CONSUMER_SECRET,       I DON'T THINK I'M USING THESE
#                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#token = client.get_access_token(OAUTH_VERIFIER)
 
'''
$ git clone https://github.com/inueni/birdy.git
$ sudo easy_install birdy
''' 

