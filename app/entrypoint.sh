#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Comment below lines if you don't want to flush the db every time the container is started
# python3 manage.py flush --no-input
# python3 manage.py migrate


# Check return
exec "$@"