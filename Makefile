.ONESHELL:
.PHONY: clean venv act tests scripts

ACTIVATE_LINUX:=. venv/bin/activate

venv:
	test -d venv || python3 -m venv venv
	
install: 
	@pip install -r requirements.txt
	@pip install -e .	


show:
	greetings --help