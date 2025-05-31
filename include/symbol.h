#ifndef LANI_SYMBOL_H
#define LANI_SYMBOL_H

#include <stdint.h>

#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef struct {
  PyObject_HEAD

  // pointer to storage
  void *storage;

  // space for immediate (literal) data
  char immediate[64];

  // dimension, size, and dim*size of storage
  unsigned long long size;
  unsigned long long dim;
  unsigned long long length;

  // 1-byte, 2-half word, 4-full word, 8-double word, or 16-quad word boundary
  char boundary;

  // type of data
  char datatype;
  char exttype;

  // parent symbol or section
  PyObject *section;

} Symbol;

#endif
