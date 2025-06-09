#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include "symbol.h"

static void Symbol_dealloc(Symbol *self) {
  /*
  Destructor.
  */
  return;
}

static PyObject *Symbol_new(PyTypeObject *type, PyObject *args,
  PyObject *kwargs) {
  /*
  Constructor.
  */
  Symbol *self;
  self = (Symbol *) type->tp_alloc(type, 0);
  self->storage = NULL;
  self->size = 0;
  self->dim = 0;
  self->length = 0;
  self->boundary = 0;
  self->datatype = 'U';
  self->exttype = 0;
  return (PyObject *) self;
}

static int Symbol_init(Symbol *self, PyObject *args,
  PyObject *kwargs) {
  /*
  Initialization.
  */
  PyObject *value = NULL;
  PyObject *section = NULL;

  static char *keywords[] = {
    "value", "size", "dim", "boundary", "datatype", "exttype", "section", NULL};

  if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|OKKbCCO", keywords,
      &value,
      &self->size, &self->dim, &self->boundary,
      &self->datatype, &self->exttype,
      &self->section))
    return -1;

  return 0;
}

static PyMemberDef Symbol_members[] = {
  {"size", T_ULONGLONG, offsetof(Symbol, size), READONLY,
   "Size of the symbol in bytes."},
  {NULL}
};

static PyMethodDef Symbol_methods[] = {
  {NULL}
};

static PyTypeObject SymbolType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "symbol.Symbol",
  .tp_doc = PyDoc_STR("This class represents constant or variable data " \
    "in the `lani` language."),
  .tp_basicsize = sizeof(Symbol),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_dealloc = (destructor) Symbol_dealloc,
  .tp_new = Symbol_new,
  .tp_init = (initproc) Symbol_init,
  .tp_members = Symbol_members,
  .tp_methods = Symbol_methods,
};

static PyModuleDef symbolModule = {
  PyModuleDef_HEAD_INIT,
  .m_name = "symbol",
  .m_doc = "This module defines the Symbol class.",
  .m_size = -1,
};

PyMODINIT_FUNC PyInit_symbol(void) {
  /*
  Initialize the SymbolType class, the `symbol` module, and add 
  SymbolType to the module dictionary.
  */
  PyObject *m;

  if (PyType_Ready(&SymbolType) < 0)
    return NULL;

  if ((m = PyModule_Create(&symbolModule)) == NULL)
    return NULL;

  Py_INCREF(&SymbolType);
  if (PyModule_AddObject(m, "Symbol", (PyObject *) &SymbolType) < 0) {
    Py_DECREF(&SymbolType);
    Py_DECREF(&m);
    return NULL;
  }

  return m;
}
