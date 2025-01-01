
# ======================================================================
# Ceres Search
#   Advent of Code 2024 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         w o r d s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTAS = {
    "e": (0, 1),
    "w": (0, -1),
    "s": (1, 0),
    "n": (-1, 0),
    "ne": (1, 1),
    "se": (-1, 1),
    "nw": (1, -1),
    "sw": (-1, -1),
}

DIRECTIONS = ["e", "w", "s", "n", "ne", "nw", "se", "sw"]


# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def next_loc(here, direction):
    "Return the next location for here in the given direction"
    delta = DELTAS[direction]
    return (here[0] + delta[0], here[1] + delta[1])

# ======================================================================
#                                                                  Words
# ======================================================================


class Words(object):   # pylint: disable=R0902, R0205
    "Object for Ceres Search"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.letters = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Initialize letters
        for letter in "XMAS":
            self.letters[letter] = []

        # 2. Loop for every line of the text
        for row, line in enumerate(text):

            # 3. Loop for every letter in the line
            for col, letter in enumerate(line):

                 # 4. If it is a letter in the word, save its location
                if letter in self.letters:
                    self.letters[letter].append((row, col))

        # 1. Freeze the lists
        for letter in "XMAS":
            self.letters[letter] = frozenset(self.letters[letter])

    def is_word_here(self, word, location, direction):
        "Is there a word starting at this location in this direction"

        # 1. Loop for the letters in the word
        for letter in word:

            # 2. If the letter is not at this location, return false
            if location not in self.letters[letter]:
                return False

            # 3. Advance to the next location
            location = next_loc(location, direction)

        # 4. We made it to the end, found the word
        return True

    def find_direction(self, word, direction):
        "Count all the words found in a given direction"

        # 1. Start with nothing
        result = 0

        # 1. Loop for all the starting locations
        for location in self.letters[word[0]]:

            # 2. Is there a word there, increment the count
            if self.is_word_here(word, location, direction):
                result += 1

        # 3. Return the count of words found in this direction
        return result

    def find_all_directions(self, word):
        "Find the word in all directions"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all directions
        for direction in DIRECTIONS:

            # 3. Increment the count by the words in this direction
            result += self.find_direction(word, direction)

        # 4. Return the number of time the word was found
        return result

    def is_cross_dir(self, word, loc, dir1, dir2):
        "Check a leg of the cross"

        # 1. Get the two other locations
        loc1 = next_loc(loc, dir1)
        loc2 = next_loc(loc, dir2)

        # 2. Check top to bottom
        if loc1 in self.letters[word[0]] and loc2 in self.letters[word[2]]:
            return True

        # 3. Check bottom to top
        if loc1 in self.letters[word[2]] and loc2 in self.letters[word[0]]:
            return True

        # 4. No cross word here
        return False

    def is_cross_at(self, word, loc):
        "Is there a cross word here"

        # 1. Check the center letter
        if not loc in self.letters[word[1]]:
            return False

        # 2. Check one leg of the cross
        if not self.is_cross_dir(word, loc, "ne", "sw"):
            return False

        # 3, And then the other
        if not self.is_cross_dir(word, loc, "se", "nw"):
            return False

        # 4. It checks out
        return True

    def find_all_crosses(self, word):
        "Find the word in all crosses"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the starting locations
        for loc in self.letters[word[1]]:

            # 3. Is there a cross here, increment count
            if self.is_cross_at(word, loc):
                result += 1

        # 4. Return the number of cross words
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if not self.text:
            return None
        return self.find_all_directions("XMAS")

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if not self.text:
            return None
        return self.find_all_crosses("MAS")

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      w o r d s . p y                     end
# ======================================================================
