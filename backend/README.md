# Backend

Backend for boilerplate project. Built with python, fastAPI, Postgres and TortoiseORM

> Note: This is setting up and running this backend project as a standalone service

## Setup

```sh
rename env.sample to .env and fill out the necessary variables

# Project setup
python -m venv venv #setup environment
source venv/bin/activate #activate environment

# install dependencies
pip install -r requirements.txt
```

## Database setup + migration

```sh
# Initialise config file and generate root migrate location
aerich init -t src.database.database.TORTOISE_ORM #creates ./migrations folder

# generate schema for "models" and migration location in migrations/models
aerich init-db

# generate migrate changes file
aerich migrate

# upgrade database to use latest migrate changes
aerich upgrade
```

## Run app

```sh
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Useful resources

[TortoiseORM docs](https://tortoise.github.io/)
