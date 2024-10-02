from pydantic import BaseModel, Field
from pydantic.networks import HttpUrl


class FileUrlInput(BaseModel):
    file_url: HttpUrl = Field(..., title="File URL", max_length=2000)
