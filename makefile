build:
	python3 -m pip install  --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel

publish:
	python3 -m pip install --user --upgrade twine
	python3 -m twine upload --repository testpypi dist/*
