#ifndef LANI_INSTRUCTION_H
#define LANI_INSTRUCTION_H

#include <stdint.h>

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "symbol.h"

typedef struct {
  // already included in Symbol type
  //PyObject_HEAD

  // subclass of Symbol
  Symbol symbol;

  // two-byte opcode
  unsigned short opcode;

} Instruction;

typedef struct {
  // already included in Instruction type
  //PyObject_HEAD

  // subclass of Instruction
  Instruction instruction;
  
  // operands
  unsigned char *r1;
  unsigned char *r2;
  unsigned char *r3;

} RRFInstruction;

#endif
