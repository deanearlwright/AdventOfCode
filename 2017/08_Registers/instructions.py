# ======================================================================
# largest value in any register
#   Advent of Code 2017 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                   i n s t r u c t i o n s . p y
# ======================================================================
"A solver for largest value in any register for AoC 2017 Day 08"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DECODE = re.compile(r'([a-z]+) ([a-z]+) (-?[0-9]+) if ([a-z]+) ([=<>!]+) (-?[0-9]+)')

ACTIONS = {'inc': 1,
           'dec': -1}

COMPARE = {'==': lambda x, y: x == y,
           '!=': lambda x, y: x != y,
           '<': lambda x, y: x < y,
           '>': lambda x, y: x > y,
           '<=': lambda x, y: x <= y,
           '>=': lambda x, y: x >= y}

# ======================================================================
#                                                            Instruction
# ======================================================================


class Instruction(object):
    """Object representing a single register instruction"""

    def __init__(self, actreg=None, action='inc', actval=0,
                 cmpreg=None, cmpopr='==', cmpval=0, text=None):

        # 1. Set the initial values
        self.actreg = actreg
        self.action = action
        self.actval = actval
        self.cmpreg = cmpreg
        self.cmpopr = cmpopr
        self.cmpval = cmpval

        # 2. If text is not None, set the values from it
        if text is not None:
            match = DECODE.match(text)
            if not match:
                print("Unable to decode %s" % (text))
            else:
                #print("decoding %s to %s" % (text, match.groups()))
                self.actreg = match.group(1)
                self.action = match.group(2)
                self.actval = int(match.group(3))
                self.cmpreg = match.group(4)
                self.cmpopr = match.group(5)
                self.cmpval = int(match.group(6))

    def __str__(self):
        return "%s %s %d if %s %s %d" % (
            self.actreg, self.action, self.actval,
            self.cmpreg, self.cmpopr, self.cmpval)


    def execute(self, regs=None, verbose=False):
        "Execute a the instruction"

        # 1. Inititalize the registers
        if regs is None:
            regs = defaultdict(lambda: 0)

        # 2. Determine if conditional is true
        conditional = COMPARE[self.cmpopr](regs[self.cmpreg], self.cmpval)

        # 3. If conditional is true, do the increment / decrement
        old_value = regs[self.actreg]
        if conditional:
            new_value = regs[self.actreg] + ACTIONS[self.action] * self.actval
            if verbose:
                print("   %s %s by %d from %d to %d because %s %s %d" %
                      (self.action, self.actreg, self.actval,
                       old_value, new_value,
                       self.cmpreg, self.cmpopr, self.cmpval))
            regs[self.actreg] = new_value
        elif verbose:
            print("   Leaving %s at %d because %s is not %s %d" %
                  (self.actreg, old_value,
                   self.cmpreg, self.cmpopr, self.cmpval))


# ======================================================================
#                                                           Instructions
# ======================================================================


class Instructions(object):
    """Object representing a series of Instructions"""

    def __init__(self, part2=False, text=None):

        # 1. Set the initial values
        self.part2 = part2
        self.highest_value = 0
        self.insts = []
        if text is not None:
            for line in text:
                inst = Instruction(text=line)
                self.insts.append(inst)

    def __str__(self):
        return '\n'.join(str(_) for _ in self.insts)

    def largest(self, verbose=False, limit=0):
        "Determine the largest register after running the instructions"

        # 1. Create a set of registers
        regs = defaultdict(lambda: 0)

        # 2. Execute the instructions
        self.execute(regs, verbose=verbose)

        # 3. Return the largest value in any register
        return max(regs.values())

    def execute(self, regs=None, verbose=False):
        "Execute all of the instructions in turn"

        # 1. Inititalize the registers
        if regs is None:
            regs = defaultdict(lambda: 0)

        # 2. Loop for all of the instructions
        for inum, inst in enumerate(self.insts):

            # 3. Execute each instructions
            if verbose:
                print("%d Executing %s" % (inum, str(inst)))
            inst.execute(regs, verbose=verbose)

            # 4. If part2, determine the highest value held
            if self.part2:
                highest = max(regs.values())
                if highest > self.highest_value:
                    self.highest_value = highest
                    if verbose:
                        print("Setting highest value to %d" % (highest))

    def highest(self, verbose=False, limit=0):
        "Determine the highest value held in any register"

        # 1. Create a set of registers
        regs = defaultdict(lambda: 0)

        # 2. Execute the instructions
        self.highest_value = 0
        self.execute(regs, verbose=verbose)

        # 3. Return the highest value held in any register
        return self.highest_value

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 i n s t r u c t i o n s . p y                  end
# ======================================================================
