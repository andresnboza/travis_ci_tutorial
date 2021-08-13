PYTHON = python3
REPO_NAME = andresnboza/travis_ci_training

start: dockerCompose

test:
	${PYTHON} -m pytest

dockerCompose:
	docker-compose up --build

dockerhub_push_local:
	docker image build -t ${REPO_NAME} .
	docker push ${REPO_NAME}

dockerhub_push:
	docker login --username $$DOCKER_USER --password $$DOCKER_PASS
	docker image build -t ${REPO_NAME} .
	docker push ${REPO_NAME}