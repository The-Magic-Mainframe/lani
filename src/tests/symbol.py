"""symbol.py - Test the Symbol type"""

import unittest

from ..symbol import *

class TestSymbol(unittest.TestCase):
  """
  Tests for the Symbol type.
  """
  def test_basics(self):
    """
    Initialize and destroy an instance of Symbol.
    """
    s = Symbol()
    del s
