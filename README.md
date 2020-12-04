# DATA601-Final

## Overview


## Goals

- Identify the features that predict the likelihood of a parking violation
- Determine if geographic factors have any impact on parking violations
- Determine if day and/or time have any impact on parking violations
- Create a model that scores 85% or better

## Motivation & Background

After almost 10 years of not owning a car, in 2015 I purchased a new car for my family.  Within a month I received a parking ticket.  The pace continued, and I received on average 2 tickets a year.  I even received tickets at parking meters that I had paid for!

Parking tickets are an expensive nuisance, an unexpected expense often totaling $100.  What if one could understand the likelihood of a parking ticket at a given place and time?

## Data


## Table of Contents

The final solution should look like this

```shell
├── LICENSE
├── README.md
├── coverage.xml
├── data
│   └── Parking_Violations_Issued_in_August_2018.csv
├── env.sh
├── environment.yaml
├── notebooks
│   ├── Cleaning,\ Preparation\ and\ Modeling.ipynb
│   ├── EDA.ipynb
│   ├── Getting\ Data.ipynb
│   ├── Models.ipynb
│   └── Report.ipynb
├── scripts
│   ├── __init__.py
│   ├── api.py
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
./env.sh
```

The shell script will build a `data` directory and create a conda environment `burgwyn_data601_final`

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
