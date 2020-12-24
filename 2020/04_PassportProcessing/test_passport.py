# ======================================================================
# Passport Processing
#   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a s s p o r t . p y
# ======================================================================
"Test passport for Advent of Code 2020 day 04, Passport Processing"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import passport

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
EXAMPLES = [
    {'text': "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", 'result': True},
    {'text': "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929", 'result': False},
    {'text': "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm", 'result': True},
    {'text': "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in", 'result': False},
]

# ======================================================================
#                                                           TestPassport
# ======================================================================


class TestPassport(unittest.TestCase):  # pylint: disable=R0904
    "Test Passport object"

    def test_empty_init(self):
        "Test the default Passport creation"

        # 1. Create default Passport object
        myobj = passport.Passport()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.fields.keys()), 0)

    def test_text_init(self):
        "Test the Passport object creation from text"

        # 1. Create Passport object from text
        myobj = passport.Passport(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.fields.keys()), 8)
        self.assertEqual('ecl' in myobj.fields, True)
        self.assertEqual('hgt' in myobj.fields, True)

        # 3. Check methods
        self.assertEqual(myobj.is_valid(), True)

    def test_examples(self):
        "Test the Passport object using the problem examples"

        # 1. Loop for all of the examples
        for example in EXAMPLES:
            print(example)

            # 2. Build the passport object
            myobj = passport.Passport(text=example['text'])

            # 3. Check if the passport is valid
            self.assertEqual(myobj.is_valid(), example['result'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ p a s s p o r t . p y                end
# ======================================================================
