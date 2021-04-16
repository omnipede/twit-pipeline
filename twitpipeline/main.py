"""
Main script
"""
from twitpipeline.mq.googlepubsub import create_google_pubsub_publisher
from twitpipeline.twit.listener import TweetStreamListener
from twitpipeline.mq.publisher import Publisher

__version__ = "1.0.0"

from twitpipeline.twit.stream import create_twit_stream


def main():
    """
    Main script
    """

    # Google pubsub publisher 생성.
    publisher: Publisher = create_google_pubsub_publisher()

    # Twitter stream listener 정의.
    twit_stream_listener = TweetStreamListener(publisher)

    # Twit stream 생성
    twit_stream = create_twit_stream(twit_stream_listener)

    # 스트리밍 시작
    twit_stream.filter(track=['game'])


if __name__ == "__main__":
    main()
