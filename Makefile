install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

lint:
	poetry run flake8 tests scripts

test-coverage:
	poetry run pytest --cov
