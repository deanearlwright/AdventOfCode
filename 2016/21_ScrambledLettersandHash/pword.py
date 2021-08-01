# ======================================================================
# Scrambled Letters and Hash
#   Advent of Code 2016 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p w o r d . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART_ONE_CLEAR = "abcdefgh"
PART_TWO_SCRAMBLED = "fbgdceah"
UNSCRAMBLE_ROTATE_BASED_5 = [1, 3, 0, 2, 4]
UNSCRAMBLE_ROTATE_BASED_8 = [1, 1, 6, 2, 7, 3, 0, 4]

# ======================================================================
#                                                                  Pword
# ======================================================================


class Pword(object):   # pylint: disable=R0902, R0205
    "Object for Scrambled Letters and Hash"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def scrambler(self, clear_text):
        "Scramble clear text into encrypted text"

        # 1. Start with the clear text
        result = clear_text

        # 2. Loop for each of the scrampling instructions
        for inst in self.text:

            # 3. Execute the instruction
            result = Pword.execute(inst, result)

        # 4. Returned the scrambled result
        return result

    @staticmethod
    def execute(inst, in_word):
        "Execute a single scrambler instruction"

        # 1. Split the word into letters
        letters = list(in_word)

        # 2. Break up the instruction into words
        words = inst.split(' ')

        # 3. Execute the instruction
        if words[0] == "swap" and words[1] == "position":
            # swap position X with position Y
            # means that the letters at indexes X and Y (counting from 0) should be swapped.
            x_indx = int(words[2])
            y_indx = int(words[5])
            temp = letters[x_indx]
            letters[x_indx] = letters[y_indx]
            letters[y_indx] = temp
        elif words[0] == "swap" and words[1] == "letter":
            # swap letter X with letter Y
            # means that the letters X and Y should be swapped
            #   (regardless of where they appear in the string).
            x_indx = letters.index(words[2])
            y_indx = letters.index(words[5])
            temp = letters[x_indx]
            letters[x_indx] = letters[y_indx]
            letters[y_indx] = temp
        elif words[0] == "rotate" and words[1] == "left":
            # rotate left/right X steps
            # means that the whole string should be rotated
            #   for example, one right rotation would turn abcd into dabc.
            length = len(letters)
            steps = int(words[2]) % length
            letters = letters + letters
            letters = letters[steps:steps + length]
        elif words[0] == "rotate" and words[1] == "right":
            # rotate left/right X steps
            # means that the whole string should be rotated
            #   for example, one right rotation would turn abcd into dabc.
            length = len(letters)
            steps = int(words[2]) % length
            letters = letters + letters
            letters = letters[length - steps:length - steps + length]
        elif words[0] == "rotate" and words[1] == "based":
            # rotate based on position of letter X
            # means that the whole string should be rotated to the right based on the
            # index of letter X (counting from 0) as determined before this instruction
            # does any rotations. Once the index is determined, rotate the string to the
            # right one time, plus a number of times equal to that index, plus
            # one additional time if the index was at least 4.
            length = len(letters)
            steps = letters.index(words[6])
            if steps >= 4:
                steps += 1
            steps += 1
            steps = steps % length
            letters = letters + letters
            letters = letters[length - steps:length - steps + length]
        elif words[0] == "reverse" and words[1] == "positions":
            # reverse positions X through Y
            # means that the span of letters at indexes X through Y
            # (including the letters at X and Y) should be reversed in order.
            x_indx = int(words[2])
            y_indx = int(words[4])
            rev = letters[x_indx:y_indx + 1]
            rev.reverse()
            letters = letters[0:x_indx] + rev + letters[y_indx + 1:]
        elif words[0] == "move" and words[1] == "position":
            # move position X to position Y
            # means that the letter which is at index X should be removed from the string,
            # then inserted such that it ends up at index Y.
            x_indx = int(words[2])
            y_indx = int(words[5])
            x_letter = letters[x_indx]
            del letters[x_indx]
            letters.insert(y_indx, x_letter)

        # 4. Return the slighly more scrambled
        return ''.join(letters)

    def unscrambler(self, encrypted):
        "Uncramble encrypted back to the clear text"

        # 1. Start with the encrypted
        result = encrypted

        # 2. Loop for each of the scrampling instructions
        for indx in range(len(self.text), 0, -1):
            inst = self.text[indx - 1]

            # 3. Un-Execute the instruction
            result = Pword.unexecute(inst, result)

        # 4. Returned the unscrambled result
        return result

    @staticmethod
    def unexecute(inst, in_word):
        "Reverse a single scrambler instruction"

        # 1. Split the word into letters
        letters = list(in_word)

        # 2. Break up the instruction into words
        words = inst.split(' ')

        # 3. Reverse the instruction
        if words[0] == "swap" and words[1] == "position":  # Reverse is the same
            # swap position X with position Y
            # means that the letters at indexes X and Y (counting from 0) should be swapped.
            x_indx = int(words[2])
            y_indx = int(words[5])
            temp = letters[x_indx]
            letters[x_indx] = letters[y_indx]
            letters[y_indx] = temp
        elif words[0] == "swap" and words[1] == "letter":  # Reverse is the same
            # swap letter X with letter Y
            # means that the letters X and Y should be swapped
            #   (regardless of where they appear in the string).
            x_indx = letters.index(words[2])
            y_indx = letters.index(words[5])
            temp = letters[x_indx]
            letters[x_indx] = letters[y_indx]
            letters[y_indx] = temp
        elif words[0] == "rotate" and words[1] == "left":  # Reverse is rotate right
            # rotate left/right X steps
            # means that the whole string should be rotated
            #   for example, one right rotation would turn abcd into dabc.
            length = len(letters)
            steps = int(words[2]) % length
            letters = letters + letters
            letters = letters[length - steps:length - steps + length]
        elif words[0] == "rotate" and words[1] == "right":  # Reverse is rotate left
            # rotate left/right X steps
            # means that the whole string should be rotated
            #   for example, one right rotation would turn abcd into dabc.
            length = len(letters)
            steps = int(words[2]) % length
            letters = letters + letters
            letters = letters[steps:steps + length]
        elif words[0] == "rotate" and words[1] == "based":  # left instead of right
            # rotate based on position of letter X
            # means that the whole string should be rotated to the right based on the
            # index of letter X (counting from 0) as determined before this instruction
            # does any rotations. Once the index is determined, rotate the string to the
            # right one time, plus a number of times equal to that index, plus
            # one additional time if the index was at least 4.
            indx = letters.index(words[6])
            length = len(letters)
            if length == 8:
                steps = UNSCRAMBLE_ROTATE_BASED_8[indx]
            else:
                steps = UNSCRAMBLE_ROTATE_BASED_5[indx]
            letters = letters + letters
            letters = letters[steps:steps + length]
        elif words[0] == "reverse" and words[1] == "positions":  # Same as execute
            # reverse positions X through Y
            # means that the span of letters at indexes X through Y
            # (including the letters at X and Y) should be reversed in order.
            x_indx = int(words[2])
            y_indx = int(words[4])
            rev = letters[x_indx:y_indx + 1]
            rev.reverse()
            letters = letters[0:x_indx] + rev + letters[y_indx + 1:]
        elif words[0] == "move" and words[1] == "position":  # reverse swaps the indexes
            # move position X to position Y
            # means that the letter which is at index X should be removed from the string,
            # then inserted such that it ends up at index Y.
            x_indx = int(words[5])
            y_indx = int(words[2])
            x_letter = letters[x_indx]
            del letters[x_indx]
            letters.insert(y_indx, x_letter)

        # 4. Return the slighly clearer work
        return ''.join(letters)

    def part_one(self, verbose=False, limit=0, word=PART_ONE_CLEAR):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.scrambler(word)

    def part_two(self, verbose=False, limit=0, word=PART_TWO_SCRAMBLED):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.unscrambler(word)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         p w o r d . p y                        end
# ======================================================================
