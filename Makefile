# Makefile

# install location
INSTALL = lani

# source and target directories
DOC = docs
INC = h
OBJ = o
PDF = pdf
PYSRC = py
SRC = c
TXT = txt
VENV = venv

# compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -O2 -fPIC

# gather python compile information
PYTHON := python3
PIP := pip3
PYINCLUDE = $(shell $(PYTHON)-config --includes)
PYLDFLAGS = $(shell $(PYTHON)-config --ldflags)
PYSUFFIX = $(shell $(PYTHON)-config --extension-suffix)

# lani package
LANI := $(INSTALL)/__init__.py
LANI += $(INSTALL)/all.py
LANI += $(INSTALL)/core.py
LANI += $(INSTALL)/variable$(PYSUFFIX)

# lani.general (instructions) package
LANI_GENERAL := $(INSTALL)/general/__init__.py
LANI_GENERAL += $(INSTALL)/general/all.py
LANI_GENERAL += $(INSTALL)/general/add_logical_high.py

# lani.tests package
LANI_TESTS := $(INSTALL)/tests/__init__.py
LANI_TESTS += $(INSTALL)/tests/all.py
LANI_TESTS += $(INSTALL)/tests/console.py
LANI_TESTS += $(INSTALL)/tests/fuller.py
LANI_TESTS += $(INSTALL)/tests/health.py
LANI_TESTS += $(INSTALL)/tests/iebiball.py

# headers
HEADERS := $(INC)/variable.h

# PDFs
PDFS := $(PDF)/pops_z16.pdf

# default rule - build, compile, and test
default: $(LANI) $(LANI_GENERAL) $(LANI_TESTS)
	$(PYTHON) -m compileall $(INSTALL)
	#$(PYTHON) -m pdoc -o $(DOC) $(INSTALL)
	$(PYTHON) -m unittest lani.all
	$(PYTHON) -m unittest lani.tests.all

# build everything
lani: $(LANI) $(LANI_GENERAL) $(LANI_TESTS)

# copy python source files
$(INSTALL)/%.py: $(PYSRC)/%.py
	mkdir -p $(@D)
	cp $< $@

# bind extension modules
$(INSTALL)/%$(PYSUFFIX): $(OBJ)/%.o
	mkdir -p $(@D)
	$(CC) $(PYLDFLAGS) -shared $< -o $@

# compile source files
$(OBJ)/%.o: $(SRC)/%.c $(HEADERS)
	mkdir -p $(@D)
	$(CC) $(CFLAGS) $(PYINCLUDE) -I$(INC) -c $< -o $@

# generate python bytecode for all modules
compile:
	$(PYTHON) -m compileall $(INSTALL)

# run tests
test:
	$(PYTHON) -m unittest lani.all
	$(PYTHON) -m unittest lani.tests.all

# create documentation
doc:
	mkdir -p $(DOC)
	$(PYTHON) -m pdoc -o $(DOC) $(INSTALL)

# full build with logging
logs:
	make clean
	mkdir -p $(TXT)
	make lani > $(TXT)/build.txt
	make compile > $(TXT)/compile.txt
	make test > $(TXT)/tests.txt

# create python virtual environment
venv:
	$(PYTHON) -m venv $(VENV)

# install requirements
reqs:
	$(PIP) install -r requirements.txt

# update requirements.txt file with current python requirements
freeze:
	$(PIP) freeze > requirements.txt

# download all PDFs
pdf: $(PDFS)

# PDF sources
$(PDF)/pops_z16.pdf:
	mkdir -p $(@D)
	curl https://publibfp.dhe.ibm.com/epubs/pdf/a227832d.pdf > $(PDF)/pops_z16.pdf

# convert PDFs to text files (requires pdftotext package)
convert:
	mkdir -p $(TXT)
	pdftotext -layout $(PDF)/pops_z16.pdf $(TXT)/pops_z16.txt

# clean up 
clean:
	rm -rf $(INSTALL) $(OBJ) $(DOC)

# clean up, including python virtual environment and PDF directory
cleanall:
	rm -rf $(INSTALL) $(OBJ) $(DOC) $(VENV) $(PDF)

# keep these around
.PRECIOUS: $(OBJ)/%.o
