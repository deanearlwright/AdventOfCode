# ======================================================================
# Balance Bots
#   Advent of Code 2016 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b o t . p y
# ======================================================================
"Test Bot for Advent of Code 2016 day 10, Balance Bots"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import bot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_GOES = "value 5 goes to bot 2"
EXAMPLE_RULE = "bot 2 gives low to bot 1 and high to bot 0"

# ======================================================================
#                                                             TestBot
# ======================================================================


class TestBot(unittest.TestCase):  # pylint: disable=R0904
    "Test Bot object"

    def test_empty_init(self):
        "Test the default Bot creation"

        # 1. Create default Bot object
        myobj = bot.Bot()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, None)
        self.assertEqual(myobj.chips, [])
        self.assertEqual(myobj.low, None)
        self.assertEqual(myobj.high, None)

    def test_text_goes(self):
        "Test the Bot object creation from goes"

        # 1. Create Bots object from text
        myobj = bot.Bot(text=EXAMPLE_GOES)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 21)
        self.assertEqual(myobj.number, 2)
        self.assertEqual(myobj.chips, [5])
        self.assertEqual(myobj.low, None)
        self.assertEqual(myobj.high, None)

    def test_text_rule(self):
        "Test the Bot object creation from rule"

        # 1. Create Bots object from text
        myobj = bot.Bot(text=EXAMPLE_RULE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 42)
        self.assertEqual(myobj.number, 2)
        self.assertEqual(myobj.chips, [])
        self.assertEqual(myobj.low, 1)
        self.assertEqual(myobj.high, 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ b o t . p y                end
# ======================================================================
