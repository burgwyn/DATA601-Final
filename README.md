# DATA601-Final

## Getting Started

### Manage Environment

Execute the shell script `env.sh` to build the project environment and install the require dependencies.

```shell script
# make script executable
chmod +x ./env.sh
./env.sh
```

The shell script will build a `data` directory and create a conda environment `burgwyn_data601_final`

### Install pip

Install `pip`, the package manager, via [the instructions](https://pip.pypa.io/en/stable/installing/)

```shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
rm get-pip.py
```

### Install requirements

Install dependencies

```shell
pip install -r requirements.txt
```