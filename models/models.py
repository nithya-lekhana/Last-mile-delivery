from dataclasses import dataclass


@dataclass
class Delivery:
    id: str
    pickup: str
    drop: str
    weight: int
    deadline: int
    profit: int