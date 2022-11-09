.PHONY: clean
clean:
	rm -rf dist
	rm -rf build
	rm -rf line-counter.spec

.PHONY: dist
dist:
	python3 -m PyInstaller line-counter.py -F --onefile
