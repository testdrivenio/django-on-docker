# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Want to learn how to build this?

Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## Want to use this project?

1. Fork/Clone

1. Build the images and run the containers:

    - development (django default server):

    ```sh
    $ docker-compose up -d --build
    ```
    Test it out at [http://localhost:8000](http://localhost:8000)

    App's folder is mounted into container and your changes apply automatically.

    - production (gunicorn + nginx):

    ```sh
    $ docker-compose -f docker-compose.prod.yml up --build -d
    ```
    No mounted folders -- to apply changes container should be rebuilt

    Test it out at [http://localhost:1337](http://localhost:1337)
