# react-blog

## About

React-Blog project is about organization and running Flask app as a backend
and React app as frontend in a docker-compose containers.

## Pre-Build

-   install docker [https://github.com/docker/docker](https://github.com/docker/docker)
-   install docker-compose [https://docs.docker.com/compose/install](https://docs.docker.com/compose/install)

## Usage

### Pull images

-   ```docker-compose pull```

### Build an image

-   ```docker-compose build```

### Start a cluster

To start applications with development environment:

-   ```docker-compose up -d```

### Migrations

To upgrade your database with migration:

- ```docker-compose run api python manage.py db upgrade```

### Stop and destroy a cluster

- ```docker-compose stop && docker-compose rm -f```

### Logs and troubleshooting

To check standard logs:

- ```docker-compose logs```
