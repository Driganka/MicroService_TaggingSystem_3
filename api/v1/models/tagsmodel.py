from pydantic import BaseModel
from typing import List

class Tags(BaseModel):
    id: str
    uname: str
    utags: List[str]
