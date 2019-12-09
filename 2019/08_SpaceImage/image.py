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
            self. layers = layers

        # 3. If given text, process it
        if text:
            pass

        # 4. Check the layers
        self.check_layers()

    def check_layers(self):
        'Check the size of each layer'

        # 1. Assume success
        result = False

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
        "Return # ones time # twos in layer with the most zeroes"

        # 2. if there are no layers, this is pretty easy
        if not self.layers:
            return 0

        # 2. Start with nothing
        counts = []

        # 3. Loop for all the layers and count the numbers
        for indx in range(len(self.layers)):
            counts[indx] = Counter(self.layers[indx])

        # 4. Find the layer with the most zeroes
        most_zeroes = (0, counts[0]['0'])
        for indx in range(1, len(self.layers)):
            if counts[indx]['0'] > most_zeroes[1]:
                most_zeroes = (indx, counts[indx]['0'])

        # 5. Return the number of ones times the number of twos
        return counts[most_zeroes[0]]['1']*counts[most_zeroes[0]]['1']


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           u o m a p . p y                      end
# ======================================================================
