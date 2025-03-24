#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "variable.h"

static PyTypeObject VariableType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "variable.Variable",
  .tp_doc = PyDoc_STR("This class represents variable data in the `lani` language."),
  .tp_basicsize = sizeof(Variable),
  .tp_itemsize = 0,
  .tp_flags = Py_TPFLAGS_DEFAULT,
  .tp_new = PyType_GenericNew,
};

static PyModuleDef variableModule = {
  PyModuleDef_HEAD_INIT,
  .m_name = "variable",
  .m_doc = "This module defines the Variable class.",
  .m_size = -1,
};

PyMODINIT_FUNC PyInit_variable(void) {
  /*
  Initialize the VariableType class, the `variable` module, and add 
  VariableType to the module dictionary.
  */
  PyObject *m;

  if (PyType_Ready(&VariableType) < 0)
    return NULL;

  if ((m = PyModule_Create(&variableModule)) == NULL)
    return NULL;

  Py_INCREF(&VariableType);
  if (PyModule_AddObject(m, "Variable", (PyObject *) &VariableType) < 0) {
    Py_DECREF(&VariableType);
    Py_DECREF(&m);
    return NULL;
  }

  return m;
}
