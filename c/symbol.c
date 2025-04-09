#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "symbol.h"

static PyTypeObject SymbolType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "symbol.Symbol",
  .tp_doc = PyDoc_STR("This class represents constant or variable data " \
    "in the `lani` language."),
  .tp_basicsize = sizeof(Symbol),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT,
  .tp_new = PyType_GenericNew,
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
