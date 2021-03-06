# ======================================================================
# Mine Cart Madness
#   Advent of Code 2018 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            t r a c k . p y
# ======================================================================
"Tracks for the Mine Card Madness problem day 13 of Advent of Code 2018"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import cart

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

TRACK_PIECES = "|-+/\\"
CART_PIECES = "^v<>"
ALL_PIECES = TRACK_PIECES + CART_PIECES

# ======================================================================
#                                                                  Track
# ======================================================================


class Track(object):                      # pylint: disable=E0012,R0205
    """Object representing a map of Mine Card Madness"""

    def __init__(self):
        self.tracks = {}
        self.carts = []
        self.max_rows = 0
        self.max_cols = 0
        self.time = 0
        self.crashed = None

    def add_track(self, location, track):
        "Set a piece of track at a location"

        # 0. Preconditions
        assert track in ALL_PIECES
        assert location[0] >= 0
        assert location[1] >= 0

        # 1. Add the track
        self.tracks[location] = track

        # 2. Adjust the size as needed
        if location[0] > self.max_cols:
            self.max_cols = location[0]
        if location[1] > self.max_rows:
            self.max_rows = location[1]

        # 3. If this is a cart, add it to the carts
        if track in CART_PIECES:
            self.carts.append(cart.Cart(location=location, direction=track))

    def set_track(self, location, track):
        "Set a piece of track at a location"

        # 0. Preconditions
        assert track in ALL_PIECES
        assert(location[0] >= 0 and location[0] <= self.max_cols)
        assert(location[1] >= 0 and location[1] <= self.max_rows)

        # 1. Set the track at that location
        self.tracks[location] = track

    def set_crashed(self, location):
        "Set a piece of track at a location"

        # 0. Preconditions
        assert(location[0] >= 0 and location[0] <= self.max_cols)
        assert(location[1] >= 0 and location[1] <= self.max_rows)

        # 1. Set the track at that location to indicate a crash
        self.tracks[location] = 'X'

        # 2. Remember where we crashed
        self.crashed = location

    def get_track(self, location):
        "Get the track at a location, if no track return blank"

        # 0. Preconditions
        assert(location[0] >= 0 and location[0] <= self.max_cols)
        assert(location[1] >= 0 and location[1] <= self.max_rows)

        # 1. If there is track there, return it
        if location in self.tracks:
            return self.tracks[location]

        # 2. Else return a blank
        return ' '

    def size(self):
        "Return the size of the tracks grid"

        return (self.max_cols, self.max_rows)

    def __str__(self):
        result = []
        for row in range(1 + self.max_rows):
            one_row = []
            for col in range(1 + self.max_cols):
                one_row.append(self.get_track((col, row)))
            result.append(''.join(one_row).rstrip())
        return '\n'.join(result)

    def from_file(self, filepath):
        "Read the tracks from a file"

        self.from_text(open(filepath).read())

    def from_text(self, text):
        "Set the track from a text string"

        # 1. We start with row zero
        row = 0

        # 2. Loop for lines in the text
        for line in text.split('\n'):

            # 3. But ignore blank and comment lines
            line = line.rstrip(' \r')
            if not line:
                continue
            if line.startswith('#'):
                continue

            # 4. Walk through the tracks in this row
            for col, track in enumerate(line):

                # 5. We don't bother to store blanks
                #    because carts can't go there
                if track == ' ':
                    continue

                # 6. Add this track piece (or cart) to the tracks
                self.add_track((col, row), track)

            # 7. Done this this row
            row += 1

    def tick(self, stop=True):
        "Move all the carts one space, return True if crash"

        # 3. Increment the clock
        self.time += 1

        # 2. Put the carts in the order (rows by columns)
        self.carts.sort()

        # 3. Loop for all of the carts
        for kart in self.carts:

            # 4. Move the cart
            crashed = kart.tick(track=self)

            # 5. If the cart crashed and are stopping at the first crash, stop
            if crashed and stop:
                return True

            # 6. If the cart crashed, do immediate repairs
            if crashed:
                self.repair()

        # 7. Permantely remove any crashed carts
        self.cleanup()

        # 8. No crashes to report
        return False

    def solve(self, maxtime=0):
        "Determine where the mine carts collide"

        # 1. Loop until there is a crash
        while not self.crashed:

            # 2. Bug out early if this is taking too long
            if maxtime > 0 and self.time > maxtime:
                return None

            # 3. Move the carts one tick, stopping on crash
            self.tick()

        # 4. Return the location of the traffic mishap
        return self.crashed

    def derby(self, maxtime=0):
        "Determine the last cart standing"

        # 1. Loop until there is only one cart
        while len(self.carts) > 1:

            # 2. Bug out early if this is taking too long
            if maxtime > 0 and self.time > maxtime:
                return None

            # 3. Move the carts one tick, not stopping on a crash
            self.tick(stop=False)

        # 4. Return the location of the lonesome cart
        if not self.carts:
            return None
        return self.carts[0].location

    def repair(self):
        "Immediate clean up after a collision"

        # 0. Preconditions
        assert self.crashed is not None

        # 1. Find the carts involved
        location = self.crashed
        broken = []
        for kart in self.carts:
            if kart.location == location:
                kart.crashed = location
                broken.append(kart)
                #print("repair: (%d, %d) %s" % (location[0], location[1], kart.space))

        # 2. Repair the track
        for kart in broken:
            if kart.space not in CART_PIECES:
                self.set_track(location, kart.space)
                break

        # 3. Reset crashed indicator
        self.crashed = None

    def cleanup(self):
        "Final clean up after collisions"

        # 1. Find the non-crashed carts
        working = []
        for kart in self.carts:
            if not kart.crashed:
                working.append(kart)

        # 2. Keep only the working carts
        self.carts = working


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        t r a c k . p y                         end
# ======================================================================
