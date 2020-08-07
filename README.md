# Django and PostgreSQL on Docker :rocket:
Use this project to start a Djando Project with PosgreSQL.

Clone with:
```
git clone https://github.com/iraidamercedes/django_base_project.git
```
Create a .env.dev file in the root folder and set the values for the following parameters:

```
DEBUG=1
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=db
SQL_PORT=5432
```

Buld the image with:
```
docker-compose build
```

Run the cointainer:
```
docker-compose up -d
```