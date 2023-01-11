#####################
#    Envs           #
#####################

include .env
export $(shell sed 's/=.*//' .env)


#####################
#    Gitlab         #
#####################

login:
	docker login registry.gitlab.com


#####################
#    Core           #
#####################

core-build:
	docker-compose build blip-core


core-run:
	docker-compose run blip-core

core-run-cpu:
	docker-compose run blip-core-cpu


#####################
#    Jupyter        #
#####################

jupyter-build: core-build
	docker-compose build blip-jupyter

jupyter-run:
	docker-compose up blip-jupyter-gpu

jupyter-run-cpu:
	docker-compose up blip-jupyter-cpu

vastai-build: jupyter-build
	docker-compose build blip-vastai

vastai-push:
	docker-compose push blip-vastai

api-build: core-build-cpu
	docker-compose build blip-api

api-run:
	docker-compose run \
			-e PIPELINE_PATH=$(pipeline_path) \
			-e HOST=$(host) \
			-e PORT=$(port) \
		blip-api