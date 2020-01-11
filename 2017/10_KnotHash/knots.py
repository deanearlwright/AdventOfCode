# ======================================================================
# Knot Hash
#   Advent of Code 2017 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         k n o t s . p y
# ======================================================================
"A solver for Knot Hash for Advent of Code 2017 Day 10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Knots
# ======================================================================


class Knots(object):
    """Knotty String Object"""

    def __init__(self, part2=False, length=0):

        # 1. Set the initial values
        self.part2 = part2
        self.length = length
        self.level = 0
        self.current = 0
        self.skip = 0
        self.values = list(range(length))

    def process_knots(self, text=None, verbose=False, limit=0):
        "Process the text of knots"

        # 1. If no text, not much to do
        if text is None:
            return None

        # 2. Loop for all of the knot lengths
        for knum, klen in enumerate([int(_) for _ in text.split(',')]):

            # 3. Process the character
            self.process_one_knot(klen, verbose=verbose)

            # 4. Check if processing limit reached
            if knum > limit > 0:
                break

        # 5. Return the product of the first two values
        return self.values[0] * self.values[1]

    def process_one_knot(self, klen, verbose=False):
        "Process a single know"

        # 1. Reverse the order of length elements in the list,
        #    starting with the element at the current position
        new_values = self.reverse(klen)

        # 2. Move the current position forward by that length plus the skip size
        new_current = (self.current + klen + self.skip) % self.length

        # 3. Increase the skip size by one
        new_skip = self.skip + 1

        # 4. Descibe the changes
        if verbose:
            print("klen=%d, cur=%d, skip=%d, newc=%d, news=%d, v=%s" %
                  (klen, self.current, self.skip, new_current, new_skip, new_values))

        # 5. Update the values and the skip size
        self.values = new_values
        self.current = new_current
        self.skip = new_skip

    def reverse(self, klen):
        "Reverse a portion of the values"

        # 1. Get beginning and ending offsets of the values to reverse
        rev_beg = self.current
        rev_end = self.current + klen

        # 2. Pretty easy if not past end of string
        result = self.values.copy()
        if rev_end < self.length:
            rev_vals = self.values[rev_beg:rev_end]
            rev_vals.reverse()
            result = self.values[:rev_beg] + rev_vals + self.values[rev_end:]

        # 3. Else: Take some from the back and the front
        else:
            rev_mod = rev_end % self.length
            rev_len = rev_end - self.length
            rev_vals = self.values[rev_beg:] + self.values[:rev_mod]
            rev_vals.reverse()
            #print("l=%d b=%d e=%d m=%d l=%d" %
            #      (klen, rev_beg, rev_end, rev_mod, rev_len))
            #print("%s: %s %s %s" %
            #      (str(rev_vals), str(rev_vals[-rev_len:]),
            #       str(self.values[rev_mod:rev_beg]), str(rev_vals[:-rev_len])))
            result = rev_vals[-rev_len:] + self.values[rev_mod:rev_beg] + rev_vals[:-rev_len]

        # 4. Return the modified values
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          k n o t s . p y                       end
# ======================================================================
