# ======================================================================
# The Sum of Its Parts
#   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ w o r k e r . p y
# ======================================================================
"Test worker for Advent of Code 2018 day 07, The Sum of Its Parts"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import worker

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             TestWorker
# ======================================================================


class TestWorker(unittest.TestCase):  # pylint: disable=R0904
    "Test Worker object"

    def test_empty_init(self):
        "Test the default Worker creation"

        # 1. Create default Worker object
        myobj = worker.Worker()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.id, None)
        self.assertEqual(myobj.step, None)
        self.assertEqual(myobj.when, None)

    def test_init_with_letter(self):
        "Test the Worker creation with an argument"

        # 1. Create default Worker object
        myobj = worker.Worker(id=1)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.id, 1)
        self.assertEqual(myobj.step, None)
        self.assertEqual(myobj.when, None)

        # 3. Walk through the solution
        myobj.assign_task('C', 64)
        self.assertEqual(myobj.step, 'C')
        self.assertEqual(myobj.when, 64)

# ======================================================================
#                                                            TestWorkers
# ======================================================================


class TestWorkers(unittest.TestCase):  # pylint: disable=R0904
    "Test Workers object"

    def test_empty_init(self):
        "Test the default Worker creation"

        # 1. Create default Workers object
        myobj = worker.Workers()

        # 2. Make sure it has the default values
        self.assertEqual(len(myobj.workers), worker.DEFAULT_NUMBER)
        self.assertEqual(myobj.workers[0].id, 1)
        self.assertEqual(myobj.workers[0].step, None)
        self.assertEqual(myobj.workers[0].when, None)

    def test_init_with_letter(self):
        "Test the Workers creation with an argument"

        # 1. Create default Worker object
        myobj = worker.Workers(number=2, seconds=0)

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.workers), 2)
        self.assertEqual(myobj.workers[0].id, 1)
        self.assertEqual(myobj.workers[0].step, None)
        self.assertEqual(myobj.workers[0].when, None)

        # 3. Walk through the part 2 example
        # 3a. Time 0
        wrkr = myobj.idle_worker()
        self.assertEqual(wrkr.id, 1)
        wrkr.assign_task('C', 3)
        self.assertEqual(myobj.idle_worker().id, 2)

        # 3b. Time 3
        wrkr = myobj.next_completion()
        self.assertEqual(wrkr.id, 1)
        self.assertEqual(wrkr.step, 'C')
        self.assertEqual(wrkr.when, 3)
        wrkr.finished()
        myobj.assign_steps(3, ['A', 'F'])
        self.assertEqual(myobj.idle_worker(), None)
        wrkr = myobj.workers[0]
        self.assertEqual(wrkr.id, 1)
        self.assertEqual(wrkr.step, 'A')
        self.assertEqual(wrkr.when, 4)
        wrkr = myobj.workers[1]
        self.assertEqual(wrkr.id, 2)
        self.assertEqual(wrkr.step, 'F')
        self.assertEqual(wrkr.when, 9)

        # 3c. Time 4
        wrkr = myobj.next_completion()
        self.assertEqual(wrkr.id, 1)
        self.assertEqual(wrkr.step, 'A')
        self.assertEqual(wrkr.when, 4)
        wrkr.finished()
        wrkr = myobj.idle_worker()
        self.assertEqual(wrkr.id, 1)
        wrkr.assign_task('B', 6)
        self.assertEqual(myobj.idle_worker(), None)

        # 3d. Time 6
        wrkr = myobj.next_completion()
        self.assertEqual(wrkr.id, 1)
        self.assertEqual(wrkr.step, 'B')
        self.assertEqual(wrkr.when, 6)
        wrkr.finished()
        wrkr = myobj.idle_worker()
        self.assertEqual(wrkr.id, 1)
        wrkr.assign_task('D', 10)
        self.assertEqual(myobj.idle_worker(), None)

        # 3e. Time 9
        wrkr = myobj.next_completion()
        self.assertEqual(wrkr.id, 2)
        self.assertEqual(wrkr.step, 'F')
        self.assertEqual(wrkr.when, 9)
        wrkr.finished()
        wrkr = myobj.idle_worker()
        self.assertEqual(wrkr.id, 2)

        # 3f. Time 10
        wrkr = myobj.next_completion()
        self.assertEqual(wrkr.id, 1)
        self.assertEqual(wrkr.step, 'D')
        self.assertEqual(wrkr.when, 10)
        wrkr.finished()
        wrkr = myobj.idle_worker()
        self.assertEqual(wrkr.id, 1)
        wrkr.assign_task('E', 15)
        self.assertEqual(myobj.idle_worker().id, 2)

        # 3f. Time 15
        wrkr = myobj.next_completion()
        self.assertEqual(wrkr.id, 1)
        self.assertEqual(wrkr.step, 'E')
        self.assertEqual(wrkr.when, 15)
        wrkr.finished()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ w o r k e r . p y                  end
# ======================================================================

