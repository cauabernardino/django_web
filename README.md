# Dockerized Django Web App

A web application made with Django working with a PostgreSQL database, both dockerized from Alpine images, in order to obtain light and efficient containers.

## Remarks ✔

- You should have Docker and Docker-Compose installed

- Docker Images used are:
    - python:3.8.3-alpine
    - postgres:12.0-alpine

- It is recommended to use the Django Admin panel to manage the database

## How to run ⚙

- First of all, clone this repo
    ```bash
    git clone https://github.com/cauabernardino/django_web.git
    ```

- Take off the `-sample` from `.env.dev-sample` and `.env.dev.db-sample`

- In `.env.dev` change the following environment variables.
    ```bash
    SECRET_KEY=django_secret_key
    SQL_DATABASE=name_db
    SQL_USER=user
    SQL_PASSWORD=password
    ```
    - The name, user and password for the Database can be whichever you want

    - A new `SECRET_KEY` can be generated running the function below (this can be done after building the containers)
    ```bash
    python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

- In `.env.dev.db` change the values to match the equivalent values in the `.env.dev` file


- Build the images, create and run the containers with

    ```bash
    docker-compose up -d --build
    ```

- To check if the Django server is running from the container

    ```bash
    # Find the container ID for web app
    docker ps -a

    # Check (and follow) the logs from the Django server with
    docker logs -f <CONTAINER_ID>  
    ```

- To start/stop the container without deleting it

    ```bash
    docker-compose stop

    docker-compose start
    ```

  - If you want to persist the database not flushing it every time the container runs, go to `entrypoint.sh` file in the `app` folder and comment the indicated lines

- To create a superuser (admin)

    ```bash
    docker-compose exec web python3 manage.py createsuperuser
    ```
    - To execute other commands it can use the same syntax

- To access the server and the admin area
    ```bash
    # Index page
    localhost:8000

    # Admin area
    localhost:8000/controlroom
    ```

- To bring down and delete the containers, images and volume
    ```bash
    docker-compose down -v
    ```