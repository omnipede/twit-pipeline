"""
Publisher that sends message to message queue.
"""
from abc import ABCMeta, abstractmethod

from google.cloud import pubsub_v1
from google.oauth2 import service_account

from twitpipeline.config import google_credential_file, google_pubsub_topic


class Publisher(metaclass=ABCMeta):
    """
    Message queue 로 데이터를 publish 할 때 사용하는 인터페이스
    """
    @abstractmethod
    def publish(self, data: bytes):
        """
        :param data Data to publish
        """


class GooglePubsub(Publisher):
    """
    Google pub/sub 을 이용한 MQ publisher 구현체
    """
    _google_credential_scope = 'https://www.googleapis.com/auth/cloud-platform'

    def __init__(self):
        # Google credential 이용해서 google pubsub client 생성
        credentials = service_account.Credentials.from_service_account_file(
            google_credential_file,
            scopes=[self._google_credential_scope])
        # Create pubsub client
        self._client = pubsub_v1.PublisherClient(credentials=credentials)

    def publish(self, data: bytes) -> None:
        # Google pubsub client 이용하여 데이터 publish
        pubusb_client: pubsub_v1.PublisherClient = self._client
        pubusb_client.publish(google_pubsub_topic, data=data)
