# ======================================================================
# Balance Bots
#   Advent of Code 2016 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b o t s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import bot

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART_ONE_VALUES = (61, 17)

# ======================================================================
#                                                                  Bots
# ======================================================================


class Bots(object):   # pylint: disable=R0902, R0205
    "Object for Balance Bots"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.bots = {}
        self.outputs = {}
        self.twos = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in self.text:
                self._process_line(line)

    def _process_line(self, line):
        "Assign values from text"

        assert line is not None and len(line) > 0

        # 1. Get bot number
        number = bot.Bot.get_bot_number(line)
        if number is None:
            print("*** Unable to determine bot number from text: %s" % line)
            return

        # 2. Is this a new bot?
        if number not in self.bots:

            # 3. Add the new bot
            self.bots[number] = bot.Bot(line, self.part2)

        else:
            # 4. Update an existing bot
            self.bots[number].add_text(line)

        # 5. Remember if the bot has two chips
        if self.bots[number].has_two():
            self.twos.add(number)

    def zooming_around(self, values=PART_ONE_VALUES):
        "Have the robots do thier thing"

        # 1. Loop until there is an answer or nothing to do
        while len(self.twos) > 0:

            # 2. Get the number of a robot with somthing to do
            number = self.twos.pop()
            robot = self.bots[number]

            # 3. Check if this is the solution to part one
            if self.part2 is False and robot.am_i_the_one(values):
                return number

            # 4. Get the recipients of the bot's largess
            low_who, low_value, high_who, high_value = robot.gives()

            # 5. Distribute the chips
            if low_who in self.bots:
                if self.bots[low_who].receive(low_value):
                    self.twos.add(low_who)
            else:
                self.outputs[low_who - bot.OUTPUT_BASE] = low_value

            if high_who in self.bots:
                if self.bots[high_who].receive(high_value):
                    self.twos.add(high_who)
            else:
                self.outputs[high_who - bot.OUTPUT_BASE] = high_value

            # 6. Check for the solution to part2
            if 0 in self.outputs and 1 in self.outputs and 2 in self.outputs:
                return self.outputs[0] * self.outputs[1] * self.outputs[2]

        # 7. Return Failure
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.zooming_around()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.zooming_around()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      b o t s . p y                     end
# ======================================================================
