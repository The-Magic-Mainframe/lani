"""load_program_status_word.py - LOAD PROGRAM STATUS WORD

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

* [SA22-7832-13] IBM Principles of Operations, pg 10-56
"""
from ..core import SIInstruction as _SIInstruction

class LPSW(_SIInstruction):
  """
  LPSW  D2,B2                  [SI]
  +----+--------+----+------------+
  |0x82|////////| B2 | D2         |
  +----+--------+----+------------+
  0    4        16   20          31
  """
  def __init__(self, D2, B2):
    """
    Build the LPSW instruction.
    """
    super().__init__(0x82, D2, B2)
