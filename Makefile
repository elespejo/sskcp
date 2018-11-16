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
SKC_x86=$(DEPLOYMENT)/sskcp-client-imageAPI-x86
# directory of ss kcp server x86
SKS_x86=$(DEPLOYMENT)/sskcp-server-imageAPI-x86
# directory of ss kcp client armv6
SKC_armv6=$(DEPLOYMENT)/sskcp-client-imageAPI-armv6

mk-deployment-SKC_armv6: $(SKC_armv6)
	mkdir sskcp-client-imageAPI-armv6
	cp $(SKC_armv6)/docker-compose.yml $(SKC_armv6)/temp.env $(SKC_armv6)/Makefile sskcp-client-imageAPI-armv6
	sed -i "s/VERSION=latest/VERSION=$(VERSION)/g" sskcp-client-imageAPI-armv6/temp.env
	zip -r sskcp-client-imageAPI-armv6-$(VERSION).zip sskcp-client-imageAPI-armv6
	rm -r sskcp-client-imageAPI-armv6

mk-deployment-SKC_x86: $(SKC_x86)
	mkdir sskcp-client-imageAPI-x86
	cp $(SKC_x86)/docker-compose.yml $(SKC_x86)/temp.env $(SKC_x86)/Makefile sskcp-client-imageAPI-x86
	sed -i "s/VERSION=develop/VERSION=$(VERSION)/g" sskcp-client-imageAPI-x86/temp.env
	zip -r sskcp-client-imageAPI-x86-$(VERSION).zip sskcp-client-imageAPI-x86
	rm -r sskcp-client-imageAPI-x86

mk-deployment-SKS_x86: $(SKS_x86)
	mkdir sskcp-server-imageAPI-x86
	cp $(SKS_x86)/docker-compose.yml $(SKS_x86)/temp.env $(SKS_x86)/Makefile sskcp-server-imageAPI-x86 
	sed -i "s/VERSION=develop/VERSION=$(VERSION)/g" sskcp-server-imageAPI-x86/temp.env
	zip -r sskcp-server-imageAPI-x86-$(VERSION).zip sskcp-server-imageAPI-x86
	rm -r sskcp-server-imageAPI-x86

mk-deployment-CONFGEN: $(DEPLOYMENT)/confgenerator
	mkdir sskcp-confgenerator
	cp -r $(CONFGEN)/* sskcp-confgenerator
	zip -r sskcp-confgenerator-$(VERSION).zip sskcp-confgenerator
	rm -r sskcp-confgenerator

mk-deployment: mk-deployment-CONFGEN mk-deployment-SKC_x86 mk-deployment-SKS_x86 mk-deployment-SKC_armv6

clean-deployment: $(REPO).zip
	rm $(REPO).zip


.PHONY: pushtohub
pushtohub:
	docker tag $(OWNER)/$(REPO)-$(ARCH) $(OWNER)/$(REPO)-$(ARCH):$(TAG)
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker push $(OWNER)/$(REPO)-$(ARCH):$(TAG)
