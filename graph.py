from typing import Union, List
from pydantic import BaseModel
from matplotlib.figure import Figure

Num = Union[int, float]

class SequenceData(BaseModel):
    data: List[tuple[Num, Num]]