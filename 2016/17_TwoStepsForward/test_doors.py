# ======================================================================
# Two Steps Forward
#   Advent of Code 2016 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ d o o r s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 17, Two Steps Forward"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import doors

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
ihgpwlah
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "DDRRRD"
PART_TWO_RESULT = 370

# ======================================================================
#                                                              TestDoors
# ======================================================================


class TestUtility(unittest.TestCase):  # pylint: disable=R0904
    "Test utility functions"

    def test_mdr_hash(self):
        "Check the mdr hashing"
        self.assertEqual(doors.md5_hash("hijkl")[:4], "ced9")
        self.assertEqual(doors.md5_hash("hijklD")[:4], "f2bc")
        self.assertEqual(doors.md5_hash("hijklDR")[:4], "5745")
        self.assertEqual(doors.md5_hash("hijklDU")[:4], "528e")

    def test_is_unlocked(self):
        "Check the door locking"
        self.assertEqual(doors.is_unlocked("0"), False)
        self.assertEqual(doors.is_unlocked("1"), False)
        self.assertEqual(doors.is_unlocked("2"), False)
        self.assertEqual(doors.is_unlocked("3"), False)
        self.assertEqual(doors.is_unlocked("4"), False)
        self.assertEqual(doors.is_unlocked("5"), False)
        self.assertEqual(doors.is_unlocked("6"), False)
        self.assertEqual(doors.is_unlocked("7"), False)
        self.assertEqual(doors.is_unlocked("8"), False)
        self.assertEqual(doors.is_unlocked("9"), False)
        self.assertEqual(doors.is_unlocked("a"), False)
        self.assertEqual(doors.is_unlocked("b"), True)
        self.assertEqual(doors.is_unlocked("c"), True)
        self.assertEqual(doors.is_unlocked("d"), True)
        self.assertEqual(doors.is_unlocked("e"), True)
        self.assertEqual(doors.is_unlocked("f"), True)

    def test_doors_unlocked(self):
        "Check the unlocked doors"
        self.assertEqual(doors.unlocked("hijkl"), "UDL")
        self.assertEqual(doors.unlocked("hijklD"), "ULR")
        self.assertEqual(doors.unlocked("hijklDR"), "")
        self.assertEqual(doors.unlocked("hijklDU"), "R")

    def test_is_wall(self):
        "Check for walls"
        self.assertEqual(doors.is_wall((0, 0), "U"), True)
        self.assertEqual(doors.is_wall((0, 0), "D"), False)
        self.assertEqual(doors.is_wall((0, 0), "L"), True)
        self.assertEqual(doors.is_wall((0, 0), "R"), False)
        self.assertEqual(doors.is_wall((0, 3), "U"), False)
        self.assertEqual(doors.is_wall((0, 3), "D"), True)
        self.assertEqual(doors.is_wall((0, 3), "L"), True)
        self.assertEqual(doors.is_wall((0, 3), "R"), False)
        self.assertEqual(doors.is_wall((1, 1), "U"), False)
        self.assertEqual(doors.is_wall((1, 1), "D"), False)
        self.assertEqual(doors.is_wall((1, 1), "L"), False)
        self.assertEqual(doors.is_wall((1, 1), "R"), False)
        self.assertEqual(doors.is_wall((3, 0), "U"), True)
        self.assertEqual(doors.is_wall((3, 0), "D"), False)
        self.assertEqual(doors.is_wall((3, 0), "L"), False)
        self.assertEqual(doors.is_wall((3, 0), "R"), True)
        self.assertEqual(doors.is_wall((3, 3), "U"), False)
        self.assertEqual(doors.is_wall((3, 3), "D"), True)
        self.assertEqual(doors.is_wall((3, 3), "L"), False)
        self.assertEqual(doors.is_wall((3, 3), "R"), True)

    def test_is_vault(self):
        "Check for the valult"
        self.assertEqual(doors.is_vault((0, 0)), False)
        self.assertEqual(doors.is_vault((1, 1)), False)
        self.assertEqual(doors.is_vault((1, 3)), False)
        self.assertEqual(doors.is_vault((3, 3)), True)

    def test_exits(self):
        "Check the unlocked doors that are not walls"
        self.assertEqual(doors.exits((0, 0), "hijkl"), "D")
        self.assertEqual(doors.exits((0, 1), "hijklD"), "UR")
        self.assertEqual(doors.exits((1, 1), "hijklDR"), "")
        self.assertEqual(doors.exits((0, 0), "hijklDU"), "R")


class TestDoors(unittest.TestCase):  # pylint: disable=R0904
    "Test Doors object"

    def test_empty_init(self):
        "Test the default Doors creation"

        # 1. Create default Doors object
        myobj = doors.Doors()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.seed, None)

    def test_text_init(self):
        "Test the Doors object creation from text"

        # 1. Create Doors object from text
        myobj = doors.Doors(text=aoc_17.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.seed, "ihgpwlah")

        # 3. Check methods
        self.assertEqual(myobj.shortest(), "DDRRRD")
        self.assertEqual(myobj.longest(), 370)

    def test_shortest(self):
        "Test the shortest path"
        self.assertEqual(doors.Doors(["ihgpwlah"]).shortest(), "DDRRRD")
        self.assertEqual(doors.Doors(["kglvqrro"]).shortest(), "DDUDRLRRUDRD")
        self.assertEqual(doors.Doors(["ulqzkmiv"]).shortest(), "DRURDRUDDLLDLUURRDULRLDUUDDDRR")

    def test_longest(self):
        "Test the longest path"
        self.assertEqual(doors.Doors(["ihgpwlah"]).longest(), 370)
        self.assertEqual(doors.Doors(["kglvqrro"]).longest(), 492)
        self.assertEqual(doors.Doors(["ulqzkmiv"]).longest(), 830)

    def test_part_one(self):
        "Test part one example of Doors object"

        # 1. Create Doors object from text
        myobj = doors.Doors(text=aoc_17.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Doors object"

        # 1. Create Doors object from text
        myobj = doors.Doors(part2=True, text=aoc_17.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ d o o r s . p y                   end
# ======================================================================
