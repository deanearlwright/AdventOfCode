
# ======================================================================
# Never Tell Me The Odds
#   Advent of Code 2023 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       h a i l s t o n e s . p y
# ======================================================================
"Hailstones for the Advent of Code 2023 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
import z3

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Position = namedtuple("Position", "px, py, pz")
Velocity = namedtuple("Velocity", "vx, vy, vz")
Hailstone = namedtuple("Hailstore", "pos, vel")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Hailstones
# ======================================================================


class Hailstones(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Never Tell Me The Odds"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.hailstones = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Loop for each line in the text
        for line in text:

            # 2. Separate the position from the velocity
            position, velocity = line.split(" @ ")

            # 3. Separate the indivitual integers
            pos = [int(p) for p in position.split(",")]
            pos = Position(*[int(p) for p in position.split(",")])
            vel = Velocity(*[int(v) for v in velocity.split(",")])

            # 4. Create a Hailstone
            hailstone = Hailstone(pos=pos, vel=vel)

            # 5. Add it to the other hailstones
            self.hailstones.append(hailstone)

    def xyintersections(self, test_low=0, test_high=0):
        "Return the number of hailstones future paths that cross inside the test boundary"

        # 1. Adjust the boundaries (if necessary)
        if test_low == test_high:
            if len(self.hailstones) == 5:
                test_low, test_high = 7, 27
            else:
                test_low, test_high = 200000000000000, 400000000000000

        # 2. Start with nothing
        result = 0

        # 3. Loop for the pairs of hailstones
        for findx, first in enumerate(self.hailstones[:-1]):
            for second in self.hailstones[findx:]:

                # 4. Calcalulate an intersection between the two hailstones
                try:
                    inter_y = (second.pos.px - (second.vel.vx / second.vel.vy * second.pos.py) +
                               (first.vel.vx / first.vel.vy * first.pos.py) - first.pos.px) / (
                        first.vel.vx / first.vel.vy - second.vel.vx / second.vel.vy
                    )
                    inter_x = (((inter_y - first.pos.py) / first.vel.vy) *
                               first.vel.vx + first.pos.px)

                    # 5. Check that it is the test area
                    if (
                        test_low <= inter_x <= test_high
                        and test_low <= inter_y <= test_high
                    ):
                        # 6. Is it really, really in the test area?
                        if (
                            (Hailstones.sign(inter_x - first.pos.px)
                             == Hailstones.sign(first.vel.vx))
                            and (Hailstones.sign(inter_y - first.pos.py)
                             == Hailstones.sign(first.vel.vy))
                            and (Hailstones.sign(inter_x - second.pos.px)
                             == Hailstones.sign(second.vel.vx))
                            and (Hailstones.sign(inter_y - second.pos.py)
                             == Hailstones.sign(second.vel.vy))
                        ):
                            # 7. It is, increment the number of intersections
                            result += 1

                # 8. Don't let something as simple as a zero velocity get in the way of progress
                except ZeroDivisionError:
                    pass

        # 9. Return the total number of observations within the test area
        return result

    @staticmethod
    def sign(number):
        "Returns the sign of the number: -1, 0, or 1"

        if number > 0:
            return 1
        if number < 0:
            return -1
        return 0

    def xyzintersections(self):
        "Return the starting coordicates of a rock to destroy all the hailstones"

        # 1. Create the solver
        solver = z3.Solver()
        posx, posy, posz, velx, vely, velz = [z3.Int(var) for var in
                                              ["posx", "posy", "posz", "velx", "vely", "velz"]]

        # 2. Use only the first three hailstones to determine the solution
        for hindx, hailstone in enumerate(self.hailstones[:3]):

            time = z3.Int(f"time{hindx}")
            solver.add(time >= 0)
            solver.add(posx + velx * time == hailstone.pos.px + hailstone.vel.vx * time)
            solver.add(posy + vely * time == hailstone.pos.py + hailstone.vel.vy * time)
            solver.add(posz + velz * time == hailstone.pos.pz + hailstone.vel.vz * time)

        # 3. If it lools good, solve it
        if solver.check() == z3.sat:
            model = solver.model()
            (posx, posy, posz) = (model.eval(posx), model.eval(posy), model.eval(posz))
            return posx.as_long() + posy.as_long() + posz.as_long()

        # 4. This should have worked!
        print("Not satisified")
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    h a i l s t o n e s . p y                   end
# ======================================================================
