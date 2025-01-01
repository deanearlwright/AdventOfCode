
# ======================================================================
# Red-Nosed Reports
#   Advent of Code 2024 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e p o r t s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import report

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Reports
# ======================================================================


class Reports(object):   # pylint: disable=R0902, R0205
    "Object for Red-Nosed Reports"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.reports = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for each line of text
        for line in text:

            # 2. Create a report from that line
            a_report = report.Report(text=line, part2=self.part2)

            # 3. Append it to the list of reports
            self.reports.append(a_report)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the reports
        for one_report in self.reports:

            # 3. Increment the result if safe
            if one_report.is_safe():
                result += 1

        # 4. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the reports
        for one_report in self.reports:

            # 3. Increment the result if safe
            if one_report.is_safe_two():
                result += 1

        # 4. Return the solution for part two
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       r e p o r t s . p y                      end
# ======================================================================
