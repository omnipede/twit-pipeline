"""
Publisher that sends message to message queue.
"""
from abc import ABCMeta, abstractmethod


class Publisher(metaclass=ABCMeta):
    """
    Message queue 로 데이터를 publish 할 때 사용하는 인터페이스
    """
    @abstractmethod
    def publish(self, data: bytes):
        """
        :param data: Data to publish
        """
