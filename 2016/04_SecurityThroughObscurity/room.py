# ======================================================================
# Security Through Obscurity
#   Advent of Code 2016 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             r o o m . p y
# ======================================================================
"A Room Object for the Advent of Code 2016 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_INFO = re.compile("([-a-z]+)-([0-9]+)\[([a-z]+)\]")
LETTERS = "abcdefghijklmnopqrstuvwxyz"

# ======================================================================
#                                                                   List
# ======================================================================


class Room(object):   # pylint: disable=R0902, R0205
    "Object for Security Through Obscurity"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        if text:
            self.text = text
        else:
            self.text = ''
        self.name = ''
        self.id = 0
        self.checksum = ''
        self.valid = False

        # 2. Process text (if any)
        if text and len(text) > 0:
            self.process_text()

    def process_text(self):
        "Break up the room text into it's parts and validate it"

        # 1. Break up the text with a regular expression
        match = RE_INFO.match(self.text)

        # 2. If the input is valid, save the parts
        if match:
            self.name = match.group(1)
            self.id = int(match.group(2))
            self.checksum = match.group(3)

            # 3. Validate the room
            self.valid = self.validate_room()

        # 4. Not what I was expecting
        else:
            print("Unable to parse %s" % self.text)

    def validate_room(self):
        "Return true if the room's checksum is valid"

        # 1. Generate a checksum for the room
        chksum = self.generate_checksum()

        # 2. The room is valid if the saved checksum matches the generated one
        return self.checksum == chksum

    def generate_checksum(self):
        "Generate a checksum from the room name"

        # 1. Get rid of the dashes
        name = self.name.replace('-', '')

        # 2. Get a count of all of the letters in from high to low
        counts = Counter(name).most_common()

        # 3. Combine the letters with the same counts
        letters = []
        letter = ''
        count = 0
        while len(counts) > 0:
            letter2, count2 = counts.pop(0)
            if count == count2:
                letter += letter2
            else:
                if len(letter) > 0:
                    letters.append(''.join(sorted(letter)))
                letter = letter2
                count = count2
        if len(letter) > 0:
            letters.append(''.join(sorted(letter)))

        # 4. Start with the most populular letter(s)
        result = letters.pop(0)

        # 5. Loop until we get at least five letters in the result
        while len(result) < 5:

            #  6. Get the next most common letter(s)
            result += letters.pop(0)

        # 7. Get Return the first five characters as the checksum
        return result[:5]

    def decrypt(self):
        "Return the decrypted room name"

        # 1. Start with nothing
        result = []

        # 2. Loop for the characters in the encrypted name
        for char in self.name:

            # 3. Dashses become spaces and letters are rotated
            if char == '-':
                char = ' '
            else:
                char = LETTERS[(ord(char) - ord('a') + self.id) % 26]

            # 4. Added the decoded character to the result
            result.append(char)

        # 5. Return the decrypted room name
        return ''.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           r o o m . p y                        end
# ======================================================================

