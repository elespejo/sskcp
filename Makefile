GITBOOK = $(CURDIR)/gitbook
DOCS = $(CURDIR)/docs
IMAGE_ENV = $(CURDIR)/image
DF = $(IMAGE_ENV)/Dockerfile
DEPLOYMENT = $(CURDIR)/deployment
OWNER = elespejo
REPO = sskcp

.PHONY: mk-book clean-book
mk-book: $(GITBOOK)
	gitbook build $(GITBOOK) $(DOCS)

clean-book:
	rm -rf $(DOCS)/*

.PHONY: mk-image clean-image
mk-image:
	docker run --rm --privileged multiarch/qemu-user-static:register --reset
	docker build -t $(OWNER)/$(REPO)-$(ARCH) -f $(DF)-$(ARCH) $(IMAGE_ENV) 

clean-image:
	docker rmi $(OWNER)/$(REPO)-$(ARCH)


.PHONY: mk-deployment clean-deployment
mk-deployment-sskcp-client-x86: ${DEPLOYMENT}/sskcp-client-x86
	zip -j sskcp-client-x86-${VERSION}.zip ${DEPLOYMENT}/sskcp-client-x86

mk-deployment-sskcp-client-armv6: ${DEPLOYMENT}/sskcp-client-armv6
	zip -j sskcp-client-armv6-${VERSION}.zip ${DEPLOYMENT}/sskcp-client-armv6

mk-deployment: mk-deployment-sskcp-client-x86 mk-deployment-sskcp-client-armv6

clean-deployment: $(REPO).zip
	rm $(REPO).zip


.PHONY: pushtohub
pushtohub:
	docker tag $(OWNER)/$(REPO)-$(ARCH) $(OWNER)/$(REPO)-$(ARCH):$(TAG)
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker push $(OWNER)/$(REPO)-$(ARCH):$(TAG)
