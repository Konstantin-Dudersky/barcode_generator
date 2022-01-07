import logging
import os
import shutil
from logging.handlers import RotatingFileHandler

import treepoem
import yaml
from PIL import Image
from colorama import Fore, init
from reportlab.pdfgen import canvas
from tqdm import tqdm

import config
from draw_images import DrawImages

# logger global setup

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(name)s:%(lineno)d - %(funcName)s | %(message)s',
    level=logging.INFO,
    handlers=[
        RotatingFileHandler(
            filename='logs/log.log',
            mode='a',
            maxBytes=5 * 1024 * 1024,
            backupCount=2,
            encoding=None,
            delay=False,
        )
    ]
)
# logger local setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# colorama
init()

# очистка папки
try:
    shutil.rmtree('output')
    os.makedirs('output', exist_ok=True)
except FileNotFoundError:
    pass
    os.makedirs('output', exist_ok=True)

# читаем файл с настройками
try:
    with open('config.yaml') as stream:
        config_file = config.Config(**yaml.safe_load(stream))
        logger.info('config file read successfully')
        print(
            f"Файл конфигурации прочитан,"
            f"генерируем код {config_file.barcode_type}"
            )
except FileNotFoundError:
    logging.exception('error reading config.yaml file')
    print(Fore.RED + "Ошибка чтения файла конфигурации config.yaml")
    exit(1)

# читаем файл с кодами
codes = []

try:
    with open('input.csv') as stream:
        codes = stream.readlines()
        logger.info('input file read successfully')
        print(f"Файл с кодами прочитан, в файле {len(codes)} кодов")
except FileNotFoundError:
    logging.exception('error reading input.csv file')
    print(Fore.RED + "Ошибка чтения файла с кодами input.csv")
    exit(1)

# генерируем штрих-коды
for code in tqdm(codes):
    _code = code.strip()

    options = {}

    image = treepoem.generate_barcode(
        barcode_type=config_file.barcode_type,
        options=config_file.options,
        data=_code,

    )
    image.convert("1").save(f"output/{_code}.png")

# создаем pdf
cvs = canvas.Canvas("output/output.pdf")
draw_images = DrawImages(
    x_init_offset=20,
    y_init_offset=20,
    scale_factor=config_file.pdf_scale_factor,
    space_between=config_file.pdf_space_between,
)
for f in os.listdir('output'):
    draw_images.draw_image(
        cvs=cvs,
        image=Image.open(f'output/{f}'),
    )
cvs.showPage()
cvs.save()

print(Fore.GREEN + "Генерация штрих-кодов завершена")
