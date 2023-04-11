BROWSER=firefox
DCYML=docker/compose.yaml
GRID_HOST=localhost
GRID_PORT=4444
PROJECT=selene_multiple_browsers
PYTESTOPTS?=
PYTHON_VERSION?=3.10.0
SCALE_CHROME=0
SCALE_FIREFOX=2


.PHONY: pyenv
pyenv:
	pyenv install ${PYTHON_VERSION} --skip-existing
	pyenv uninstall ${PROJECT} || true
	pyenv virtualenv ${PYTHON_VERSION} ${PROJECT}
	pyenv local ${PROJECT}
	pip install black pytest pdbpp poetry
	sed -i '/export VIRTUAL_ENV=/d' .envrc || true
	echo "export VIRTUAL_ENV=\$$$\(pyenv prefix)" >> .envrc
	direnv allow || true

.PHONY: all
all:
	poetry build

.PHONY: install
install:
	poetry install

.PHONY: run
run:
	poetry run ...

.PHONY: test
test:
	poetry run pytest \
		--driver=Remote \
		--selenium-host=${GRID_HOST} \
		--selenium-port=${GRID_PORT} \
		--capability browserName ${BROWSER} \
		--verbose \
		--tb=short \
		${PYTESTOPTS}

.PHONY: test-env-up
test-env-up:
	docker-compose \
		-f ${DCYML} \
		-p ${PROJECT} \
		up \
			-d \
			--scale firefox=${SCALE_FIREFOX} \
			--scale chrome=${SCALE_CHROME} \
			selenium-hub \
			chrome \
			firefox

.PHONY: test-env-down
test-env-down:
	docker-compose \
		-f ${DCYML} \
		-p ${PROJECT} \
		down


.PHONY: clean
clean:
	find . \( -name '*.pyc' -or -name '*.pyo' \) -print -delete
	find . \( -name '__pycache__' -or -name '.pytest_cache' \) -print -exec rm -r {} \; -prune
