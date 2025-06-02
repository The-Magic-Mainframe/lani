# Makefile

# install location
INSTALL = lani

# source and target directories
DOC = docs
INC = include
OBJ = obj
SRC = src
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
LANI += $(INSTALL)/symbol$(PYSUFFIX)

# lani.general (instructions) subpackage
LANI_GENERAL := $(INSTALL)/general/__init__.py
LANI_GENERAL += $(INSTALL)/general/all.py
LANI_GENERAL += $(INSTALL)/general/add_logical_high.py
LANI_GENERAL += $(INSTALL)/general/set_program_mask.py

# lani.decimal (instructions) subpackage
LANI_DECIMAL := $(INSTALL)/decimal/__init__.py
LANI_DECIMAL += $(INSTALL)/decimal/all.py

# lani.floating (instructions) subpackage
LANI_FLOATING_POINT := $(INSTALL)/floating/__init__.py
LANI_FLOATING_POINT += $(INSTALL)/floating/all.py

# lani.control (instructions) subpackage
LANI_CONTROL := $(INSTALL)/control/__init__.py
LANI_CONTROL += $(INSTALL)/control/all.py

# lani.io (instructions) subpackage
LANI_IO := $(INSTALL)/io/__init__.py
LANI_IO += $(INSTALL)/io/all.py

# lani.vector (instructions) subpackage
LANI_VECTOR := $(INSTALL)/vector/__init__.py
LANI_VECTOR += $(INSTALL)/vector/all.py

# lani.tests subpackage
LANI_TESTS := $(INSTALL)/tests/__init__.py
LANI_TESTS += $(INSTALL)/tests/all.py
LANI_TESTS += $(INSTALL)/tests/symbol.py

# all instructions
LANI_INSTRUCTIONS := $(LANI_GENERAL)
LANI_INSTRUCTIONS += $(LANI_DECIMAL)
LANI_INSTRUCTIONS += $(LANI_FLOATING_POINT)
LANI_INSTRUCTIONS += $(LANI_CONTROL)
LANI_INSTRUCTIONS += $(LANI_IO)
LANI_INSTRUCTIONS += $(LANI_VECTOR)

# headers
HEADERS := $(INC)/symbol.h

# default rule - build, compile, and test
default: $(LANI) $(LANI_INSTRUCTIONS) $(LANI_TESTS)
	$(PYTHON) -m compileall $(INSTALL)
	$(PYTHON) -m unittest lani.all
	$(PYTHON) -m unittest lani.tests.all

# build everything
lani: $(LANI) $(LANI_INSTRUCTIONS) $(LANI_TESTS)

# copy python source files
$(INSTALL)/%.py: $(SRC)/%.py
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

# clean up 
clean:
	rm -rf $(INSTALL) $(OBJ)

# clean up, including documentation and python virtual environment
cleanall:
	rm -rf $(INSTALL) $(OBJ) $(DOC) $(VENV)

# keep these around
.PRECIOUS: $(OBJ)/%.o
