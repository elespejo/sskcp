
ARCH = x86
ORG = elespejo
REPO = sskcp
TAG = develop
DOCKER_USER = user
DOCKER_PASS = password

.PHONY: build
build:
	docker build -f src/Dockerfile-${ARCH} -t sskcp-${ARCH} src

.PHONY: deploy
deploy:
	docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}
	docker tag ${REPO}-${ARCH} ${ORG}/${REPO}-${ARCH}:${TAG}
	docker push ${ORG}/${REPO}-${ARCH}:${TAG}
