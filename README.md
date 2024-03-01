# Simple movie library with Django and Django Rest Framewrok
## To start project locally (via 🐋Docker and docker-compose):
Into the project directory should create .env file and create values for database: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT` and `POSTGRES_DB`

Also you should register on `https://www.omdbapi.com/` and create value `OMDb_API_KEY` into `.env` file.

```docker compose up --build -d``` (for the first run) ```docker compose up -d``` (for subsequent runs)

Go to `http://localhost:8000/docs` to view Swagger API documentation

## Populate DB
To populate database with some movie from OMDb Enter: 
`docker exec -it [name of django container]-1 sh` to go to the docker container and  `python manage.py populate_db` to populate db
