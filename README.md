# DATA601-Final

## Overview

Explore parking violation data from Washington, DC and build a classifier

<img src="https://github.com/burgwyn/DATA601-Final/blob/main/images/map-plot.png" alt="Plot of Washington, DC" />

## Goals

- Identify the features that predict the likelihood of a parking violation
- Determine if geographic factors have any impact on parking violations
- Determine if day and/or time have any impact on parking violations
- Create a model that scores 85% or better
- Incorporate unit tests and linting through GitHub Actions in an effort to mimic a professional setting

## Motivation & Background

After almost 10 years of not owning a car, in 2015 I purchased a new car for my family.  Within a month I received a parking ticket.  The pace continued, and I received on average 2 tickets a year.  I even received tickets at parking meters that I had paid for!

Parking tickets are an expensive nuisance, an unexpected expense often totaling $100.  What if one could understand the likelihood of a parking ticket at a given place and time?

## Data

This effort makes use of publicly available [parking violation data](https://opendata.dc.gov/datasets/parking-violations-issued-in-august-2018) published by the city of DC.

| Column Name | Type |
|---|---|
| DISPOSITION_CODE | Number |
| DISPOSITION_DATE | Date or Time |
| DISPOSITION_DESC | Text |
| DISPOSITION_TYPE | Text |
| FINE_AMOUNT | Number |
| GIS_LAST_MOD_DTTM | Date or Time |
| ISSUE_DATE | Date or Time |
| ISSUE_TIME | Text |
| ISSUING_AGENCY_CODE | Number |
| ISSUING_AGENCY_NAME | Text |
| ISSUING_AGENCY_SHORT | Text |
| LATITUDE | Number |
| LOCATION | Text |
| LONGITUDE | Number |
| MAR_ID | Number |
| MULTI_OWNER_NUMBER | Text |
| OBJECTID | Unique ID |
| PENALTY_1 | Number | 
| PENALTY_2 | Number |
| PENALTY_3 | Number |
| PENALTY_4 | Number |
| PENALTY_5 | Number |
| PLATE_STATE | Text |
| TOTAL_PAID | Number |
| VEHICLE_TYPE | Text |
| VIOLATION_CODE | Text |
| VIOLATION_PROC_DESC | Text |
| XCOORD | Number |
| YCOORD | Number |

## Table of Contents

The final solution should look like this

```shell
├── LICENSE
├── README.md
├── coverage.xml
│   ├── cleaned
│   │   ├── April_2018.csv
│   │   ├── August_2018.csv
│   │   ├── December_2018.csv
│   │   ├── February_2018.csv
│   │   ├── January_2018.csv
│   │   ├── July_2018.csv
│   │   ├── June_2018.csv
│   │   ├── March_2018.csv
│   │   ├── May_2018.csv
│   │   ├── November_2018.csv
│   │   ├── October_2018.csv
│   │   └── September_2018.csv
│   ├── config
│   │   └── parking_data.json
│   ├── final
│   │   └── all_cleaned.csv
│   │   └── final_model.pkl
│   ├── incoming
│   │   ├── April_2018.csv
│   │   ├── August_2018.csv
│   │   ├── December_2018.csv
│   │   ├── February_2018.csv
│   │   ├── January_2018.csv
│   │   ├── July_2018.csv
│   │   ├── June_2018.csv
│   │   ├── March_2018.csv
│   │   ├── May_2018.csv
│   │   ├── November_2018.csv
│   │   ├── October_2018.csv
│   │   └── September_2018.csv
│   └── sample
│       └── Parking_Violations_Issued_in_August_2018.csv
├── env.sh
├── environment.yaml
├── notebooks
│   ├── Cleaning\ and\ Preparation.ipynb
│   ├── EDA.ipynb
│   ├── Getting\ Data.ipynb
│   ├── Models.ipynb
│   └── Report.ipynb
├── scripts
│   ├── __init__.py
│   ├── api.py
│   ├── cleaning.py
│   ├── main.py
│   ├── model.py
│   └── utils.py
└── tests
    ├── test_api.py
    └── test_utils.py
```

## Getting Started

### Manage Environment

Execute the shell script `env.sh` to build the project environment and install the required dependencies.

```shell script
# make script executable
chmod +x ./env.sh
source ./env.sh
```

The shell script will build a `data` directory, create a conda environment `burgwyn_data601_final` and fetch and clean the data.

## Project Info

Contributors: [Nat Burgwyn](https://github.com/burgwyn)

### Packages and Software

Languages: Python

Tools: PyCharm, Jupyter Notebook

Libraries:

| Library | Version |
|---|---|
| jupyterlab | 2.1.5 |
| matplotlib | 3.3.2 |
| numpy | 1.19.2 |
| pandas | 1.1.3 |
| requests | 2.24.0 |
| seaborn | 0.11.0 |
| coverage | 5.3 |
| flake8 | 3.8.4 |
| python-dateutil | 2.8.1 |
| requests | 2.24.0 |
| responses | 0.12.1 |
| scikit-learn | 0.23.2 |
