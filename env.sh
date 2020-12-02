#!/bin/bash

# create the data directory
mkdir data

conda env create -f environment.yaml
conda activate burgwyn_data601_final
