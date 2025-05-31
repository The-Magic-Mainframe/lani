"""set_program_mask.py - SET PROGRAM MASK

The first operand is used to set the condition code and the program mask of
the current PSW.

Bits 34 and 35 of general register R1 replace the condition code, and bits
36-39 replace the program mask. Bits 0-33 and 40-63 of general register R1
are ignored.

Resulting Condition Code:

The code is set as specified by bits 34 and 35 of general register R1.

Program Exceptions: None

* [SA22-7832-13] IBM Principles of Operations, pg 7-382
"""
from ..core import RRInstruction as _RRInstruction

class SPM(_RRInstruction):
  """
  SPM   R1        [RR]
  +--------+----+----+
  | 0x04   | R1 |////|
  +--------+----+----+
  0        8    12  15
  """
  def __init__(self, R1):
    """
    Build the SPM instruction.
    """
    super().__init__(0x4, R1)