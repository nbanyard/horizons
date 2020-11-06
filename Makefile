test: test_python

test_python:
	cd python; python3 -m unittest test_*.py
