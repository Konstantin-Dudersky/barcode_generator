"""Класс для хранения настроек."""

from dataclasses import dataclass


@dataclass
class Config:
    """Класс для хранения настроек."""

    barcode_type: str
    options: dict

    pdf_scale_factor: float
    pdf_space_between: int
