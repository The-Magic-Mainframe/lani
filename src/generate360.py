#!/usr/bin/python
"""generate360.py - Create python skeleton modules for S/360 instructions

See: Wikibooks - https://en.wikibooks.org/wiki/360_Assembly/360_Instructions
See: z16 POPs - https://publibfp.dhe.ibm.com/epubs/pdf/a227832d.pdf
"""

<<<<<<< HEAD
# S/360 general instructions
instructions = {
  # opcode: (mnemonic, name, iformat, itype, [operands])
  0x04: ('SPM', 'SET PROGRAM MASK', 'RR', 'general', ['R1'])
}

diagrams = {
  0x04: """
  SPM   R1        [RR]
=======
# S/360 general instructions - 
#   (opcode, mnemonic, name, iformat, itype, [operands], diagram, description)
instructions = [
  (0x04, 'SPM', 'SET PROGRAM MASK', 'RR', 'general', ['R1'], 
  """SPM   R1        [RR]
>>>>>>> 4653cab (generate skeleton files)
  +--------+----+----+
  | 0x04   | R1 |////|
  +--------+----+----+
  0        8    12  15""",
<<<<<<< HEAD
}

descriptions = {
  0x04: """
The first operand is used to set the condition code and the program mask of
=======
  """The first operand is used to set the condition code and the pgoram mask of
>>>>>>> 4653cab (generate skeleton files)
the current PSW.

Bits 34 and 35 of general register R1 replace the condition code, and bits
36-39 replace the program mask. Bits 0-33 and 40-63 of general register R1
are ignored.

Resulting Condition Code:

The code is set as specified by bits 34 and 35 of general register R1.

Program Exceptions: None

<<<<<<< HEAD
* [SA22-7832-13] IBM Principles of Operations, pg 7-382""",
}

# generate
for opcode in instructions:
  mnemonic, name, iformat, itype, operands = instructions[opcode]
  camel_name = ''.join(s[0].upper() + s[1:].lower() for s in name.split())
  under_name = name.replace(' ', '_').lower()
  file_name = f"{itype}/{name.replace(' ', '_').lower()}.py"
  diagram = diagrams[opcode]
  description = descriptions[opcode]
  code = f'''"""{under_name}.py - {name.upper()}
=======
* [SA22-7832-13] IBM Principles of Operations, pg 7-382""")
]

# generate
for (opcode, mnemonic, name, iformat, itype, operands, diagram, description) in instructions:
  camel_name = ''.join(s[0].upper() + s[1:].lower() for s in name.split())
  code = f'''"""{name.replace(' ', '_').lower()}.py - {name.upper()}
  
>>>>>>> 4653cab (generate skeleton files)
{description}
"""
from ..core import {iformat}Instruction as _{iformat}Instruction

class {mnemonic.upper()}(_{iformat}Instruction):
<<<<<<< HEAD
  """{diagram}
=======
  """
  {diagram}
>>>>>>> 4653cab (generate skeleton files)
  """
  def __init__(self, {', '.join(operands)}):
    """
    Build the {mnemonic.upper()} instruction.
    """
    super().__init__({hex(opcode)}, {', '.join(operands)})'''

  # write to file
<<<<<<< HEAD
  print(f"Opening '{file_name}'")
  with open(file_name, 'w') as f:
    print(f"Writing to '{file_name}'")
=======
  fn = f"{itype}/{name.replace(' ', '_').lower()}.py"
  print(f"Opening '{fn}'")
  with open(fn, 'w') as f:
    print(f"Writing to '{fn}'")
>>>>>>> 4653cab (generate skeleton files)
    f.write(code)
