# ======================================================================
# Combo Breaker
#   Advent of Code 2020 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h a n d s h a k e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INITIAL_SUBJECT_NUMBER = 7
DIVISOR = 20201227
HARD_LIMIT = 99999999

# ======================================================================
#                                                              Handshake
# ======================================================================


class Handshake(object):   # pylint: disable=R0902, R0205
    "Object for Combo Breaker"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.card_public = None
        self.door_public = None
        self.card_private = None
        self.door_private = None

        # 2. Process text (if any)
        if text:
            assert len(text) == 2
            self.card_public = int(text[0])
            self.door_public = int(text[1])

    @staticmethod
    def transform_number(number, private):
        "Transform the number using the private key (loop size)"
        assert number > 0
        assert private > 0

        # 1. Always start with 1
        value = 1

        # 2. Loop private key times
        for _ in range(private):
            assert _ >= 0

            # 3. Set the value to itself multiplied by the subject number
            value *= number

            # 4. Set the value to the remainder after dividing the value by 20201227
            value = value % DIVISOR

        # 5. Return the transformed number
        return value

    @staticmethod
    def guess_private(public, limit=0):
        "Determine the private key from the public key"

        # 1. Impose a hard_limit
        hard_limit = limit
        if limit == 0:
            hard_limit = HARD_LIMIT

        # 2. Start with the initial subject number
        value = 1

        # 3. Try various loop sizes
        for loop_size in range(1, hard_limit):

            # 4. Transform the current value
            value *= INITIAL_SUBJECT_NUMBER
            value = value % DIVISOR

            # 5. If we were able to generate the public key, loop_size is the private key
            if value == public:
                return loop_size

        # 6. Hard failure
        return 0

    def guess_encryption_key(self, verbose=False, limit=0):
        "Determine the encryption key is the handshake trying to establish"

        # 1. Determine the card's private key
        self.card_private = self.guess_private(self.card_public, limit=limit)
        if verbose:
            print("The card's private key is %d" % self.card_private)

        # 2. Determine the door's private key
        self.door_private = self.guess_private(self.door_public, limit=limit)
        if verbose:
            print("The door's private key is %d" % self.door_private)

        # 3. Have the card generate the encryption key
        card_encryption = self.transform_number(self.door_public, self.card_private)
        if verbose:
            print("The card's encryption key is %d" % card_encryption)

        # 4. Have the door generate the encryption key
        door_encryption = self.transform_number(self.card_public, self.door_private)
        if verbose:
            print("The door's encryption key is %d" % door_encryption)

        # 5. The encription keys should be the same
        if card_encryption != door_encryption:
            return None

        # 6. Return the shared encryption key
        return card_encryption

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        assert verbose in (True, False)
        assert limit >= 0

        # 1. Return the solution for part one
        return self.guess_encryption_key(verbose=verbose, limit=limit)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        assert verbose in (True, False)
        assert limit >= 0

        # 1. Return the solution for part two
        return self.guess_encryption_key(verbose=verbose, limit=limit)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      h a n d s h a k e . p y                   end
# ======================================================================
