
# ======================================================================
# Crossed Wires
#   Advent of Code 2024 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           g a t e . p y
# ======================================================================
"Gate for the Advent of Code 2024 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Gate
# ======================================================================


class Gate(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Crossed Wires"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = None
        self.type = None
        self.inputs = {}
        self.output = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Split text
        input_1, gate_type, input_2, arrow, name = text.split()
        assert arrow == "->"

        # 2. Set the values
        self.name = name
        self.type = gate_type
        self.inputs[input_1] = None
        self.inputs[input_2] = None

    def reset(self):
        "Clear gate -- usesful in testing"
        for inp in self.inputs:
            self.inputs[inp] = None
        self.output = None

    def waiting_on(self, wires):
        "Return the names of the input wires without values"

        # 1. If we can intuit, the result there is nothing to wait on
        if self.intuit(wires) is not None:
            return set()

        # 2. Else return what we are still looking for
        return set([name for name, value in self.inputs.items()
                    if value is None])

    def get_values_from_wires(self, wires):
        "Try to get missing wire values, Return count of values"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the input wires
        for in_wire, in_value in self.inputs.items():

            # 3. If we know the value, increase the count
            if in_value is not None:
                result += 1
                continue

            # 4. Look for the value
            if in_wire in wires:
                self.inputs[in_wire] = wires[in_wire]
                result += 1

        # 5. Return the count of the input wires with values
        return result

    def process(self, wires):
        "Return the value of the gate"
        assert self.type is not None

        # 1. Return the value if it is already known
        if self.output is not None:
            return self.output

        # 2. Get the values for the wires
        value_knt = self.get_values_from_wires(wires)

        # 3. Do don't have all the values, return unknown
        if value_knt < 2:
            return None

        # 4. Process the inputs
        values = list(self.inputs.values())
        match self.type:
            case "AND":
                result = values[0] & values[1]
            case "OR":
                result = values[0] | values[1]
            case "XOR":
                result = values[0] ^ values[1]

        # 5. Save and return the result
        self.output = result
        return result

    def intuit(self, wires):
        "Intuit the gate result even if there is an input missing"

        # 1. Get the regular result (if there is one)
        result = self.process(wires)

        # 2. We are done if we already know the result
        if result is not None:
            return result

        # 3. Get the values for the wires
        value_knt = self.get_values_from_wires(wires)

        # 4. If both are unknown, not much we can do
        if value_knt == 0:
            return None

        # 5. Get the values
        values = list(self.inputs.values())

        # 6. Get the known value
        if values[0] is None:
            value = values[1]
        else:
            value = values[0]

        # 7. Try to process with what we know
        result = None
        match self.type:
            case "AND":
                if value == 0:
                    result = 0
            case "OR":
                if value == 1:
                    result = 1

        # 8. Save and return the result
        self.output = result
        return result

    def has_inputs(self, in1, in2):
        "Return true if the gate has these inputs"
        return in1 in self.inputs and in2 in self.inputs

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          g a t e . p y                         end
# ======================================================================
