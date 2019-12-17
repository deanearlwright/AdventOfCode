# ======================================================================
# Oxygen System
#   Advent of Code 2019 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            d r o i d . p y
# ======================================================================
"Repair droid for Oxygen System problem for Advent of Code 2019 Day 15"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from random import choice

import intcode

import ship

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
STATE_SEARCHING = 1
STATE_FOUND = 2
STATE_BACKTRACKING = 3

MOVE_INVALID = 0
MOVE_NORTH = 1
MOVE_SOUTH = 2
MOVE_WEST = 3
MOVE_EAST = 4
MOVE_REPAIR = 5

MOVE = {'N': MOVE_NORTH,
        'S': MOVE_SOUTH,
        'W': MOVE_WEST,
        'E': MOVE_EAST}

REVERSE = {'N': 'S',
           'S': 'N',
           'W': 'E',
           'E': 'W'}

DIRS = ['?', 'N', 'S', 'W', 'E']
RDIR = ['?', 'S', 'N', 'E', 'W']


DELTA = {MOVE_NORTH: (0, -1),
         MOVE_SOUTH: (0, 1),
         MOVE_WEST: (-1, 0),
         MOVE_EAST: (1, 0)}

STATUS_WALL = 0
STATUS_FWD = 1
STATUS_OS = 2

# ======================================================================
#                                                                  Droid
# ======================================================================


class Droid():
    """Object representing a ship's repair droid"""

    def __init__(self, origin=(0, 0), text=None):

        # 1. Set the initial values
        self.origin = (0, 0)
        self.state = STATE_SEARCHING
        self.computer = intcode.IntCode(text=text)
        self.ship = ship.Ship()
        self.loc = origin
        self.next_cmd = MOVE_NORTH
        self.oxygen = None

    def __str__(self):
        return str(self.ship)

    def run(self, watch=False, max_dist=False):
        "Run the droid until it stops"

        # 1. Assume the computer wants input
        result = intcode.STOP_INP

        # 2. Run while the computer wants input
        while result == intcode.STOP_INP and self.state != STATE_FOUND:

            # 3. Run the computer until it stops
            result = self.computer.run(inp=[self.next_cmd])

            # 4. If still looking for input, get and execute the output
            if result == intcode.STOP_INP:

                # 5. Ouput is either wall, forward, oxygen system
                outputs = self.computer.outputs()
                assert len(outputs) == 1
                status = outputs[0]

                # 6. If we hit a wall, record it
                last_dir = DIRS[self.next_cmd]
                if status == STATUS_WALL:
                    if watch:
                        print("Wall: state = %d, loc=(%d,%d), status = %d, dir=%s" %
                              (self.state, self.loc[0], self.loc[1], status, last_dir))
                    self.ship.record_wall(self.loc, last_dir)
                    new_loc = self.loc
                else:
                    delta = DELTA[self.next_cmd]
                    new_loc = (self.loc[0] + delta[0], self.loc[1] + delta[1])
                    if watch:
                        print("Move: state = %d, loc=(%d,%d), status = %d, dir=%s, new=(%d,%d)" %
                              (self.state, self.loc[0], self.loc[1],
                               status, last_dir, new_loc[0], new_loc[1]))
                    if self.state == STATE_SEARCHING:
                        if status == STATUS_FWD or max_dist:
                            self.ship.record_move(self.loc, last_dir, new_loc, False)
                        else:
                            self.ship.record_move(self.loc, last_dir, new_loc, True)
                            self.state = STATE_FOUND
                            self.oxygen = new_loc
                            if watch:
                                print("Oxygen found at (%d,%d)" %
                                      (new_loc[0], new_loc[1]))


                # 7. Set new location
                self.loc = new_loc

                # 8. Determine the next command
                self.next_cmd = self.next_command()

        # 9. Return the reason for the machine stopping
        return result

    def next_command(self):
        "Determine the next command for the droid base on state and location"

        # 1. Start with an invalid command
        next_cmd = MOVE_INVALID

        # 2. If we found the oxygen system, repair it
        if self.state == STATE_FOUND:
            next_cmd = MOVE_REPAIR

        # 3. If searching, find a direction we haven't tried
        if self.state == STATE_SEARCHING:
            choices = self.ship.explore(self.loc)
            if choices:
                next_cmd = MOVE[choice(choices)]
            else:
                self.state = STATE_BACKTRACKING

        # 4. If backtracking, move back toward the origin
        if self.state == STATE_BACKTRACKING:
            choices = self.ship.explore(self.loc)
            if choices:
                next_cmd = MOVE[choice(choices)]
                self.state = STATE_SEARCHING
            else:
                if self.loc != self.origin:
                    back_dir = self.ship.go_back(self.loc)
                    next_cmd = MOVE[back_dir]

        # 5. Return the new command
        return next_cmd

    def oxygen_path(self, watch=False):
        "Return the path to the oxygen system"

        # 1. Start with a very short path
        result = []

        # 2. Check that there is one
        if self.oxygen is None:
            return result

        # 3. Start at the oxygen and trace the path backward
        loc = self.oxygen

        # 4. Loop until we reach the origin
        while loc != self.origin:

            # 5. Determine direction back toward the origin
            #print(self.ship.area[loc])
            rdir = self.ship.go_back(loc)
            delta = DELTA[MOVE[rdir]]
            new_loc = (loc[0] + delta[0], loc[1] + delta[1])
            if watch:
                print("loc=(%d,%d), dir=%s, to=(%d,%d)" %
                      (loc[0], loc[1], rdir, new_loc[0], new_loc[1]))

            # 6. Record the droid move
            result.append(rdir)
            loc = new_loc

        # 7. Return the reverse path joined into a string
        return ''.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d r o i d . p y                        end
# ======================================================================
