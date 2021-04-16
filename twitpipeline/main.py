"""
Main script
"""

from twitpipeline.datasource.listener import Listener, TweetListener
from twitpipeline.mq.publisher import Publisher, GooglePubsub

__version__ = "1.0.0"


def main():
    """
    Main script
    """

    # Google PUBSUB 으로 데이터를 전송하는 객체
    publisher: Publisher = GooglePubsub()

    # Twit 데이터를 불러오는 객체. 데이터를 불러온 뒤 바로 publiser 를 이용해 PUBSUB 으로 데이터를 전송함.
    listener: Listener = TweetListener(publisher)

    # 'game' 라는 단어가 포함된 트윗을 블러옴
    listener.listen(track=['game'])


if __name__ == "__main__":
    main()
