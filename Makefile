# Makefile
INSTALL = lani
SRC = c
PYSRC = py
OBJ = o
INC = h
TXT = txt

# compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -O2 -fPIC

# gather python compile information
PYTHON := python3
PYINCLUDE = $(shell $(PYTHON)-config --includes)
PYLDFLAGS = $(shell $(PYTHON)-config --ldflags)
PYSUFFIX = $(shell $(PYTHON)-config --extension-suffix)

# lani package
LANI := $(INSTALL)/__init__.py
LANI += $(INSTALL)/all.py
LANI += $(INSTALL)/core.py
LANI += $(INSTALL)/variable$(PYSUFFIX)

# lani.tests package
LANI_TESTS := $(INSTALL)/tests/__init__.py
LANI_TESTS += $(INSTALL)/tests/all.py
LANI_TESTS += $(INSTALL)/tests/fuller.py
LANI_TESTS += $(INSTALL)/tests/health.py

# headers
HEADERS := $(INC)/variable.h

# default rule - build, compile, and test
default: $(LANI) $(LANI_TESTS)
	$(PYTHON) -m compileall $(INSTALL)
	$(PYTHON) -m unittest lani.tests.all

# build everything
lani: $(LANI) $(LANI_TESTS)

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
	$(PYTHON) -m unittest lani.tests.all

# full build with logging
logs:
	make clean
	mkdir -p $(TXT)
	make lani > $(TXT)/build.txt
	make compile > $(TXT)/compile.txt
	make test > $(TXT)/tests.txt

# clean up 
clean:
	rm -rf $(INSTALL) $(OBJ) $(TXT)

# keep these around
.PRECIOUS: $(OBJ)/%.o
