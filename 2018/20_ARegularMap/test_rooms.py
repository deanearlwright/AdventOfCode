# ======================================================================
# A Regular Map
#   Advent of Code 2018 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o o m s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 20, A Regular Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import rooms
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
^WNE$
"""

EXAMPLE_STR = """
#####
#.|.#
#-###
#.|X#
#####
"""
EXAMPLE_TWO_TEXT = """
 ^ENWWW(NEEE|SSE(EE|N))$

 """


EXAMPLE_TWO_STR = """
#########
#.|.|.|.#
#-#######
#.|.|.|.#
#-#####-#
#.#.#X|.#
#-#-#####
#.|.|.|.#
#########
"""

EXAMPLE_THREE_TEXT = """
^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$
"""

EXAMPLE_THREE_STR = """
###########
#.|.#.|.#.#
#-###-#-#-#
#.|.|.#.#.#
#-#####-#-#
#.#.#X|.#.#
#-#-#####-#
#.#.|.|.|.#
#-###-###-#
#.|.|.#.|.#
###########
"""

EXAMPLE_FOUR_TEXT = """
^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""

EXAMPLE_FOUR_STR = """
#############
#.|.|.|.|.|.#
#-#####-###-#
#.#.|.#.#.#.#
#-#-###-#-#-#
#.#.#.|.#.|.#
#-#-#-#####-#
#.#.#.#X|.#.#
#-#-#-###-#-#
#.|.#.|.#.#.#
###-#-###-#-#
#.|.#.|.|.#.#
#############"""


EXAMPLE_FIVE_TEXT = """
^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""

EXAMPLE_FIVE_STR = """
###############
#.|.|.|.#.|.|.#
#-###-###-#-#-#
#.|.#.|.|.#.#.#
#-#########-#-#
#.#.|.|.|.|.#.#
#-#-#########-#
#.#.#.|X#.|.#.#
###-#-###-#-#-#
#.|.#.#.|.#.|.#
#-###-#####-###
#.|.#.|.|.#.#.#
#-#-#####-#-#-#
#.#.|.|.|.#.|.#
###############"""

EXAMPLES = [
    {
        'text': EXAMPLE_TEXT,
        'str': EXAMPLE_STR,
        'doors': 3,
    },
    {
        'text': EXAMPLE_TWO_TEXT,
        'str': EXAMPLE_TWO_STR,
        'doors': 10,
    },
    {
        'text': EXAMPLE_THREE_TEXT,
        'str': EXAMPLE_THREE_STR,
        'doors': 18,
    },
    {
        'text': EXAMPLE_FOUR_TEXT,
        'str': EXAMPLE_FOUR_STR,
        'doors': 23,
    },
    {
        'text': EXAMPLE_FIVE_TEXT,
        'str': EXAMPLE_FIVE_STR,
        'doors': 31,
    },
    ]


PART_ONE_TEXT = EXAMPLE_FIVE_TEXT
PART_TWO_TEXT = ''

PART_ONE_RESULT = 31
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestRooms
# ======================================================================


class TestRooms(unittest.TestCase):  # pylint: disable=R0904
    "Test Rooms object"

    def test_empty_init(self):
        "Test the default Rooms creation"

        # 1. Create default Rooms object
        myobj = rooms.Rooms()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.regex, None)
        self.assertEqual(myobj.doors, None)

    def test_text_init(self):
        "Test the Rooms object creation from text"

        # 1. Create Rooms object from text
        myobj = rooms.Rooms(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.regex, EXAMPLE_TEXT.strip())
        self.assertEqual(len(myobj.doors), 3 * 2)
        dims = myobj.dimensions()
        self.assertEqual(dims['N'], -1)
        self.assertEqual(dims['S'], 0)
        self.assertEqual(dims['E'], 0)
        self.assertEqual(dims['W'], -1)
        self.assertEqual(str(myobj), EXAMPLE_STR.strip())

    def test_example_two(self):
        "Test the Rooms object creation from text"

        # 1. Create Rooms object from text
        myobj = rooms.Rooms(text=aoc_20.from_text(EXAMPLE_TWO_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.regex, EXAMPLE_TWO_TEXT.strip())
        self.assertEqual(len(myobj.doors), 15 * 2)
        dims = myobj.dimensions()
        self.assertEqual(dims['N'], -2)
        self.assertEqual(dims['S'], 1)
        self.assertEqual(dims['E'], 1)
        self.assertEqual(dims['W'], -2)
        self.assertEqual(str(myobj), EXAMPLE_TWO_STR.strip())

    def test_examples(self):
        "Test all of the examples"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Created the Rooms object from text
            myobj = rooms.Rooms(text=aoc_20.from_text(example['text']))
            self.assertEqual(myobj.regex, example['text'].strip())

            # 3. Check the map
            self.assertEqual(str(myobj), example['str'].strip())

            # 4. Check the doors
            mypath = path.Path(start=rooms.START, doors=myobj.doors)
            self.assertEqual(mypath.furthest(), example['doors'])


    def test_part_one(self):
        "Test part one example of Rooms object"

        # 1. Create Rooms object from text
        myobj = rooms.Rooms(text=aoc_20.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Rooms object"

        # 1. Create Rooms object from text
        myobj = rooms.Rooms(part2=True, text=aoc_20.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r o o m s . p y                  end
# ======================================================================
