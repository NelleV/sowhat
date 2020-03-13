
PYTHON ?= python
CYTHON ?= cython
NOSETESTS ?= nosetests
PYTEST ?= pytest
CTAGS ?= ctags

all:

install:
	$(PYTHON) setup.py install

trailing-spaces:
	find summertime -name "*.py" | xargs perl -pi -e 's/[ \t]*$$//'

clean:
	rm -rf build
	rm -rf sdist
	rm -rf dist
	rm -rf example/*PM*
	rm -rf example/*MDS*
	find summertime -name "*.pyc" -delete 

in: inplace # just a shortcut
inplace:
	$(PYTHON) setup.py build_ext -i

test: in
	$(PYTEST) summertime --showlocals -v --cov=summertime

test-coverage:
	rm -rf coverage .coverage
	$(PYTEST) summertime --showlocals -v --cov=summertime

cython:
	find summertime -name "*.pyx" -exec $(CYTHON) --cplus {} \;

doc: inplace
	$(MAKE) -C doc html

doc-noplot: inplace
	$(MAKE) -C doc html-noplot

code-analysis:
	flake8 summertime | grep -v __init__ | grep -v external
	pylint -E -i y summertime/ -d E1103,E0611,E1101

