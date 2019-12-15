# ======================================================================
# Space Stoichiometry
#   Advent of Code 2019 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          r e a c t i o n . p y
# ======================================================================
"A reaction for Space Stoichiometry for Advent of Code 2019 Day 14"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
REACTION_RE = re.compile(r'((?:[0-9]+ [A-Z]+[, ]+)+)=> ([0-9]+) ([A-Z]+)')

# ======================================================================
#                                                               Reaction
# ======================================================================


class Reaction():   # pylint: disable=R0903
    """Object representing a single moon"""

    def __init__(self, produces=None, quanity=1, requires=None,
                 text=None):

        # 1. Set the initial values
        self.produces = produces
        self.quanity = quanity
        if requires is None:
            self.requires = []
        else:
            self.requires = requires

        # 2. If there is a text, decode and set the reaction
        if text:
            match = REACTION_RE.match(text)
            if match is None:
                print("Unable to parse reaction input %s" % text)
            else:
                #print("1=%s, 2=%s, 3=%s" % (match.group(1), match.group(2), match.group(3)))
                self.produces = match.group(3)
                self.quanity = int(match.group(2))
                self.requires = [_.strip() for _ in match.group(1).split(',')]

    def __str__(self):
        return "%s => %d %s" % (', '.join(self.requires), self.quanity, self.produces)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      r e a c t i o n . p y                     end
# ======================================================================
