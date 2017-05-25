#!/usr/bin/env bash

pip install virtualenv


pyvenv venv
source venv/bin/activate
python src/summarize_api/setup.py install
export PYTHONPATH=.:$PYTHONPATH
python src/summarize_api/application_dev.py