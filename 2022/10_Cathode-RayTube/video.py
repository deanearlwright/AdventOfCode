# ======================================================================
# Cathode-Ray Tube
#   Advent of Code 2022 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v i d e o . p y
# ======================================================================
"Video for the Advent of Code 2022 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
STRENGTH = [20, 60, 100, 140, 180, 220]

# ======================================================================
#                                                                  Video
# ======================================================================


class Video(object):   # pylint: disable=R0902, R0205
    "Object for Cathode-Ray Tube"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pc = 0  # pylint: disable=invalid-name
        self.cycle = 0
        self.x = 1  # pylint: disable=invalid-name

    def step(self):
        "Execute a single instruction"

        # 1. Have we run out of program?
        if self.pc >= len(self.text):
            return []

        # 2. Get the instruction
        instruction = self.text[self.pc]
        self.pc += 1

        # 3. Execute the instruction
        if instruction == "noop":
            self.cycle += 1
            return [self.x]
        if instruction.startswith("addx"):
            old_x = self.x
            value = int(instruction.split()[1])
            self.x += value
            self.cycle += 2
            return [old_x, self.x]

        # 4. What???
        print("step illegal instruction", self.pc - 1, instruction)
        return []

    def run(self):
        "Run the computer and return the values of x"

        # 1. Start with nothing
        history = [self.x]

        # 2. Run until the initial value is reached
        while True:
            more = self.step()
            if len(more) == 0:
                return history
            history.extend(more)

        # 3. Should never reach here
        print("run end", self.pc, self.cycle, self.x, len(history))
        return history

    def strength(self):
        "Return the signal strength"

        # 1. Start with nothing
        result = 0

        # 2. Get the running history
        history = self.run()

        # 3. Quick out if not enough history
        if len(history) < STRENGTH[-1]:
            return 0

        # 4. Loop for the important cycles
        for cycle in STRENGTH:

            # 5. Add in strength at this cycle
            value = history[cycle - 1]
            result += cycle * value

        # 6. Return the signal strength
        return result

    def draw(self):
        "Run the video computer and return the screen"

        # 1. Start with nothing
        result = []

        # 2. Get the x value for all the cycles
        history = self.run()

        # 3. Loop for each row
        for row in range(6):
            pixels = []
            offset = row * 40

            # 3. Loop for each pixel in the row
            for pixel in range(40):

                # 4. If x value matches (nearly) the pixel number, set it
                if history[offset + pixel] in [pixel, pixel - 1, pixel + 1]:
                    pixels.append('#')
                else:
                    pixels.append(".")

            # 5. Add the row to the result
            result.append("".join(pixels))

        return "\n".join(result)

    def reset(self):
        "Reset the computer"

        self.pc = 0
        self.cycle = 0
        self.x = 1


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         v i d e o . p y                        end
# ======================================================================
