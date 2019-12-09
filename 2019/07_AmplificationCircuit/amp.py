# ======================================================================
# Amplification Circuit
#   Advent of Code 2019 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             u o m a p . p y
# ======================================================================
"Amps for Amplification Circuit problem for Advent of Code 2019 Day 07"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from __future__ import print_function

from itertools import permutations

import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PHASES = '01234'
FEEDBACK = '56789'
LETTERS = 'ABCDE'

# ======================================================================
#                                                                   Amps
# ======================================================================


class Amps(object):
    """Object representing a series of amplifiers"""

    def __init__(self, num=5, inp=0, text=None, feedback=False):

        # 1. Start with no amplifiers
        self.amps = []
        self.num = num
        self.inp = inp
        self.text = text
        self.output = 0
        self.phases = None
        self.feedback = feedback
        #print("Creating amplifiers feedback=%s" % (feedback))

        # 2. Create as many amplifiers as needed
        assert num <= 5
        for indx in range(num):

            # 3. Create an amplifier and add it to the list
            self.amps.append(Amp(letter=LETTERS[indx], text=text))

    def find_best(self, watch=False):
        "Find the ordering of phases to maximize output"

        #print("find_best feedback=%s watch=%s" % (self.feedback, watch))
        # 1. Start with a very poor output
        best_output = 0

        # 2. loop for all of the permutations of the phases
        if self.feedback:
            phase_numbers = FEEDBACK
        else:
            phase_numbers = PHASES
        for phases in list(permutations(phase_numbers)):

            # 3, Run this set of phases
            if self.feedback:
                output = self.run_feedback(phases=phases, inp=self.inp, watch=watch)
            else:
                output = self.run_series(phases=phases, inp=self.inp)

            # 4. If this is better that what we had before, save it
            if output > best_output:
                best_output = output
                self.output = output
                self.phases = phases
                if watch:
                    print("Setting best to %d for phase %s" % (output, phases))

        # 5. Return the best output
        return best_output

    def run_series(self, phases=PHASES, inp=None):
        "Run all the amplifiers in series"

        # 1. Start with no final output and the initial input
        self.output = None
        if inp is None:
            inp = self.inp

        # 2. Run all the amplifiers in turn
        for indx in range(self.num):

            # 3. Run one amplifier
            output = self.amps[indx].run(inp=inp, phase=int(phases[indx]))

            # 4. If there was a problem exit
            if output is None:
                break

            # 5. Set up to run the next amplifier
            inp = output

        # 6. Return the result from the last amplifier run
        return output

    def run_feedback(self, phases=FEEDBACK, inp=None, watch=False):
        "Run all the amplifiers in series with a feedback loop"

        # 1. Start with no final output and the initial input
        self.output = None
        inputs = [0, 0, 0, 0, 0, 0]
        status = [intcode.STOP_RUN,
                  intcode.STOP_RUN,
                  intcode.STOP_RUN,
                  intcode.STOP_RUN,
                  intcode.STOP_RUN,
                  intcode.STOP_RUN,]
        outputs = [0, 0, 0, 0, 0, 0]
        if inp is None:
            inputs[0] = self.inp
        else:
            inputs[0] = inp

        # 2. Reset all of the amplifiers
        for indx in range(self.num):
            self.amps[indx].computer = None

        # 3. Run amplifiers until done:
        while status[0] != intcode.STOP_HLT:
            if watch:
                print('Starting feedback loop with input=%s' % (inputs[0]))

            # 4. Run all the amplifiers in turn
            for indx in range(self.num):

                # 5. Run one amplifier
                output = self.amps[indx].fb_run(inp=inputs[indx], phase=int(phases[indx]))

                # 6. If there was a problem exit
                if output is None:
                    return None

                # 7. Set up to run the next amplifier
                if watch:
                    print("phases=%s, amp %s output=%s" % (phases, indx, output))
                status[indx] = output[0]
                output = output[1]
                outputs[indx] = output
                inputs[0] = output
                inputs[indx+1] = output

        # 8. Return the result from the last amplifier run
        return output

# ======================================================================
#                                                                    Amp
# ======================================================================


class Amp(object):   #pylint: disable=R0903
    """Object representing a series of amplifier"""

    def __init__(self, letter='Z', text=None):

        # 1. Store the values
        self.letter = letter
        self.text = text
        self.computer = None

    def run(self, phase=0, inp=0):
        "Return the result of running the computer with inputs phase and inp"

        # 1. Create a computer with the program from text
        self.computer = intcode.IntCode(text=self.text)

        # 3. Run the computer with inputs
        result = self.computer.run(inp=[phase, inp])

        # 4. Make sure it ended with a halt instruction
        if result != intcode.STOP_HLT:
            print("amplifier %s input=[%d,%d] ended with %d" %
                  (self.letter, phase, inp, result))
            return None

        # 5. Return the output
        output = self.computer.outputs()
        if len(output) != 1:
            print("amplifier %s input=[%d,%d] ended produced %d outputs" %
                  (self.letter, phase, inp, len(output)))
            return None
        return output[0]

    def fb_run(self, phase=0, inp=0):
        "Return the status and output of running the amplifier with inputs phase and inp"

        # 1. Create a computer with the program from text (if not already created)
        if self.computer is None:
            self.computer = intcode.IntCode(text=self.text)
            inp = [phase, inp]
        else:
            inp = [inp]

        # 3. Run the computer with inputs
        #print("Running computer with input = %s, counter=%s" % (inp, self.computer.counter))
        result = self.computer.run(inp=inp)

        # 4. Make sure it ended with a halt instruction or input instruction
        if result not in (intcode.STOP_HLT, intcode.STOP_INP):
            print("amplifier %s input=%s ended with %d" % (self.letter, inp, result))
            return None

        # 5. Return the result and output
        output = self.computer.outputs()
        if len(output) != 1:
            print("amplifier %s input=%s ended produced %d outputs" %
                  (self.letter, inp, len(output)))
            return None
        return (result, output[0])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           u o m a p . p y                      end
# ======================================================================
