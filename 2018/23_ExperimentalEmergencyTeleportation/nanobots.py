# ======================================================================
# Experimental Emergency Teleportation
#   Advent of Code 2018 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# The solution for part 2 was inspired by the on by seligman99 in
# www.reddit.com/r/adventofcode/comments/a8s17l/2018_day_23_solutions/
# I though about trying to use z3 but my brain wasn't up for it
# ======================================================================

# ======================================================================
#                         n a n o b o t s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Nanobot
# ======================================================================


class Nanobot(object):   # pylint: disable=R0902, R0205
    "Object for Experimental Emergency Teleportation"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.x = None
        self.y = None
        self.z = None
        self.r = None

        # 2. Process the text (if any)
        if text is not None and len(text) > 0:
            #pos=<0,0,0>, r=4
            parts = text.replace('=', ' ').replace(',', ' ').replace('<','').replace('>','').split(' ')
            self.x = int(parts[1])
            self.y = int(parts[2])
            self.z = int(parts[3])
            self.r = int(parts[6])

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def in_range(self, other):
        return self.manhattan_distance(other) <= self.r


# ======================================================================
#                                                               Nanobots
# ======================================================================


class Nanobots(object):   # pylint: disable=R0902, R0205
    "Object for Experimental Emergency Teleportation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.bots = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.bots.append(Nanobot(text=line))

    def largest_signal_radius(self):
        # 1. If no bots, not much of a choice
        if not self.bots:
            return None
        # 2. Assume the first is the greatest
        result = self.bots[0]
        # 3. Loop for all the bots
        for bot in self.bots:
            # 4. If this bot has a stronger signal, save it
            if bot.r > result.r:
                result = bot
        # 5. Return the bot with the strongest signal
        return result

    def bots_in_range(self, bot):
        # 1. Start with none
        result = 0
        # 2. Loop for all the bots
        for other in self.bots:
            # 3. If this bot is in range, increment count
            if bot.in_range(other):
                result += 1
        # 4. Return the number of bots in range
        return result

    def seligman99(self):
        # 1. Find the range of the bots
        xs = [b.x for b in self.bots] + [0]
        ys = [b.y for b in self.bots] + [0]
        zs = [b.z for b in self.bots] + [0]

        # 2. Pick a starting resolution big enough ti find all of the bots (powers of two)
        dist = 1
        while dist < max(xs) - min(xs) or dist < max(ys) - min(ys) or dist < max(zs) - min(zs):
            dist *= 2

        # 3. Offset to there are no strange issues wrapping around zero
        ox = -min(xs)
        oy = -min(ys)
        oz = -min(zs)

        # 4. Try to find all of the bots, backing off with a bin search until we get most of them
        span = 1
        while span < len(self.bots):
            span *= 2
        forced_check = 1
        tried = {}

        best_val, best_count = None, None

        while True:
            # We might try the same value multiple times, save some time if we've seen it already
            if forced_check not in tried:
                tried[forced_check] = self.seligman99_find(set(), xs, ys, zs, dist, ox, oy, oz, forced_check)
            test_val, test_count = tried[forced_check]

            if test_val is None:
                # Nothing found at this level, so go back
                if span > 1:
                    span = span // 2
                forced_check = max(1, forced_check - span)
            else:
                # We found something, so go forward
                if best_count is None or test_count > best_count:
                    best_val, best_count = test_val, test_count
                if span == 1:
                    # This means we went back one, and it was empty, so we're done!
                    break
                forced_check += span

        print("The max count I found was: " + str(best_count))
        return best_val

    def seligman99_find(self, done, xs, ys, zs, dist, ox, oy, oz, forced_count):
        at_target = []

        for x in range(min(xs), max(xs)+1, dist):
            for y in range(min(ys), max(ys)+1, dist):
                for z in range(min(zs), max(zs)+1, dist):

                    # See how many bots are possible
                    count = 0
                    for bot in self.bots:
                        bx = bot.x
                        by = bot.y
                        bz = bot.z
                        bdist = bot.r
                        if dist == 1:
                            calc = abs(x - bx) + abs(y - by) + abs(z - bz)
                            if calc <= bdist:
                                count += 1
                        else:
                            calc =  abs((ox+x) - (ox+bx))
                            calc += abs((oy+y) - (oy+by))
                            calc += abs((oz+z) - (oz+bz))
                            # The minus three is to include the current box
                            # in any bots that are near it
                            if calc //dist - 3 <= (bdist) // dist:
                                count += 1

                    if count >= forced_count:
                        at_target.append((x, y, z, count, abs(x) + abs(y) + abs(z)))

        while len(at_target) > 0:
            best = []
            best_i = None

            # Find the best candidate from the possible boxes
            for i in range(len(at_target)):
                if best_i is None or at_target[i][4] < best[4]:
                    best = at_target[i]
                    best_i = i

            if dist == 1:
                # At the end, just return the best match
                return best[4], best[3]
            else:
                # Search in the sub boxes, see if we find any matches
                xs = [best[0], best[0] + dist//2]
                ys = [best[1], best[1] + dist//2]
                zs = [best[2], best[2] + dist//2]
                a, b = self.seligman99_find(done, xs, ys, zs, dist // 2, ox, oy, oz, forced_count)
                if a is None:
                    # This is a false path, remove it from consideration and try any others
                    at_target.pop(best_i)
                else:
                    # We found something, go ahead and let it bubble up
                    return a, b

        # This means all of the candidates yeild false paths, so let this one
        # be treated as a false path by our caller
        return None, None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.bots_in_range(self.largest_signal_radius())


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.seligman99()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      n a n o b o t s . p y                     end
# ======================================================================
