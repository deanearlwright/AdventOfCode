
# ======================================================================
# Claw Contraption
#   Advent of Code 2024 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m a c h i n e . p y
# ======================================================================
"Machine for the Advent of Code 2024 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MAX_PRESSES = 100
PART2_PRIZE = 10000000000000

# ======================================================================
#                                                                Machine
# ======================================================================


class Machine(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Claw Contraption"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.buttons = []
        self.prize = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0
        assert len(text) == 3
        assert text[0].startswith("Button A:")
        assert text[1].startswith("Button B:")
        assert text[2].startswith("Prize:")

        # 1. Process button A:
        parts = text[0].split()
        self.buttons.append((int(parts[2][2:-1]), int(parts[3][2:])))

        # 2. Process button B:
        parts = text[1].split()
        self.buttons.append((int(parts[2][2:-1]), int(parts[3][2:])))

        # 3. Prize:
        parts = text[2].split()
        self.prize = (int(parts[1][2:-1]), int(parts[2][2:]))

        # 4. Part 2 moves the prize
        if self.part2:
            self.prize = (PART2_PRIZE + self.prize[0], PART2_PRIZE + self.prize[1])

    def brute_presses(self):
        "Determine the number of presses by brute force"

        # 1. Loop for all the possible A presses
        for a_presses in range(MAX_PRESSES):
            a_moves = (a_presses * self.buttons[0][0], a_presses * self.buttons[0][1])
            if a_moves[0] > self.prize[0] or a_moves[1] > self.prize[1]:
                break

            # 2. Loop for all the possible B presses
            for b_presses in range(MAX_PRESSES):
                b_moves = (a_moves[0] + b_presses * self.buttons[1][0],
                           a_moves[1] + b_presses * self.buttons[1][1])
                if b_moves[0] > self.prize[0] or b_moves[1] > self.prize[1]:
                    break

                # 3. Are we there yet?
                if b_moves == self.prize:
                    return (a_presses, b_presses)

        # 4. Never got to the prize (this game is rigged)
        return (0, 0)

    def brute_tokens(self):
        "Determine the number of tokens by brute force"

        # 1. Determine the number of presses needed
        ab_presses = self.brute_presses()

        # 2. Return the cost in tokens
        return 3 * ab_presses[0] + ab_presses[1]

    @staticmethod
    def cramer_two(a, b, c, d, e, f):  # pylint: disable=C0103, R0913
        "Solve 2x2 linear equations of the form ax+by=e and cx+dy=f"

        # 1. Calculate the determinat
        deteterminat = a * d - b * c
        if deteterminat == 0:
            return (0, 0)

        # 2. Solve for x and y
        x = (e * d - b * f) / deteterminat  # pylint: disable=C0103
        y = (a * f - e * c) / deteterminat  # pylint: disable=C0103

        # 3. Return the result
        return (x, y)

    def presses(self):
        """Determines the number of button presses to reach the prize

        Button A is pressed x times and button B is pressed y times

           button[0][0]*x + button[1][0]*y = prize[0]
            button[0][1]*x + button[1][1]*y = prize[1]

        Integer number of presses only
        """

        # 1. Solve the equations
        cramer = Machine.cramer_two(self.buttons[0][0], self.buttons[1][0],
                                    self.buttons[0][1], self.buttons[1][1],
                                    self.prize[0], self.prize[1])

        # 2. Ensure integer solutions
        int_cramer = (int(cramer[0]), int(cramer[1]))
        if cramer[0] != int_cramer[0] or cramer[1] != int_cramer[1]:
            return (0, 0)

        # 3. Return the integer solution
        return int_cramer

    def tokens(self):
        "Determine the number of token needed (0 if impossible)"

        # 1. Determine the number of presses needed
        ab_presses = self.presses()

        # 2. Return the cost in tokens
        return 3 * ab_presses[0] + ab_presses[1]

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       m a c h i n e . p y                      end
# ======================================================================
