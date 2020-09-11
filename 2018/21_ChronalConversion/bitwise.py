# ======================================================================
# Chronal Conversion
#   Advent of Code 2018 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b i t w i s e . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Bitwise
# ======================================================================


class Bitwise(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Conversion"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.device = device.Device(text=text, part2=part2)

    def run_until(self, pc=0, verbose=False, limit=0):
        self.device.reset()
        steps = 0
        pc_before = self.device.pc
        regs_before = [r for r in self.device.regs]

        while self.device.step() and (limit == 0 or steps < limit) and pc_before != pc:
            if verbose:
                inst = self.device.program[pc_before]
                print("ip=%d %s %s %d %d %d %s" %
                      (pc_before, str(regs_before),
                       inst[device.OPCODE], inst[device.REGA], inst[device.REGB], inst[device.REGC],
                       str(self.device.regs)))
            steps += 1
            pc_before = self.device.pc
            regs_before = [r for r in self.device.regs]
        if verbose:
            inst = self.device.program[pc_before]
            print("Stopped at ip=%d %s %s %d %d %d %s" %
                  (pc_before, str(regs_before),
                   inst[device.OPCODE], inst[device.REGA], inst[device.REGB], inst[device.REGC],
                   str(self.device.regs)))


    def run_until_repeat(self, pc=0, reg=0, verbose=False, limit=0):
        self.device.reset()
        steps = 0
        pc_before = self.device.pc
        regs_before = [r for r in self.device.regs]
        result = None
        reg_seen = set()

        while self.device.step() and (limit == 0 or steps < limit):
            if pc_before == pc:
                if regs_before[reg] in reg_seen:
                    return result
                result = regs_before[reg]
                reg_seen.add(result)
            steps += 1
            pc_before = self.device.pc
            regs_before = [r for r in self.device.regs]
        if verbose:
            print("Stopped at ip=%d steps=%s regs=%s" % (pc_before, steps, str(regs_before)))
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Run until important check
        self.run_until(pc=28, verbose=verbose, limit=limit)
        # 2. Return the solution for part one
        return self.device.regs[4]


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.run_until_repeat(pc=28, reg=4, verbose=verbose, limit=limit)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      b i t w i s e . p y                     end
# ======================================================================
