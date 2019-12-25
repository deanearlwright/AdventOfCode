# ======================================================================
# Cryostasis
#   Advent of Code 2019 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a d v _ d r o i d . p y
# ======================================================================
"Adventure droid for the Cryostasis problem for AoC 2019 Day 25"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

from textwrap import wrap

import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NL = 10

SOLVE_CMD = 'SOLVE'
SOLVE_ITEMS = ['p', 'c', 'l', 'a', 'f', 'b', 'm', 'u']
SOLVE_START = 2**len(SOLVE_ITEMS)
SOLVE_DIR = 'north'
SOLVE_ALERT = "Alert! Droids on this ship"

TRANSLATE0 = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west',
    'i': 'inv',
    't': 'take',
    'd': 'drop',
    'x': SOLVE_CMD,
    'q': 'quit'}

TRANSLATE1 = {
    'c': 'candy cane',
    'b': 'boulder',
    'i': 'infinite loop',
    'm': 'mutex',
    'u': 'mug',
    'p': 'prime number',
    'g': 'giant electromagnet',
    'e': 'escape pod',
    'l': 'loom',
    'h': 'photons',
    'o': 'molten lava',
    'f': 'food ration',
    'a': 'asterisk'}

META_CMDS = {
    '1': [
        's',     # -> Holo Deck (3)
        't b',   # boulder
        'e',     # -> Science Lab (18)
        't f',   # food ration
        'w',     # -> Holo Deck (3)
        'w',     # -> Observatory (19)
        't a',   # asterisk
        'e',     # -> Holo Deck (3)
        'n',     # -> Hull Breach (1)
        'e',     # -> Crew Quarter (2)
        't c',   # candy cane
        'n',     # -> Stables (4)
        # 't i',   # infinate loop [Well what did you expect?]
        'n',     # -> Hallway (5)
        't m',   # mutex
        'w',     # -> Arcade (9)
        # 't g',   # giant electromagnet [Stuck - can't move]
        'e',     # -> Hallway (5)
        'n',     # -> Hot Chocolate Fountain (8)
        't p',   # take prime number
        'e',     # -> Cooridor (10)
        # 't e',   # escape pod [Launched into space]
        'w',     # -> Hot Chocolate Fountain (8)
        's',     # -> Hallway (5)
        's',     # -> Stables (4)
        'e',     # -> Engineering (6)
        'n',     # -> Navigation (7)
        't u',   # mug
        's',     # -> Engineering (6)
        'w',     # -> Stables (4)
        's',     # -> Crew Quarter (2)
        'e',     # -> Kitchen (11)
        'n',     # -> Storage (12)
        't l',   # loom
        's',     # -> Kitchen (11)
        'e',     # -> Warp Drive (13)
        's',     # -> Passages (14)
        'w',     # -> Gift Wrapping (16)
        # 't o',   # molten lava [Too hot - you melt]
        'e',     # -> Passages (14)
        'e',     # -> Sick Bay (15)
        # 't h',   # photons [Eaten by a Grue]
        'e',     # -> Security Checkpoint (17)
    ],
}

TEXT_WIDTH = 70


# ======================================================================
#                                                                  Droid
# ======================================================================


class Droid():
    """Object representing an adventure droid"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.computer = intcode.IntCode(text=text)
        self.out = None
        self.inp = None
        self.items = None
        self.carrying = None
        self.attempting = 256

    def interactive(self, watch=False):
        "Run the droid interactively"

        # 1. Assume that the droid will want more input
        halted = intcode.STOP_INP

        # 2. Loop while obtaining input
        while halted == intcode.STOP_INP:

            # 3. Run the droid
            halted = self.computer.run(watch=watch)

            # 4. Output anything from the droid
            self.out = self.computer.outputs()
            output = ''.join([chr(_) for _ in self.out]).replace('\n', '\n \n')
            alert = False
            for text in output.split(chr(NL)):
                for line in wrap(text, width=TEXT_WIDTH):
                    if SOLVE_ALERT in line:
                        alert = True
                    print(line)

            # 5. Get human (or auto human) input
            if self.items:
                if not alert:
                    print("Solved ...")
                    self.items = None
                    self.inp = 'inv'
                else:
                    self.inp = self.solving_inp()
            else:
                self.inp = Droid.get_input()
            if self.inp == 'quit':
                break
            if self.inp == SOLVE_CMD:
                self.items = SOLVE_ITEMS
                self.carrying = set(SOLVE_ITEMS)
                self.attempting = SOLVE_START
                self.inp = self.solving_inp()

            # 6. If this is a meta command, expand it
            if self.inp in META_CMDS:
                self.inp = '\n'.join([Droid.get_input(_) for _ in META_CMDS[self.inp]])

            # 7. Send the input to the computer
            for inp in self.inp:
                self.computer.add_inp([ord(inp)])
            self.computer.add_inp([NL])

        # 8. Return computer status
        return halted

    @staticmethod
    def get_input(meta=None):
        "Get an massage human input"

        # 1. Assume human has nothing to say
        human = ''

        # 2. Loop until we get some input
        while not human:

            # 3. Attemp to obtain some input
            if meta:
                human = meta
            else:
                human = input('--> ').strip().lower()

            # 4. Break it into words
            words = human.split()

            # 5. Expand single letter commands
            for index, word in enumerate(words):

                # 5a. Expand verbs
                if index == 0 and word in TRANSLATE0:
                    words[0] = TRANSLATE0[word]

                # 5b. Expand nouns
                if index == 1 and word in TRANSLATE1:
                    words[1] = TRANSLATE1[word]

            # 6. Put the words back together
            human = ' '.join(words)

        # 7. Return the input
        return human

    def solving_inp(self):
        "Try another assortment of objects"

        # 1. We may have failed
        self.attempting -= 1
        if self.attempting < 0:
            print("Solving failed!!!")
            self.items = None
            return 'inv'

        # 2. Get a set of what we want
        binary = '{0:08b}'.format(self.attempting)  # Should be using valiable width
        want = set()
        for index, bdigit in enumerate(binary):
            if bdigit == '1':
                want.add(self.items[index])

        # 3. Determine what to take and drop
        take = want.difference(self.carrying)
        drop = self.carrying.difference(want)
        print("w=%s, t=%s, d=%s" % (want, take, drop))

        # 4. Collect the commands to make that happen
        cmds = []
        for item in take:
            cmds.append('take %s' % TRANSLATE1[item])
            self.carrying.add(item)
        for item in drop:
            cmds.append('drop %s' % TRANSLATE1[item])
            self.carrying.remove(item)

        # 5. Add the direction command
        cmds.append(SOLVE_DIR)

        # 6. Return the commands seperated by new lines
        return '\n'.join(cmds)



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     a d v _ d r o i d . p y                    end
# ======================================================================
