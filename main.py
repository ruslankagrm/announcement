from typing import Optional, List

import fastapi
from fastapi import FastAPI

from announcement_manager import AnnouncementSender, AnnouncementReceiver
from models import Announcement

description = """
## AnnouncementApp API helps you to send announcements to AWS SQS. 🚀

### Utility
You can **create new announcements**.

You can **read all existing announcements from message queue**.

"""

announcement_api = FastAPI(
    title="AnnouncementApp",
    description=description,
    version="0.0.1",
)


@announcement_api.post("/api/announcement",
                       description="### This endpoint is to create a new Announcement",
                       status_code=201)
async def create_announcement(announcement: Announcement):
    sender = AnnouncementSender()
    sender.send_announcement(announcement)
    return fastapi.Response(status_code=201)


@announcement_api.get("/api//announcements", response_model=List[Optional[Announcement]],
                      description="### This endpoint will return a list of all existing Announcements, or an empty list if no Announcements are available",
                      status_code=200)
async def get_announcements():
    receiver = AnnouncementReceiver()
    announcements = receiver.receive_announcements()
    return announcements
