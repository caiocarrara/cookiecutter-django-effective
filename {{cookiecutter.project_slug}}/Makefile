build_base_image:
	docker build --tag={{cookiecutter.company_slug}}/{{cookiecutter.project_slug}} --file=Dockerfile .

build: build_base_image
	docker-compose build

check_rebuild:
	./scripts/rebuild.sh

clean:
	@find . -name *.pyc -delete
	@find . -name __pycache__ -delete

createsuperuser: check_rebuild
	./scripts/run.sh python {{cookiecutter.project_slug}}/manage.py createsuperuser

format: ${VIRTUAL_ENV}/scripts/black ${VIRTUAL_ENV}/scripts/isort
	isort -rc --atomic tigger_api
	black tigger_api

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

lint: ${VIRTUAL_ENV}/scripts/black
	black --check tigger_api

lock: pip-tools
	CUSTOM_COMPILE_COMMAND="make lock" pip-compile --generate-hashes --output-file requirements.txt requirements/base.in requirements/deploy.in

lock-dev: pip-tools
	CUSTOM_COMPILE_COMMAND="make lock-dev" pip-compile --generate-hashes --output-file requirements-dev.txt requirements/dev.in

migrate: check_rebuil	d
	./scripts/run.sh python {{cookiecutter.project_slug}}/manage.py migrate --no-input

makemigrations: check_rebuild
	./scripts/run.sh python {{cookiecutter.project_slug}}/manage.py makemigrations

pip-tools: ${VIRTUAL_ENV}/scripts/pip-sync

run: check_rebuild
	docker-compose up

setup: lock build

start-%:
	@docker-compose up -d $(@:start-%=%)

stop:
	@docker-compose stop

test: clean check_rebuild
	./scripts/run.sh pytest {{cookiecutter.project_slug}}


${VIRTUAL_ENV}/scripts/black:
	pip install black

${VIRTUAL_ENV}/scripts/isort:
	pip install isort

${VIRTUAL_ENV}/scripts/pip-sync:
	pip install pip-tools
