"""Класс для размещения изображений на листе A4 по строкам."""

from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


class DrawImages:
    """Класс для размещения изображений на листе A4 по строкам."""

    def __init__(
        self: 'DrawImages',
        x_init_offset: int,
        y_init_offset: int,
        scale_factor: float,
        space_between: int,
    ) -> None:
        """Create object for inserting images."""
        self.x_init_offset = x_init_offset
        self.y_init_offset = y_init_offset
        self.scale_factor = scale_factor
        self.space_between = space_between

        self.x = self.x_init_offset
        self.y = self.y_init_offset
        self.h_max = 0

    def draw_image(self: 'DrawImages', cvs: canvas, image: Image) -> None:
        """Метод для вставки изображений на canvas."""
        width = image.width * self.scale_factor
        height = image.height * self.scale_factor

        self.h_max = max(self.h_max, height)

        self.move_to_new_row(cvs, width)

        cvs.drawImage(
            ImageReader(image),
            x=self.x,
            y=self.y,
            width=width,
            height=height,
        )

        self.x += width + self.space_between

    def move_to_new_row(
        self: 'DrawImages',
        cvs: canvas,
        image_width: float,
    ) -> None:
        """
        Проверяем, помещается ли новое изображение в строке.

        Если не помещается, переносим на новую строку.
        """
        # noinspection PyProtectedMember
        cvs_width, cvs_height = cvs._pagesize

        if self.x + image_width + self.x_init_offset > cvs_width:
            self.x = self.x_init_offset
            self.y = self.y + self.h_max + self.space_between
