from pydantic import BaseModel, Field


class PatchMeRequest(BaseModel):
    display_name: str | None = Field(default=None, max_length=100)
    public_profile: bool | None = None
