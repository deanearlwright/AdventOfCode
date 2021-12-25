# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b u r r o w . p y
# ======================================================================
"The map for the Advent of Code 2021 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import hallway
import room

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
AMPHIPODS = 'ABCD'
WALL = '#'
SPACE = ' '
PART_TWO_ADDIN = ["  #D#C#B#A#", "  #D#B#A#C#"]

# ======================================================================
#                                                                 Burrow
# ======================================================================


class Burrow(object):   # pylint: disable=R0902, R0205
    "Object for Amphipod"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.hallway = None
        self.rooms = {}
        self.hall_len = 0
        self.room_len = 0
        self.poss_len = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 3:
            if self.part2:
                self.text = text.copy()
                self.text.insert(3, PART_TWO_ADDIN[1])
                self.text.insert(3, PART_TWO_ADDIN[0])
            self.map_burrow()

    def map_burrow(self):
        "Decode the burrow information"

        # 1. Decode the hallway
        self.hallway = hallway.Hallway(text=self.text, part2=self.part2)

        # 2. For each doorway in the hall there is a room
        for doorway in self.hallway.doorways:

            # 3. Who wants to be in this room
            homeroom = AMPHIPODS[len(self.rooms)]

            # 4. But who is really in the room?
            contents = []
            for line in self.text[2:]:
                if line[doorway + 1] != WALL:
                    contents.append(line[doorway + 1])

            # 5. Construct the room
            the_room = room.Room(doorway=doorway,
                                 homeroom=homeroom,
                                 contents=contents)

            # 6. Add it to the rooms
            self.rooms[doorway] = the_room

        # 7. Set the lengths
        self.hall_len = len(self.hallway.spaces)
        self.room_len = len(contents)
        self.poss_len = self.hall_len + len(self.rooms) * self.room_len

    def is_in_hall(self, index):
        "Return True if this position is in the hall?"
        return index < self.hall_len

    def position(self, index):
        "Return the value (space, amhipod) in the given position"

        # 1. Hallways are easy
        if self.is_in_hall(index):
            return self.hallway.spaces[index]

        # 2. Which room and depth
        room_index = (index - self.hall_len) // self.room_len
        room_depth = (index - self.hall_len) % self.room_len

        # 3. Return the room value
        return self.rooms[self.hallway.doorways[room_index]].contents[room_depth]

    def positions(self):
        "Return all the value in all the positions"

        return ''.join([self.position(_) for _ in range(self.poss_len)])

    def __str__(self):
        "A nice little diagram"

        # 1. Start with nothing
        result = []

        # 2. Build some walls
        top_wall = [WALL for _ in range(2 + len(self.hallway.spaces))]
        bot_wall = top_wall[:-2]
        bot_wall[0] = SPACE
        bot_wall[1] = SPACE

        # 3. Need a top wall
        result.append(''.join(top_wall))

        # 4. Add the hallway
        result.append(str(self.hallway))

        # 5. First row of room
        room_row = top_wall.copy()
        for _ in self.rooms.values():
            room_row[1 + _.doorway] = _.contents[0]
        result.append(''.join(room_row))

        # 6. Second row of room
        room_row = bot_wall.copy()
        for _ in self.rooms.values():
            room_row[1 + _.doorway] = _.contents[1]
        result.append(''.join(room_row))

        # 7. Finish it off with a bottom wall
        result.append(''.join(bot_wall))

        # 8. Return the complete diagram
        return '\n'.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        b u r r o w . p y                       end
# ======================================================================
