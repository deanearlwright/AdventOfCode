# ======================================================================
# Fractal Art
#   Advent of Code 2017 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f r a c t a l . p y
# ======================================================================
"A solver for fractal for Advent of Code 2017 Day 21"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INITIAL_PATTERN = ".#...####"
INITIAL_SIZE = 3

Transforms = namedtuple('Transforms',
                        ['rotate', 'fliprow', 'flipcol'])
TRANSFORMS = {
    2: Transforms([1, 3, 0, 2], [2, 3, 0, 1], [1, 0, 3, 2]),
    3: Transforms([2, 5, 8, 1, 4, 7, 0, 3, 6],
                  [6, 7, 8, 3, 4, 5, 0, 1, 2],
                  [2, 1, 0, 5, 4, 3, 8, 7, 6])}

PART_ONE_ITERATIONS = 5
PART_TWO_ITERATIONS = 18

# ======================================================================
#                                                                   Rule
# ======================================================================


class Rule(object):   # pylint: disable=R0902, R0205
    "Rule Object for Fractal Art"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text
        self.size = 0
        self.base = []
        self.matches = set()
        self.replace = ""

        # 2. Process text (if any)
        if text is not None:
            self.load_rule()

    def load_rule(self):
        "Load rule from text"

        # 1. Break rule into match => replace parts
        match, self.replace = [_.strip() for _ in self.text.split('=>')]
        self.replace = self.replace.replace('/','')

        # 2. Get the size of the match pattern
        self.size = 1 + match.count('/')

        # 3. Set the base match pattern
        match = match.replace('/', '')
        self.base = list(match)

        # 4. Loop for the four rotations
        for rnum in range(4):

            # 5. Get the rotated base
            rot = self.rotated(rnum)

            # 6. Add it to the matches
            self.matches.add(''.join(rot))

            # 7. As well as the horizontal and vertical flips
            self.matches.add(''.join([rot[_] for _ in TRANSFORMS[self.size].fliprow]))
            self.matches.add(''.join([rot[_] for _ in TRANSFORMS[self.size].flipcol]))


    def match(self, art):
        "Returns Transform if the art matches one of the patterns else None"

        if art in self.matches:
            return self.replace
        return None


    def rotated(self, rnum):
        result = self.base.copy()
        for _ in range(rnum % 4):
            result = [result[_] for _ in TRANSFORMS[self.size].rotate]
        return result

# ======================================================================
#                                                                Fractal
# ======================================================================


