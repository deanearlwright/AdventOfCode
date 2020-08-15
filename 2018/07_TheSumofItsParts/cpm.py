# ======================================================================
# The Sum of Its Parts
#   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c p m . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import step
import worker

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Cpm
# ======================================================================


class Cpm(object):   # pylint: disable=R0902, R0205
    "Object for The Sum of Its Parts"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.steps = {}
        self.completed = set()
        self.ordered = []
        self.letters = set()

        # 2. Process text (if any)
        if text is not None:
            self.processText(text)

    def processText(self, text):
        # 1. Start with nothing
        self.steps = {}
        self.completed = set()
        self.ordered = []
        self.letters = set()

        # 2. Loop for every line of the text
        for line in text:

            # 3. Get the prerequisite and step from the line
            parts = line.split(' ')
            before = parts[1]
            letter = parts[7]

            # 4. If this is a new letter or step, add it
            if letter not in self.letters:
                self.letters.add(letter)
            if before not in self.letters:
                    self.letters.add(before)
            if letter not in self.steps:
                self.steps[letter] = step.Step(letter=letter)

            # 5. Add the prerequisite
            self.steps[letter].add_before(before)

    def get_start(self):
        # 1. If there are no steps, can't really start
        if len(self.letters) == 0:
            return set()
        # 2. Find a letter that is part part of any step rule
        return self.letters - set(self.steps.keys())

    def complete(self, letter):
        # 1. Record step complion
        self.completed.add(letter)
        self.ordered.append(letter)
        # print("letter=%s completed=%s ordered=%s" % (letter, self.completed, self.ordered))


    def next_step(self):
        # 1. Start at the beginning if just starting
        result = self.get_start() - self.completed

        # 2. If nothing has been completed, we only have the start(s)
        if len(self.completed) == 0:
            return result

        # 3. Loop for all of the steps
        for step in self.steps.values():

            # 4. Ignore step is already completed
            if step.letter in self.completed:
                continue

            # 5. Are the prerequisites for this step complete
            # print("step=%s before=%s completed=%s intersection=%s" % (step.letter, step.before, self.completed, step.before-self.completed))
            if len(step.before - self.completed) == 0:
                result.add(step.letter)

        # 6. If we got some steps
        if len(result) >= 0:
            return result

        # 7. So sorry we didn't find any
        return set()


    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Loop until there isn't a step
        next = self.next_step()
        while len(next) > 0:

            # 2. Take the first step alphabetically
            step = sorted(next)[0]
            self.complete(step)

            # 3. Determine the next step
            next = self.next_step()

        # 4. Did we complete all the steps
        if len(self.letters) != len(self.ordered):
            return None

        # 5. Return the steps as a string
        return ''.join(self.ordered)


    def part_two(self,
                 number=worker.DEFAULT_NUMBER,
                 seconds=worker.DEFAULT_SECONDS,
                 verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Track time and workers
        current = 0
        wrkrs = worker.Workers(number=number, seconds=seconds)

        # 1. Loop until there isn't a step
        next = self.next_step()
        while len(next) > 0:
            if verbose:
                print("time=%d, next=%s" % (current, next))

            # 2. Assign the tasks out
            wrkrs.assign_steps(current, sorted(next))

            # 3. Advance time to the next event
            wrkr = wrkrs.next_completion()
            if verbose:
                print("completion id=%d, step=%s, time=%d" % (wrkr.id, wrkr.step, wrkr.when))
            self.complete(wrkr.step)
            current = wrkr.when
            wrkr.finished()

            # 4. Determine the next step
            next = self.next_step()

        # 4. Did we complete all the steps
        if len(self.letters) != len(self.ordered):
            return None

        # 5. Return the current time
        return current


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           c p m . p y                          end
# ======================================================================
