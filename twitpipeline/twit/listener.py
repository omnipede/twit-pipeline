"""
Twit data streaming
"""
import json

from tweepy import StreamListener

from twitpipeline.mq.publisher import Publisher


class TweetStreamListener(StreamListener):
    """
    tweepy StreamListener 구현체. Tweet stream 에 대해 listening 하다가
    데이터를 publisher 에게 넘겨준다
    """
    def __init__(self, publisher: Publisher):
        super().__init__()
        self.__publisher = publisher

    def on_status(self, status) -> None:
        print(status)
        tweet = json.dumps({
            'id': status.id, 'created_at': status.created_at, 'text': status.text
        }, default=str)
        self.__publisher.publish(data=tweet.encode('utf-8'))

    def on_error(self, status_code):
        print('ERROR', status_code)
        if status_code == 420:
            return False
        return True
