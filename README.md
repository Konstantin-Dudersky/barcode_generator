Штрих-коды генерируются с помощью библиотеки [BWIPP](https://github.com/bwipp/postscriptbarcode). Документация к настройкам кодов - [https://github.com/bwipp/postscriptbarcode/wiki/Symbologies-Reference](https://github.com/bwipp/postscriptbarcode/wiki/Symbologies-Reference)

## Зависимости

Перед установкой в системе должен быть установлен Python версии 3.10

## Установка

Ввести командной строке

    wget https://github.com/Konstantin-Dudersky/barcode_generator/releases/latest/download/setup.sh && chmod +x setup.sh && ./setup.sh && rm setup.sh

При работе скрипта в системе установятся [ghostscript](https://www.ghostscript.com/) и [poetry](https://python-poetry.org/).

## Использование

Настройка штрих-кодов выполняется в файле config.yaml. 

- barcode_type - тип штрих-код (например gs1datamatrix, qrcode)
- options - опциональные параметры. Зависят от типа штрих-кода. Если параметры не нужны, оставить поле options пустым

Коды для генерации записываются в файл input.csv - одна строка на код.

Коды генерируются при запуске файла start.sh.

### GS1 datamatrix

Проверяется корректность исходного кода. Символы FNC1 и GS1 добавляются автоматически. Идентификаторы полей должны обозначаться круглыми скобками. Например:

    (01)04810729011067(21)2Pt8IuIu(93)EwYR