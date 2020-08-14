# ======================================================================
# Chronal Coordinates
#   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a r e a . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import coord

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Area
# ======================================================================


class Area(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Coordinates"

    def __init__(self, text=None, part2=False, total=10000):

        # 1. Set the initial value
        self.part2 = part2
        self.text = text
        self.coords = []
        self.closest = {}
        self.maxX = 0
        self.maxY = 0
        self.total = total
        self.distances = {}
        self.distCoord = None

        # 2. Process text (if any)
        if text is not None:
            self.processText(text)

        # 3. Find Coordinated dimensions for part 1
        if not self.part2:
            for coordinate in self.coords:
                self.findDimensions(coordinate)

        # 4. Find total dimensions for part 2
        if self.part2:
            self.distCoord = self.totalDimensions()

    def processText(self, text):
        # 1. Loop for all of the lines in the text
        for line in text:

            # 2. Get the x and y coordinates
            parts = line.split(',')
            x=int(parts[0])
            y=int(parts[1])

            # 3. Create and save the coordinate
            self.coords.append(coord.Coord(x=x, y=y))

            # 4. Keep track of the maximum x and y
            if x > self.maxX:
                self.maxX = x
            if y > self.maxY:
                self.maxY = y

    def findDimensions(self, coordinate):
        # 1. Find the lowest X dimension
        for coordinate.minX in range(coordinate.x, -1, -1):
            if self.nearest(coordinate.minX, coordinate.y) != coordinate:
                coordinate.minX += 1
                break

        # 2. Find the lowest y dimension
        for coordinate.minY in range(coordinate.y, -1, -1):
            if self.nearest(coordinate.x, coordinate.minY) != coordinate:
                coordinate.minY += 1
                break

        # 3. Find the highest X dimension
        for coordinate.maxX in range(coordinate.x, self.maxX+1):
            if self.nearest(coordinate.maxX, coordinate.y) != coordinate:
                coordinate.maxX -= 1
                break

        # 4. Find the highest y dimension
        for coordinate.maxY in range(coordinate.y, self.maxY+1):
            if self.nearest(coordinate.x, coordinate.maxY) != coordinate:
                coordinate.maxY -= 1
                break

        # 5. Determine if infinite or finite
        if coordinate.minX == 0 or coordinate.minY == 0 or coordinate.maxX == self.maxX or coordinate.maxY == self.maxY:
            coordinate.isInfinite = True
        else:
            coordinate.isInfinite = False

        # 6. If finite, determine size
        if not coordinate.isInfinite:

            # 6a. Determine gross area
            coordinate.area = (1 + coordinate.maxX - coordinate.minX) * (1 + coordinate.maxY - coordinate.minY)

            # 6b. Start count of closest squares
            coordinate.closest = 0

            # 6c. Loop for the x and y area
            for x in range(coordinate.minX, coordinate.maxX + 1):
                for y in range(coordinate.minY, coordinate.maxY + 1):

                    # 6d. Increment count if coordinate is closest
                    if self.nearest(x, y) == coordinate:
                        coordinate.closest += 1


    def nearest(self, x, y):
        # 1. If Have we already calculated the nearest coordinate, just return it
        if (x,y) in self.closest:
            return self.closest[(x,y)]

        # 2. Start with no nearest coordinate
        result = None
        distance = None

        # 3. Loop for all coordinates
        for coordinate in self.coords:

            # 4. Determine the distance to the coordinate
            dist = coordinate.distance(x, y)

            # 5. Is this one closer, save the coordinate
            if distance == None or dist < distance:
                result = coordinate
                distance = dist

            # 6. But if it is the same distance, neither is closer
            elif distance == dist:
                result = None

        # 7. Save the result from possible re-use
        self.closest[(x,y)] = result

        # 8. Return the closest coordinate (if any)
        return result

    def totalDistance(self, x, y):
        # 1. If we have been here before, returned saved result
        if (x, y) in self.distances:
            return self.distances[(x, y)]

        # 2. Start with no distance at all
        result = 0

        # 3. Loop for all the coordinates
        for coordinate in self.coords:

            # 4. Get the distance to this coordinate
            dist = coordinate.distance(x, y);

            # 5. Add it to the total
            result += dist

        # 6. Save the total distance for next time
        self.distances[(x, y)] = result

        # 7. And return the total distance
        return result

    def totalDimensions(self):
        # 1. Create a coordinate to hold the dimensions
        coordinate = coord.Coord(x=self.maxX // 2, y=self.maxY // 2)

        # 2. Check that it satisifies
        if self.totalDistance(coordinate.x, coordinate.y) >= self.total:
            print("(%d, %d) does not satisify" % (coordinate.x, coordinate.y))
            return None

        # 2. Find the lowest X dimension
        for coordinate.minX in range(coordinate.x, -1, -1):
            if self.totalDistance(coordinate.minX, coordinate.y) > self.total:
                coordinate.minX += 1
                break

        # 3. Find the lowest y dimension
        for coordinate.minY in range(coordinate.y, -1, -1):
            if self.totalDistance(coordinate.x, coordinate.minY) > self.total:
                coordinate.minY += 1
                break

        # 4. Find the highest X dimension
        for coordinate.maxX in range(coordinate.x, self.maxX+1):
            if self.totalDistance(coordinate.maxX, coordinate.y) > self.total:
                coordinate.maxX -= 1
                break

        # 5. Find the highest y dimension
        for coordinate.maxY in range(coordinate.y, self.maxY+1):
            if self.totalDistance(coordinate.x, coordinate.maxY) > self.total:
                coordinate.maxY -= 1
                break

        # 6. Determine if infinite or finite
        if coordinate.minX == 0 or coordinate.minY == 0 or coordinate.maxX == self.maxX or coordinate.maxY == self.maxY:
            coordinate.isInfinite = True
        else:
            coordinate.isInfinite = False

        # 7. return coordinate with dimensions
        return coordinate

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Assume that there is no result
        result = None

        # 2. Loop for all coordinates
        for coordinate in self.coords:

            # 3. Only interested in the finite ones
            if not coordinate.isInfinite:

                # 4. Keep the largest nearest area
                if result == None or result < coordinate.closest:
                    result = coordinate.closest

        # 5 Return the solution for part one
        return result


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. If there was a problem with the center, we have no solution
        if self.distCoord == None:
            print("no distCoord")
            return None

        # 2. If infinite, we have no solution
        if self.distCoord.isInfinite:
            print("Infinite")
            return None

        # 3. Determine gross area
        self.distCoord.area = (1 + self.distCoord.maxX - self.distCoord.minX) * (1 + self.distCoord.maxY - self.distCoord.minY)
        print("area = %d" % self.distCoord.area)
        # 4. Start count of squares less than total
        self.distCoord.closest = 0

        # 5. Loop for the x and y area
        for x in range(self.distCoord.minX - 2, self.distCoord.maxX + 3):
            for y in range(self.distCoord.minY - 2, self.distCoord.maxY + 3):

                # 6. Increment count if coordinate is closest
                if self.totalDistance(x, y) < self.total:
                        self.distCoord.closest += 1

        # 7. Return the solution for part two
        print("part2 = %d" % self.distCoord.closest)
        return self.distCoord.closest

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          a r e a . p y                         end
# ======================================================================
