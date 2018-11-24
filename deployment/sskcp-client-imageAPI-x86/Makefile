
COMP_DIR=$(CURDIR)/compose
ENV_TEMP=$(CURDIR)/temp.env
ENV=$(CURDIR)/.env

.PHONY: config test_config
config:
	cp $(ENV_TEMP) $(ENV)
	cat $(CONFIG)/config.env >> $(ENV)
	echo "\nCONF_DIR=$(CONFIG)/conf" >> $(ENV)
	cat $(ENV)
	mkdir -p $(COMP_DIR)
	docker-compose -p $(NAME) -f $(CURDIR)/docker-compose.yml config | tee $(COMP_DIR)/$(NAME).yml
	rm $(ENV)
test_config:
	docker-compose -f $(COMP_DIR)/$(NAME).yml config

.PHONY: start test_start
start: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml up -d 
test_start: status

.PHONY: stop test_stop
stop: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml down
test_stop: status

.PHONY: restart test_restart
restart: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml up -d --force-recreate
test_restart: status

.PHONY: remove test_remove
remove: $(COMP_DIR)/$(NAME).yml
	rm $(COMP_DIR)/$(NAME).yml
test_remove: 
	((test -e $(COMP_DIR)/$(NAME).yml) && echo "$(NAME).yml exists.") || echo "$(NAME).yml does NOT exists."

.PHONY: status
status: $(COMP_DIR)/$(NAME).yml
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml ps || true
	docker-compose -p $(NAME) -f $(COMP_DIR)/$(NAME).yml logs | tail -n 100 || true

.PHONY: list
list: $(COMP_DIR)
	for compose in `ls $(COMP_DIR)`;do name=`echo $$compose|awk -F "." '{print $$1}'`;echo $$name;docker-compose -p $$name -f $(COMP_DIR)/$$compose ps;done
