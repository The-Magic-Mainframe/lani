"""iebiball.py - An implementation of the IEBIBALL system utility for z/OS."""

import unittest

from ..core import *
from .console import *

class IEBIBALL(RSECT):
  """
  https://www.etsy.com/listing/1535332741/iebiball-black-glossy-mug
  """
  WTO('Message 1')
  WTO('Message 2')
  WTO('Message 3')

  def __init__(self, messages=[]):
    """
    Initialize an instance of IEBIBALL.
    """
    self.messages = messages

class Tests(unittest.TestCase):
  """
  Test the IEBIBALL program.
  """
  messages = [
    # 24 July, 2024 - 12:18pm CDT
    ":wave:",
    "Nothing.",
    "I was going to complain about some behavior on this discord "
    "server that I perceived as toxic, but I'm probably just overly "
    "sensitive. I really despise the mainframe community sometimes.",
    "I'm not even complaining about the one message, it was the "
    "\"I'm an expert and I know everything and I'm not going to explain "
    "it to you unless you ask the right questions\" attitude.",
    # 4 November, 2024 - 3:15pm CST
    "Hey, are you still looking for volunteers to help moderate "
    "the SZE server? Just wanted to express my interest.",
    "My experience is that I used to be a wikipedia administrator",
    "Lol",
    "Sick",
    ":sweat:",
    "Get well soon!!",
    "I had an awesome time at re:ipl",
    "Like it was honestly the highlight of going to share",
    ":smiling_face_with_3_hearts",
    # 7 January, 2025 - 1:41pm CST
    "I keep thinking someone posted porn in the zos channel lmfao",
    "we??",
    "crowdsourced discord administration",
    "put it in a wow game",
    "brann your task is to administer this server",
    '"no"',
    "I haven't played since cata",
    "I'd love to play vanilla again",
    "I loved getting destroyed by deathwing in random zones",
    "Oh  man, it's been ages. I can't remember, honestly. I raided "
    "in WOTLK but only a little bit in cata.",
    "damn! you lasted a lot longer than me",
    "I ended up switching from WoW to FF14 shortly after college "
    "and that became my main mmo for a long time",
    "then I had kids",
    "that's incredible!!",
    "so you have experience leading online communities",
    "I really admire that",
    "I'm glad you recognized that",
    "All",
    "Human warrior was main",
    "Alliance",
    "so lame",
    "haha",
    "I tanked",
    "Mine was Redcap with an umlaut on the a",
    "I really loved playing resto druid",
    "And an alteration(?) shman named Roxanne",
    "i wonder she's doing now",
    "I got locked out of my account and I've been putting off recovering "
    "for years",
    "Probably will end up creating a new one if I ever get back into it",
    "how big is your screenshot folder?",
    "BRO",
    "Let me see if I can find my characters",
    "I played on <redacted> mainly"
  ]

  def test_fuller(self):
    """
    Assemble, load, and execute the IEBIBALL.
    """
    f = IEBIBALL(self.messages)
    f()
