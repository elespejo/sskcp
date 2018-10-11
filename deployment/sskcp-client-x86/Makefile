
COMP_DIR=$(CURDIR)/compose
ENV_TEMP=$(CURDIR)/temp.env
ENV=$(CURDIR)/.env

.PHONY: config
config:
	cp $(ENV_TEMP) $(ENV)
	echo "CONF_DIR=$(CONF)" >> $(ENV)
	echo "LOG_DIR=$(LOG)" >> $(ENV)
	cat $(ENV)
	mkdir -p $(COMP_DIR)
	docker-compose -f $(CURDIR)/docker-compose.yml config | tee $(COMP_DIR)/$(NAME).yml
	sed -i "s/SERVICE_NAME/sskcp-client-x86-$(NAME)/g" $(COMP_DIR)/$(NAME).yml
	rm $(ENV)
	mkdir -p $(LOG)

.PHONY: start
start: $(COMP_DIR)/$(NAME).yml
	docker-compose -f $(COMP_DIR)/$(NAME).yml up --no-recreate -d 

.PHONY: stop
stop: $(COMP_DIR)/$(NAME).yml
	docker-compose -f $(COMP_DIR)/$(NAME).yml down

.PHONY: restart
restart: $(COMP_DIR)/$(NAME).yml
	docker-compose -f $(COMP_DIR)/$(NAME).yml up -d --force-recreate

.PHONY: status
status: $(COMP_DIR)/$(NAME).yml
	docker-compose -f $(COMP_DIR)/$(NAME).yml ps
	docker-compose -f $(COMP_DIR)/$(NAME).yml logs

.PHONY: list
list: $(COMP_DIR)
	for compose in `ls $(COMP_DIR)`;do echo $$compose;docker-compose -f $(COMP_DIR)/$$compose ps;done

.PHONY: remove
remove: $(COMP_DIR)/$(NAME).yml
	rm $(COMP_DIR)/$(NAME).yml
