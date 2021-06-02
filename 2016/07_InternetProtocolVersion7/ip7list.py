# ======================================================================
# Internet Protocol Version 7
#   Advent of Code 2016 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         i p 7 l i s t . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import ip7addr

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Ip7list
# ======================================================================


class Ip7list(object):   # pylint: disable=R0902, R0205
    "Object for Internet Protocol Version 7"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.addrs = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all of the lines of the text
        for line in text:

            # 2. Create and append the address info
            self.addrs.append(ip7addr.Ip7addr(line, self.part2))

    def count_tls(self):
        "Return the count of address that support TLS"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the addresses
        for addr in self.addrs:

            # 3. If the address supports TLS, increment count
            if addr.is_tls():
                result += 1

        # 4. Return the number of address that support TLS
        return result

    def count_ssl(self):
        "Return the count of address that support SSL"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the addresses
        for addr in self.addrs:

            # 3. If the address supports SSL, increment count
            if addr.is_ssl():
                result += 1

        # 4. Return the number of address that support SSL
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.count_tls()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.count_ssl()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       i p 7 l i s t . p y                      end
# ======================================================================
