"""console.py - Console services"""

import unittest

from ..core import *

#---------------------------------------------------------------------#
#     WTO (SVC 35) parameter list.                                    #
#---------------------------------------------------------------------#

class WTO_PARMLIST(DSECT):
  pass

#---------------------------------------------------------------------#
#     WTO callable service.                                           #
#---------------------------------------------------------------------#

class WTO(RSECT):
  """
  Define the WTO callable service.
  """
  SVC(35)

  def __init__(self, *args):
    """
    Initialize an instance of FULLER.
    """
    pass

class TestConsole(unittest.TestCase):
  """
  Test the WTO parmlist and callable service.
  """
  def test_wto(self):
    """
    Create the SVC35 parmlist and call SVC35.
    """
    p = WTO_PARMLIST()
    w = WTO()
    w()
