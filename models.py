from pydantic import BaseModel
from typing import Dict

class Symbol(BaseModel):
    symbol_id: str
    symbol_type: str
    image_path: str
    properties: Dict