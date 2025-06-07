#!/usr/bin/python
"""generate360.py - Create python skeleton modules for S/360 instructions

See: Wikibooks - https://en.wikibooks.org/wiki/360_Assembly/360_Instructions
See: z16 POPs - https://publibfp.dhe.ibm.com/epubs/pdf/a227832d.pdf
"""
import os

# POPS chapters
#   07 - general
#   08 - decimal
#   09 - floating
#   10 - control
#   14 - I/O
#   18 - floating hexadecimal
#   19 - floating binary
#i  20 - floating decimal
#   22 - vector integer
#   23 - vector string
#   24 - vector floating
#   25 - vector decimal

# S/360 general instructions - 
#   (opcode, mnemonic, name, iformat, itype, [operands], diagram, description)
instructions = {
  0x04: ('SPM', 'SET PROGRAM MASK', 'RR', 'general', ['R1']),
  0x05: ('BALR', 'BRANCH AND LINK', 'RR',  'general', ['R1', 'R2']),
  0x06: ('BCTR', 'BRANCH ON COUNT', 'RR', 'general', ['R1', 'R2']),
  0x07: ('BCR', 'BRANCH ON CONDITION', 'RR', 'general', ['M1', 'R1']),
  #0x08: ('SSK', 'SET STORAGE KEY', 'RR', 'general', ['R1', 'R2']),
  #0x09: ('ISK', 'INSERT STORAGE KEY', 'RR', 'general', ['R1', 'R2']),
  0x0a: ('SVC', 'SUPERVISOR CALL', 'I', 'general', ['I']),
  0x0d: ('BASR', 'BRANCH AND SAVE', 'RR', 'general', ['R1', 'R2']),
  0x10: ('LPR', 'LOAD POSITIVE', 'RR', 'general', ['R1', 'R2']),
  0x11: ('LNR', 'LOAD NEGATIVE', 'RR', 'general', ['R1', 'R2']),
  0x12: ('LTR', 'LOAD AND TEST', 'RR', 'general', ['R1', 'R2']),
  0x13: ('LCR', 'LOAD AND COMPLEMENT', 'RR', 'general', ['R1', 'R2']),
  0x14: ('NR', 'AND', 'RR', 'general', ['R1', 'R2']),
  0x15: ('CLR', 'COMPARE LOGICAL', 'RR', 'general', ['R1', 'R2']),
  0x16: ('OR', 'OR', 'RR', 'general', ['R1', 'R2']),
  0x17: ('XR', 'EXCLUSIVE OR', 'RR', 'general', ['R1', 'R2']),
  0x18: ('LR', 'LOAD', 'RR', 'general', ['R1', 'R2']),
  0x19: ('CR', 'COMPARE', 'RR', 'general', ['R1', 'R2']),
  0x1a: ('AR', 'ADD', 'RR', 'general', ['R1', 'R2']),
  0x1b: ('SR', 'SUBTRACT', 'RR', 'general', ['R1', 'R2']),
  0x1c: ('MR', 'MULTIPLY', 'RR', 'general', ['R1', 'R2']),
  0x1d: ('DR', 'DIVIDE', 'RR', 'general', ['R1', 'R2']),
  0x1e: ('ALR ', 'ADD LOGICAL', 'RR', 'general', ['R1', 'R2']),
  0x1f: ('SLR ', 'SUBTRACT LOGICAL', 'RR', 'general', ['R1', 'R2']),
  0x20: ('LPDR', 'LOAD POSITIVE', 'RR', 'floating', ['R1', 'R2']),
  0x21: ('LNDR', 'LOAD NEGATIVE', 'RR', 'floating', ['R1', 'R2']),
  0x22: ('LTDR', 'LOAD AND TEST', 'RR', 'floating', ['R1', 'R2']),
  0x23: ('LCDR', 'LOAD COMPLEMENT LONG', 'RR', 'floating', ['R1', 'R2']),
  0x24: ('HDR', 'HALVE', 'RR', 'floating', ['R1', 'R2']),
  0x25: ('LRDR', 'LOAD ROUNDED', 'RR', 'floating', ['R1', 'R2']),
  0x26: ('MXR', 'MULTIPLY', 'RR', 'floating', ['R1', 'R2']),
  0x27: ('MXDR', 'MULTIPLY', 'RR', 'floating', ['R1', 'R2']),
  0x28: ('LDR', 'LOAD', 'RR', 'floating', ['R1', 'R2']),
  0x29: ('CDR', 'COMPARE', 'RR', 'floating', ['R1', 'R2']),
  0x2a: ('ADR', 'ADD NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x2b: ('SDR', 'SUBTRACT NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x2c: ('MDR', 'MULTIPLY', 'RR', 'floating', ['R1', 'R2']),
  0x2d: ('DDR', 'DIVIDE', 'RR', 'floating', ['R1', 'R2']),
  0x2e: ('AWR', 'ADD UNNORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x2f: ('SWR', 'SUBTRACT UNNORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x30: ('LPER', 'LOAD POSITIVE', 'RR', 'floating', ['R1', 'R2']),
  0x31: ('LNER', 'LOAD NEGATIVE', 'RR', 'floating', ['R1', 'R2']),
  0x32: ('LTER', 'LOAD AND TEST', 'RR', 'floating', ['R1', 'R2']),
  0x33: ('LCER', 'LOAD COMPLEMENT', 'RR', 'floating', ['R1', 'R2']),
  0x34: ('HER', 'HALVE', 'RR', 'floating', ['R1', 'R2']),
  0x35: ('LRER', 'LOAD ROUNDED', 'RR', 'floating', ['R1', 'R2']),
  0x36: ('AXR', 'ADD NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x37: ('SXR', 'SUBTRACT NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x38: ('LER', 'LOAD', 'RR', 'floating', ['R1', 'R2']),
  0x39: ('CER', 'COMPARE', 'RR', 'floating', ['R1', 'R2']),
  0x3a: ('AER', 'ADD NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x3b: ('SER', 'SUBTRACT NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x3c: ('MER', 'MULTIPLY NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x3d: ('DER', 'DIVIDE NORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x3e: ('AUR', 'ADD UNNORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x3f: ('SUR', 'SUBTRACT UNNORMALIZED', 'RR', 'floating', ['R1', 'R2']),
  0x40: ('STH', 'STORE HALFWORD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x41: ('LA', 'LOAD ADDRESS', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x42: ('STC', 'STORE CHARACTER', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x43: ('IC', 'INSERT CHARACTER', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x44: ('EX', 'EXECUTE', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x45: ('BAL', 'BRANCH AND LINK', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x46: ('BCT', 'BRANCH ON COUNT', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x47: ('BC', 'BRANCH ON CONDITION', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x48: ('LH', 'LOAD HALFWORD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x49: ('CH', 'COMPARE HALFWORD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x4a: ('AH', 'ADD HALFWORD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x4b: ('SH', 'SUBTRACT HALFWORD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x4c: ('MH', 'MULTIPLY HALFWORD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x4d: ('BAS', 'BRANCH AND SAVE', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x4e: ('CVD', 'CONVERT TO DECIMAL', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x4f: ('CVB', 'CONVERT TO BINARY', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x50: ('ST', 'STORE', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x54: ('N', 'AND', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x55: ('CL', 'COMPARE LOGICAL', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x56: ('O', 'OR', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x57: ('X', 'EXCLUSIVE OR', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x58: ('L', 'LOAD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x59: ('C', 'COMPARE', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x5a: ('A', 'ADD', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x5b: ('S', 'SUBTRACT', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x5c: ('M', 'MULTIPLY', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x5d: ('D', 'DIVIDE', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x5e: ('AL', 'ADD LOGICAL', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x5f: ('SL', 'SUBTRACT LOGICAL', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  0x60: ('STD', 'STORE', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x67: ('MXD', 'MULTIPLY', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x68: ('LD', 'LOAD', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x69: ('CD', 'COMPARE', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x6a: ('AD', 'ADD NORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x6b: ('SD', 'SUBTRACT NORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x6c: ('MD', 'MULTIPLY', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x6d: ('DD', 'DIVIDE', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x6e: ('AW', 'ADD UNNORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x6f: ('SW', 'SUBTRACT UNNORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x70: ('STE', 'STORE', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x78: ('LE', 'LOAD', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x79: ('CE', 'COMPARE', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x7a: ('AE', 'ADD NORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x7b: ('SE', 'SUBTRACT NORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x7c: ('ME', 'MULTIPLY', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x7d: ('DE', 'DIVIDE', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x7e: ('AU', 'ADD UNNORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x7f: ('SU', 'SUBTRACT UNNORMALIZED', 'RX', 'floating', ['R1', 'D2', 'X2', 'B2']),
  0x80: ('SSM', 'SET SYSTEM MASK', 'SI', 'control', ['D2', 'B2']),
  0x82: ('LPSW', 'LOAD PROGRAM STATUS WORD', 'SI', 'control', ['D2', 'B2']),
  0x83: ('DIAGNOSE', 'DIAGNOSE', 'RX', 'general', ['R1', 'D2', 'X2', 'B2']),
  #0x84: ('WRD', 'WRITE DIRECT', 'RX', 'io', ['R1', 'D2', 'X2', 'B2']),
  #0x85: ('RDD', 'READ DIRECT', 'RX', 'io', ['R1', 'D2', 'X2', 'B2']),
  0x86: ('BXH', 'BRANCH ON INDEX HIGH', 'RS', 'general', ['R1', 'R3', 'D2', 'B2']),
  0x87: ('BXLE', 'BRANCH ON INDEX LOW OR EQUAL', 'RS', 'general', ['R1', 'R3', 'D2', 'B2']),
  0x88: ('SRL', 'SHIFT RIGHT SINGLE LOGICAL', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x89: ('SLL', 'SHIFT LEFT LOGICAL', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x8a: ('SRA', 'SHIFT RIGHT', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x8b: ('SLA', 'SHIFT LEFT', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x8c: ('SRDL', 'SHIFT RIGHT DOUBLE LOGICAL', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x8d: ('SLDL', 'SHIFT LEFT DOUBLE', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x8e: ('SRDA', 'SHIFT RIGHT DOUBLE', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x8f: ('SLDA', 'SHIFT LEFT DOUBLE', 'RS', 'general', ['R1', 'D2', 'B2']),
  0x90: ('STM', 'STORE MULTIPLE', 'RS', 'general', ['R1', 'R3', 'D2', 'B2']),
  0x91: ('TM', 'TEST UNDER MASK', 'SI', 'general', ['D2', 'B2', 'I1']),
  0x92: ('MVI', 'MOVE IMMEDIATE', 'SI', 'general', ['D2', 'B2', 'I1']),
  0x93: ('TS', 'TEST AND SET', 'SI', 'general', ['D2', 'B2']),
  0x94: ('NI', 'AND', 'SI', 'general', ['D2', 'B2', 'I1']),
  0x95: ('CLI', 'COMPARE LOGICAL', 'SI', 'general', ['D2', 'B2', 'I1']),
  0x96: ('OI', 'OR', 'SI', 'general', ['D2', 'B2', 'I1']),
  0x97: ('XI', 'EXCLUSIVE OR', 'SI', 'general', ['D2', 'B2', 'I1']),
  0x98: ('LM', 'LOAD MULTIPLE', 'RS', 'general', ['R1', 'R3', 'D2', 'B2']),
  #0x9c: ('SIO', 'START IO', 'SI', 'io', ['D2', 'B2']),
  #0x9d: ('TIO', 'TEST IO', 'SI', 'io', ['D2', 'B2']),
  #0x9e: ('HIO', 'HALT IO', 'SI', 'io', ['D2', 'B2']),
  #0x9f: ('TCH', 'TEST CHANNEL', 'SI', 'io', ['D2', 'B2']),
  0xd1: ('MVN', 'MOVE NUMERICS', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xd2: ('MVC', 'MOVE', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xd3: ('MVZ', 'MOVE ZONES', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xd4: ('NC', 'AND', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xd5: ('CLC', 'COMPARE LOGICAL', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xd6: ('OC', 'OR', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xd7: ('XC', 'EXCLUSIVE OR', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xdc: ('TR', 'TRANSLATE', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xdd: ('TRT', 'TRANSLATE AND TEST', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xde: ('ED', 'EDIT', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xdf: ('EDMK', 'EDIT AND MARK', 'SS', 'general', ['L', 'D1', 'B1', 'D2', 'B2']),
  0xf0: ('SRP', 'SHIFT AND ROUND DECIMAL', 'SS', 'decimal', ['D1', 'L1', 'B1', 'D2', 'B2', 'I3']),
  0xf1: ('MVO', 'MOVE WITH OFFSET', 'SS', 'general', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xf2: ('PACK', 'PACK', 'SS', 'general', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xf3: ('UNPK', 'UNPACK', 'SS', 'general', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xf8: ('ZAP', 'ZERO AND ADD', 'SS', 'decimal',  ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xf9: ('CP', 'COMPARE DECIMAL', 'SS', 'decimal', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xfa: ('AP', 'ADD DECIMAL', 'SS', 'decimal', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xfb: ('SP', 'SUBTRACT DECIMAL', 'SS', 'decimal', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xfc: ('MP', 'MULTIPLY DECIMAL', 'SS', 'decimal', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
  0xfd: ('DP', 'DIVIDE DECIMAL', 'SS', 'decimal', ['D1', 'L1', 'B1', 'D2', 'L2', 'B2']),
}

diagrams = {
  0x04: """
  SPM   R1        [RR]
  +--------+----+----+
  | 0x04   | R1 |////|
  +--------+----+----+
  0        8    12  15""",
  0x05: """
  BALR  R1,R2     [RR]
  +--------+----+----+
  | 0x05   | R1 | R2 |
  +--------+----+----+
  0        8    12  15""",
  0x06: """
  BCTR  R1,R2     [RR]
  +--------+----+----+
  | 0x06   | R1 | R2 |
  +--------+----+----+
  0        8    12  15""",
  0x07: """
  BCR   M1,R2     [RR]
  +--------+----+----+
  | 0x07   | M1 | R2 |
  +--------+----+----+
  0        8    12  15""",
  0x0a: """
  SVC   I          [I]
  +--------+---------+
  | 0x0a   | I       |
  +--------+---------+
  0        8        15""",
  0x0d: """
  BASR  R1,R2     [RR]
  +--------+---------+
  | 0x0d   | R1 | R2 |
  +--------+----+----+
  0        8    12  15""",
  0x80: """
  SSM   D2,B2                  [SI]
  +----+--------+----+------------+
  |0x80|////////| B2 | D2         |
  +----+--------+----+------------+
  0    4        16   20          31""",
  0x82: """
  LPSW  D2,B2                  [SI]
  +----+--------+----+------------+
  |0x82|////////| B2 | D2         |
  +----+--------+----+------------+
  0    4        16   20          31""",
}

descriptions = {
  0x04: """
The first operand is used to set the condition code and the program mask of
the current PSW.

Bits 34 and 35 of general register R1 replace the condition code, and bits
36-39 replace the program mask. Bits 0-33 and 40-63 of general register R1
are ignored.

Resulting Condition Code:

The code is set as specified by bits 34 and 35 of general register R1.

Program Exceptions:

None

Source:

* [SA22-7832-13] IBM Principles of Operations, pg 7-382""",
  0x80: """
Bits 0-7 of the current PSW are replaced by the byte at the location
designated by the second-operand address.

Bits 8-15 of the instruction are reserved and should contain zeros; otherwise,
the program may not operate compatibly in the future.

Special Conditions:

When the SSM-suppression-control bit, bit 33 of control register 0, is one and
the CPU is in the supervisor state, a special-operation exception is 
recognized.

The value to be loaded in the PSW is not checked for validity before loading.
However, immediately after loading, a specification is recognized, and
a program interruption occurs, if either (a) the contents of bit positions
0 and 2-4 of the PSW are not all zeros, or (b) in the ESA/390-compatibility
mode, bit position of the PSW does not contain a zero. In either of these
cases, the instruction is completed, and the instruction-length code is set
to 2 or 3. The specification exception, which is listed as a program
exception for this instruction, is described in "Early Exception Recognition"
on page 6-9.

The operation is suppressed on all addressing and protection exceptions.

Condition Code:

The code remains unchanged.

Program Exceptions:

* Access (fetch, operand 2)
* Privileged operation
* Special operation
* Specification
* Transaction constraint

Source:

* [SA22-7832-13] IBM Principles of Operations, pg 10-143""",
  0x82: """
The current PSW is replaced by a 16-byte PSW formed from the contents of the
doubleword at the location designated by the second-operand address.

Bits 8-15 of the instruction are reserved and should contain zeros; otherwise,
the program may not operate compatibly in the future.

Bit 12 of the doubleword must be one; otherwise, depending on the model, a 
specification exception may be recognized and the operation suppressed.

Bits 0-11, 13-32, and 33-63 of the doubleword are placed in bit positions 0-11,
13-32, and 97-127 of the current PSW, respectively. Bits 33-96 of the current
PSW are set to zeros.

Bit 12 of the doubleword is inverted and then placed in bit 12 of the current
PSW. This applies in the z/Architecture architectural mode and in the 
ESA/390-compatibility mode.

A serialization and checkpoint-synchronization function is performed before or
after the operand is fetched and again after the operation is completed.

Special Conditions:

The operand must be designated on a doubleword boundary; otherwise, a
specification exception is recognized. A specification exception may be 
recognized if the key alue in bits 8-11 of the operand is nonzero.

The other PSW fields which are to be loaded by the instruction are not checked
for validity before they are loaded, exception for the optional checking of
bit 12. However, immediately after loading, a specification
exception is recognized, and a program interruption occurs, when any of the
following is true for the newly loaded PSW:

* Any bits 0, 2-4, 12, or 25-30 is a one.

* In the ESA/390-compatibility mode, bit 5 of the PSW is one.

* Bit 24 is one (recognition of this condition is optional)

* Bit 31 and 32 are both zero, and bits 97-103 are not all zeros.

* Bits 31 and 32 are one and zero, respectively.

* In the ESA/390-compatibility mode, bit 31 is one (recognition of this
  condition is unpredictable).

In these cases, the operation is completed, and the resulting instruction-
length code is 0.

The test for a specification after the PSW is loaded is described in "Early
Exception Recognition" on page 6-9.

The operation is suppressed on all addressing and protection exceptions.

Resulting Condition Code:

The code is set as specified in the new PSW loaded.

Program Exceptions:

* Access (fetch, operand 2)
* Privileged operation
* Special operation
* Specification
* Transaction constraint

Source:

* [SA22-7832-13] IBM Principles of Operations, pg 10-56""",
}

# remove existing files
for opcode in instructions:
  mnemonic, name, iformat, itype, operands = instructions[opcode]
  camel_name = ''.join(s[0].upper() + s[1:].lower() for s in name.split())
  under_name = name.replace(' ', '_').lower()
  file_name = f"{itype}/{under_name}.py"

  try:
    os.remove(file_name)
    print(f'Removed {file_name}')
  except FileNotFoundError:
    pass

# generate
for opcode in instructions:
  mnemonic, name, iformat, itype, operands = instructions[opcode]
  camel_name = ''.join(s[0].upper() + s[1:].lower() for s in name.split())
  under_name = name.replace(' ', '_').lower()
  file_name = f"{itype}/{under_name}.py"
  description = descriptions[opcode] if opcode in descriptions else ""
  diagram = diagrams[opcode] if opcode in diagrams else ""
  code = f'''"""{under_name}.py - {name.upper()}
{description}
"""
from ..core import {iformat}Instruction as _{iformat}Instruction

class {mnemonic.upper()}(_{iformat}Instruction):
  """{diagram}
  """
  def __init__(self, {', '.join(operands)}):
    """
    Build the {mnemonic.upper()} instruction.
    """
    super().__init__({hex(opcode)}, {', '.join(operands)})
'''

  # append to file
  print(f"Opening '{file_name}'")
  with open(file_name, 'a') as f:
    print(f"Writing to '{file_name}'")
    f.write(code)
