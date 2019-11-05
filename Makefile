SHELL :=/bin/bash
PATH  :=$(PWD)/vendor:$(PATH)
PYTHONPATH :=$(PWD)/vendor:$(PYTHONPATH)

usage:
	@echo "usage"

run_server:
	@pipenv run python src/server.py

run_robot:
	@pipenv run python src/robot.py

trun_robot:
	@pipenv run python src/robot.py -t

test:
	@pipenv run python tests/request.py
