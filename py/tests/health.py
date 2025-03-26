"""health.py - Data areas for the IBM z/OS Health Checker for Z/OS"""

import unittest

from ..core import *

#-------------------------------------------------------------------#
#     HZSDPQE data areas.                                           #
#-------------------------------------------------------------------#

class HZSDPQE(DSECT):
  pass

class DPQE_LASTUPDATEDBY_TYPE(DSECT):
  pass

#-------------------------------------------------------------------#
#     HZSMGB data areas.                                            #
#-------------------------------------------------------------------#

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

class MGB_MSGINSERTD(DSECT):
  """
  Map the MGB_MSGINSERTD data area, described in MVS Data Areas, Volume 2.
  """
  """Insert description"""
  MGB_MSGINSERTD_HEADER = DS('0CL2')
  """The length of the insert For a null insert, use a length of 0."""
  MGB_MSGILEN = DS('H')
  MGB_MSGINSERTD_DATA = DS('0C')
  """The insert value"""
  MGB_MSGIVAL = DS('C')
  MGB_MSGINSERTLEN = 0x100
  """
  "*-MGB_MsgInsertD\"
  """
  MGB_MSGINSERTD_LEN = 0x2

class HZSMGB1(DSECT):
  """
  Map the HZSMGB1 data area, described in MVS Data Areas, Volume 2.
  """
  MGB1_INSERT_STRUCTURE = DS('0CL8')
  # Message inserts header
  MGB1_INSERT_STRUCTURE_HEADER = DS('0CL8')
  """
  The message number. This is the value provided in
  "XREFTEXT=MessageNumber" within the <msgnum> tag of the message
  source. This field need not be when REQUEST=HZSMSSG is specified on
  HZSFMSG.
  """
  MGB1_MESSAGENUMBER = DS('0F')
  # Same as MGB1_MessageNumber
  MGB1_ID = DS('F')
  # The number of insert addresses in the MGB1_Insert_Structure_Entries area
  MGB1_INSERT_CNT = DS('F')
  """
  The start of a contiguous area identifying the inserts. The area consist of
  "MGB1_insert_cnt" 8-byte segments where each segment is mappe dby DSECT
  MGB1_MsgInsertDesc. Note that equate HZSMGB1_LEN provides only enough
  room for the HZSMGB1 area itself. To account for inserts as well, use
  something like HZSMGB1_Len + (n)*MGB1_MsgInsertDesc_Len where n is the number
  of inserts.
  """
  MGB1_INSERT_STRUCTURE_ENTRIES = DS('0C')
  # "20" The maximum number of inserts
  MGB1_MAXINSERTS = 0x14
  # "*-HZSMGB1"
  MGB_MSGINSERTD_LEN = 0x8

class MGB1_MSGINSERTDESC(DSECT):
  """
  Map the MGB1_MSGINSERTDESC data area, described in MVS Data Areas, Volume 2.
  """
  # The length of the insert. For a null insert, use a length of 0.
  MGB1_MSGINSERTDESC_LENGTH = DS('H')
  # Reserved
  DS('XL2')
  # The address of the insert. This need not be set when the length is 0.
  MGB1_MSGINSERTDESC_ADDR = DS('A')
  # "256" The maximum length of an insert.
  MGB1_MSGINSERTLEN = 0x100
  # "*-MGB1_MsgInsertDesc"
  MGB1_MSGINSERTDESC_LEN = 0x8

#-------------------------------------------------------------------#
#     HZSPQE data areas.                                            #
#-------------------------------------------------------------------#

class HZSPQE(DSECT):
  pass

class PQE_LASTUPDATEDBY_TYPE(DSECT):
	pass

#-------------------------------------------------------------------#
#     HZSQUAA data areas.                                           #
#-------------------------------------------------------------------#

class HZSQUAAHDR(DSECT):
  pass
  
class HZSQUAAHDR64(DSECT):
  pass
  
class HZSQUAAC(DSECT):
  pass
  
class HZSQUAAC1(DSECT):
  pass
  
class HZSQUAAG(DSECT):
  pass
  
class HZSQUAACS(DSECT):
  pass
  
#-------------------------------------------------------------------#
#     HZSCONS data areas.                                           #
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#     HZSZCPAR data areas.                                          #
#-------------------------------------------------------------------#

class CPARAREA(DSECT):
  pass
  
class CPARKEYWORDENTRY(DSECT):
  pass
  
class CPARKEYWORDVALUEENTRY(DSECT):
  pass
  
class CPARKEYWORDINFO(DSECT):
  pass
  
class CPARKEYWORDFLAGS(DSECT):
  pass
  
class CPARKEYWORDDATA(DSECT):
  pass

#-------------------------------------------------------------------#
#     HZSZENF data areas.                                           #
#-------------------------------------------------------------------#

class ENF067(DSECT):
  pass
  
class ENF067_BITQUAL(DSECT):
  pass
  
#-------------------------------------------------------------------#
#     HZSZHCKL data areas.                                          # 
#-------------------------------------------------------------------#

class HCKLOG(DSECT):
  pass
  
class HCKLOGE(DSECT):
  pass
  
#-------------------------------------------------------------------#
#     Tests.                                                        #
#-------------------------------------------------------------------#

class TestHealth(unittest.TestCase):
  """
  Tests for the `health.py` module.
  """
  def test_hzsdpqe(self):
    """
    Create and destroy all DSECTs defined in the HZSDPQEMGB data area.
    """
    dsects = (HZSDPQE, DPQE_LASTUPDATEDBY_TYPE)
    for D in dsects:
      d = D()
      del d

  def test_hzsmgb(self):
    """
    Create and destroy all DSECTs defined in the HZSMGB data area.
    """
    dsects = (HZSMGB, MGB_MSGINSERTD, HZSMGB1, MGB1_MSGINSERTDESC)
    for D in dsects:
      d = D()
      del d

  def test_hzspqe(self):
    """
    Create and destroy all DSECTs defined in the HZSPQE data area.
    """
    dsects = (HZSPQE, PQE_LASTUPDATEDBY_TYPE)
    for D in dsects:
      d = D()
      del d

  def test_hzsquaa(self):
    """
    Create and destroy all DSECTs defined in the HZSQUAA data area.
    """
    dsects = (HZSQUAAHDR, HZSQUAAHDR64, HZSQUAAC, HZSQUAAC1, HZSQUAAG, HZSQUAACS)
    for D in dsects:
      d = D()
      del d

  def test_hzszcons(self):
    """
    Create and destroy all DSECTs defined in the HZSZCONS data area.
    """
    dsects = []
    for D in dsects:
      d = D()
      del d

  def test_hzscpar(self):
    """
    Create and destroy all DSECTs defined in the HZSCPAR data area.
    """
    dsects = (CPARAREA, CPARKEYWORDENTRY, CPARKEYWORDVALUEENTRY,
      CPARKEYWORDINFO, CPARKEYWORDFLAGS, CPARKEYWORDDATA)
    for D in dsects:
      d = D()
      del d

  def test_hzszenf(self):
    """
    Create and destroy all DSECTs defined in the HZSCZENF data area.
    """
    dsects = (ENF067, ENF067_BITQUAL)
    for D in dsects:
      d = D()
      del d

  def test_hzszhckl(self):
    """
    Create and destroy all DSECTs defined in the HZSZHCKL data area.
    """
    dsects = (HCKLOG, HCKLOGE)
    for D in dsects:
      d = D()
      del d
