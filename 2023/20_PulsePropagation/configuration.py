
# ======================================================================
# Pulse Propagation
#   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    c o n f i g u r a t i o n . p y
# ======================================================================
"Configuration for the Advent of Code 2023 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import prod, lcm

from module import Module, PULSELOW, Pulse, TYPECONJUNCTION

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
BUTTON_TEXT = "button -> broadcaster"
SINK_TEXT = "$%s -> "

# ======================================================================
#                                                          Configuration
# ======================================================================


class Configuration(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pulse Propagation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.modules = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Precondition axioms
        assert text is not None and len(text) > 0

        # 2. Loop for all lines of the input
        for line in text:

            # 3. Create a module from the line of text and save it
            mod = Module(text=line, part2=self.part2)
            self.modules[mod.name] = mod

        # 4. Create and add the Desert Machine Headquarters button
        mod = Module(text=BUTTON_TEXT, part2=self.part2)
        self.modules[mod.name] = mod

        # 5. Make all the input connections
        for mod in list(self.modules.values()):
            for out in mod.outputs:

                # 6. New modules, add as a sink
                if out not in self.modules:
                    newmod = Module(text=SINK_TEXT % out, part2=self.part2)
                    self.modules[newmod.name] = newmod

                # 7. Connect the input
                self.modules[out].add_input(mod.name)

    def press_button(self):
        "Press the button"

        # 1. Start with the initial button press
        pulses = [Pulse(orig="button", level=PULSELOW, dest="broadcaster")]

        # 2. Loop while there is something to do
        while pulses:
            pulse = pulses.pop(0)

            # 3. Record the pulse in the sending module counts
            self.modules[pulse.orig].pulse_out(pulse.level)

            # 4. Tell the receiving module of the pulse
            out_pulse = self.modules[pulse.dest].pulse_in(pulse.level, pulse.orig)

            # 5. Record the outgoing pulse
            for dest in out_pulse.dest:
                new_pulse = Pulse(orig=out_pulse.orig, level=out_pulse.level, dest=dest)
                pulses.append(new_pulse)

        # 6. Return the pulse level totals
        return self.total_pulses()

    def total_pulses(self):
        "Return the total low and high pulses"

        return (sum(mod.low_pulses for mod in self.modules.values()),
                sum(mod.high_pulses for mod in self.modules.values()))

    def reset_all(self):
        "Reset all the modules to their initial state"
        for mod in self.modules.values():
            mod.reset()

    def multiple_presses(self, pressed=1000):
        "Press the Desert Machine Headquarters button module a bunch of times"

        # 1. Press it a lot
        for _ in range(pressed):
            self.press_button()

        # 2. Return the total pulse counts
        return prod(self.total_pulses())

    def low_pulse_to_rx(self):
        "Returns the number of pulses needed to send a low pulse to rx"

        # 1. Get the inputs to the ultimate conjunction
        con_inputs = self.inputs_to_rx()

        # 2. Start with no presses found
        con_presses = {}
        for con in con_inputs:
            con_presses[con] = 0

        # 3. Loop until we find the press count for all of the inputs
        presses = 0
        while any(0 == p for p in con_presses.values()) and presses < 9999:

            # 4. Press the button
            self.press_button()
            presses += 1

            # 5. Did any of the conjunction inputs produce a new high pulse
            for con in con_inputs:
                if con_presses[con] > 0:
                    continue
                if self.modules[con].high_pulses == 1:
                    con_presses[con] = presses
                    print(f"high on {con} at {presses} presses")

        # 6. Return the number of presses When all the cycles match
        return lcm(*con_presses.values())

    def inputs_to_rx(self):
        "Return the inputs to rx"

        # 1. Get the single conjunction input to rx
        to_rx = list(self.modules["rx"].inputs.keys())
        assert len(to_rx) == 1, f"Not just input to rx {to_rx}"
        assert self.modules[to_rx[0]].type == TYPECONJUNCTION, f"{to_rx[0]} is not a conjunction"

        # 2. Return the inputs to the conjunction
        return sorted(self.modules[to_rx[0]].inputs.keys())


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 c o n f i g u r a t i o n . p y                end
# ======================================================================
