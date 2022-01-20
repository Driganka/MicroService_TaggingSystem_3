from pydantic import BaseModel
from typing import List

class Products(BaseModel):
    pid: str
    pname: str
    ptags: List[str]
