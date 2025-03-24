# Makefile
INSTALL = lani
SRC = c
PYSRC = py
OBJ = o
INC = h

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
LANI += $(INSTALL)/variable$(PYSUFFIX)

# headers
HEADERS := $(INC)/variable.h

# build everything
all: $(LANI)

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

# clean up 
clean:
	rm -rf $(INSTALL) $(OBJ)

# keep these around
.PRECIOUS: $(OBJ)/%.o
