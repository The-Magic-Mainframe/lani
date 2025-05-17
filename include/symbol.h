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
  uint64_t dim;
  uint64_t size;
  uint64_t length;

  // 1-byte, 2-half word, 4-full word, 8-double word, or 16-quad word boundary
  char boundary;

  // type of data
  char datatype;

} Symbol;

#endif
