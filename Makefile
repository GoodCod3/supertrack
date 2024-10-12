PYTHON=python
FILENAME=manage.py
DJANGO_COMMAND=runserver
DJANGO_TEST_COMMAND=test
DJANGO_MIGRATIONS_COMMAND=makemigrations
DJANGO_MIGRATE_COMMAND=migrate
DJANGO_LOAD_DATA_COMMAND=load_initial_data
ARGS ?=
TEST_ARGS = $(if $(ARGS),$(ARGS),supertrack)

run:
	${PYTHON} ${FILENAME} ${DJANGO_COMMAND}

load-data:
	docker compose exec web python manage.py load_initial_data

create-initial-user:
	docker compose exec web python manage.py create_initial_user

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

lint:
	poetry run flake8

isort:
	poetry run  isort . --check-only

isort-fix:
	poetry run  isort .

pre-commit:
	pre-commit run --all-files

freeze-dependencies:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

test:
	docker compose exec web coverage run --source='.' manage.py test $(TEST_ARGS)

test-ci:
	SECRET_KEY='1234567890' ${PYTHON} ${FILENAME} ${DJANGO_TEST_COMMAND} $(TEST_ARGS)

coverage:
	SECRET_KEY=123 coverage run --source='.' manage.py test supertrack
	coverage html --omit="*/migrations*,*/__tests__/*,*/__init__*,*/fixtures/*,*/migrations/*",*/models.py,*/admin.py,*/urls.py,*/wsgi.py,*/manage.py,*/tests/*

docker-db-ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' supertrack-db-1

dump-data:
	docker compose exec web python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json

release-major:
	@poetry version major && \
	echo "Publicando versión $$(poetry version --no-interaction | cut -d ' ' -f 2)" && \
	git ci -am "New release v$$(poetry version --no-interaction | cut -d ' ' -f 2)" && \
	git push origin master && \
	git tag v$$(poetry version --no-interaction | cut -d ' ' -f 2) && \
	git push origin --tags

release-minor:
	@poetry version minor && \
	echo "Publicando versión $$(poetry version --no-interaction | cut -d ' ' -f 2)" && \
	git ci -am "New release v$$(poetry version --no-interaction | cut -d ' ' -f 2)" && \
	git push origin master && \
	git tag v$$(poetry version --no-interaction | cut -d ' ' -f 2) && \
	git push origin --tags


release-patch:
	@poetry version patch && \
	echo "Publicando versión $$(poetry version --no-interaction | cut -d ' ' -f 2)" && \
	git ci -am "New release v$$(poetry version --no-interaction | cut -d ' ' -f 2)" && \
	git push origin master && \
	git tag v$$(poetry version --no-interaction | cut -d ' ' -f 2) && \
	git push origin --tags
