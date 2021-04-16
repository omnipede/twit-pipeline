"""
Google pubsub publisher 구현체를 생성하여 반환하는 메소드
"""
from google.cloud import pubsub_v1
from google.oauth2 import service_account

from twitpipeline.config import google_credential_file, google_pubsub_topic
from twitpipeline.mq.publisher import Publisher


class GooglePubsub(Publisher):
    """
    Google pub/sub 을 이용한 MQ publisher 구현체
    """
    _google_credential_scope = 'https://www.googleapis.com/auth/cloud-platform'

    def __init__(self, client: pubsub_v1.PublisherClient):
        self._client = client

    def publish(self, data: bytes) -> None:
        # Google pubsub client 이용하여 데이터 publish
        pubusb_client: pubsub_v1.PublisherClient = self._client
        pubusb_client.publish(google_pubsub_topic, data=data)


def create_google_pubsub_publisher() -> GooglePubsub:
    """
    Google credential JSON 파일을 이용하여 google pubsub 으로 메시지를 전송하는
    Publisher 를 생성하는 메소드
    """
    google_credential_scope = 'https://www.googleapis.com/auth/cloud-platform'
    # Google credential 이용해서 google pubsub client 생성
    credentials = service_account.Credentials.from_service_account_file(
        google_credential_file,
        scopes=[google_credential_scope])
    # Create pubsub client
    pubsub_client = pubsub_v1.PublisherClient(credentials=credentials)
    # Create publisher impl
    return GooglePubsub(pubsub_client)
