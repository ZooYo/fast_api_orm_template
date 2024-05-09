[markdown怎麼寫](https://gist.github.com/billy3321/1001749662c370887c63bb30f26c9e6e)

# 專案結構
Web: FastAPI

DataBase: MySQL

ORM: sqlalchemy

Migration: alembic

Package Management: Poetry



# migration
```bash
alembic revision --autogenerate -m "Initial migration"

alembic upgrade head
```

# Docker
```bash
有更新Poetry
docker-compose -f docker-compose.dev.yml up --build

docker-compose -f docker-compose.dev.yml up
```

# PROD
settings.py