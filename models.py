from datetime import datetime

from pydantic import BaseModel, Field


class Announcement(BaseModel):
    title: str = Field(description="An announcement title")
    description: str = Field(description="An announcement description")
    date: datetime = Field(description="A creation date")

    def __str__(self):
        return f"title = {self.title}, description = {self.description}, date = {self.date.strftime('%y-%m-%d')}"

    @classmethod
    def str_to_instance(cls, string: str):
        title = string[len(("title = ")):string.find(", description = ")]
        description = string[string.find("description = ") + len("description = "):string.find(", date = ")]
        date = string[string.find("date = ") + len("date = "):]
        return Announcement(title=title, description=description,
                            date=datetime.strptime(date, "%y-%m-%d"))
