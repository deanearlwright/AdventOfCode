# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p l a y e r . p y
# ======================================================================
"Player for the Advent of Code 2015 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Player
# ======================================================================


class Player(object):   # pylint: disable=R0902, R0205
    "Object for Wizard Simulator 20XX"

    def __init__(self, name="noone", text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = name
        self.attributes = {
            'hitpoints': 0,
            'damage': 0,
            'armor': 0,
            'mana': 0,
            'used': 0,
        }

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all the lines
        for line in text:

            # 2. Split line into attribute and number
            attribute, number = line.split(':')

            # 3. Save the number as hitpoints, damage, or armor
            self.attributes[attribute.lower().replace(' ', '')] = int(number)

    def is_dead(self):
        "Return True is the player is an ex-Player"
        return self.attributes['hitpoints'] <= 0

    def defend(self, attack):
        "Take damage based on the attack minus armor"
        self.attributes['hitpoints'] -= max(1, attack - self.attributes['armor'])
        self.attributes['hitpoints'] = max(0, self.attributes['hitpoints'])
        return self.is_dead()

    def wack(self):
        "Take a single point of damage"
        self.attributes['hitpoints'] -= 1

    def attack(self):
        "Returns the player's damage rating"
        return self.attributes['damage']

    def clone(self):
        "Make a duplicate player"

        # 1. Start with a clean player
        result = Player()

        # 2. Copy the fields
        result.text = self.text
        result.name = self.name
        result.part2 = self.part2
        for key, value in self.attributes.items():
            result.attributes[key] = value

        # 3. Return the copy
        return result

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key] = int(value)

    def __str__(self):
        non_zero = ["%s:%d" % (_[0], self.attributes[_]) for _ in self.attributes
                    if self.attributes[_] > 0]
        return "%s(%s)" % (self.name[0], ",".join(non_zero))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p l a y e r . p y                       end
# ======================================================================
