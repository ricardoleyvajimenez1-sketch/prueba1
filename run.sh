#!/bin/bash

# Instalar dependencias si no están instaladas
pip install -r requirements.txt

# Ejecutar el script de scraping
python3 scrape_liga.py