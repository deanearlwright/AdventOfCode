
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           s o r t e r . p y
# ======================================================================
"Sorter for the Advent of Code 2023 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from part import Part
from workflows import Workflows

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LEFT_BRACE = "{"
ACCEPTED = "A"

# ======================================================================
#                                                                 Sorter
# ======================================================================


class Sorter(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Aplenty"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.workflows = None
        self.parts = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Create a workflow
        self.workflows = Workflows(text=None, part2=self.part2)

        # 1. Loop for each line in the text
        for line in text:

            # 2. If the line starts with a left brace, it is a part
            if line.startswith(LEFT_BRACE):
                self.parts.append(Part(text=line, part2=self.part2))
                continue

            # 3. Add the workflow
            self.workflows.add_workflow(line)

    def evaluate_all(self):
        "Evaluate all parts and return the accepted total"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all parts
        for part in self.parts:

            # 3. Evalute the part
            final = self.workflows.evaluate(part)

            # 4. If the part is accepted, accumulate the total
            if final == ACCEPTED:
                result += part.total()

        # 5. Return the total of the accepted parts
        return result

    def combinations(self):
        "Return the number of part combinations"
        return self.workflows.combinations()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o r t e r . p y                       end
# ======================================================================
