# ======================================================================
# Space Image Format
#   Advent of Code 2019 Day 08-- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             i m a g e . p y
# ======================================================================
"Image for Space Image Format problem for Advent of Code 2019 Day 08"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from __future__ import print_function

from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Image
# ======================================================================


class Image(object):
    """Space Image Format from the Digital Sending Network"""

    def __init__(self, width=0, height=0, layers=None, text=None):

        # 1. Save width, height, and no layers (yet)
        self.width = width
        self.height = height
        self.layers = []

        # 2. If given layers, store them
        if layers:
            self.layers = layers

        # 3. If given text, process it
        if text:
            chunk_size = self.width * self.height
            assert len(text) % chunk_size == 0
            while text:
                self.layers.append(text[:chunk_size])
                text = text[chunk_size:]

        # 4. Check the layers
        self.check_layers()

    def check_layers(self):
        'Check the size of each layer'

        # 1. Assume success
        result = None

        # 2. loop fo all the layers
        for indx in range(len(self.layers)):

            # 3. Check the length of this layer
            if len(self.layers[indx]) != self.width * self.height:

                # 4. Print an error and return the layer number
                print('Error in layer %d, length is %d, should be %d' %
                      (indx, len(self.layers[indx]), self.width * self.height))
                result = indx
                break

        # 5 Return the good (None) or bad (indx) news
        return result

    def part_one(self):
        "Return number of ones time number of twos in layer with the most zeroes"

        # 2. if there are no layers, this is pretty easy
        if not self.layers:
            return None

        # 2. Start with nothing
        counts = []

        # 3. Loop for all the layers and count the numbers
        for indx in range(len(self.layers)):
            counts.append(Counter(self.layers[indx]))
        print("counts = %s" % (counts))

        # 4. Find the layer with the fewest number of zeroes
        least_zeroes = (-1, self.width*self.height+1)
        for indx in range(len(counts)):
            if '0' in counts[indx]:
                zeroes = counts[indx]['0']
            else:
                zeroes = 0
            if zeroes < least_zeroes[1]:
                least_zeroes = (indx, zeroes)

        # 5. Return the number of ones times the number of twos
        best = least_zeroes[0]
        if best == -1:
            return None
        if '1' in counts[best]:
            ones = counts[best]['1']
        else:
            ones = 0
        if '2' in counts[best]:
            twos = counts[best]['2']
        else:
            twos = 0
        print('best = %d, zeroes = %d, ones = %d, twos = %d. solution = %d' %
              (best, least_zeroes[1], ones, twos, ones * twos))
        return ones * twos


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           u o m a p . p y                      end
# ======================================================================
