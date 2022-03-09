cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

build:
	docker build --build-arg LOG_PATH=$(LOG_PATH) -t $(APP_NAME) .

run:
	docker run -i -t --rm --env-file=./config.env --cap-add NET_ADMIN -v $(PWD)/$(HOST_LOG_PATH):$(LOG_PATH) --name="$(APP_NAME)" $(APP_NAME)

up: build run

stop:
	docker stop $(APP_NAME); docker rm $(APP_NAME)
