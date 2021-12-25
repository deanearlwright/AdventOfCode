# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p o s i t i o n s . p y
# ======================================================================
"Positions for the Advent of Code 2021 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
AMPHIPODS = ["A", "B", "C", "D"]
SPACE = '.'
WALL = '#'
ENERGY = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

# ======================================================================
#                                                              Positions
# ======================================================================


class Positions(object):   # pylint: disable=R0902, R0205, too-many-public-methods
    "Object for Amphipod"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.text = text
        self.part2 = False
        self.hall_len = 11
        self.room_len = 2
        if part2:
            self.room_len = 4
        self.room_num = 4
        if text:
            self.spaces = list(text)
        else:
            self.spaces = [SPACE for _ in range(self.hall_len + self.room_len * self.room_num)]
        self.doorways = [2 + 2 * _ for _ in range(self.room_num)]
        self.homerooms = {}
        for index, who in enumerate(AMPHIPODS):
            self.homerooms[who] = \
                [self.hall_len + self.room_len * index + _ for _ in range(self.room_len)]

    def __str__(self):
        return ''.join(self.spaces)

    def display(self):
        "A nice little diagram"

        # 1. Start with nothing
        result = []

        # 2. Build some walls
        top_wall = [WALL for _ in range(2 + self.hall_len)]
        bot_wall = top_wall[:-2]
        bot_wall[0] = ' '
        bot_wall[1] = ' '

        # 3. Need a top wall
        result.append(''.join(top_wall))

        # 4. Add the hallway
        result.append(''.join([WALL, ''.join(self.spaces[:self.hall_len]), WALL]))

        # 5. First row of rooms
        result.append(self.display_rooms(top_wall, 0))

        # 6. The rest of the rows
        for row in range(1, self.room_len):
            result.append(self.display_rooms(bot_wall, row))

        # 7. Finish it off with a bottom wall
        result.append(''.join(bot_wall))

        # 8. Return the complete diagram
        return '\n'.join(result)

    def display_rooms(self, wall, row):
        "Format a row of rooms"

        # 1. Copy the background
        result = wall.copy()

        # 2. Loop for all of the different rooms
        for index in range(self.room_num):

            # 3. Get the value for that room
            value = self.spaces[self.hall_len + index * self.room_len + row]

            # 4. Save it in the result
            result[1 + self.doorways[index]] = value

        # 5. Return the row
        return ''.join(result)

    def are_all_home(self):
        "Returns if all amphipods are in their home rooms"

        # 1. Loop for all of the home rooms
        for who, rooms in self.homerooms.items():

            # 2. Loop for all the spaces in the room
            for space in rooms:

                # 3. Are you at home?
                if self.spaces[space] != who:
                    return False

        # 4. It must be past ten o'clock
        return True

    def is_in_hall(self, index):
        "Return True if this position is in the hall?"
        return index < self.hall_len

    def am_i_in_my_room(self, index, who):
        "Return True if this position is in the amphipod's home room"

        # 1. Check for theNot in the hallway
        return index in self.homerooms[who]

    def frozen(self):
        "Return positions that must not be moved"

        # 1. Start with none
        result = []

        # 2. Loop for all of the homerooms
        for who, rooms in self.homerooms.items():

            # 3. Loop for for the rooms (in reverse order)
            for index in range(len(rooms) - 1, -1, -1):
                room = rooms[index]

                # 4. If the amphipod is at home, don't move him
                if who == self.spaces[room]:
                    result.append(room)
                else:
                    break

        # 5. Return the positions that should not be moved
        return result

    def moves_from(self, origin, who=None):
        "Where can we go from here"

        # 1. Start with nothing
        result = []

        # 2. Get who wants to move (if we don't know)
        if not who:
            who = self.spaces[origin]
        if who == SPACE:
            return []

        # 3. Is this a room or hallway
        if self.is_in_hall(origin):
            result = self.moves_from_hall(origin, who=who)
        else:
            result = self.moves_from_room(origin, who=who)

        # 9. Return result
        return result

    def moves_from_hall(self, origin, who=None):
        "Return the room destination from moving from the hall"

        # 1. Get which kind of amphipod is moving (if not given)
        if not who:
            who = self.spaces[origin]

        # 2. Get the doorway for this amphipod
        doorway = self.doorway_for_who(who)

        # 3. Is there a clear path to the doorway
        if not self.clear_hallway(origin, doorway):
            return []

        # 4. Get the deepest room
        deepest = self.deepest_room(who)
        if not deepest:
            return []

        # 5. Verify the space
        if not self.can_enter_room(who, deepest):
            return []

        # 6. Return the single destination
        return [deepest]

    def clear_hallway(self, from_pos, to_pos):
        "Returns True if the hallway is clear"

        # 1. Get the numbers of the hallway spaces
        if from_pos < to_pos:
            spaces = range(from_pos + 1, to_pos + 1)
        else:
            spaces = range(to_pos, from_pos)

        # 2. Loop for the spaces in the hallway the amhipod must traverse
        for space in spaces:

            # 3. If the step is not clear, return False
            if self.spaces[space] != SPACE:
                return False

        # 4. Clear sailing
        return True

    def can_enter_room(self, who, which):
        "Can the amphipod enter the room"

        # 1. If it is not a homeroom then that's a big no
        if not which in self.homerooms[who]:
            return False

        # 2. Need to have a space to go with only like minded amphipods
        for space in self.homerooms[who]:
            what = self.spaces[space]
            if what not in [SPACE, who]:
                return False

        # 3. Looks good to me
        return True

    def whose_room_is_this(self, which):
        "Determine which type of amphipod lives in this room"

        # 1. Find the space in the homerooms
        for who, spaces in self.homerooms.items():
            if which in spaces:
                return who

        # 2. Well that is strange
        print("*** Very odd %d is not in a room" % which)
        return None

    def can_leave_room(self, which):
        "Can the amphipod leave the room"

        # 1. Whose homeroom is this?
        who = self.whose_room_is_this(which)
        if not who:
            return False

        # 2. Can always leave from the space next to the doorway
        if which == self.homerooms[who][0]:
            return True

        # 3. Otherwise the spaces between here and the doorway must be clear
        for space in self.homerooms[who]:
            if space == which:
                return True
            if self.spaces[space] != SPACE:
                return False

        # 4. Now this is odd, which should have been in the homerooms
        return False

    def deepest_room(self, who):
        "Return the position of the deepest space in the room, or None if occupied"

        # 1. Get the rooms for this amphipod
        rooms = self.homerooms[who]

        # 2. No where to go it the the first room is occupied?
        if self.spaces[rooms[0]] != SPACE:
            return None

        # 3. We can at least make it to the room near the doorway
        result = rooms[0]

        # 4. Can we go deeper ()
        for room in rooms[1:]:
            if self.spaces[room] != SPACE:

                # 5. This is as deep as we can go but what lies below?
                if self.spaces[room] == who:
                    return result
                return None
            result = room

        # 5. Return the location of the deepest space in the amphipod's homeroom
        return result

    def moves_from_room(self, origin, who=None):
        "Return the destination from moving from a room"

        # 1. Get which kind of amphipod is moving (if not given)
        if not who:
            who = self.spaces[origin]

        # 2. Can we leave from here?
        if not self.can_leave_room(origin):
            return []

        # 3. Start with nothing
        result = []

        # 4. Get the doorway for the room
        doorway = self.doorway_for_room(origin)

        # 5. Loop for all the non-doorway spaces in the hallway
        for space in range(self.hall_len):
            if space in self.doorways:
                continue

            # 6. Is the way clear to this space, add it
            if self.clear_hallway(doorway, space):
                result.append(space)

        # 7. Return the destinations
        return result

    def all_moves(self, who=None):
        "Return all the possible moves"

        # 1. Get the amphipods who do not need to move
        fixed = self.frozen()

        # 2. Start with nothing
        result = []

        # 3. Loop for all of the non-empty positions
        for origin, space in enumerate(self.spaces):
            if space == SPACE:
                continue

            # 4. Don't move frozen amphipods
            if origin in fixed:
                continue

            # 5. Are we limiting moves to just on type of amhipod?
            if who and space != who:
                continue

            # 6. Get all of the place you can go from here
            destinations = self.moves_from(origin, who=who)

            # 7. Save the moves
            for where in destinations:
                result.append((origin, where))

        # 8. Return all the possible moves
        return result

    def doorway_for_who(self, who):
        "Return the position of the amphipod's doorway"

        # 1. Get the doorway index
        index = AMPHIPODS.index(who)

        # 2. Return the position of the doorway
        return self.doorways[index]

    def doorway_for_room(self, room):
        "Return the position of the room's doorway"

        # 1. Whose room is this
        who = self.whose_room_is_this(room)

        # 2. Get the doorway index
        return self.doorway_for_who(who)

    def hall_steps(self, move, who=None):
        "Return the number of steps when moving from the hall"

        # 1. Get which kind of amphipod is moving (if not given)
        if not who:
            who = self.spaces[move[0]]

        # 2. Get the location of their doorway
        doorway = self.doorway_for_who(who)

        # 3. Get how far into the room they are going
        into_room = self.homerooms[who].index(move[1])

        # 4. Total steps is from the hall position to the doorway and then into the room
        return 1 + abs(doorway - move[0]) + into_room

    def room_steps(self, move):
        "Return the number of steps when moving from a room"

        # 1. Get the location of the nearest doorway and depth in the room
        doorway, depth = self.nearest_doorway(move[0])

        # 2. Total steps is from the room position to the doorway and then down the hall
        return 1 + depth + abs(doorway - move[1])

    def nearest_doorway(self, origin):
        "Return the location of the room's doorway and the depth in the room"

        # 1. Loop for all of the rooms
        for whose, rooms in self.homerooms.items():

            # 2. Are we here?
            if origin in rooms:

                # 3. Get the location of the doorway
                doorway = self.doorways[AMPHIPODS.index(whose)]

                # 4. Get room depth
                into_room = rooms.index(origin)

                # 5. Return both
                return doorway, into_room

        # 6. Something is wrong
        print("Unable to determine nearest doorway for position %s" % origin)
        return None, None

    def steps(self, move, who=None):
        "Returns the number of steps in the move"

        # 1. Get which kind of amphipod is moving (if not given)
        if not who:
            who = self.spaces[move[0]]

        # 2. Is this a move from the hall to a room or from a room
        if self.is_in_hall(move[0]):
            return self.hall_steps(move, who=who)

        # 3. Is this a move from a room to the hall or room to room
        if self.is_in_hall(move[1]):
            return self.room_steps(move)

        # 4. So, it must be room to room via a a pair of doorways
        doorway = self.doorway_for_who(who)
        return self.room_steps([move[0], doorway]) + self.hall_steps([doorway, move[1]], who=who)

    def cost(self, move, who=None):
        "Return the cost of the move"

        # 1. Who is moving, First Base
        if not who:
            who = self.spaces[move[0]]
            if who == SPACE:
                print("*** Bad move: %d %s to %d %s <%s> [%s]" %
                      (move[0], self.spaces[move[0]], move[1], self.spaces[move[1]],
                       self.text, ''.join(self.spaces)))
                return None

        # 2. How many steps are being moved
        how_far = self.steps(move, who=who)

        # 3. Return the cost of the move
        return ENERGY[who] * how_far

    def execute(self, move):
        "Return the updated position as text"

        # 1. Get who is moving
        who = self.spaces[move[0]]

        # 2. Make a copy of the spaces
        new_spaces = self.spaces.copy()

        # 3. Where they were is now empty
        new_spaces[move[0]] = SPACE

        # 4. They are now at the destination
        assert new_spaces[move[1]] == SPACE
        new_spaces[move[1]] = who

        # 5. Return the updated text
        return ''.join(new_spaces)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     p o s i t i o n s . p y                    end
# ======================================================================
