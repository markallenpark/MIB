#!/bin/bash

cd /app

if ! test -d venv; then
    python -m venv venv
fi

. venv/bin/activate

pip install -r requirements.txt

python -u app.py
