# FastAPI + Nuxt3 boilerplate

A boilerplate for a full-stack web application built with Nuxt3 on the frontend, Python/FastAPI, PostgreSQL and TortoiseORM (with aerich for migration) on the backend.

## Run app

> Note: You should modify the environments in docker-compose.yml to fit your requirements

```sh
docker-compose up -d --build

# NOTE: backend running on port 8000 by default
# NOTE: frontend running on port 3000 by default
```

## Setup database

```sh
# Initialise config file and generate root migrate location
docker compose exec backend aerich init -t src.database.database.TORTOISE_ORM #creates ./migrations folder

# generate schema for "models" and migration location in migrations/models
docker compose exec backend aerich init-db

# generate migrate changes file
docker compose exec backend aerich migrate

# upgrade database to use latest migrate changes
docker compose exec backend aerich upgrade
```

Lots of help from:

- [Developing a Single Page App with FastAPI and Vue.js by Michael Herman](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/#models-and-migrations)

- [TortoiseORM docs](https://tortoise.github.io/)
