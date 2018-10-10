.PHONY: start
start:
	docker-compose -f ${CURDIR}/docker-compose.yml up -d 

.PHONY: stop
stop:
	docker-compose -f ${CURDIR}/docker-compose.yml down

.PHONY: restart
restart:
	docker-compose -f ${CURDIR}/docker-compose.yml up -d --force-recreate

.PHONY: status
status:
	docker-compose -f ${CURDIR}/docker-compose.yml ps
	docker-compose -f ${CURDIR}/docker-compose.yml logs