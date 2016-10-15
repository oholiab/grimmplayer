bin:
	virtualenv -p python3.4 .

dev-env:
	pip install -r dev-requirements.txt

testrun:
	PYTHONPATH=.:$$PYTHONPATH python grimmplayer/main.py
