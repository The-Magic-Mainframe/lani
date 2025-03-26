"""fuller.py - FULLER - A fuller SPOOL archiver
***********************************************************************
*                                                                     *
* MODULE NAME = FULLER                                                *
*                                                                     *
* DESCRIPTIVE NAME = A SPOOL archival tool for z/OS.                  *
*                                                                     *
* STATUS = z/OS                                                       *
*                                                                     *
* FUNCTION = A SPOOL archival tool for z/OS.                          *
*                                                                     *
* NOTES =                                                             *
*                                                                     *
*    DEPENDENCIES = Standard MVS services                             *
*                                                                     *
*    RESTRICTIONS = None                                              *
*                                                                     *
*    REGISTER CONVENTIONS = See entry point documentation             *
*                                                                     *
*    PATCH LABEL = None                                               *
*                                                                     *
* MODULE TYPE = Procedure ( RSECT Type )                              *
*                                                                     *
*    PROCESSOR = IBM High Level Assembler/MVS 1.6.0                   *
*                                                                     *
*    MODULE SIZE = See MODLEN equate                                  *
*                                                                     *
*    ATTRIBUTES = Reentrant, RMODE ANY, AMODE 31                      *
*                                                                     *
* ENTRY POINT =                                                       *
*                                                                     *
*    PURPOSE = See function                                           *
*                                                                     *
*    LINKAGE = See entry point documentation                          *
*                                                                     *
*    INPUT = See entry point documentation                            *
*                                                                     *
*    OUTPUT = See entry point documentation                           *
*                                                                     *
*    EXIT-NORMAL = See entry point documentation                      *
*                                                                     *
*    EXIT-ERROR = See entry point documentation                       *
*                                                                     *
* EXTERNAL REFERENCES                                                 *
*                                                                     *
*    ROUTINES = None                                                  *
*                                                                     *
*    DATA AREAS = See WORKAREA definition                             *
*                                                                     *
*    CONTROL BLOCKS = None                                            *
*                                                                     *
* MACROS = MVS  -                                                     *
*                                                                     *
* CHANGE ACTIVITY                                                     *
*                                                                     *
* A000000-999999     Created for z/OS Release 3.1                     *
*                                                                     *
***********************************************************************
"""
import unittest

from ..core import *

class FULLER(RSECT):
  """
  Define the Fuller class.
  """
  AMODE (31)                       # 31-bit addressing
  RMODE ('ANY')                    # 31-bit or 24-bit residency
  TITLE ('FULLER - Main entry point')
  #-------------------------------------------------------------------#
  #     Main entry point.                                             #
  #-------------------------------------------------------------------#
  SPACE (1) 
  J     ('START')                  # Skip around module identification
  SPACE (1)
  USING ('*', 12)                  # Establish local base register
  USING ('WORKAREA', 10)           # Local work area
  SPACE (1)
  START = STM(14, 12, 12, 13)      # Save caller's registers
  SPACE (1)
  LARL  (12, START)                # Set local base register
  LHI   (10, 0)                    # No work area, yet!
  TITLE ('FULLER - Exit point')
  #-------------------------------------------------------------------#
  #     Return to caller.                                             #
  #-------------------------------------------------------------------#
  SPACE (1)
  BR    (14)                       # Return to caller
  SPACE (1)
  DROP  (10, 12)                   # Drop work area, local base
  SPACE (1)
  LTORG ()                         # Literals go here

  def __init__(self):
    """
    Initialize an instance of FULLER.
    """
    #print("Yo!")
    pass

class WORKAREA(DSECT):
  """
	Define a local work area for the Fuller class.
  """
  DS    ('XL4096')                 # 4K page
  ORG   ('*-4096')                 # Redefine
  SAVEAREA = DS('18F')             # Standard save area
  DS    ('0D')                     # End of work area

  def __init__(self):
    """
    Initialize work area.
    """
    self.SAVEAREA = [0x7FFFFBAD] * 18

class TestFuller(unittest.TestCase):
  """
  Test the FULLER program.
  """
  def test_fuller(self):
    """
    Assemble, load, and execute the FULLER program.
    """
    f = FULLER()
    f()
    del f
    d = WORKAREA()
    del d
