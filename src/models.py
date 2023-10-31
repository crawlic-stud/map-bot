from pathlib import Path
from pydantic import BaseModel, Field


class LocationInDb(BaseModel):
    latitude: float
    longitude: float
    name: str
    user_id: int
    address: str | None
    tags: list[str] = Field(default_factory=list)
    favorite: bool = False
    icon: str = "url(../static/icons/marker.svg)"


class IconInfo(BaseModel):
    path: str
    name: str
    content: str


class PatchIcon(BaseModel):
    icon_data: str
