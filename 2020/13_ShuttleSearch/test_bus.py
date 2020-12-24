# ======================================================================
# Shuttle Search
#   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t e s t _ b u s . p y
# ======================================================================
"Test people mover for Advent of Code 2020 day 13, Shuttle Search"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import bus

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = [
    {'at': 929, 'bid': 7, 'departs': 931},
    {'at': 929, 'bid': 13, 'departs': 936},
    {'at': 929, 'bid': 59, 'departs': 944},
    {'at': 929, 'bid': 31, 'departs': 930},
    {'at': 929, 'bid': 19, 'departs': 931},
    {'at': 931, 'bid': 7, 'departs': 931},
    {'at': 931, 'bid': 13, 'departs': 936},
    {'at': 931, 'bid': 59, 'departs': 944},
    {'at': 931, 'bid': 19, 'departs': 931},
    {'at': 939, 'bid': 7, 'departs': 945},
    {'at': 939, 'bid': 13, 'departs': 949},
    {'at': 939, 'bid': 59, 'departs': 944},
]

# ======================================================================
#                                                              TestBus
# ======================================================================


class TestBus(unittest.TestCase):  # pylint: disable=R0904
    "Test Bus object"

    def test_empty_init(self):
        "Test the default Bus creation"

        # 1. Create default Bus object
        myobj = bus.Bus()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.bid, 0)
        self.assertEqual(myobj.offset, 0)

    def test_value_init(self):
        "Test the Bus object creation from text"

        # 1. Create Bus object from text
        myobj = bus.Bus(bid='7', offset=2)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.bid, 7)
        self.assertEqual(myobj.offset, 2)

    def test_part_one(self):
        "Test part one examples of Bus object"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Create Bus object from values
            myobj = bus.Bus(bid=example['bid'])

            # 3. Check the part one result
            self.assertEqual(myobj.next_depart_after(example['at']), example['departs'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ b u s . p y                     end
# ======================================================================
