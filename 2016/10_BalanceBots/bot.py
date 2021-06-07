# ======================================================================
# Balance Bots
#   Advent of Code 2016 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b o t . p y
# ======================================================================
"Bot for the Advent of Code 2016 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
OUTPUT_BASE = 1000

# ======================================================================
#                                                                    Bot
# ======================================================================


class Bot(object):   # pylint: disable=R0902, R0205
    "Object for Balance Bots"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = None
        self.chips = []
        self.low = None
        self.high = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.add_text(text)

    @staticmethod
    def get_bot_number(text):
        "Return the bot number for the text or None"

        parts = text.split()
        if parts[0] == "value":
            return int(parts[5])
        if parts[0] == "bot":
            return int(parts[1])
        return None

    def has_two(self):
        "Returns True if the bot has two chips"
        return len(self.chips) == 2

    def add_text(self, text):
        "Add bot information based on the text type"
        if text.startswith('value '):
            self.add_value(text)
        else:
            self.add_rule(text)

    def add_value(self, text):
        "Add initial value to an existing bot"

        # 1. Parse the value line
        parts = text.split()
        if len(parts) != 6:
            print("*** Invalid value text: %s" % text)
            return False
        number = int(parts[5])
        chip = int(parts[1])

        # 2. Check that the bot numbers match
        if self.number is not None and number != self.number:
            print("*** Bot numbers (%d != %d) for value text: %s" % (self.number, number, text))
            return False
        self.number = number

        # 3. Make sure we have the carrying capability
        if self.has_two():
            print("*** Bot %d already has two chips (%d and %d): %s" %
                  (self.number, self.chips[0], self.chips[1], text))
            return False

        # 4. Add the chip
        self.chips.append(chip)

        # 5. Return success
        return True

    def add_rule(self, text):
        "Add rule to an existing bot"

        # 1. Parse the rule line
        parts = text.split()
        if len(parts) != 12:
            print("*** Invalid rule text: %s" % text)
        number = int(parts[1])
        low_what = parts[5]
        low_who = int(parts[6])
        high_what = parts[10]
        high_who = int(parts[11])

        # 2. Check that the bot numbers match
        if self.number is not None and number != self.number:
            print("*** Bot numbers (%d != %d) for rule text: %s" % (self.number, number, text))
            return False
        self.number = number

        # 3. Check that the bot doesn't already have a rule
        if self.high is not None:
            print("*** Bot %d already has a rule, text: %s" % (self.number, text))
            return False

        # 4. Set the rule
        if low_what == 'bot':
            self.low = low_who
        else:
            self.low = low_who + OUTPUT_BASE
        if high_what == 'bot':
            self.high = high_who
        else:
            self.high = high_who + OUTPUT_BASE

        # 5. Return success
        return True

    def gives(self):
        "Determine who gets what, returns [low_who, low_value, high_who, high_value]"

        # 1. Make sure we have two items
        if not self.has_two():
            print("*** bot %d has %d chips" % (self.number, len(self.chips)))
            return [None, None, None, None]

        # 2. Determine which chip is high and which is low
        low = min(self.chips)
        high = max(self.chips)

        # 3. The bot now has zero chips
        self.chips = []

        # 4. Return (what, who) low and high pairs
        return [self.low, low, self.high, high]

    def receive(self, chip):
        "Receive a chip, Return True if we now have two"

        # 1. You can have too many chips
        if self.has_two():
            print("*** bot %d already has two chips (%d and %d), can't accept %d" %
                  (self.number, self.chips[0], self.chips[1], chip))
            return True

        # 2. Add the chip
        self.chips.append(chip)

        # 3. Return True if we now have two chips
        return self.has_two()

    def am_i_the_one(self, values):
        "Returns true if bot will compare the given chips"

        if not self.has_two():
            return False

        values_min = min(values)
        values_max = max(values)
        chips_min = min(self.chips)
        chips_max = max(self.chips)

        return values_min == chips_min and values_max == chips_max


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      b o t . p y                     end
# ======================================================================
