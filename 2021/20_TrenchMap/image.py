# ======================================================================
# Trench Map
#   Advent of Code 2021 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         i m a g e . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LIGHT = '#'
DARK = '.'
DELTA = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (0, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
]

# ======================================================================
#                                                                  Image
# ======================================================================


class Image(object):   # pylint: disable=R0902, R0205
    "Object for Trench Map"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.algorithm = None
        self.pixels = {}
        self.flash = False

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.algorithm = text[0]
            for r_number, row in enumerate(text[1:]):
                for c_number, char in enumerate(row):
                    self.pixels[(c_number, r_number)] = char
            if self.algorithm[0] == LIGHT and self.algorithm[511] == DARK:
                self.flash = True

    def count_light(self):
        "Count the number of light pixels"

        # 1. Start with none
        result = 0

        # 2. Loop for all of the pixels
        for pixel in self.pixels.values():

            # 3. If this is a light pixel, count it
            if pixel == LIGHT:
                result += 1

        # 4. Return the number of lit pixels
        return result

    @staticmethod
    def neighbors(loc):
        "Return the neighbors of this location (and the location itself)"

        # 1. Start with nothing
        result = []

        # 2. Loop for the directions to the neighbor
        for delta in DELTA:

            # 3. Get the location of this neighbor
            n_loc = (loc[0] + delta[0], loc[1] + delta[1])

            # 4. Add it to the list
            result.append(n_loc)

        # 5. Return the neighbors
        assert len(result) == 9
        return result

    def neighbor(self, loc, void=DARK):
        "Return the pixel and it's immediate neighbors as a number"

        # 1. Start with nothing
        result = []

        # 2. Loop for the neighbots
        for n_loc in Image.neighbors(loc):

            # 3. Lights are 1, darks are 0
            if n_loc in self.pixels:
                pixel = self.pixels[n_loc]
            else:
                pixel = void
            if pixel == LIGHT:
                result.append('1')
            else:
                result.append('0')

        # 4. Return the neighborhood as a number
        assert len(result) == 9
        return int(''.join(result), 2)

    def next_pixel(self, loc, void=DARK):
        "Determine the value for the next pixel at the location"

        # 1. Get the neighborhood number
        index = self.neighbor(loc, void)

        # 2. Return the algorithm value
        return self.algorithm[index]

    def next_image(self, step):
        "Return the next image taking on/off border into account"

        # 1. Start with nothing
        new_pixels = {}
        if self.flash and step % 2 == 0:
            void = LIGHT
        else:
            void = DARK

        # 2. Get minimum and maximum row and columns
        for loc in self.pixels:

            # 3. Get all of the neighbors
            for n_loc in self.neighbors(loc):

                # 4. Nothing to do if we have already done it
                if n_loc in new_pixels:
                    continue

                # 5. Determine the next pixel of this location
                pixel = self.next_pixel(n_loc, void)

                # 6. Save the new pixel in the new image
                new_pixels[n_loc] = pixel

        # 7. Set the new image
        self.pixels = new_pixels

        # 9. Return the number of light pixels
        return self.count_light()

    def enhance(self, times):
        "Enhance the image multiple times"

        # 1. Loop for the number of times requested
        for step in range(times):

            # 2. Enhance the image
            self.next_image(step + 1)

        # 3. Return the number of lit pixels
        return self.count_light()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.enhance(2)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.enhance(50)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         i m a g e . p y                        end
# ======================================================================
