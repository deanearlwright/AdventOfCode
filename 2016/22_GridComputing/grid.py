# ======================================================================
# Grid Computing
#   Advent of Code 2016 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g r i d . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import node

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Grid
# ======================================================================


class Grid(object):   # pylint: disable=R0902, R0205
    "Object for Grid Computing"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.nodes = {}
        self.max_loc = [0, 0]

        # 2. Process text (if any)
        if text is not None and len(text) > 2:

            # 3. Loop for all of the line of the text
            for line in text[2:]:

                # 4. Create a node from the line
                anode = node.Node(text=line, part2=self.part2)
                self.nodes[anode.loc] = anode

                # 5. Adjust the outer limits
                if anode.loc[0] > self.max_loc[0]:
                    self.max_loc[0] = anode.loc[0]
                if anode.loc[1] > self.max_loc[1]:
                    self.max_loc[1] = anode.loc[1]

    def viable_pairs(self):
        """Return the number of viable pairs

           A viable pair is any two nodes (A,B), regardless
           of whether they are directly connected, such that:

             - Node A is not empty (its Used is not zero).
             - Nodes A and B are not the same node.
             - The data on node A (its Used) would fit on node B (its Avail).
        """

        # 1. Start with none
        result = 0

        # 2. Loop for all of the non-empty "A" nodes
        for node_a in self.nodes.values():
            if node_a.is_empty():
                continue

            # 3. Loop for all of the "B" nodes
            for node_b in self.nodes.values():
                if node_a == node_b:
                    continue

                # 4. Would the data on node a fit on node b?
                if node_b.can_hold(node_a.used):

                    # 5. Yes, found a viable pair
                    result += 1

        # 6. Return the number of viable pairs
        return result

    def __str__(self):

        # 1. Start with nothing
        result = []

        # 2. Loop for all the rows
        for row_num in range(self.max_loc[1] + 1):

            # 3. Start a new row
            row = []

            # 4. Loop for all columns
            for col_num in range(self.max_loc[0] + 1):

                # 5. Determine the character
                char = '.'
                if row_num == 0 and col_num == 0:
                    char = '!'
                elif row_num == 0 and col_num == self.max_loc[0]:
                    char = 'G'
                elif (col_num, row_num) in self.nodes:
                    a_node = self.nodes[(col_num, row_num)]
                    if a_node.is_empty():
                        char = '_'
                    elif a_node.is_wall():
                        char = '#'

                # 6. Add the character to the row
                row.append(char)

            # 7. Add the row to the result
            result.append(''.join(row))

        # 8. Return the grid
        return '\n'.join(result)

    def find_access(self):
        "Returns the only accessible node"
        if (0, 0) in self.nodes:
            return self.nodes[(0, 0)]
        return None

    def find_goal(self):
        "Returns the goal node"
        if self.max_loc[0] > 0 and self.max_loc[1] > 0 and (self.max_loc[0], 0) in self.nodes:
            return self.nodes[(self.max_loc[0], 0)]
        return None

    def find_wall(self):
        "Returns the left most wall node"

        # 1. Get the upper right node -- runs checks for us
        upper_right = self.find_goal()
        if upper_right is None:
            return None

        # 2. Loop down until we hit a wall
        wall_right = None
        for row in range(self.max_loc[1]):
            a_node = self.nodes[upper_right.loc[0], row]
            if a_node.is_wall():
                wall_right = a_node
                break
        if wall_right is None:
            return None

        # 3. Find the left end of the wall
        wall_left = None
        for col in range(wall_right.loc[0], 0, -1):
            a_node = self.nodes[(col, wall_right.loc[1])]
            if a_node.is_wall():
                wall_left = a_node
            else:
                break

        # 4. Return the left most wall node
        return wall_left

    def find_empty(self):
        "Returns the empty node (used == 0)"

        # 1. Loop for all of the nodes
        for a_node in self.nodes.values():

            # 2. Return the node if this the one
            if a_node.is_empty():
                return a_node

        # 3. That's odd.  There should be one
        return None

    def min_steps(self, verbose=False):
        "Return the minimum number of steps"

        # 1. Get the critical nodes
        access = self.find_access()
        goal = self.find_goal()
        wall = self.find_wall()
        empty = self.find_empty()

        # 2. Can't solve if one or more not found
        if access is None or goal is None or wall is None or empty is None:
            return None

        # 3. Display locations
        if verbose:
            print('access', access.loc)
            print('goal', goal.loc)
            print('wall', wall.loc)
            print('empty', empty.loc)

        # 1 = (0,0), G = (36, 0), E = (20, 6)
        # The wall is from 15 to 36 on row 2.
        # Distance = 36-20+6 = 22.
        # To get past wall = 6 cols = 22+12=34
        # Five step cycle = 5 * 35 = 175.
        # Total moves = 34 + 175 = 209.

        # 4. Compute distances
        empty_goal = empty.distance(goal)
        around_wall = 2 * (1 + abs(wall.loc[0] - empty.loc[0]))
        goal_access = 5 * (goal.loc[0] - 1)
        result = empty_goal + around_wall + goal_access

        # 5. Display Distances
        if verbose:
            print('empty to goal', empty_goal)
            print('around_wall', around_wall)
            print('goal_access', goal_access)
            print('result', result)

        # 7. Return the total number of steps
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if verbose:
            print(self)
        return self.viable_pairs(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if verbose:
            print(self)
        return self.min_steps(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          g r i d . p y                         end
# ======================================================================
