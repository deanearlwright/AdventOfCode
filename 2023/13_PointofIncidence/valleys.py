
# ======================================================================
# Point of Incidence
#   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v a l l e y s . p y
# ======================================================================
"Valleys for the Advent of Code 2023 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from valley import Valley

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Valleys
# ======================================================================


class Valleys(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Point of Incidence"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.valleys = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Precondition axioms
        assert text is not None and len(text) > 0

        # 2. Start with nothing
        valley_text = []

        # 3. Loop for all the lines in the text
        for line in text:

            # 4. If this is a blank line, create and save the valley
            if not line:
                self.valleys.append(Valley(text=valley_text,
                                           part2=self.part2))
                valley_text = []
                continue

            # 5. Else add the line to the valley text
            valley_text.append(line)

        # 6. Save the final valley
        self.valleys.append(Valley(text=valley_text, part2=self.part2))

    def reflections(self):
        "Return the total reflection value"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the valleys
        for _, val in enumerate(self.valleys):

            # 3. Get the reflections for this valley
            ref = val.reflections()
            # print(f"{ref}")

            # 4. Add it into the total
            result += ref

        # 5. Return the sum of the reflections
        return result

    def corrected_reflections(self):
        "Return the total reflection value"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the valleys
        for _, val in enumerate(self.valleys):

            # 3. Get the reflections for this valley
            ref = val.corrected_reflections()

            # 4. Add it into the total
            result += ref

        # 5. Return the sum of the reflections
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       v a l l e y s . p y                      end
# ======================================================================
