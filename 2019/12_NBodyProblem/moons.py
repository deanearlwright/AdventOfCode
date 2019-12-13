# ======================================================================
# The N-Body Problem
#   Advent of Code 2019 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            m o o n s . p y
# ======================================================================
"Multiple moons for The N-Body Problem for Advent of Code 2019 Day 12"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import moon

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Moons
# ======================================================================


class Moons():
    """Object representing multiple moons"""

    def __init__(self, text=None):

        # 1. Start with very few moons
        self.moons = []

        # 2. If we have text, create moons and add to list
        if text is not None:

            # 3. Loop for each line of text
            for line in text:

                # 4. Create a new orbiting body
                body = moon.Moon(text=line)

                # 5. Add this moon to the list
                self.moons.append(body)


    def __str__(self):

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the moons
        for body in self.moons:

            # 3. Add this moon to the result
            result.append(str(body))

        # 4. Return all the moons
        return '\n'.join(result)

    def total_energy(self):
        "Return the total enery in the system"

        # 1. Start with nothing
        return sum([_.energy() for _ in self.moons])

    def run(self, watch=False, steps=0):
        "Run the system for a specified number of steps"

        # 1. Loop until number of steps reached
        tick = 0
        while steps < 0 or tick < steps:

            # 2. Loop for each of the moons
            for moon_num, one_moon in enumerate(self.moons):

                # 3. Loop for the remaining moons
                for other_moon in self.moons[moon_num:]:

                    # 4. Compute the effect that these two bodies have on each other
                    one_moon.apply_gravity(other_moon)

            # 5. Loop for each of the moons (again)
            for one_moon in self.moons:

                # 6. Apply the delta in velocity
                one_moon.update_velocity_and_position()

            # 7. Increment the cosmic clock
            tick += 1

            # 8. If desired, Show the current start of the system
            if watch:
                print("After %d steps:" % (tick))
                print(str(self))

        # 4. Return number of steps
        return tick

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         h u l l . p y                          end
# ======================================================================
