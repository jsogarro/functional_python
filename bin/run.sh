#!/bin/bash

find . -iname "*.py" | xargs pylint 
pytest
python main.py
