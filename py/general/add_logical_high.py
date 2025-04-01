"""add_logical_high.py - ADD LOGICAL HIGH instructions"""

import unittest as _unittest

from ..core import RRFInstruction as _RRFInstruction

class ALHHHR(_RRFInstruction):
  """
  """
  pass

class ALHHLR(_RRFInstruction):
  """
  """
  pass

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
