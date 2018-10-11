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


# Build deployment
.PHONY: mk-deployment clean-deployment mk-deployment-SKC_x86 mk-deployment-SKS_x86 mk-deployment-CONFGEN 

# directory of configuration generator
CONFGEN=$(DEPLOYMENT)/confgenerator
# directory of ss kcp client x86
SKC_x86=$(DEPLOYMENT)/sskcp-client-x86
# directory of ss kcp server x86
SKS_x86=$(DEPLOYMENT)/sskcp-server-x86
BUILD_DEPLOY=build_deployment

mk-deployment-SKC_x86: $(SKC_x86)
	mkdir sskcp-client-x86
	cp $(SKC_x86)/docker-compose.yml $(SKC_x86)/temp.env $(SKC_x86)/Makefile sskcp-client-x86
	sed -i "s/VERSION=develop/VERSION=$(VERSION)/g" sskcp-client-x86/temp.env
	zip -r sskcp-client-x86-$(VERSION).zip sskcp-client-x86
	rm -r sskcp-client-x86

mk-deployment-SKS_x86: $(SKS_x86)
	mkdir sskcp-server-x86
	cp $(SKS_x86)/docker-compose.yml $(SKS_x86)/temp.env $(SKS_x86)/Makefile sskcp-server-x86 
	sed -i "s/VERSION=develop/VERSION=$(VERSION)/g" sskcp-server-x86/temp.env
	zip -r sskcp-server-x86-$(VERSION).zip sskcp-server-x86
	rm -r sskcp-server-x86

mk-deployment-CONFGEN: $(DEPLOYMENT)/confgenerator
	mkdir confgenerator
	cp $(CONFGEN)/cli.py $(CONFGEN)/gen.py $(CONFGEN)/gensskcp.py $(CONFGEN)/genss.py confgenerator
	zip -r sskcp-conf-generator-$(VERSION).zip confgenerator
	rm -r confgenerator

#mk-deployment-sskcp-client-armv6: $(DEPLOYMENT)/sskcp-client-armv6
#	zip -j sskcp-client-armv6-$(VERSION).zip $(DEPLOYMENT)/sskcp-client-armv6

mk-deployment: mk-deployment-SKC_x86 mk-deployment-SKS_x86 mk-deployment-CONFGEN

clean-deployment: $(REPO).zip
	rm $(REPO).zip


.PHONY: pushtohub
pushtohub:
	docker tag $(OWNER)/$(REPO)-$(ARCH) $(OWNER)/$(REPO)-$(ARCH):$(TAG)
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker push $(OWNER)/$(REPO)-$(ARCH):$(TAG)
