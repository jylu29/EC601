import tweepy


def get_auth():
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    access_token = 'access_token'
    access_token_secret = 'access_token_secret'
    auth = tweepy.OAuthHandler(
        consumer_key, consumer_secret, access_token
    )
    auth.set_access_token(access_token, access_token_secret)
    return auth


# Get the user timeline
def get_timeline(auth):
    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


# Get the user status
def get_status(auth, id):
    api = tweepy.API(auth)
    return api.get_status(id)


#  Get the followers of specified id or screen name
def get_followers(auth, id):
    api = tweepy.API(auth)
    return api.followers(id)


if __name__ == '__main__':
    auth = get_auth()
    get_timeline(auth)
    print(get_followers(auth, ''))
