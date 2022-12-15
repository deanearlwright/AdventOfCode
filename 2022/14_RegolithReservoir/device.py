
# ======================================================================
# Regolith Reservoir
#   Advent of Code 2022 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"Device for the Advent of Code 2022 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import scan

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Regolith Reservoir"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.scan = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Initialize the scanner
        self.scan = scan.Scan(text="500,0", part2=self.part2)

        # 2. Loop for each line of text
        for line in text:

            # 3. Add the line to the scanner
            self.scan.add_path(line)

        # 4. Determine the lowest segment of rock
        self.scan.find_lowest()

    def count_sand(self):
        "Drop sand until it reaches the void"

        # 1. We need a scanner for this to work
        if self.scan is None:
            return None

        # 2. Loop until we reach the void
        while True:
            # print(f"Dropping {self.scan.sand + 1}")

            # 3. Drop some sand
            void = self.scan.drop()

            # 4. Are we staring into the face of oblivian?
            if void is None:
                return self.scan.sand


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
