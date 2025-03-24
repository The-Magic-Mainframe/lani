# Makefile
INSTALL = lani
CSRC = c
PYSRC = py
OBJ = o

# compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -O2 -fPIC

# gather python compile information
PY_INCLUDE = $(shell python3-config --includes)
PY_LDFLAGS = $(shell python3-config --ldflags)
PY_SUFFIX = $(shell python3-config --extension-suffix)

# lani package
LANI := $(INSTALL)/__init__.py

# lani.variable module
VARIABLE := $(INSTALL)/variable.$(PY_SUFFIX)

# build everything
all: $(LANI)

# copy python source files
$(INSTALL)/%.py: $(PYSRC)/%.py
	mkdir $(@D)
	cp $< $@

# compile python extensions
$(TARGET): $(OBJS)
	$(CC) -shared $(OBJS) -o $(TARGET) $(PY_LDFLAGS)

# compile source files
%.o: %.c
	$(CC) $(CFLAGS) $(PY_INCLUDE) -c $< -o $@

# Clean up build files
clean:
	rm -rf $(INSTALL) $(OBJ)
