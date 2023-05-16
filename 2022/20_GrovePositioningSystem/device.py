
# ======================================================================
# Grove Positioning System
#   Advent of Code 2022 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
Indexed = namedtuple('Indexed', 'index number')
KEY = 811589153

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Grove Positioning System"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.numbers = deque()
        self.key = 1

        # 2. Part2 has a harder to remember key
        if self.part2:
            self.key = KEY

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for each line of text
        for index, line in enumerate(text):

            # 2. Add the number to the initial bunch
            self.numbers.append(Indexed(index=index,
                                        number=self.key * int(line)))

    def mixer(self):
        "Mix the numbers based on the original ordering"

        # 1. Loop for the numbers in the original order
        for index in range(len(self.numbers)):
            # print(index, [x.number for x in self.numbers])

            # 2. Move it to the left most position
            while index != self.numbers[0].index:
                self.numbers.rotate(-1)

            # 3. Take it out
            indexed = self.numbers.popleft()

            # 4. Move to where it goes back in
            self.numbers.rotate(-indexed.number)

            # 5. And put it back
            self.numbers.appendleft(indexed)

    def coordinates(self):
        "Return the grove coordinates"

        # 1. Find the zero and set it at the front
        while self.numbers[0].number != 0:
            self.numbers.rotate(-1)

        # 2. Get the x
        self.numbers.rotate(-1000)
        coord_x = self.numbers[0].number

        # 3. Get the y
        self.numbers.rotate(-1000)
        coord_y = self.numbers[0].number

        # 4. And the z coordinate
        self.numbers.rotate(-1000)
        coord_z = self.numbers[0].number

        # 5. Return a the number
        return coord_x, coord_y, coord_z

    def mixer_ten(self):
        "Mix the numbers up ten times"

        # 1. Loop 10 times
        for _ in range(10):

            # 2. And mix things up
            self.mixer()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
