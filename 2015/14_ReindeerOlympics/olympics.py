# ======================================================================
# Reindeer Olympics
#   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         o l y m p i c s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import reindeer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RACE_TIME = 2503

# ======================================================================
#                                                               Olympics
# ======================================================================


class Olympics(object):   # pylint: disable=R0902, R0205
    "Object for Reindeer Olympics"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.reindeer = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in self.text:
                new_deer = reindeer.Reindeer(text=line, part2=self.part2)
                self.reindeer[new_deer.name] = new_deer

    def start(self):
        "Initialize all of the reindeer"
        for deer in self.reindeer.values():
            deer.start()

    def tick(self):
        "Advance the time for all of the reindeer"
        for deer in self.reindeer.values():
            deer.tick()
        for deer in self.furthest():
            deer.add_point()

    def furthest(self):
        "Returns the reindeer or multiple reindeer that has traveled the furthest"
        result = []
        distance = 0
        for deer in self.reindeer.values():
            if deer.distance > distance:
                distance = deer.distance
                result = [deer]
            elif deer.distance == distance:
                result.append(deer)
        return result

    def pointiest(self):
        "Returns the reindeer or multiple reindeer that have the most points"
        result = []
        points = 0
        for deer in self.reindeer.values():
            if deer.points > points:
                points = deer.points
                result = [deer]
            elif deer.points == points:
                result.append(deer)
        return result

    def race(self, race_time=RACE_TIME):
        "Run a race"

        # 1. On your marks, get set. ...
        self.start()

        # 2. Go!
        for _ in range(race_time):
            self.tick()

        # 3. Return the result of the race
        if self.part2:
            return self.pointiest()[0].points
        return self.furthest()[0].distance

    def part_one(self, verbose=False, limit=0, race_time=RACE_TIME):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.race(race_time=race_time)

    def part_two(self, verbose=False, limit=0, race_time=RACE_TIME):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.race(race_time=race_time)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      o l y m p i c s . p y                     end
# ======================================================================
