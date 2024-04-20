
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        w o r k f l o w s . p y
# ======================================================================
"Workflows for the Advent of Code 2023 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

from workflow import Workflow

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
START = "in"
FINAL = "AR"
ACCEPT = "A"
REJECT = "R"
LESS = "<"
MORE = ">"

# ----------------------------------------------------------------------
#                                                                  Types
# ----------------------------------------------------------------------
Range = namedtuple('Range', 'low high')
State = namedtuple('State', 'name x m a s')


def len_range(rnge):
    "Return the length of the range"
    return 1 + rnge.high - rnge.low


def len_state(state):
    "Return the product of the ranges in the search state"
    return (len_range(state.x) * len_range(state.m) *
            len_range(state.a) * len_range(state.s))

# ======================================================================
#                                                              Workflows
# ======================================================================


class Workflows(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Aplenty"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        if text is None:
            self.text = []
        else:
            self.text = text
        self.workflows = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Loop for each line of the text
        for line in text:

            # 2. Create and add a workflow
            new_wf = Workflow(text=line, part2=self.part2)
            name = new_wf.name
            assert name not in self.workflows
            self.workflows[name] = new_wf

    def add_workflow(self, text):
        "Add an additional workflow"

        # 1. Add the text and new workflow
        self.text.append(text)
        new_wf = Workflow(text=text, part2=self.part2)
        name = new_wf.name
        assert name not in self.workflows
        self.workflows[name] = new_wf

        # 2. Return the name of the new workflow
        return name

    def evaluate(self, part):
        "Evaluate the part returning A or R"

        # 0. Precondition axioms
        assert START in self.workflows

        # 1. Start at the very beginning
        state = START
        states = [state]

        # 2. Loop until we reach a final state
        while state not in FINAL:

            # 3. Test the part against the specified workflow
            assert state in self.workflows, f"{state} not in workflows"
            state = self.workflows[state].evaluate(part)
            states.append(state)

        # 4. Add the terminal state (last of the states)
        return state

    def combinations(self):
        "Return the number of part combinations"

        # 1. Start at the beginning
        searches = [State(name=START,
                          x=Range(low=1, high=4000),
                          m=Range(low=1, high=4000),
                          a=Range(low=1, high=4000),
                          s=Range(low=1, high=4000))]
        result = 0

        # 2. Loop while there is something to search
        while searches:

            # 3. Get the most recent search
            search = searches.pop()
            ranges = {
                "x": search.x,
                "m": search.m,
                "a": search.a,
                "s": search.s,
            }

            # 4. Have we reached a terminal state?
            name = search.name
            if name == REJECT:
                continue
            if name == ACCEPT:
                result += len_state(search)
                continue

            # 5. Loop for the rules in the named workflow
            for rule in self.workflows[name].get_rules():
                rule_category = rule.category
                rule_test = rule.test
                rule_value = rule.value
                rule_branch = rule.branch

                # 6. Adjust the ranges based on the test (if any)
                new_ranges = ranges.copy()
                if rule_test == LESS:
                    new_ranges[rule_category] = \
                        Range(low=new_ranges[rule_category].low, high=rule_value - 1)
                    ranges[rule_category] = Range(low=rule_value, high=ranges[rule_category].high)
                elif rule_test == MORE:
                    new_ranges[rule_category] = \
                        Range(low=rule_value + 1, high=new_ranges[rule_category].high)
                    ranges[rule_category] = Range(low=ranges[rule_category].low, high=rule_value)

                # 7. Add a new search to explore
                searches.append(State(name=rule_branch,
                                      x=new_ranges["x"],
                                      m=new_ranges["m"],
                                      a=new_ranges["a"],
                                      s=new_ranges["s"]))

        # 8. Return the combinations of ratings
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     w o r k f l o w s . p y                    end
# ======================================================================
