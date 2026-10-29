from pydantic import BaseModel, Field

class Task_EV(BaseModel):
    id: int = Field()
    task: str = Field(min_length=1)
    completed: bool = Field()