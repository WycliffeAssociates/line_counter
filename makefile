.PHONY: clean
clean:
	rm -rf dist
	rm -rf build
	rm -rf line_counter.spec

.PHONY: dist
dist:
	python3 -m PyInstaller line_counter.py -F --onefile

.PHONY: lint
lint:
	mypy *.py
	pylint *.py
