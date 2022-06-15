# Cookiecutter Django Effective

This cookiecutter generates modern and effective Django project structure.

## Project structure output

```
my_test_project
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.dev
├── Makefile
├── my_test_project
│   ├── config
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── frontend
│   │   ├── static
│   │   └── templates
│   ├── manage.py
│   └── tests
├── pyproject.toml
├── pytest.ini
├── requirements
│   ├── base.in
│   ├── deploy.in
│   └── dev.in
└── setup.cfg
```

## Usage

- Install cookiecutter

```sh
$ pip install cookiecutter
```

- Navigate to where you want the new project directory be created and run cookiecutter against this repository

```sh
$ cookiecutter https://github.com/caiocarrara/cookiecutter-django-effective
```

The new project directory should be created now.

On project directory just created run:

```sh
$ make lock lock-dev
```

Now it's possible to install the dependencies with install or
install-dev actions:

```sh
$ make install install-dev
```