class Fractal(object):   # pylint: disable=R0902, R0205
    "Object for Fractal Art"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.art = INITIAL_PATTERN
        self.art_size = INITIAL_SIZE
        self.rule_size = self.determine_rule_size()
        self.rules = {2: [], 3: []}

        # 2. Process text (if any)
        if text is not None:
            self.load_rules()

    def determine_rule_size(self):
        "Determine the rule size to use"

        if 0 == self.art_size % 2:
            result = 2
        elif 0 == self.art_size % 3:
            result = 3
        else:
            raise Exception("art_size not divisiable by 2 or 3")

        return result

    def load_rules(self):
        "Process rules Fractal Art Rules"

        # 1. Loop for all the text
        for line in self.text:

            # 2. Create a rule object from the text
            rule = Rule(text=line)

            # 3. Add it to the appropiate set of rules
            self.rules[rule.size].append(rule)

    def step(self):
        "Process the grid by applying the art rules one time"

        # 1. Start with an empty result
        pieces = []

        # 2. Loop for all of the squares
        for art_square in self.squares():

            # 3. Transform the art square
            new_square = self.transform(art_square)
            #print("s=%s ns=%s"%
            #      (art_square, new_square))

            # 4. Collect all of the transformed squares
            pieces.append(new_square)

        # 5. Set the new art
        self.join_new_art(pieces)

        # 6. Set the new rule_size
        self.rule_size = self.determine_rule_size()

    def squares(self):
        "Generator for art squares"

        # 1. Determine the number of squares to transform
        num_squares = self.art_size // self.rule_size
        num_squares *= num_squares
        #print("art_size=%d, rule_size=%d, num_squares=%d" %
        #      (self.art_size, self.rule_size, num_squares))

        # 2. Loop for all of the squares
        for snum in range(num_squares):

            # 3. Return a square
            yield self.square(snum)

    def square(self, number):
        "Return the specified square of the art"

        # 1. Start with nothing
        result = []

        # 2. Determine the range arguments
        sqs_per_row = self.art_size // self.rule_size
        sq_row = number // sqs_per_row
        sq_col = number % sqs_per_row
        sq_start = sq_row * self.art_size * self.rule_size + sq_col * self.rule_size
        #print("  num=%d, spr=%d, r=%d, c=%d, ss=%d" %
        #      (number, sqs_per_row, sq_row, sq_col, sq_start))

        # 3. Loop for the rows in the square
        for rnum in range(self.rule_size):

            # 4. Get one row for the square
            row_start = sq_start + rnum * self.art_size
            row_finish = row_start + self.rule_size
            row = self.art[row_start:row_finish]
            #print("    rnum=%d, s=%d, f=%d, r=%s" %
            #      (rnum, row_start, row_finish, row))

            # 5. Add the row to the result
            result.append(row)

        # 6. Return the square
        return ''.join(result)

    def join_new_art(self, pieces):
        "make art from the new art pieces"

        # 1. Start with nothing
        new_art = []
        new_art_size = self.rule_size + 1

        # 1. How many pieces are in a row?
        sqs_per_row = self.art_size // self.rule_size

        # 2. Loop for all the squares that start a row of squares
        for beg_square in range(0, len(pieces), sqs_per_row):

            # 3. Loop for all the rows in the square
            for rnum in range(new_art_size):

                # 4. Start the row
                row = []

                # 5. Loop for all the squares in the row
                for snum in range(sqs_per_row):

                    # 6. Get the sections of new art for the row
                    pnum = beg_square + snum
                    piece = pieces[pnum]
                    row_beg = rnum * new_art_size
                    section = piece[row_beg:row_beg + new_art_size]
                    #print("nas=%d, spr=%d, bs=%d, rn=%d, sn=%d, pn=%d, p=%s, rb=%d, s=%s" %
                    #      (new_art_size, sqs_per_row, beg_square, rnum, snum, pnum, piece, row_beg, section))

                    # 7. Append it to the row
                    row.append(section)

                # 8. Append the row to the new_art
                new_art.append(''.join(row))

        # 9. Return the combined rows
        self.art = ''.join(new_art)
        self.art_size = new_art_size * sqs_per_row


    def transform(self, art_square):
        "Transform a portion of the art based on rules"

        # 1. Loop for all the rule
        for rule in self.rules[self.rule_size]:

            # 2. Does this rule match?
            matched = rule.match(art_square)

            # 3. If it does, we are done
            if matched:
                return matched

        # 4. Opps
        return "Opps"


    def pixels(self):
        "Return the number of pixels that are on"

        return Counter(self.art)['#']

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Loop for required iterations
        if limit == 0:
            limit = PART_ONE_ITERATIONS
        for iteration in range(limit):

            # 2. Take a single step
            self.step()

            # 3. Display information if requested
            if verbose:
                print("Iteration %d: art_size=%d, rule_size=%d, pixels=%d" %
                      (iteration, self.art_size, self.rule_size, self.pixels() ))

        # 4. Return the number of ON pixels
        return self.pixels()


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Loop for required iterations
        if limit == 0:
            limit = PART_TWO_ITERATIONS
        for iteration in range(limit):

            # 2. Take a single step
            self.step()

            # 3. Display information if requested
            if verbose:
                print("Iteration %d: art_size=%d, rule_size=%d, pixels=%d" %
                      (iteration, self.art_size, self.rule_size, self.pixels() ), flush=True)

        # 4. Return the number of ON pixels
        return self.pixels()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       f r a c t a l . p y                      end
# ======================================================================
