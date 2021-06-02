# ======================================================================
# Internet Protocol Version 7
#   Advent of Code 2016 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         i p 7 a d d r . p y
# ======================================================================
"Ip7addr for the Advent of Code 2016 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_SPLIT = re.compile(r'\[|\]')

# ======================================================================
#                                                                Ip7addr
# ======================================================================


class Ip7addr(object):   # pylint: disable=R0902, R0205
    "Object for Internet Protocol Version 7"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.nob_abba = set()
        self.inb_abba = set()
        self.nob_aba = set()
        self.inb_aba = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Split the address on the brackets
        parts = RE_SPLIT.split(text)

        # 2. Are you a in a bracket or out of a bracker?
        for indx, part in enumerate(parts):

            # 3. Even number parts are no bracket, odd ones are in bracket
            if indx % 2 == 0:
                self.nob_abba |= Ip7addr.get_abba(part)
                self.nob_aba |= Ip7addr.get_aba(part)
            else:
                self.inb_abba |= Ip7addr.get_abba(part)
                self.inb_aba |= Ip7addr.get_aba(part)

    @staticmethod
    def get_abba(part):
        "Get all of the abba phrases"

        # 1. Start with nothing
        result = set()

        # 2. Add some extra at the end
        xpart = part + '_-='

        # 3. Loop for all of the characters
        for indx, char in enumerate(part):

            # 4. Do we have an abba pattern
            if char != xpart[indx + 1] and \
              char == xpart[indx + 3] and \
              xpart[indx + 1] == xpart[indx + 2]:

                # 5. Yes, add it to the result
                result.add(part[indx:indx + 4])

        # 6. Return the set of abba patterns
        return result

    @staticmethod
    def get_aba(part):
        "Get all of the aba phrases"

        # 1. Start with nothing
        result = set()

        # 2. Add some extra at the end
        xpart = part + '_-='

        # 3. Loop for all of the characters
        for indx, char in enumerate(part):

            # 4. Do we have an aba pattern
            if char != xpart[indx + 1] and \
              char == xpart[indx + 2]:

                # 5. Yes, add it to the result
                result.add(part[indx:indx + 3])

        # 6. Return the set of abba patterns
        return result

    def is_tls(self):
        "Return true of the address supports TLS"

        return len(self.nob_abba) > 0 and len(self.inb_abba) == 0

    def is_ssl(self):
        "Return true of the address supports SSL"

        # 1. There needs to be both non-bracket and in-bracket abas
        if len(self.nob_aba) == 0 or len(self.inb_aba) == 0:
            return False

        # 2. Loop for all out of bracket abas
        for aba in self.nob_aba:

            # 3. Create the cooresponding bab from the aba
            bab = ''.join([aba[1], aba[0], aba[1]])

            # 4. If we find the bab between the brackets, the address supports SSL
            if bab in self.inb_aba:
                return True

        # 5. We don't have a match, return False
        return False


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       i p 7 a d d r . p y                      end
# ======================================================================
