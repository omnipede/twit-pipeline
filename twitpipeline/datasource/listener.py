"""
Foo bar
"""
import json
from abc import ABCMeta, abstractmethod

import tweepy
from tweepy import StreamListener

from twitpipeline.config import twit_api_key, \
    twit_api_secret_key, \
    twit_access_token, \
    twit_access_token_secret
from twitpipeline.mq.publisher import Publisher


class Listener(metaclass=ABCMeta):
    """
    Data source listener interface
    """
    @abstractmethod
    def listen(self, track: list[str]) -> None:
        """
        Start listening
        """


class TweetListener(Listener):
    """
    Listener 구현체
    """
    def __init__(self, publisher: Publisher):
        self._stream_listener: StreamListener = TweetStreamListener(publisher=publisher)

    def listen(self, track: list[str]) -> None:
        """
        Twitter API 를 통해 데이터를 스트리밍하는 메소드
        """
        twitter_stream = self.__open_twit_stream()
        twitter_stream.filter(track=['game'])

    def __open_twit_stream(self) -> tweepy.Stream:
        """
        Open twit data stream with Twitter OAuth license
        """
        stream_listener: StreamListener = self._stream_listener
        tweet_auth = tweepy.OAuthHandler(twit_api_key, twit_api_secret_key)
        tweet_auth.set_access_token(twit_access_token, twit_access_token_secret)
        return tweepy.Stream(tweet_auth, stream_listener)


class TweetStreamListener(StreamListener):
    """
    tweepy StreamListener 구현체
    """
    def __init__(self, publisher: Publisher):
        super().__init__()
        self._publisher = publisher

    def on_status(self, status) -> None:
        tweet = json.dumps({
            'id': status.id, 'created_at': status.created_at, 'text': status.text
        }, default=str)
        self._publisher.publish(data=tweet.encode('utf-8'))

    def on_error(self, status_code):
        print('ERROR', status_code)
        if status_code == 420:
            return False
        return True
