from dataclasses import dataclass


@dataclass
class Config:
    barcode_type: str
    options: dict
