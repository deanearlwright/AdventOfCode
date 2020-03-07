# ======================================================================
# The Halting Problem
#   Advent of Code 2017 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t u r i n g . p y
# ======================================================================
"A solver for turing for Advent of Code 2017 Day 25"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict, namedtuple

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LEFT = -1
RIGHT = 1
MOVE = {
    'right.': RIGHT,
    'left.': LEFT,
}

# ======================================================================
#                                                                   Rule
# ======================================================================
Rule = namedtuple('Rule', 'state current write move nxt_state')

# ======================================================================
#                                                                 Turing
# ======================================================================


class Turing(object):   # pylint: disable=R0902, R0205
    "Object for The Halting Problem"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.tape = defaultdict(int)
        self.position = 0
        self.state = None
        self.steps = 0
        self.rules = defaultdict(list)

        # 2. Process text (if any)
        if text is not None:
            self.process_text(text)

    def process_text(self, text):
        "Processs the text setting initial state, number of diagnostic steps, and rules"

        # 1. First line is the initial state
        assert text[0].startswith('Begin in state ')
        self.state = text[0][-2]

        # 2. Second line is number of diagnostic steps
        assert text[1].startswith('Perform a diagnostic ')
        self.steps = int(text[1].split()[-2])

        # 3. Process the states
        for lnum in range(2, len(text), 9):

            # 4. Get the state
            assert text[lnum].startswith('In state ')
            state = text[lnum][-2]
            assert state.isupper()

            # 5. Get the zero and one rules
            self.rules[state].append(self.process_text_rule(text, state, lnum + 1))
            self.rules[state].append(self.process_text_rule(text, state, lnum + 5))

    def process_text_rule(self, text, state, lnum):
        "Get one one rule from the text"

        # 1. Make sure all is well
        assert text[lnum].startswith('  If the current value is ')
        assert text[lnum + 1].startswith('    - Write the value ')
        assert text[lnum + 2].startswith('    - Move one slot to the ')
        assert text[lnum + 3].startswith('    - Continue with state ')

        # 2. Get the rule parts: current, write, move, next
        current = int(text[lnum][-2])
        write = int(text[lnum + 1][-2])
        move = MOVE[text[lnum + 2].split()[-1]]
        nxt_state = text[lnum + 3][-2]

        # 3. Return a rule tupple
        return Rule(state=state, current=current, write=write, move=move, nxt_state=nxt_state)

    def ones(self):
        "Return the number of ones on the tape"
        return sum(self.tape.values())

    def tape_read(self):
        "Return the value of the tape at the current position"
        return self.tape[self.position]

    def tape_write(self, value):
        "Write a value on the tape at the current position"
        self.tape[self.position] = value

    def step(self):
        "Run the Turing machine for a single step"

        # 0. Preconditions
        assert self.state != None

        # 1. Get rule to use based on the current state and value of the tape at the current position
        rule = self.rules[self.state][self.tape_read()]

        # 2. Write the rule value to the tape
        self.tape_write(rule.write)

        # 3. Move the position of the cursor over the tape
        self.position += rule.move

        # 4. Set the next state
        self.state = rule.nxt_state

    def run(self, verbose=False, limit=0):
        "Run the Turing machine until the diagnostic steps are complete"

        # 1. Loop until steps complete
        while self.steps > 0:

            # 2. Execute a single step
            self.step()

            # 3. Decrement the step count
            self.steps -= 1

            # 4. Output intermediate values (if desired)
            if verbose:
                if limit > 0 and self.steps % limit == 0:
                    print('To go %s, position %d, ones %d' %
                          (self.steps, self.position, self.ones()), flush=True)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Run the Turing machine until the diagnostics are complete
        self.run(verbose=verbose, limit=limit)

        # 1. Return the solution for part one
        return self.ones()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        t u r i n g . p y                       end
# ======================================================================
