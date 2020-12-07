# ======================================================================
# Handy Haversacks
#   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r u l e . p y
# ======================================================================
"Single bab rule for the Advent of Code 2020 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
BAGS_CONTAIN = ' bags contain '
COMMA = ', '
SPACE = ' '
PERIOD = '.'
NO_OTHER = 'no other bags'
SHINY_GOLD = 'shiny gold'

# ======================================================================
#                                                                   Rule
# ======================================================================


class Rule(object):   # pylint: disable=R0902, R0205
    "Object for Handy Haversacks"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.bag = None
        self.bags = []
        self.numbers = []
        self.can_contain_shiny_gold = None
        self.bags_within = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        "Fill in the rule from a line of text"

        # 1. Get the bag name
        self.bag, contains = text.split(BAGS_CONTAIN)

        # 2. Some bags allow no other
        if contains.startswith(NO_OTHER):
            self.can_contain_shiny_gold = False
            self.bags_within = 0
            return

        # 3. Save the bag names and numbers
        for part in contains.split(COMMA):
            num, name1, name2, _ = part.split(SPACE)
            name = name1 + ' ' + name2
            self.bags.append(name)
            self.numbers.append(int(num))

            # 4. Can the bag directly hold a shiny gold one?
            if name == SHINY_GOLD:
                self.can_contain_shiny_gold = True

    def sumation(self):
        "Returns the number of bags it can directly hold"
        return sum(self.numbers)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           r u l e . p y                        end
# ======================================================================
