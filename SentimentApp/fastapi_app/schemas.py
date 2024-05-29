from pydantic import BaseModel, Field

class SentimentRequest(BaseModel):
    text: str = Field(..., example="I love you!")
