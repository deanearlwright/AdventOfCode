
# ======================================================================
# Monkey Map
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f a c e s . p y
# ======================================================================
"Test Faces for Advent of Code 2022 day 22, Monkey Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import faces

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "4"

# ======================================================================
#                                                              TestFaces
# ======================================================================


class TestFaces(unittest.TestCase):  # pylint: disable=R0904
    "Test Faces object"

    def test_empty_init(self):
        "Test the default Faces creation"

        # 1. Create default Faces object
        myobj = faces.Faces()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.edge_len, 1)
        self.assertEqual(len(myobj.faces), 0)
        self.assertEqual(len(myobj.face_warp), 7)

    def test_text_init(self):
        "Test the Faces object creation from text"

        # 1. Create Faces object from text
        myobj = faces.Faces(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.edge_len, 4)
        self.assertEqual(len(myobj.faces), 7)
        self.assertEqual(len(myobj.face_warp), 7)
        self.assertEqual(myobj.faces[0], None)
        self.assertEqual(myobj.faces[1],
                         faces.Face(number=1,
                                    min_col=9, max_col=12,
                                    min_row=1, max_row=4))
        self.assertEqual(myobj.faces[2],
                         faces.Face(number=2,
                                    min_col=1, max_col=4,
                                    min_row=5, max_row=8))
        self.assertEqual(myobj.faces[3],
                         faces.Face(number=3,
                                    min_col=5, max_col=8,
                                    min_row=5, max_row=8))
        self.assertEqual(myobj.faces[4],
                         faces.Face(number=4,
                                    min_col=9, max_col=12,
                                    min_row=5, max_row=8))
        self.assertEqual(myobj.faces[5],
                         faces.Face(number=5,
                                    min_col=9, max_col=12,
                                    min_row=9, max_row=12))
        self.assertEqual(myobj.faces[6],
                         faces.Face(number=6,
                                    min_col=13, max_col=16,
                                    min_row=9, max_row=12))

        # 3. Check methods
        self.assertEqual(myobj.on_face(faces.Loc(col=0, row=0)), 0)
        self.assertEqual(myobj.on_face(faces.Loc(col=10, row=2)), 1)
        self.assertEqual(myobj.on_face(faces.Loc(col=4, row=6)), 2)
        self.assertEqual(myobj.on_face(faces.Loc(col=5, row=6)), 3)
        self.assertEqual(myobj.on_face(faces.Loc(col=12, row=6)), 4)
        self.assertEqual(myobj.on_face(faces.Loc(col=13, row=6)), 0)
        self.assertEqual(myobj.on_face(faces.Loc(col=12, row=9)), 5)
        self.assertEqual(myobj.on_face(faces.Loc(col=13, row=9)), 6)
        self.assertEqual(myobj.on_face(faces.Loc(col=13, row=16)), 0)

        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=2), '<'),
                         ((12, 2), '<'))    # 1 to 1 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=12, row=3), '>'),
                         ((9, 3), '>'))     # 1 to 1 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=1), '^'),
                         ((9, 12), '^'))    # 1 to 5 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=10, row=12), 'v'),
                         ((10, 1), 'v'))    # 5 to 1 v
        self.assertEqual(myobj.warp_to(faces.Loc(col=2, row=8), 'v'),
                         ((2, 5), 'v'))     # 2 to 2 v
        self.assertEqual(myobj.warp_to(faces.Loc(col=2, row=5), '^'),
                         ((2, 8), '^'))     # 2 to 2 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=4, row=8), 'v'),
                         ((4, 5), 'v'))     # 3 to 2 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=4, row=5), '^'),
                         ((4, 8), '^'))     # 3 to 3 v
        self.assertEqual(myobj.warp_to(faces.Loc(col=13, row=12), 'v'),
                         ((13, 9), 'v'))    # 6 to 6 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=14, row=9), '^'),
                         ((14, 12), '^'))   # 6 to 6 v
        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=2), '<'),
                         ((12, 2), '<'))    # 1 to 1 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=12, row=3), '>'),
                         ((9, 3), '>'))     # 1 to 1 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=12, row=6), '>'),
                         ((1, 6), '>'))     # 4 to 2 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=1, row=7), '<'),
                         ((12, 7), '<'))    # 2 to 4 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=16, row=10), '>'),
                         ((9, 10), '>'))    # 6 to 5 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=11), '<'),
                         ((16, 11), '<'))   # 5 to 6 <

    def test_text_two(self):
        "Test the Faces object creation from text for part two"

        # 1. Create Faces object from text
        myobj = faces.Faces(text=EXAMPLE_TEXT, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.edge_len, 4)
        self.assertEqual(len(myobj.faces), 7)
        self.assertEqual(len(myobj.face_warp), 7)
        self.assertEqual(myobj.faces[0], None)
        self.assertEqual(myobj.faces[1],
                         faces.Face(number=1,
                                    min_col=9, max_col=12,
                                    min_row=1, max_row=4))
        self.assertEqual(myobj.faces[2],
                         faces.Face(number=2,
                                    min_col=1, max_col=4,
                                    min_row=5, max_row=8))
        self.assertEqual(myobj.faces[3],
                         faces.Face(number=3,
                                    min_col=5, max_col=8,
                                    min_row=5, max_row=8))
        self.assertEqual(myobj.faces[4],
                         faces.Face(number=4,
                                    min_col=9, max_col=12,
                                    min_row=5, max_row=8))
        self.assertEqual(myobj.faces[5],
                         faces.Face(number=5,
                                    min_col=9, max_col=12,
                                    min_row=9, max_row=12))
        self.assertEqual(myobj.faces[6],
                         faces.Face(number=6,
                                    min_col=13, max_col=16,
                                    min_row=9, max_row=12))

        # 3. Check methods
        self.assertEqual(myobj.on_face(faces.Loc(col=0, row=0)), 0)
        self.assertEqual(myobj.on_face(faces.Loc(col=10, row=2)), 1)
        self.assertEqual(myobj.on_face(faces.Loc(col=4, row=6)), 2)
        self.assertEqual(myobj.on_face(faces.Loc(col=5, row=6)), 3)
        self.assertEqual(myobj.on_face(faces.Loc(col=12, row=6)), 4)
        self.assertEqual(myobj.on_face(faces.Loc(col=13, row=6)), 0)
        self.assertEqual(myobj.on_face(faces.Loc(col=12, row=9)), 5)
        self.assertEqual(myobj.on_face(faces.Loc(col=13, row=9)), 6)
        self.assertEqual(myobj.on_face(faces.Loc(col=13, row=16)), 0)

        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=2), '<'),
                         ((6, 5), 'v'))     # 1 to 3 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=12, row=3), '>'),
                         ((16, 10), '<'))   # 1 to 6 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=1), '^'),
                         ((4, 5), 'v'))     # 1 to 2 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=10, row=4), 'v'),
                         ((10, 5), 'v'))    # 1 to 4 v

        self.assertEqual(myobj.warp_to(faces.Loc(col=1, row=8), '<'),
                         ((13, 12), '^'))   # 2 to 6 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=4, row=6), '>'),
                         ((5, 6), '>'))     # 2 to 3 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=2, row=5), '^'),
                         ((11, 1), 'v'))    # 2 to 1 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=2, row=8), 'v'),
                         ((11, 12), '^'))   # 2 to 5 v

        self.assertEqual(myobj.warp_to(faces.Loc(col=8, row=7), '>'),
                         ((9, 7), '>'))     # 3 to 4 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=5, row=5), '<'),
                         ((4, 5), '<'))     # 3 to 2 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=7, row=5), '^'),
                         ((9, 3), '>'))     # 3 to 1 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=5, row=8), 'v'),
                         ((9, 12), '>'))    # 3 to 5 v

        self.assertEqual(myobj.warp_to(faces.Loc(col=12, row=6), '>'),
                         ((15, 9), 'v'))    # 4 to 6 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=7), '<'),
                         ((8, 7), '<'))     # 4 to 3 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=11, row=5), '^'),
                         ((11, 4), '^'))    # 4 to 1 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=10, row=8), 'v'),
                         ((10, 9), 'v'))    # 4 to 5 v

        self.assertEqual(myobj.warp_to(faces.Loc(col=12, row=11), '>'),
                         ((13, 11), '>'))   # 5 to 6 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=9, row=10), '<'),
                         ((7, 8), '^'))     # 5 to 3 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=11, row=9), '^'),
                         ((11, 8), '^'))    # 5 to 4 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=10, row=12), 'v'),
                         ((3, 8), '^'))     # 5 to 2 v

        self.assertEqual(myobj.warp_to(faces.Loc(col=16, row=11), '>'),
                         ((12, 2), '<'))    # 6 to 1 >
        self.assertEqual(myobj.warp_to(faces.Loc(col=13, row=10), '<'),
                         ((12, 10), '<'))   # 6 to 5 <
        self.assertEqual(myobj.warp_to(faces.Loc(col=15, row=9), '^'),
                         ((12, 6), '<'))     # 6 to 4 ^
        self.assertEqual(myobj.warp_to(faces.Loc(col=14, row=12), 'v'),
                         ((1, 7), '>'))     # 6 to 2 v


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ f a c e s . p y                    end
# ======================================================================
