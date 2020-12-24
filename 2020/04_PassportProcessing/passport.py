# ======================================================================
# Passport Processing
#   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a s s p o r t . p y
# ======================================================================
"A passport object for the Advent of Code 2020 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
REQUIRED = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
EYE_COLOR = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
HEX_DIGITS = '0123456789abcdef'
# ======================================================================
#                                                                Scanner
# ======================================================================


class Passport(object):   # pylint: disable=R0902, R0205
    "Object of Passport Processing"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.fields = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            parts = text.split(' ')
            for part in parts:
                field, value = part.split(':')
                assert field in FIELDS
                self.fields[field] = value

    def is_valid(self):
        "Returns True if the passport has all the required fields"

        # 1. Check that the passport has the required fields
        for field in REQUIRED:
            if field not in self.fields:
                return False

        # 2. That's all you need for part 1
        if not self.part2:
            return True

        # 3. Check the years
        if not Passport.check_number(self.fields['byr'], 4, 1920, 2020):
            return False
        if not Passport.check_number(self.fields['iyr'], 4, 2010, 2020):
            return False
        if not Passport.check_number(self.fields['eyr'], 4, 2020, 2030):
            return False

        # 5. Check the height
        hgt = self.fields['hgt']
        if hgt.endswith('in'):
            num = hgt.replace('in', '')
            if not Passport.check_number(num, 2, 59, 76):
                return False
        elif hgt.endswith('cm'):
            num = hgt.replace('cm', '')
            if not Passport.check_number(num, 3, 150, 193):
                return False
        else:
            return False

        # 6. Check the hair color
        hcl = self.fields['hcl']
        if len(hcl) != 7:
            return False
        if hcl[0] != '#':
            return False
        for digit in hcl[1:]:
            if digit not in HEX_DIGITS:
                return False

        # 7. Check the eye color
        if not self.fields['ecl'] in EYE_COLOR:
            return False

        # 8. Check the passport id
        if not Passport.check_number(self.fields['pid'], 9, 0, 999999999):
            return False

        # 9. Then I guess it is good enough
        return True

    @staticmethod
    def check_number(number, length, min_num, max_num):
        "Check that the number has the correct number of digits"
        if not number.isdigit():
            return False
        if len(number) != length:
            return False
        num = int(number)
        if num < min_num:
            return False
        if num > max_num:
            return False
        return True


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      p a s s p o r t . p y                     end
# ======================================================================
