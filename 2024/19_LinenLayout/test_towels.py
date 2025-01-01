
# ======================================================================
# Linen Layout
#   Advent of Code 2024 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t o w e l s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 19, Linen Layout"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import towels

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

GOOD_DESIGNS = ["brwrr", "bggr", "gbbr", "rrbgbr", "bwurrg", "brgr"]
BAD_DESIGNS = ["ubwu", "bbrgwb"]
WAYS_DESIGNS = {
    "brwrr": 2,
    "bggr": 1,
    "gbbr": 4,
    "rrbgbr": 6,
    "bwurrg": 1,
    "brgr": 2,
    "ubwu": 0,
    "bbrgwb": 0}


PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 6
PART_TWO_RESULT = 16

INPUT_TEXT = """
guwgbuug, bubbb, grw, wwrbbgug, wrruwb, wgw, wgubbrwu, rrgb, gbrr, gbbgb, rrr, grbrgrur, bgrrub, uubrbwwr, ubwug, rgggg, gwggb, rruwbbbw, uubr, gugwwru, rwru, bgg, rrbgug, brgrw, brwwgrg, ubrrb, wugb, ggrg, buu, bwu, urru, rguw, uuwu, wbr, wuw, rwubww, uwgggb, gbb, guubur, ruw, bwwgrbur, bbbrbbbw, wbrbg, rwgrw, bwgb, uwubwug, bur, bbuwgbug, uurw, rwwbrr, ggur, ugr, wwu, uwbwbu, brg, bw, urg, ubwgguu, wwbuwug, bbgbw, ubrgu, wub, rruur, ggg, rgwgr, wgrrg, wwbr, gbgbru, uuugru, ggbwrbw, rbbrg, bgwrb, rgrgubb, wwbug, wrrrwbwr, b, gurb, rurwg, wuwb, rrw, rbub, gwr, bwr, wuwuwbw, uugb, ugggu, gw, ugubbw, wurwwr, ubw, bbw, brugru, wuwuu, buruw, rwrru, wwurubr, gwu, ugrr, wuu, wgbgg, ugrw, bwgbwu, rwuu, uwbb, bgggr, wwgbu, uwgwwuwr, bwb, gwrwg, wbrb, bgbuug, gwwwgb, uwu, ggr, ubuguu, gbuurb, ugbuu, wrbgww, rrbugug, ruru, rruwr, guug, rwb, gbwurg, uuurgwwg, ruwrb, gbg, guur, gwb, gb, uwwbrb, gww, ggbwrg, grr, uubu, urbb, ugu, ggwb, buurw, bgr, rbw, uwr, urw, bgugrrg, rguuwb, wrggg, brw, urgbbw, wwrb, bgrw, ugug, brrbbb, wbwwuu, bbbu, bww, wrg, bwbgu, rgu, urrwr, gugwu, rrub, buw, ubb, rrgu, ubu, grrug, ubugbrb, uruub, gwwrg, ugg, wuuuurr, bubwwu, gbr, rwgurw, wrw, uruw, rbr, grgb, wwg, rr, ugrb, rgb, ggrw, wg, wrgwrw, rgwb, rbb, rgw, bwgw, gggg, ruu, grww, rgur, gwuu, rwwg, bwgwr, rg, bgrgu, bu, uru, ubg, gur, ubbur, rb, ggwuugw, gg, wruu, wbb, gwrrgr, bgb, bug, ruuub, ug, brr, uwg, urgub, rwu, wubr, bbbbur, bg, rub, wgu, bbwbbgw, uur, bbb, rwr, g, wbwb, urgrurgr, wgg, wbgug, ugbbb, bbr, uug, rgg, gguub, bgwg, rwurubgw, wwuwu, ubgr, bbu, bgww, uuu, bgugugg, wbbruwug, rwgg, uuurb, bwubw, bb, urrbb, grbbbb, buru, gbbg, wruuw, wwbwug, urwbrbwg, gwrb, rgug, bru, wrrbwrg, www, rur, gggw, wwgwww, grb, rgwg, wgur, wwrwrr, gru, grwug, bwuw, rru, wuruw, guw, uu, brrbgg, ggrr, ww, bwbbrw, ururgrwb, wu, rwbg, gbw, wgr, rgru, gbrg, wbub, ggb, brww, ggu, brwgu, bbwbrrg, gbwgrub, rgr, gubwrb, rbgg, rrbu, rbrw, guuuub, bwwwb, uwggww, rrg, wwwub, rrwwu, rbbr, ur, rubrurg, brb, rrwubww, rrwru, gbru, u, wr, ruwu, uruuggg, gu, uubwg, bggr, wurggw, uuwwurb, rurbuuu, wbu, gug, bbuw, urrubb, bugwrwr, urb, bggbb, ugrrrg, ugwwgg, rwg, wwrwbb, wbg, rrbrg, uwuw, rug, ugrwgbw, gwbgu, rgubbw, wbw, gwww, brruu, gwgw, uugbrub, gwwruwr, rbg, gwwwg, ru, grg, wwurg, uubbb, ugw, gruwr, uubg, gubw, wru, rwwwg, urrgwg, ugb, wbbbuug, urgrrur, ugwwguw, w, uww, urrwwu, bwgr, ugbbbwg, uub, urbww, uwwb, gubrub, uwrg, urr, gwru, uugg, uwb, uuwb, burbbu, wb, uurr, gubuu, uwuu, rbwu, wrr, wwrub, bbg, brgrb, ggw, rbu, wwbburur, wrggbwww, gbu, ugrbrr, ruurrwgu, grwrwb, uwruru, uuw, guu, gbur, ub, gbwwg, wguu, gr, ubuubr, uwgu, bub, rbwgruu, wbwrgrr, ururu, bwg, rbggg, gbubrw, wrb, buwbr, grrr, gwgbu, buug, rbrbrwg, bruurrb, brrw, ubbb, wwr, rw, bwbw, grrb, wrwbuu, ruuugru, wgwwgwg, wwb, urbw, rbrwbb, uwub, gbugg, gwbr, rwrrb, urwruuw, buuwg, rww, guburw, bggubg, wug, urggbr, rrwwg, bgw, gwg, ubrgwur, gub

ubwwwrggbwwwburgrwbugggubwrgwwrwuwwgrbrgwuwwurwrggrbggubr
ruwbwwgrgrwwwgwrgrrbrrurrwggrgrbrururgwruw
gbguggwwuggbubugbugurwbuwbuggwgrbrrbugrburggubr
uwgrrbggugrurrruugrgwrwgubrwrgggwrrrbbbruwb
"""
# ======================================================================
#                                                             TestTowels
# ======================================================================


