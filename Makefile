SHELL = /bin/bash
export PATH+=":$(PWD)/vendor"
export PYTHONPATH=":$(PWD)/vendor"

run_server:
	@python src/server.py

test:
	@python tests/request.py
