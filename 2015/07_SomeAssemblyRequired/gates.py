# ======================================================================
# Some Assembly Required
#   Advent of Code 2015 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          g a t e s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_TWO = re.compile(r'([0-9a-z]+) (AND|OR|LSHIFT|RSHIFT) ([0-9a-z]+) -> ([a-z]+)')
RE_ONE = re.compile(r'(NOT) ([0-9a-z]+) -> ([a-z]+)')
RE_SET = re.compile(r'([0-9a-z]+) -> ([a-z]+)')
SIXTEENBITS = 65535

# ======================================================================
#                                                                  Gates
# ======================================================================


class Gates(object):   # pylint: disable=R0902, R0205
    "Object for Some Assembly Required"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.wires = {}

    def run(self, verbose=False, limit=0):
        "Run the circuit"

        # 1. Start with nothing
        repeats = 0

        # 2. Loop until done
        while len(self.text) > 0 and self.value("a") is None and (repeats < limit or limit == 0):

            # 3. Run the instructions once
            self.run_once(verbose=verbose)

            # 4. Increment count
            repeats += 1

    def run_once(self, verbose=False):
        "Go through the instructions one time"

        # 1. Loop for all the instructions
        for inst in self.text:

            # 2. Decode the instruction
            inst_parts = self.decode(inst)

            # 3. If we have both operands execute the instruction
            if inst_parts[1] is not None and inst_parts[2] is not None:
                self.execute(inst_parts, verbose=verbose)

    def decode(self, inst):
        "Decode the instructions into opcode, op1, op2, and result"

        # 1. Dual operand instructions op1 AND op2 -> result
        istwo = RE_TWO.match(inst)
        if istwo is not None:
            parts = istwo.groups()
            opcode = parts[1]
            op1 = parts[0]
            op2 = parts[2]
            result = parts[3]
            return opcode, self.value(op1), self.value(op2), result

        # 2. Single operand instructions NOT op1 -> result
        isone = RE_ONE.match(inst)
        if isone is not None:
            parts = isone.groups()
            opcode = parts[0]
            op1 = parts[1]
            op2 = parts[1]
            result = parts[2]
            return opcode, self.value(op1), self.value(op2), result

        # 3. SET instruction op1 -> result
        isset = RE_SET.match(inst)
        if isset is not None:
            parts = isset.groups()
            opcode = "SET"
            op1 = parts[0]
            op2 = parts[0]
            result = parts[1]
            return opcode, self.value(op1), self.value(op2), result

        # 4. Invalid instruction
        print("Invalid instruction", inst)
        return "unknown", None, None, 'unknown'

    def execute(self, inst_parts, verbose=False):
        "Execute a single instruction"

        # 1. Instruction decode
        opcode, op1, op2, result = inst_parts

        # 2. Execute the instruction
        if opcode == "AND":
            rvalue = op1 & op2
        elif opcode == "OR":
            rvalue = op1 | op2
        elif opcode == "RSHIFT":
            rvalue = op1 >> op2
        elif opcode == "LSHIFT":
            rvalue = SIXTEENBITS & op1 << op2
        elif opcode == "NOT":
            rvalue = SIXTEENBITS & (~op1)
        else:
            if "part_one" in self.wires and result == "b":
                rvalue = self.wires["part_one"]
            else:
                rvalue = op1

        # 3. Set the value
        self.wires[result] = rvalue
        if verbose:
            print(op1, opcode, op2, "->", result, rvalue)

        # 4. And return it
        return rvalue

    def value(self, wire):
        "Return the value on the a wire"

        # 1. Numbers are just themselves
        if wire.isdigit():
            return int(wire)

        # 2. If we know the value, return it
        if wire in self.wires:
            return self.wires[wire]

        # 3. Else we don't know the value (yet)
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        self.run(verbose=verbose, limit=limit)
        return self.value("a")

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.run(verbose=verbose, limit=limit)
        part_one = self.value("a")
        if verbose:
            print("Part on result = ", part_one)
            print("Starting part2")
        self.wires = {}
        self.wires["part_one"] = part_one
        self.run(verbose=verbose, limit=limit)
        return self.value("a")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         g a t e s . p y                        end
# ======================================================================
