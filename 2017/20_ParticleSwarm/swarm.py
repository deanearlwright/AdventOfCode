# ======================================================================
# Particle Swarm
#   Advent of Code 2017 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s w a r m . p y
# ======================================================================
"A solver for swarm for Advent of Code 2017 Day 20"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
P_NUMS = '<( *-?[0-9]*),( *-?[0-9]*),( *-?[0-9]*)>'
PARTICLE = re.compile('^p=%s, v=%s, a=%s$' % (P_NUMS, P_NUMS, P_NUMS))

LONG_TERM = 1000

# ======================================================================
#                                                               Particle
# ======================================================================


class Particle(object):   # pylint: disable=R0902, R0205
    "Object for a single Particle"

    def __init__(self, text=None):
        """For each particle, it provides the X, Y, and Z coordinates for the
        particle's position (p), velocity (v), and acceleration (a), each in the
        format <X,Y,Z>."""

        # 1. Set the default values
        self.position = (0, 0, 0)
        self.velocity = (0, 0, 0)
        self.acceleration = (0, 0, 0)

        # 2. Set specific values based on text (if given)
        if text:
            matches = PARTICLE.match(text)
            if matches:
                self.position = (int(matches.group(1)),
                                 int(matches.group(2)),
                                 int(matches.group(3)))
                self.velocity = (int(matches.group(4)),
                                 int(matches.group(5)),
                                 int(matches.group(6)))
                self.acceleration = (int(matches.group(7)),
                                     int(matches.group(8)),
                                     int(matches.group(9)))
            else:
                print("Invalid particle text: %s" % (text))

    def tick(self):
        """Move the particle after adjusting for acceleration"""

        # 1. Increase velocity by acceleration
        self.velocity = (self.velocity[0] + self.acceleration[0],
                         self.velocity[1] + self.acceleration[1],
                         self.velocity[2] + self.acceleration[2])

        # 2. Increase position by velocity
        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1],
                         self.position[2] + self.velocity[2])

    def manhattan_distance(self):
        """Taxicab distance from the origin"""
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def collide(self, other):
        """Are these two particles at the same place"""

        return self.position == other.position

# ======================================================================
#                                                                  Swarm
# ======================================================================


class Swarm(object):   # pylint: disable=R0902, R0205
    "Object for Particle Swarm"

    def __init__(self, steps=None, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.particles = []
        self.clock = 0

        # 2. Process text (if any)
        if text is not None:
            for line in self.text:
                self.particles.append(Particle(text=line))

    def tick(self):
        """Move the all the particles"""

        # 1. Move the particles
        for part in self.particles:
            part.tick()

        # 2. And advance the clock
        self.clock += 1

    def closest(self):
        """Which particle is closest to the origin?"""

        # 1. Can to much if no particles
        if not self.particles:
            return None

        # 2. Assume the first is closest
        min_dist = self.particles[0].manhattan_distance()
        result = 0

        # 3. Loop for the rest
        for pnum, part in enumerate(self.particles[1:]):

            # 4. If this one is closer, save it
            part_dist = part.manhattan_distance()
            if part_dist < min_dist:
                min_dist = part_dist
                result = pnum + 1

        # 4. Return the number of the closest particle
        return result

    def remove_collisions(self):
        "Remove particles that are at the same place at the same time"

        # 1. Assume no collisions
        remove = set()

        # 2. Loop for all of the particles
        for pnum, part in enumerate(self.particles):

            # 3. Loop for the rest of the particles
            for other in self.particles[pnum+1:]:

                # 4. Do these particles collide?
                if part.collide(other):

                    # 5. Yes, Can't keep them
                    remove.add(part.position)
                    break

        # 6. If no collisions, we are done here
        if not remove:
            return False

        # 7. Keep only the particles at non-colliding locations
        keeping = []
        for part in self.particles:
            if part.position not in remove:
                keeping.append(part)
        self.particles = keeping

        # 8. Indicate that we had a collision
        return True



    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"


        # 1. Start with the closest particle
        result = self.closest()
        if result == None:
            return None
        ticks_closest = 0
        if verbose:
            print("Starting with particle %d as the closest" % (result))


        # 2. Loop forever
        while True:

            # 3. Advance all of the particles
            self.tick()

            # 4. Who is the closest now
            now_closest = self.closest()

            # 5. If it is a new particle, record it
            if now_closest != result:
                result = now_closest
                ticks_closest = 0
                if verbose:
                    print("At time %d, closest is now %d" % (self.clock, result))

            # 6. Else check if has been the closest long enough
            else:
                ticks_closest += 1
                if ticks_closest >= LONG_TERM:
                    if verbose:
                        print("%d has remained the closest for %d ticks" % (result, ticks_closest))
                    return result

            # 7. Check if this has gone on too long
            if self.clock > limit > 0:
                if verbose:
                    print("Stopping at time %d with %d as the closest" % (self.clock, result))
                break

        # 8. No particle was the closest long enough
        return None


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Start with the a simulated collistion
        ticks_since_last_collision = 0
        if verbose:
            print("Starting out with %d particles" % (len(self.particles)))

        # 2. Loop forever
        while True:

            # 3. Advance all of the particles
            self.tick()

            # 4. Remove any collisions
            collided = self.remove_collisions()

            # 5. If there was a collision, record it
            if collided:
                ticks_since_last_collision = 0
                if verbose:
                    print("There was a collision at time %d, now only %d particles" %
                          (self.clock, len(self.particles)))

            # 6. Else check if has been the closest long enough
            else:
                ticks_since_last_collision += 1
                if ticks_since_last_collision >= LONG_TERM:
                    if verbose:
                        print("There have been no collisions with %d particles for %d ticks" %
                              (len(self.particles), ticks_since_last_collision))
                    return len(self.particles)

            # 7. Check if this has gone on too long
            if self.clock > limit > 0:
                if verbose:
                    print("Stopping at time %d with %d particles" %
                          (self.clock, len(self.particles)))
                break

        # 8. Haven't gone long enough with no collisions
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s w a r m . p y                     end
# ======================================================================
