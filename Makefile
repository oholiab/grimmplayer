bin:
	virtualenv -p python3.4 .

dev-env:
	pip install -r dev-requirements.txt

testrun:
	bash -c "source bin/activate && PYTHONPATH=.:$$PYTHONPATH python grimmplayer/main.py"

fonts:
	mkdir -p fonts
	cd fonts; curl http://dl.dafont.com/dl/?f=firearmencyclope -o firearmencyclope.zip; unzip firearmencyclope.zip
	cd fonts; curl http://dl.dafont.com/dl/?f=vermin_vibes_1989 -o vermin.zip; unzip vermin.zip
