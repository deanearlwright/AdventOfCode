
# ======================================================================
# Crossed Wires
#   Advent of Code 2024 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

import gate

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
UNK = -1

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0205
    "Object for Crossed Wires"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.wires = {}  # name --> value
        self.gates = {}  # output --> gate
        self.ands = set()
        self.xors = set()
        self.ors = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for line of the text
        for line in self.text:

            # 2. If it has a colon then it is a wire
            if line[3] == ":":
                name, value = line.split(":")
                self.wires[name] = int(value)
                continue

            # 3. Else it is a gate
            new_gate = gate.Gate(text=line, part2=self.part2)
            self.gates[new_gate.name] = new_gate

            # 4. Add the gate to the appropiate set
            match new_gate.type:
                case "AND":
                    self.ands.add(new_gate)
                case "XOR":
                    self.xors.add(new_gate)
                case "OR":
                    self.ors.add(new_gate)

    def solve_unkowns(self):
        "Keep processing gate until there are no unknowns"

        # 1. Reset to base state
        self.reset_all()

        # 2. Loop forever
        while True:

            # 3. Get the names of the known gates
            unknown = self.unknown_gates()

            # 5. If there are none, we have solved it
            if len(unknown) == 0:
                break

        # 7. Return the list of the still unknown gates -- empty if solved
        return unknown

    def unknown_gates(self):
        "Return names of gates with unknown values"

        # 1. Start with nothing
        result = set()

        # 2. Loop for all the gates
        for name, a_gate in self.gates.items():

            # 3. If we already know the output of this gate, skip it
            if name is self.wires:
                continue

            # 4. Get the value from this gate
            value = a_gate.intuit(self.wires)

            # 5. If we now know the value, save it
            if value is not None:
                self.wires[name] = value

            # 6. Else add it to the unknown list
            else:
                result.add(name)

        # 7. Return the list of unknown gates/wires
        return result

    def z_number(self, prefix="z"):
        "Get the znn number"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the possible z values
        for number in range(100):

            # 3. Get the z name
            name = f"{prefix}{number:02d}"

            # 4. If the name is defined, add it in
            if name in self.wires:
                result += self.wires[name] * pow(2, number)
                continue
            else:
                break

        # 5. Return the z number
        return result

    def get_largest_z(self, prefix="z"):
        "Find the largest z wire"

        # 1. Run the adder
        unknowns = self.solve_unkowns()
        assert len(unknowns) == 0

        # 1. Loop for the possible z values
        for number in range(100):

            # 2. Get the z name
            name = f"{prefix}{number:02d}"

            # 3. If the name is defined, keep going
            if name not in self.wires:
                return number - 1

        # 4. Should not get here
        assert False

    @staticmethod
    def has_inputs(inp_1, inp_2, gates):
        "Return the gate with the specified inputs or None"

        # 1. Loop for all the gates
        for a_gate in gates:

            # 2. Does the gate have those inputs?
            result = a_gate.has_inputs(inp_1, inp_2)

            # 3. If it does, return it
            if result:
                return a_gate.name

        # 4. We never found it
        return None

    def fix_adder(self):
        """Find the swapped wires in the binary adder

        Reference: Switching and Finite Automata Theory by Zvi Kohavi

        0: Z0 = x0 XOR Y0            c0 = x0 AND y0
        1: z1 = x1 XOR y1 XOR c0     c1 = (X1 AND Y1) OR ((x1 XOR y2) AND c0)
        2: z2 = x2 XOR y2 XOR c1     c2 = (X2 AND Y2) OR ((x2 XOR y2) AND c1)
           ...
        n: zn = cn-1
        """

        # 1. Start with nothing
        result = set()
        largest_z = self.get_largest_z()

        # 2. Loop for possible the output lines
        position = 0
        while position < largest_z:

            # 3. Input and output wire names
            x_wire = f"x{position:02d}"
            y_wire = f"y{position:02d}"
            z_wire = f"z{position:02d}"

            # 4. The first position is special (no carry in)
            if position == 0:
                c_wire = self.has_inputs(x_wire, y_wire, self.ands)
                xor_gate = self.has_inputs(x_wire, y_wire, self.xors)
                assert c_wire is not None and xor_gate == z_wire

            # 5. Else we need XOR and AND and carry in gates
            else:
                and_gate = self.has_inputs(x_wire, y_wire, self.ands)
                xor_gate = self.has_inputs(x_wire, y_wire, self.xors)
                out_gate = self.has_inputs(xor_gate, c_wire, self.xors)

                # 6. Attempt fix if we can't find the z output gate
                if out_gate is None:
                    self.swap_output(result, xor_gate, and_gate)
                    position = 0
                    continue

                # 7. Attempt fix if the output is not what we expect
                if out_gate != z_wire:
                    self.swap_output(result, out_gate, z_wire)
                    position = 0
                    continue

                # 8. Get the next carry
                c_gate = self.has_inputs(xor_gate, c_wire, self.ands)
                c_wire = self.has_inputs(and_gate, c_gate, self.ors)
                assert c_gate is not None and c_wire is not None

            # 9. Forward to the next position
            position += 1

        # 10. Highest position has only carry in
        assert c_wire == f"z{position:02d}"

        # 11. Return the swaps
        return result

    @staticmethod
    def format_swaps(swaps):
        "Return the formatted swaps"

        # 1. Make it into a list
        swaps = list(swaps)

        # 2. Sort them
        swaps.sort()

        # 2. Join with commas and return
        return ",".join(swaps)

    def reset_all(self):
        "Put all the gate and wires back to unkown"

        # 1. Reset all the gates
        for a_gate in self.gates.values():
            a_gate.reset()

        # 2. Remove non-x and y wires
        for wire in list(self.wires):
            if wire.startswith("x") or wire.startswith("y"):
                continue
            del self.wires[wire]

    def check_adder(self):
        "Test the adder"

        # 1. Reset the adder
        self.reset_all()

        # 2. Run the adder
        unknowns = self.solve_unkowns()
        assert len(unknowns) == 0

        # 1. Get the inputs and outputs
        in_x = self.z_number(prefix="x")
        in_y = self.z_number(prefix="y")
        out = self.z_number(prefix="z")

        # 2. Check the result
        return out == in_x + in_y

    def swap_output(self, swaps, name1, name2):
        "Swap the two gate outputs, updating and returning swaps"
        assert name1 is not None
        assert name2 is not None

        # 1. Update swaps
        swaps.add(name1)
        swaps.add(name2)

        # 2. Get the current objects
        gate1 = self.gates[name1]
        gate2 = self.gates[name2]

        # 3. Swap the names of the two gates
        gate1.name = name2
        gate2.name = name1

        # 4. Update the gates dictionary
        self.gates[name1] = gate2
        self.gates[name2] = gate1

        # 5. Return swaps
        return swaps

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.solve_unkowns()
        return self.z_number()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        swaps = self.fix_adder()
        assert self.check_adder()
        return self.format_swaps(swaps)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        d e v i c e . p y                       end
# ======================================================================
