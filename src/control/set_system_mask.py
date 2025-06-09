"""set_system_mask.py - SET SYSTEM MASK

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

* [SA22-7832-13] IBM Principles of Operations, pg 10-143
"""
from ..core import SIInstruction as _SIInstruction

class SSM(_SIInstruction):
  """
  SSM   D2,B2                  [SI]
  +----+--------+----+------------+
  |0x80|////////| B2 | D2         |
  +----+--------+----+------------+
  0    4        16   20          31
  """
  def __init__(self, D2, B2):
    """
    Build the SSM instruction.
    """
    super().__init__(0x80, D2, B2)
