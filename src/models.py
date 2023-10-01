from pydantic import BaseModel, Field


class LocationInDb(BaseModel):
    latitude: float
    longitude: float
    name: str
    user_id: int
    tags: list[str] = Field(default_factory=list)
    favorite: bool = False
