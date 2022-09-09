import logging

from models import Announcement
from sqs_client import SQSClient

logger = logging.getLogger(__name__)


class AnnouncementManager:
    def __init__(self):
        self.sqs_client = SQSClient()


class AnnouncementSender(AnnouncementManager):
    def send_announcement(self, data: Announcement):
        try:
            self.sqs_client.send_message(data.__str__())
        except Exception as ex:
            logger.exception(ex)


class AnnouncementReceiver(AnnouncementManager):
    def receive_announcements(self):
        try:
            response = self.sqs_client.receive_message()
            return self.get_messages(response_data=response)
        except Exception as ex:
            logger.exception(ex)

    @classmethod
    def get_messages(cls, response_data: dict):
        if response_data.get("Messages"):
            return [Announcement.str_to_instance(message["Body"]) for message in response_data["Messages"]]
        return []
