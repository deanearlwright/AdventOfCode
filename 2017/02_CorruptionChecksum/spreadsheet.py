# ======================================================================
# Corruption Checksum
#   Advent of Code 2017 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      s p r e a d s h e e t . p y
# ======================================================================
"A spreadsheet for Corruption Checksum for Advent of Code 2017 Day 01"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            Spreadsheet
# ======================================================================


class Spreadsheet():
    """Object representing a Captcha solver"""

    def __init__(self, part2=False, text=None):

        # 1. Set the initial values
        self.text = text
        self.part2 = part2

    def checksum(self, verbose=False):
        "Generate the checksum for the spreadsheet"

        # 1. If we have nothing, that's what you get.
        if self.text is None:
            return None

        # 2. Start the checksum with nothing
        chk_sum = 0

        # 3. Loop for all of the row of the text
        for rnum, row in enumerate(self.text):

            # 4. Get the number in the row
            row_int = [int(_) for _ in row.split()]

            # 5. Part one or part 2
            if not self.part2:

                # 6. part1: row checksom is diff between min and max
                row_min = min(row_int)
                row_max = max(row_int)
                row_chk = row_max - row_min
                if verbose:
                    print("For row %d, min=%d, max=%d, diff=%d" %
                          (rnum, row_min, row_max, row_chk))
            else:
                # 7. Part 2: row checksum is common divisor of two numbers
                row_chk = 0
                for cnum, num1 in enumerate(row_int[:-1]):
                    for num2 in row_int[cnum+1:]:
                        if num1 % num2 == 0:
                            row_chk = num1 // num2
                        elif num2 % num1 == 0:
                            row_chk = num2 // num1
                if verbose:
                    print("For row %d, chk=%d" %
                          (rnum, row_chk))


            # 8. Cumulate the checksum
            chk_sum += row_chk

        # 9. Return the total checksum
        if verbose:
            print("Checksum is %d" % (chk_sum))
        return chk_sum

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c a p t c h a . p y                     end
# ======================================================================
