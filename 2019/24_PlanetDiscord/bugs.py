# ======================================================================
# Planet of Discord
#   Advent of Code 2019 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            b u g s . p y
# ======================================================================
"Artificial Life for the Planet of Discord problem for AoC 2019 Day 24"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EMPTY = '.'
BUGS = '#'

SIZE = 5
BIODIVERSITY = [2**_ for _ in range(LENGTH)]

# ======================================================================
#                                                                   Bugs
# ======================================================================


class Bugs():
    """Object representing the indigenous life form on Eris"""

    def __init__(self, text=None, size=SIZE):

        # 1. Set the initial values
        self.text = text
        self.size = size
        self.current = EMPTY*SIZE*SIZE
        self.previous = set()
        self.minute = 0

        # 2. If there is a text, set the current state
        if text is not None:
            self.current = self.set_current_from(text)

        # 3. Compute the adjacency indexes based on the size
        self.adjacent = self.set_adjacency()

    def set_current_from_text(self, text):
        "Set the current state from input text"

        # 0. Preconditions
        assert len(text) == size
        assert len(text[0]) == size

        # 1. Start with nothing
        result = []

        # 2. Loop through the rows of the the text
        for row in rows:

            # 3. Append the row to the result
            result.append(row)

        # 4. Return the adjoined rows
        return ''.join(result)

    def set_adjacency(self):
        "Compute and set the adjacent values"

        # 1. Start with nothing
        result = [[] for _ in range(SIZE*SIZE)]

        # 2. Loop until someone sends a message to the specified channal
        while self.first_message_to[channel] is None and halted == intcode.STOP_INP:

            # 2. Run all the network computers
            halted = self.run_all(watch=watch)

            # 3. See if we have spent too much time
            steps += 1
            if steps > maxtime > 0:
                halted = intcode.STOP_STP

        # 4. Return the reason we stopped
        return halted

    def run_until_nat_repeat(self, watch=False, maxtime=0):
        "Run the network until NAT sends to computer 0 the same message twice in a row"

        # 1. Assume that the computer will want more input
        halted = intcode.STOP_INP
        steps = 0

        # 1. Loop until nat sends the same message twice
        while halted == intcode.STOP_INP and (self.last_nat_msg == None or
                                              (self.last_nat_msg != self.prev_nat_msg)):

            # 2. Run all the network computers
            halted = self.run_all(watch=watch, nat=True)

            # 3. See if we have spent too much time
            steps += 1
            if steps > maxtime > 0:
                halted = intcode.STOP_STP

        # 4. Return the reason we stopped
        return halted

    def run_all(self, watch=False, nat=False):
        "Run each computer until it requests input"

        # 1. Assume we will want input
        halted = intcode.STOP_INP
        inp_knt = 0
        out_knt = 0

        # 2.  Loop for every computer in the network
        for cnum, comp in enumerate(self.computers):

            # 3. Is there input for this computer?
            if self.input_queue[cnum]:

                # 3a. Yes, take it from the queue and give it to the computer
                comp.add_inp(self.input_queue[cnum])
                self.input_queue[cnum] = []
                inp_knt += 1

            # 4. If the computer has no input waiting, give something
            else:
                if not comp.any_inp():
                    comp.add_inp(NO_INPUT)
                else:
                    inp_knt += 1

            # 5. Run the computer until it stops:
            halted = comp.run()
            if halted != intcode.STOP_INP:
                if watch:
                    print("Ran number %d, status = %d" % (cnum, halted))
                break

            # 6. If the computer has any output, add it to the output collected already
            outputs = comp.outputs()
            if outputs:
                out_knt += 1
                for out in outputs:
                    self.cur_output[cnum].append(out)

            # 7. Process any collected messages in the output of this computer
            snd_knt = self.process_messages(cnum, watch=watch)

        # 8. See if the NAT has something to do
        if nat:
            self.process_nat(inp_knt, out_knt, snd_knt, watch=watch)

        # 8. Return why we stopped (STOP_INP if we completed a loop without problems)
        return halted

    def process_messages(self, cnum, watch=False):
        "Process messages from the specified computer"

        # 1. Assume not messages sent
        result = 0

        # 2. Loop while we have enough output for a message
        while len(self.cur_output[cnum]) >= PACKET_LENGTH:

            # 3. Take off the first packet from the output
            packet = self.cur_output[cnum][0:PACKET_LENGTH]
            del self.cur_output[cnum][:PACKET_LENGTH]
            if watch:
                print("Packet from %d to %d: X=%d, Y=%d" %
                      (cnum, packet[0], packet[1], packet[2]))

            # 4. Add to first and last messages
            msg_from = cnum
            msg_to = packet[PACKET_DEST]
            if self.first_message_from[msg_from] is None:
                if watch:
                    print("First packet from %d is to %d: X=%d, Y=%d" %
                          (msg_from, msg_to, packet[1], packet[2]))
                self.first_message_from[msg_from] = packet
            if self.first_message_to[msg_to] is None:
                if watch:
                    print("First packet to %d is from %d: X=%d, Y=%d" %
                          (msg_to, msg_from, packet[1], packet[2]))
                self.first_message_to[msg_to] = packet
            self.last_message_from[msg_from] = packet
            self.last_message_to[msg_to] = packet

            # 5. Put the message on the queue for the appropiate computer
            self.input_queue[msg_to].append(packet[PACKET_X])
            self.input_queue[msg_to].append(packet[PACKET_Y])

            # 6. Keep track of number sent
            result += 1

        # 7. Return number of messages sent
        return result

    def get_first_msg_to(self, channel):
        "Returns the first message to the channel"
        return self.first_message_to[channel]

    def get_last_msg_to(self, channel):
        "Returns the last message to the channel"
        return self.last_message_to[channel]

    def process_nat(self, inp_knt, out_knt, snd_knt, watch=False):
        "Handle nat transmission"

        # 1. Output counts (if requested)
        if watch:
            print("inp=%d, out=%d, snd=%d, to_nat=%s, prev=%s, last=%s" %
                  (inp_knt, out_knt, snd_knt,
                   self.get_last_msg_to(NAT_RECV),
                   self.prev_nat_msg,
                   self.last_nat_msg))

        # 2. If traffic, no need for nat to send
        if inp_knt + snd_knt > 0:
            return

        # 3. If nothing to send, nothing to to
        last_nat = self.get_last_msg_to(NAT_RECV)
        if last_nat is None:
            return

        # 4. Have nat send a message
        self.input_queue[NAT_SEND].append(last_nat[PACKET_X])
        self.input_queue[NAT_SEND].append(last_nat[PACKET_Y])

        # 5. Record it
        self.prev_nat_msg = self.last_nat_msg
        self.last_nat_msg = [last_nat[PACKET_X], last_nat[PACKET_Y]]
        if watch:
            print("Sent NAT msg X=%d Y=%d from %d to %s" %
                  (last_nat[PACKET_X], last_nat[PACKET_Y], NAT_RECV, NAT_SEND))

    def get_last_nat_msg(self):
        "Returns the last message that the nat sent"
        return self.last_nat_msg

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           a i i . p y                          end
# ======================================================================
