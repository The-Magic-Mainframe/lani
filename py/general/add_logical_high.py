"""add_logical_high.py - ADD LOGICAL HIGH

The second operand is added to the third operand, and the sum is placed at
the first-operand location. The operands and the sum are treated as 32-bit
unsigned binary integers. The first and second operands are in bits 0-31 of
general registers R1 and R2, respectively; bits 32-63 of general register R1
are unchanged, and bits 32-63 of general register R2 are ignored. For ALHHHR,
the third operand is in bits 0-31 of general register R3; bits 32-63 of the 
register are ignored. For ALHHLR, the third operand is in bits 32-63 of general
register R3; bits 0-31 of the register are ignored.

Resulting Condition Code:

* 0 - Result zero; no carry
* 1 - Result not zero; no carry
* 2 - Result zero; carry
* 3 - Result not zero; carry

Program Exceptions:

* Operation (if the high-word facility is not installed)

Source:

* [SA22-7832-13] IBM Principles of Operations, pg 7-30
"""  

import unittest as _unittest

from ..core import RRFInstruction as _RRFInstruction

class ALHHHR(_RRFInstruction):
  """
  ALHHHR   R1,R2,R3      [RRF-a]
  +----------------------------+
  | 0xB9CA | R3 |////| R1 | R2 |   
  +--------+----+----+----+----+
  0        16   20   24   28  31
  """
  def __init__(self, R1, R2, R3):
    """
    Build the ALHHHR instruction.
    """
    super().__init__(0xB9CA, R1, R2, R3)

class ALHHLR(_RRFInstruction):
  """
  ALHHLR   R1,R2,R3      [RRF-a]
  +----------------------------+
  | 0xB9DA | R3 |////| R1 | R2 |   
  +--------+----+----+----+----+
  0        16   20   24   28  31
  """
  def __init__(self, R1, R2, R3):
    """
    Build the ALHHLR instruction.
    """
    super().__init__(0xB9DA, R1, R2, R3)

class _TestAddLogicalHigh(_unittest.TestCase):
  """
  Test the ALHHHR and ALHHLR instructions.
  """
  def test_add_logical_high(self):
    """
    """
    alhhhr = ALHHHR()
    del alhhhr
    alhhlr = ALHHLR()
    del alhhlr
