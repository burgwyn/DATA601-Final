#!/bin/bash

# create the data directory
mkdir data
mkdir data/sample
mkdir data/incoming
mkdir data/cleaned
mkdir data/config
mkdir data/final

# create conda environment and activate it
conda env create -f environment.yaml --name burgwyn_data601_final
conda activate burgwyn_data601_final

# fetch data
python ./scripts/main.py
