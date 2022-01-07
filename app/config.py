from dataclasses import dataclass


@dataclass
class Config:
    barcode_type: str
    options: dict

    pdf_scale_factor: float
    pdf_space_between: int
