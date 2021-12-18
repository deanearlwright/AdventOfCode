# ======================================================================
# Snailfish
#   Advent of Code 2021 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p r o b l e m . p y
# ======================================================================
"Number for the Advent of Code 2021 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Number
# ======================================================================


class Number(object):   # pylint: disable=R0902, R0205
    "Object for Snailfish"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pair = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.pair = Number.text_to_num(text)

    @staticmethod
    def text_to_num(text):
        "Convert text to snailfish number"

        # 1. If it doesn't start with a '[', return the digits
        if text[0] != '[':
            return int(text)

        # 2. Split the number into two parts
        parts = Number.split_text(text)

        # 3. Convert each of the two parts
        one = Number.text_to_num(parts[0])
        two = Number.text_to_num(parts[1])

        # 3. Return the snailfish number
        return [one, two]

    @staticmethod
    def split_text(text):
        "Split the text on the outer comma"

        # 1. Remove the outer brackets
        inner = text[1:-1]

        # 2. Find the inner comma
        comma = Number.find_comma(inner)

        # 3. Return the before and after comma parts
        return [inner[:comma], inner[comma + 1:]]

    @staticmethod
    def find_comma(text):
        "Find the location of the inner comma"

        # 1. Start at level 0
        level = 0

        # 2. Loop for all the characters
        for index, char in enumerate(text):

            # 3. If '[' increment level
            if char == '[':
                level += 1

            # 4. if ']', decrement level
            elif char == ']':
                level -= 1
                assert level >= 0

            # 5. if ',' and at outer level, found the comma
            elif char == ',' and level == 0:
                return index

        # 6. Huh?
        print("Couldn't find inner comma in", text)
        return -1

    def add(self, pair):
        "Add the other number to this one"

        # 1. First join the two numbers
        self.pair = [self.pair, pair]
        #print("joined for add", str(self))

        # 2. Then reduce the result
        self.reduce()

        # 3. And return the result (mainly for testing)
        return self.pair

    def reduce(self):
        "Reduce the number -- exploding and spliting as needed"

        # 1. Loop until reduced
        knt = 0
        while True:
            # print("Reduce %d <%s>" % (knt, str(self)))
            knt += 1
            if knt > 9999:
                print("Stopped reduce at step %d" % knt)
                return self.pair

            # 2. Attempt to explode
            if self.explode():
                continue

            # 3. Attempt to split
            if self.split():
                continue

            # 4. We are reduced
            break

        # 5. Return reduced pair (for testing)
        return self.pair

    def __str__(self):
        return str(self.pair).replace(' ', '')

    def explode(self):
        "Explode the snailfish number (if it needs it)"

        # 1. Turn the number in string
        text = str(self)

        # 2. Look for a pair nested four deep
        level = 0

        # 3. Loop for all the characters
        for index, char in enumerate(text):

            # 3. If '[' increment level
            if char == '[':
                level += 1

                # 4. Are we there yet
                if level == 5:

                    # 4a. Split up the number
                    before = text[:index]
                    comma = text.index(',', index)
                    close = text.index(']', index)
                    left = text[index + 1: comma]
                    right = text[comma + 1: close]
                    after = text[close + 1:]
                    # print("Exploding: before=<%s> left=%s right=%s after=%s" %
                    #      (before, left, right, after))

                    # 4b. Spread the numbers
                    before = Number.explode_left(before, left)
                    after = Number.explode_right(right, after)

                    # 4c. Put it back together
                    paired = before + '0' + after
                    #print("Exploded: <%s>" % paired)
                    # print()
                    self.pair = Number.text_to_num(paired)

                    # 4d. We did indeed explode
                    return True

            # 5. if ']', decrement level
            elif char == ']':
                level -= 1
                assert level >= 0

        # 6. Don't need to reduce
        return False

    @staticmethod
    def explode_left(before, left):
        "The left number is added to the number to the left (if any)"

        # 1. Find the first number to the left (if any)
        for index in range(len(before) - 1, 0, -1):
            if before[index].isdigit():

                # 2. Collect the digits
                digits = before[index]
                while before[index - len(digits)].isdigit():
                    digits = before[index - len(digits)] + digits

                # 3. Add the numbers
                number = str(int(digits) + int(left))

                # 3. Replace the number with the sum of the two digits
                return before[:1 + index - len(digits)] + number + before[index + 1:]

        # 4. No number to the left, just return what we have
        return before

    @staticmethod
    def explode_right(right, after):
        "The right number is added to the number to the right (if any)"
        #print("explode_right: right=<%s> after=<%s>" % (right, after))

        # 1. Find the first number to the left (if any)
        for index, char in enumerate(after):
            if char.isdigit():

                # 2. Collect the digits
                digits = char
                while after[index + len(digits)].isdigit():
                    digits += after[index + len(digits)]

                # 3. Add the digits and the right number
                number = str(int(digits) + int(right))

                # 4. Replace the number with the sum of the two digits
                return after[:index] + number + after[index + len(digits):]

        # 5. No number to the left, just return what we have
        return after

    def split(self):
        "split the snailfish number (if it needs it)"

        # 1. Turn the number in string
        text = str(self)

        # 2. Loop for all the characters
        for index, char in enumerate(text):

            # 3. Look for a two (or more) digit number
            if char.isdigit() and text[index + 1].isdigit():

                # 4. Split up the number
                before = text[:index]
                after = text[index:]
                number = ''
                while after[0].isdigit():
                    number += after[0]
                    after = after[1:]
                number = int(number)
                #print("Spliting: <%s> %d <%s>" % (before, number, after))

                # 5. Generate a new pair
                new_pair = "[%d,%d]" % (math.floor(number / 2), math.ceil(number / 2))

                # 6. Put it all together
                combined = before + new_pair + after
                #print("Split: combined=<%s>" % combined)
                # print()

                # 7. Set the combined pair
                self.pair = Number.text_to_num(combined)

                # 8. We did indeed split it
                return True

        # 9. It didn't need to split
        return False

    def magnitude(self):
        "Return the magnitude of the number"

        return Number.recursive_magnitude(self.pair)

    @staticmethod
    def recursive_magnitude(pair):
        "Recursively get the magnitude"

        # 1. Base case
        if isinstance(pair, int):
            return pair

        # 2. The other case
        return Number.recursive_magnitude(pair[0]) * 3 + Number.recursive_magnitude(pair[1]) * 2


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        n u m b e r . p y                       end
# ======================================================================