class TestTowels(unittest.TestCase):  # pylint: disable=R0904
    "Test Towels object"

    def test_empty_init(self):
        "Test the default Towels creation"

        # 1. Create default Towels object
        myobj = towels.Towels()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.available), 0)
        self.assertEqual(len(myobj.designs), 0)

    def test_text_init(self):
        "Test the Towels object creation from text"

        # 1. Create Towels object from text
        myobj = towels.Towels(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.available), 4)
        self.assertEqual(len(myobj.designs), 8)

        # 3. Check methods
        self.assertEqual(len(myobj.possible_start("brwrr")), 2)
        self.assertEqual(len(myobj.possible_start("xxx")), 0)

        self.assertTrue(myobj.possible("brwrr"))
        for design in GOOD_DESIGNS:
            self.assertTrue(myobj.possible(design))
        for design in BAD_DESIGNS:
            self.assertFalse(myobj.possible(design))

        self.assertEqual(myobj.count_possible(), 6)

        self.assertEqual(myobj.count_ways(), 16)

    def test_text_input(self):
        "Test the Towels object creation from the input.txt text"

        # 1. Create Towels object from text
        myobj = towels.Towels(text=aoc_19.from_text(INPUT_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.available), 5)
        self.assertEqual(len(myobj.designs), 4)

        # 3. Check methods
        self.assertEqual(len(myobj.possible_start(myobj.designs[0])), 3)

        self.assertFalse(myobj.possible(myobj.designs[0]))

        self.assertEqual(myobj.count_possible(), 2)

    def test_part_one(self):
        "Test part one example of Towels object"

        # 1. Create Towels object from text
        text = aoc_19.from_text(PART_ONE_TEXT)
        myobj = towels.Towels(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Towels object"

        # 1. Create Towels object from text
        text = aoc_19.from_text(PART_TWO_TEXT)
        myobj = towels.Towels(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ t o w e l s . p y                  end
# ======================================================================
