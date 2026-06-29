#!/bin/bash

echo "Installing dependencies..."

pip install -r requirements.txt

echo "Downloading dataset..."

python scripts/download_mot17.py

echo "Done!"