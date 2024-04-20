
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         w o r k f l o w . p y
# ======================================================================
"Workflow for the Advent of Code 2023 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from rule import Rule, NOBRANCH

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LEFT_BRACE = "{"
RIGHT_BRACE = "}"
COMMA = ","

# ======================================================================
#                                                               Workflow
# ======================================================================


class Workflow(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Aplenty"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = ""
        self.rules = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Split the name off from the rules
        parts = text.split(LEFT_BRACE)
        assert len(parts) == 2

        # 2. Save the name
        self.name = parts[0]

        # 3. Get the and save the rules
        for part in parts[1].replace(RIGHT_BRACE, "").split(COMMA):
            self.rules.append(Rule(text=part, part2=self.part2))

    def evaluate(self, part):
        "Check the part against the workflow"

        # 1. Loop for all the rules in the workflow
        for rule in self.rules:

            # 2. Evaluate the part against this rule
            goto = rule.evaluate(part)

            # 3. If there is a branch, return it
            if goto != NOBRANCH:
                return goto

        # 4. Should never reach here
        assert False, f"No branch found in evaluating part at {self.name}"

    def get_rules(self):
        "Return the rules for this work flow"
        return self.rules

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      w o r k f l o w . p y                     end
# ======================================================================
