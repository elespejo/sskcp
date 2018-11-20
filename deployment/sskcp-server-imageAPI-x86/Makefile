
COMP_DIR=$(CURDIR)/compose
ENV_TEMP=$(CURDIR)/temp.env
ENV=$(CURDIR)/.env

.PHONY: config
config:
	cp $(ENV_TEMP) $(ENV)
	cat $(CONFIG)/config.env >> $(ENV)
	echo "\nCONF_DIR=$(CONFIG)/conf" >> $(ENV)
	cat $(ENV)
	mkdir -p $(COMP_DIR)
	docker-compose -p $(NAME) -f $(CURDIR)/docker-compose.yml config | tee $(COMP_DIR)/$(NAME).yml
	rm $(ENV)

.PHONY: start
start: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml up -d 

.PHONY: stop
stop: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml down

.PHONY: restart
restart: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml up -d --force-recreate

.PHONY: status
status: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml ps || true
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml logs | tail -n 100 || true

.PHONY: list
list: $(COMP_DIR)
	for compose in `ls $(COMP_DIR)`;do name=`echo $$compose|awk -F "." '{print $$1}'`;echo $$name;docker-compose -p $$name -f $(COMP_DIR)/$$compose ps;done

.PHONY: remove
remove: $(COMP_DIR)/$(NAME).yml
	rm $(COMP_DIR)/$(NAME).yml