from pydantic import BaseModel

class Player(BaseModel):
  name: str
  age: int
  time: str