# ======================================================================
# Crossed Wires
#   Advent of Code 2019 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            w i r e d  . p y
# ======================================================================
"Computer Wire for Crossed Wires problem for Advent of Code 2018 Day 03"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

DIR_UP = 'U'
DIR_DN = 'D'
DIR_LT = 'L'
DIR_RT = 'R'

DELTA = {DIR_UP: (0, 1),
         DIR_DN: (0, -1),
         DIR_LT: (-1, 0),
         DIR_RT: (1, 0)}

CENTRAL = (0, 0)

# ======================================================================
#                                                      Utility Functions
# ======================================================================

def manhattan(point1, point2):
    "Calculate Mantattan (Taxi cab) Distance between two points"

    delta_x = point1[0] - point2[0]
    delta_y = point1[1] - point2[1]

    return abs(delta_x) + abs(delta_y)

def intersect(seg1_beg, seg1_end, seg2_beg, seg2_end):
    "Returns the intersetion point of two wire segments or None if none"

    # 1. Determine the leftmost, rightmost, uppermost, and lowermost points
    seg1_left = min(seg1_beg[1], seg1_end[1])
    seg2_left = min(seg2_beg[1], seg2_end[1])
    seg1_lower = min(seg1_beg[0], seg1_end[0])
    seg2_lower = min(seg2_beg[0], seg2_end[0])

    seg1_right = max(seg1_beg[1], seg1_end[1])
    seg2_right = max(seg2_beg[1], seg2_end[1])
    seg1_upper = max(seg1_beg[0], seg1_end[0])
    seg2_upper = max(seg2_beg[0], seg2_end[0])

    # 2. Check if can't intersect
    if seg1_right < seg2_left or seg2_right < seg1_left:
        return None
    if seg1_left > seg2_right or seg2_left > seg1_right:
        return None
    if seg1_upper < seg2_lower or seg2_upper < seg1_lower:
        return None
    if seg1_lower > seg2_upper or seg2_lower > seg1_upper:
        return None

    # 3. Determine the intersection
    if seg1_right == seg1_left:
        result = (seg2_beg[0], seg1_beg[1])
    else:
        result = (seg1_beg[0], seg2_beg[1])

    # 4. Return the intersection
    return result

def closest(target, points):
    "Return the point closest to the target"

    # 1. If there are no points, return None
    if len(points) == 0:
        return None

    # 2. Assume the first point is the closest
    result = points[0]
    result_dist = manhattan(target, result)

    # 3. Loop for the rest of the points
    for point in points[1:]:

        # 4. Compute the distance to this point
        point_dist = manhattan(target, point)

        # 5. If the distance is less, save this one
        if point_dist < result_dist:
            result = point
            result_dist = point_dist

    # 6. Return the closest point
    return result

def fastest(points, wires):
    "Return the point that is the faster along the wires"

    # 1. If there are no points, return None
    if len(points) == 0:
        return None

    # 2. Assume the first point is the fastest
    result = points[0]
    result_time = sum([wire.time_to(result) for wire in wires])

    # 3. Loop for the rest of the points
    for point in points[1:]:

        # 4. Compute the time to this point
        point_time = sum([wire.time_to(point) for wire in wires])

        # 5. If the time is less, save this one
        if point_time < result_time:
            result = point
            result_time = point_time

    # 6. Return the fastest time
    return result_time

# ======================================================================
#                                                                   Wire
# ======================================================================


class Wire():
    """Object representing a wire"""

    def __init__(self, text=None, start=None):

        # 1. Set the initial values
        if start is None:
            self.start = CENTRAL
        else:
            self.start = start
        self.finish = self.start
        self.points = [self.start]

        # 2. If there is text, process it
        if text is not None:

            # 3. For all of the directions/numbers in the text
            for dir_num in text.split(','):

                # 4. Split the direction and number
                wdir = dir_num[0]
                wnum = int(dir_num[1:])

                # 5. Compute the next point
                curpnt = self.points[-1]
                nxtpnt = (wnum*DELTA[wdir][0] + curpnt[0],
                          wnum*DELTA[wdir][1] + curpnt[1])
                #print("%s: (%d,%d) -> (%d,%d)" %
                #      (dir_num, curpnt[0], curpnt[1], nxtpnt[0], nxtpnt[1]))

                # 6. Add it to the list
                self.points.append(nxtpnt)

        # 7. Set the last point
        self.finish = self.points[-1]

    def begin(self):
        "Returns the starting point"

        return self.start

    def end(self):
        "Returns the last point"

        return self.finish

    def num_points(self):
        "Return number of points"

        return len(self.points)

    def num_segments(self):
        "Return number of segments"

        return len(self.points) - 1

    def intersections(self, other):
        "Detmine intersection between my lines and the other's"

        # 0. Preconditions
        assert(isinstance(other, Wire))

        # 1. Start with nothing
        result = set()

        # 2. Loop for all of my line segments
        for my_indx in range(self.num_segments()):
            my_beg, my_end = self.segment(my_indx)

            # 3. Loop for all of the other's line segments
            for other_indx in range(other.num_segments()):
                other_beg, other_end = other.segment(other_indx)

                # 4. Check for an intersection
                cross = intersect(my_beg, my_end, other_beg, other_end)

                # 5. If there is an intersection, save it (but not (0,0))
                if cross is not None:
                    if cross != (0, 0):
                        result.add(cross)

        # 6. Return intersections
        return list(result)

    def segment(self, indx):
        "Return beginning and ending of a line segment"

        return self.points[indx], self.points[indx+1]

    def time_to(self, point):
        "Return time to reach specified point"

        # 1. Start with a very fast time indeed
        time = 0

        # 2. Loop fpr all of the line segments
        for indx in range(self.num_segments()):
            sbeg, send = self.segment(indx)

            # 3. Does the point intersect with this segment?
            if intersect(sbeg, send, point, point) is not None:

                # 4. Yes, Add distance along the segment to the point
                time += manhattan(sbeg, point)

                # 5, Return the total time to the point
                return time

            # 6. Not on line, add length of this segment
            time += manhattan(sbeg, send)

        # 7. Point no on any segment -- should not occur
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         w i r e . p y                          end
# ======================================================================
