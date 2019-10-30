export PATH=$(PWD)/vendor
export PYTHONPATH=$(PWD)/vendor
SHELL = /bin/bash
run:
	@python src/server.py

test:
	@python tests/request.py
