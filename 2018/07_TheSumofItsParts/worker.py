# ======================================================================
# The Sum of Its Parts
#   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         w o r k e t . p y
# ======================================================================
"Workers for the Advent of Code 2018 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DEFAULT_NUMBER = 5
DEFAULT_SECONDS = 60

# ======================================================================
#                                                                 Worker
# ======================================================================


class Worker(object):   # pylint: disable=R0902, R0205
    "Worker object for The Sum of Its Parts"

    def __init__(self, id=None):

        # 1. Set the initial values
        self.id = id
        self.step = None
        self.when = None

    def assign_task(self, step, when):
        "Add a task"

        # 1. Add a step and the completion time
        self.step = step
        self.when = when

    def finished(self):
        self.step = None
        self.when = None

# ======================================================================
#                                                                Workers
# ======================================================================


class Workers(object):   # pylint: disable=R0902, R0205
    "Multiple Workers object for The Sum of Its Parts"

    def __init__(self, number=DEFAULT_NUMBER, seconds=DEFAULT_SECONDS):

        # 1. Create the initial workers
        self.workers = []
        for id in range(number):
            self.workers.append(Worker(id=id+1))

        # 2. Remember the base time to do the work
        self.seconds = seconds

    def idle_worker(self):
        # 1. Loop for all the workers
        for wrkr in self.workers:

            # 2. Is this not buzy, return it
            if wrkr.step == None:
                return wrkr

        # 3. Sorry, everyone is working
        return None

    def assign_steps(self, now, steps):

        # 1. Get the steps currently being worked
        working = set()
        for wrkr in self.workers:
            if wrkr.step != None:
                working.add(wrkr.step)

        # 2. Loop for all the steps
        for step in steps:

            # 3. If it is being worked, don't reassign
            if step in working:
                continue

            # 4. Get a worker for the step
            wrkr = self.idle_worker()

            # 5. If a workers is available, assign worker to the step
            if wrkr != None:
                completion = now + self.seconds + 1 + ord(step) - ord('A')
                wrkr.assign_task(step, completion)

    def next_completion(self):
        # 1. Start with nothing
        seconds = None
        who = None

        # 2. Loop for all the workers
        for wrkr in self.workers:

            # 2. Is buzy, check completing time
            if wrkr.when != None:
                if seconds == None or seconds > wrkr.when:

                    # 3. First or better time
                    seconds = wrkr.when
                    who = wrkr

        # 4. Return the worker who will finish next (if any)
        return who

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         w o r k e r . p y                      end
# ======================================================================
