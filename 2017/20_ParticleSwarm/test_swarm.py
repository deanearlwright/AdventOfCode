# ======================================================================
# Particle Swarm
#   Advent of Code 2017 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s w a r m . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 20, Particle Swarm"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import swarm

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
"""
PART_ONE_TEXT = EXAMPLE_TEXT

PART_TWO_TEXT = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
"""

PART_ONE_RESULT = 0

PART_TWO_RESULT = 1

# ======================================================================
#                                                               Particle
# ======================================================================


class TestParticle(unittest.TestCase):  # pylint: disable=R0904
    "Test Particle object"

    def test_empty_init(self):
        "Test the default particle creation"

        # 1. Create default Particle object
        myobj = swarm.Particle()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.position, (0, 0, 0))
        self.assertEqual(myobj.velocity, (0, 0, 0))
        self.assertEqual(myobj.acceleration, (0, 0, 0))

        # 3. Test methods
        self.assertEqual(myobj.manhattan_distance(), 0)

    def test_text_init(self):
        "Test the Particle object creation from text"

        # 1. Create Swarm object from text
        myobj = swarm.Particle(text="p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.position, (3, 0, 0))
        self.assertEqual(myobj.velocity, (2, 0, 0))
        self.assertEqual(myobj.acceleration, (-1, 0, 0))

        # 3. Test methods
        self.assertEqual(myobj.manhattan_distance(), 3)
        myobj.tick()
        self.assertEqual(myobj.position, (4, 0, 0))
        self.assertEqual(myobj.velocity, (1, 0, 0))
        self.assertEqual(myobj.acceleration, (-1, 0, 0))
        self.assertEqual(myobj.manhattan_distance(), 4)

# ======================================================================
#                                                                  Swarm
# ======================================================================


class TestSwarm(unittest.TestCase):  # pylint: disable=R0904
    "Test Swarm object"

    def test_empty_init(self):
        "Test the default Swarm creation"

        # 1. Create default Swarm object
        myobj = swarm.Swarm()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.particles), 0)
        self.assertEqual(myobj.clock, 0)

        # 3. Test methods
        myobj.tick()
        self.assertEqual(myobj.clock, 1)
        self.assertEqual(myobj.closest(), None)

    def test_text_init(self):
        "Test the Swarm object creation from text"

        # 1. Create Swarm object from text
        myobj = swarm.Swarm(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.particles), 2)
        self.assertEqual(myobj.clock, 0)
        self.assertEqual(myobj.particles[0].position, (3, 0, 0))
        self.assertEqual(myobj.particles[0].velocity, (2, 0, 0))
        self.assertEqual(myobj.particles[0].acceleration, (-1, 0, 0))
        self.assertEqual(myobj.particles[1].position, (4, 0, 0))
        self.assertEqual(myobj.particles[1].velocity, (0, 0, 0))
        self.assertEqual(myobj.particles[1].acceleration, (-2, 0, 0))

        # 3. Test methods
        self.assertEqual(myobj.closest(), 0)
        myobj.tick()
        self.assertEqual(myobj.clock, 1)
        self.assertEqual(myobj.particles[0].position, (4, 0, 0))
        self.assertEqual(myobj.particles[0].velocity, (1, 0, 0))
        self.assertEqual(myobj.particles[0].acceleration, (-1, 0, 0))
        self.assertEqual(myobj.particles[1].position, (2, 0, 0))
        self.assertEqual(myobj.particles[1].velocity, (-2, 0, 0))
        self.assertEqual(myobj.particles[1].acceleration, (-2, 0, 0))
        self.assertEqual(myobj.closest(), 1)
        myobj.tick()
        self.assertEqual(myobj.clock, 2)
        self.assertEqual(myobj.particles[0].position, (4, 0, 0))
        self.assertEqual(myobj.particles[0].velocity, (0, 0, 0))
        self.assertEqual(myobj.particles[0].acceleration, (-1, 0, 0))
        self.assertEqual(myobj.particles[1].position, (-2, 0, 0))
        self.assertEqual(myobj.particles[1].velocity, (-4, 0, 0))
        self.assertEqual(myobj.particles[1].acceleration, (-2, 0, 0))
        self.assertEqual(myobj.closest(), 1)
        myobj.tick()
        self.assertEqual(myobj.clock, 3)
        self.assertEqual(myobj.particles[0].position, (3, 0, 0))
        self.assertEqual(myobj.particles[0].velocity, (-1, 0, 0))
        self.assertEqual(myobj.particles[0].acceleration, (-1, 0, 0))
        self.assertEqual(myobj.particles[1].position, (-8, 0, 0))
        self.assertEqual(myobj.particles[1].velocity, (-6, 0, 0))
        self.assertEqual(myobj.particles[1].acceleration, (-2, 0, 0))
        self.assertEqual(myobj.closest(), 0)

    def test_part_one(self):
        "Test part one example of Swarm object"

        # 1. Create Spinlock object from text
        myobj = swarm.Swarm(text=aoc_20.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=True), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Swarm object"

        # 1. Create Spinlock object from text
        myobj = swarm.Swarm(part2=True, text=aoc_20.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=True), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ s w a r m . p y                end
# ======================================================================
