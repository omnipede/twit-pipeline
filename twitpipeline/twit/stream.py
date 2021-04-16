"""
Twit stream 관련 메소드
"""

import tweepy
from tweepy import StreamListener

from twitpipeline.config \
    import twit_api_key, twit_api_secret_key, twit_access_token_secret, twit_access_token


def create_twit_stream(stream_listener: StreamListener) -> tweepy.Stream:
    """
    설정 파일을 읽고 twitter OAuth 을 세팅한 뒤 stream 을 생성하는 메소드
    :param stream_listener: Stream listener.
    :return: Twit data stream
    """
    twit_auth = tweepy.OAuthHandler(twit_api_key, twit_api_secret_key)
    twit_auth.set_access_token(twit_access_token, twit_access_token_secret)
    return tweepy.Stream(twit_auth, stream_listener)
