from pydantic import BaseModel


class ClipInterface(BaseModel):
    """Interface that describes a clip"""

    id: int
    transcription: str
    url: str
    duration: int

    def to_dict(self):
        return {
            "id": self.id,
            "transcription": self.transcription,
            "url": self.url,
            "duration": self.duration,
        }
