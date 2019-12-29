# {{ cookiecutter.project_slug }}

## Dealing with dependencies

- It is possible to lock the dependencies to run the project with the following command

```sh
$ make lock
```

- It is also possigle to lock development dependencies with:

```sh
$ make lock-dev
```

- The lock process creates/updates the files `requirements.txt` and `requirements-dev.txt`. With these files in place it's possible to install dependencies running:

```sh
$ make install install-dev
```

## Running locally with Docker

- Start building the Docker images (make sure there's `requirements.txt` file created before building the images)

```sh
$ make build
```

- There's a shortcut to automatically lock and build Docker image

```sh
$ make setup
```

- If it's the first run, it could be necessary run migrations

```sh
$ make run migrate
```

- Than the run command can be executed
```sh
$ make run
```

Enjoy! `;-)`