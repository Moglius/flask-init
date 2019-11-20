.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python3-pip -y

python-packages:
	pip3 install -r requirements.txt

install: system-packages python-packages

tests:
	python3 manage.py test

run:
	python3 manage.py run

all: clean install tests run
