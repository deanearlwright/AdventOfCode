
# ======================================================================
# Proboscidea Volcanium
#   Advent of Code 2022 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a l v e s . p y
# ======================================================================
"Test Valves for Advent of Code 2022 day 16, Proboscidea Volcanium"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import valves

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II",
]


# ======================================================================
#                                                             TestValves
# ======================================================================


class TestValves(unittest.TestCase):  # pylint: disable=R0904
    "Test Valves object"

    def test_empty_init(self):
        "Test the default Valves creation"

        # 1. Create default Valves object
        myobj = valves.Valves()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.valves), 0)
        self.assertEqual(len(myobj.numbers), 0)
        self.assertEqual(myobj.max_rate, 0)
        self.assertEqual(myobj.max_number, 0)
        self.assertEqual(myobj.closed_mask, 0)
        self.assertEqual(len(myobj.working), 0)
        self.assertEqual(myobj.working_mask, 0)

    def test_text_init(self):
        "Test the Valves object creation from text"

        # 1. Create Valves object from text
        myobj = valves.Valves(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.valves), 10)
        self.assertEqual(len(myobj.numbers), 10)
        self.assertEqual(myobj.max_rate, 81)
        self.assertEqual(myobj.max_number, 1024)
        self.assertEqual(myobj.closed_mask, 2047)
        self.assertEqual(len(myobj.working), 6)
        self.assertEqual(myobj.working_mask, 670)

        # 3. Check methods
        self.assertEqual(myobj.loc_to_number("AA"), 1)
        self.assertEqual(myobj.loc_to_number("BB"), 2)
        self.assertEqual(myobj.loc_to_number("CC"), 4)
        self.assertEqual(myobj.number_to_loc(1), "AA")
        self.assertEqual(myobj.number_to_loc(2), "BB")
        self.assertEqual(myobj.number_to_loc(4), "CC")
        self.assertEqual(myobj.show_open(0), ("", 0))
        self.assertEqual(myobj.show_open(1), ("AA", 0))
        self.assertEqual(myobj.show_open(8), ("DD", 20))
        self.assertEqual(myobj.show_open(520), ("DD,JJ", 41))
        self.assertEqual(myobj.show_open(1023),
                         ("AA,BB,CC,DD,EE,FF,GG,HH,II,JJ", 81))
        self.assertEqual(myobj.show_open(myobj.closed(0)),
                         ("AA,BB,CC,DD,EE,FF,GG,HH,II,JJ", 81))
        self.assertEqual(myobj.show_open(myobj.closed(520)),
                         ("AA,BB,CC,EE,FF,GG,HH,II", 40))
        self.assertEqual(myobj.show_open(myobj.closed(520)),
                         ("AA,BB,CC,EE,FF,GG,HH,II", 40))
        self.assertEqual(myobj.can_open(520), "BB,CC,EE,HH")
        self.assertEqual(myobj.steps["AA"]["BB"], 1)
        self.assertEqual(myobj.steps["AA"]["JJ"], 2)
        self.assertEqual(myobj.steps["GG"]["JJ"], 6)
        self.assertEqual(myobj.most_additional_pressure(10, 520, "AA"), 267)
        self.assertEqual(myobj.most_additional_pressure(4, 520, "AA"), 49)
        self.assertEqual(myobj.most_additional_pressure(1, 520, "AA"), 0)
        self.assertEqual(myobj.is_valve_closed("AA", 0), True)
        self.assertEqual(myobj.is_valve_closed("AA", 1024), True)
        self.assertEqual(myobj.is_valve_closed("AA", 1), False)
        self.assertEqual(myobj.are_all_opened(0), False)
        self.assertEqual(myobj.are_all_opened(1234), False)
        self.assertEqual(myobj.are_all_opened(2047), True)
        self.assertEqual(myobj.are_all_opened(670), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ v a l v e s . p y                  end
# ======================================================================
