from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


class DrawImages:
    def __init__(
        self,
        x_init_offset: int,
        y_init_offset: int,
        scale_factor: float,
        space_between: int,
    ):
        self.x_init_offset = x_init_offset
        self.y_init_offset = y_init_offset
        self.scale_factor = scale_factor
        self.space_between = space_between

        self.x = self.x_init_offset
        self.y = self.y_init_offset
        self.h_max = 0

    def draw_image(self, cvs: canvas, image: Image):
        w = image.width * self.scale_factor
        h = image.height * self.scale_factor

        self.h_max = max(self.h_max, h)

        self.check_if_new_row(cvs, w)

        cvs.drawImage(
            ImageReader(image),
            x=self.x,
            y=self.y,
            width=w,
            height=h,
        )

        self.x += w + self.space_between

    def check_if_new_row(self, cvs: canvas, image_width):
        cvs_width, cvs_height = cvs._pagesize

        if self.x + image_width + self.x_init_offset > cvs_width:
            self.x = self.x_init_offset
            self.y = self.y + self.h_max + self.space_between
