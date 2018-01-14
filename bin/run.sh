#!/bin/bash

find . -iname "*.py" | xargs pylint
pytest --cov utils
python main.py
