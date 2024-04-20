
# ======================================================================
# Pulse Propagation
#   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           m o d u l e . p y
# ======================================================================
"Module for the Advent of Code 2023 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TYPEBROADCASTER = "B"
TYPEFLIPFLOP = "F"
TYPECONJUNCTION = "C"
TYPEDMHBUTTON = "D"
TYPESINK = "S"

FLAGFLIPFLOP = "%"
FLAGCONJUNCTION = "&"
FLAGBROADCASTER = "broadcaster"
FLAGBUTTON = "button"
FLAGSINK = "$"

PULSELOW = "L"
PULSEHIGH = "H"

FLIPFLOPOFF = "Off"
FLIPFLOPON = "On"


SPLITTER = " -> "
COMMA = ","

# ----------------------------------------------------------------------
#                                                                   type
# ----------------------------------------------------------------------
Pulse = namedtuple("Pulse", "orig, level, dest")

# ======================================================================
#                                                                 Module
# ======================================================================


class Module(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pulse Propagation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = None
        self.type = None
        self.outputs = []
        self.inputs = {}
        self.state = FLIPFLOPOFF
        self.low_pulses = 0
        self.high_pulses = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Split front matter from outputs
        parts = text.split(SPLITTER)
        assert len(parts) == 2

        # 2. Save the outputs
        for out in parts[1].split(COMMA):
            self.outputs.append(out.strip())

        # 3. Get the type and name
        if parts[0].startswith(FLAGFLIPFLOP):
            self.name = parts[0][1:]
            self.type = TYPEFLIPFLOP
            return
        if parts[0].startswith(FLAGCONJUNCTION):
            self.name = parts[0][1:]
            self.type = TYPECONJUNCTION
            return
        if parts[0].startswith(FLAGBROADCASTER):
            self.name = FLAGBROADCASTER
            self.type = TYPEBROADCASTER
            return
        if parts[0].startswith(FLAGBUTTON):
            self.name = FLAGBUTTON
            self.type = TYPEDMHBUTTON
            return
        if parts[0].startswith(FLAGSINK):
            self.name = parts[0][1:]
            self.type = TYPESINK
            return

        # 4. We shouldn't reach here
        assert False, f"Module unknown {text}"

    def add_input(self, who):
        "Add an input source"

        # 1. Add this input to the others
        self.inputs[who] = PULSELOW

    def pulse_out(self, pulse_level):
        "Record an outgoing pulse"

        if pulse_level == PULSELOW:
            self.low_pulses += 1
        else:
            self.high_pulses += 1

    def pulse_in(self, level, orig):
        "Recieve an incoming pulse and process by module type"

        # 1. Broadcaster proprogate the incomming pulse
        if self.type == TYPEBROADCASTER:
            return Pulse(orig=self.name, level=level, dest=self.outputs)

        # 2. Flip-flops ignore high pulses, and change state on low ones
        if self.type == TYPEFLIPFLOP:
            if level == PULSEHIGH:
                return Pulse(orig=self.name, level=level, dest=[])
            if self.state == FLIPFLOPOFF:
                level = PULSEHIGH
                self.state = FLIPFLOPON
            else:
                level = PULSELOW
                self.state = FLIPFLOPOFF
            return Pulse(orig=self.name, level=level, dest=self.outputs)

        # 3. Conjunctions remembers, and sends low pulse if all inputs were high else low
        if self.type == TYPECONJUNCTION:
            self.inputs[orig] = level
            if all(v == PULSEHIGH for v in self.inputs.values()):
                level = PULSELOW
            else:
                level = PULSEHIGH
            return Pulse(orig=self.name, level=level, dest=self.outputs)

        # 4. The Desert Machine Headquarters button sends a single low pulse
        if self.type == TYPEDMHBUTTON:
            return Pulse(orig=self.name, level=PULSELOW, dest=self.outputs)

        # 5. Pulses to syncs just go down the drain
        if self.type == TYPESINK:
            return Pulse(orig=self.name, level=PULSELOW, dest=[])

        # 6. Unknown module type
        assert False, f"Unknwn module type {self.type}"

    def reset(self):
        "Return to the original state"
        self.state = FLIPFLOPOFF
        for key in self.inputs:
            self.inputs[key] = PULSELOW
        self.high_pulses = 0
        self.low_pulses = 0

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        m o d u l e . p y                       end
# ======================================================================
