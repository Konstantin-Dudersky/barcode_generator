#!/bin/bash

# shellcheck disable=SC1090
source ~/.poetry/env
x-terminal-emulator --noclose -e "poetry run python app/main.py"
