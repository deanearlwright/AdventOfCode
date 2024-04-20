
# ======================================================================
# Cube Conundrum
#   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g a m e . p y
# ======================================================================
"Game for the Advent of Code 2023 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Game
# ======================================================================


class Game(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Cube Conundrum"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.id = 0
        self.pulls = []
        self.max = {"red": 0, "blue": 0, "green": 0}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Check if a Game
        if not text.startswith("Game"):
            print(f"Invalid Game --> {text}")
            return

        # 2. Get game number
        text = text[4:]
        parts = text.split(":")
        self.id = int(parts[0])
        text = parts[1].strip()

        # 3. Break up into pulls
        for pull in text.split(";"):
            #print(f"pull = {pull}")
            single_pull = {}

            # 4. Break the pull into pairs
            for pair in pull.split(","):
                #print(f"pair = {pair}")
                parts = pair.strip().split(" ")
                number = int(parts[0])
                color = parts[1].strip()

                # 5. Add to the single pull
                single_pull[color] = number

                # 6. Updated maximums
                if self.max[color] < number:
                    self.max[color] = number

            # 7. Add the single pull
            self.pulls.append(single_pull)

    def possible(self, red, green, blue):
        "Is it possible: no maximum exceeds given number"

        return red >= self.max["red"] and green >= self.max["green"] and blue >= self.max["blue"]

    def power_set(self):
        "Return the power set (prod of maximums)"

        return self.max["red"] * self.max["green"] * self.max["blue"]

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      g a m e . p y                     end
# ======================================================================
