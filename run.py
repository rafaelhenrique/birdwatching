import tweepy

from settings import (
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
    )


def print_home(api):
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


def print_user_timeline(api, user):
    user = api.get_user(user)
    for tweet in user.timeline():
        print(tweet.text)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(
        TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(
        TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # print_home(api)
    print_user_timeline(api, 'rafaelhenrique')
