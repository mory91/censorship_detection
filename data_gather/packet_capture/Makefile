cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

build:
	docker build -t $(APP_NAME) .

build-nc:
	docker build --no-cache -t $(APP_NAME) .

run:
	docker run -i -t --rm --env-file=./config.env --cap-add NET_ADMIN --name="$(APP_NAME)" $(APP_NAME)

up: build run

stop:
	docker stop $(APP_NAME); docker rm $(APP_NAME)
