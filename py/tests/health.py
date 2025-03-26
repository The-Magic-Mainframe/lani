"""health.py - Data areas for the IBM z/OS Health Checker for Z/OS"""

import unittest

from ..core import *

class HZSMGB(DSECT):
  """
  Map the HZSMGB data area, described in MVS Data Areas, Volume 2.
  """
  # Message inserts header
  MGB_INSERT_STRUCTURE = DS('0C')
  # Message inserts header
  MGB_INSERT_STRUCTURE_HEADER = DS('0CL8')
  """
  The message number. This is the value provided in "XREFTEXT=MessageNumber"
  within the <msgnum> tag of the message source.
  """
  MGB_MESSAGENUMBER = DS('0F')
  # Same as MGB_MessageNumber
  MGB_ID = DS('F')
  # The number of insert address in the MGB_Insert_Structure_Entries area
  MGB_INSERT_CNT = DS('F') 
  MGB_INSERT_STRUCTURE_ENTRIES = DS('0C')
  """
  An array of pointers, each of which contains the
  address of an area mapped by Mgb_MsgInsertD. Note that 
  if you use HZSMGB_LEN that will provide room for only
  one insert
  """
  MGB_INSERTS = DS('0A') 
  # Address of the Mgb_MsgInsertD area for the insert
  MGB_INSERTADDR = DS('A') 
  # "20" The maximum number of inserts
  MGB_MAXINSERTS = 0x14
  # "*-HZSMGB"
  HZSMGB_LEN = 0xC

  def __init__(self, *args):
    #print("We are moving")
    pass

class TestHealth(unittest.TestCase):
  """
  Tests for the `health.py` module.
  """
  def test_hzsmgb(self):
    """
    Create an HZSMGB object and set the fields to random values.
    """
    h = HZSMGB()
