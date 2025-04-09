#ifndef LANI_SYMBOL_H
#define LANI_SYMBOL_H

#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef struct {
  PyObject_HEAD

  // pointer to storage
  void *storage;

  // dimension, size, and dim*size of storage
  size_t dim;
  size_t size;
  size_t length;

  // type of data
  // TODO

} Symbol;

#endif
