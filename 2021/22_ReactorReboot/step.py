# ======================================================================
# Reactor Reboot
#   Advent of Code 2021 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t e p . p y
# ======================================================================
"Step for the Advent of Code 2021 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_STEP = re.compile("(o[nf]+) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)"
                     "..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)")
LIMIT_MIN = -50
LIMIT_MAX = 50

# ======================================================================
#                                                                   Step
# ======================================================================


class Step(object):   # pylint: disable=R0902, R0205
    "Object for Reactor Reboot"

    def __init__(self, text=None, part2=False,
                 on=True, ranges=None):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.turn_on = on
        self.x_beg_end = (0, 0)
        self.y_beg_end = (0, 0)
        self.z_beg_end = (0, 0)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            match = RE_STEP.match(text)
            if not match:
                print("Unable to parse <%s>" % text)
            if match.group(1) == "off":
                self.turn_on = False
            self.x_beg_end = (int(match.group(2)), int(match.group(3)))
            self.y_beg_end = (int(match.group(4)), int(match.group(5)))
            self.z_beg_end = (int(match.group(6)), int(match.group(7)))

        # 3. Process ranges (if any)
        if ranges:
            self.x_beg_end = ranges[0]
            self.y_beg_end = ranges[1]
            self.z_beg_end = ranges[2]

    def limited(self, low=LIMIT_MIN, high=LIMIT_MAX):
        "Return the dimensions limited by the given range"

        # 1. Part two gets them all
        if self.part2:
            return self.x_beg_end, self.y_beg_end, self.z_beg_end

        # 2. Get limited dimensions for part one
        limited_x = (max(low, self.x_beg_end[0]), min(high, self.x_beg_end[1]))
        limited_y = (max(low, self.y_beg_end[0]), min(high, self.y_beg_end[1]))
        limited_z = (max(low, self.z_beg_end[0]), min(high, self.z_beg_end[1]))

        # 3. Return the limited dimensions
        return limited_x, limited_y, limited_z

    def size(self):
        "Return the number of cubes referenced by the instruction"

        # 1. Get the limited ranges
        ranges = self.limited()

        # 2. Compute the individualal sizes
        size_x = 1 + ranges[0][1] - ranges[0][0]
        size_y = 1 + ranges[1][1] - ranges[1][0]
        size_z = 1 + ranges[2][1] - ranges[2][0]

        # 3. Return the total size
        return max(0, size_x) * max(0, size_y) * max(0, size_z)

    @staticmethod
    def dim_overlap(range1, range2):
        "Return the overlap of the two ranges (or None if none)"

        # 1. Is there any overlap?
        if range1[1] < range2[0] or range2[1] < range1[0]:
            return None

        # 2. Return the part the overlaps
        return (max(range1[0], range2[0]), min(range1[1], range2[1]))

    def overlap(self, other):
        "Return the area of overlap"

        # 1. Get the two ranges
        my_ranges = self.limited()
        other_ranges = other.limited()

        # 2. Check each dimension for overlap
        x_overlap = Step.dim_overlap(my_ranges[0], other_ranges[0])
        y_overlap = Step.dim_overlap(my_ranges[1], other_ranges[1])
        z_overlap = Step.dim_overlap(my_ranges[2], other_ranges[2])

        # 3. If any dimension doesn't overlap, then there is no overlap
        if not x_overlap or not y_overlap or not z_overlap:
            return None

        # 4. Return the area of overlap
        return x_overlap, y_overlap, z_overlap


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          s t e p . p y                         end
# ======================================================================
