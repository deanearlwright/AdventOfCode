# ======================================================================
# Chronal Classification
#   Advent of Code 2018 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       o b s e r v a t i o n s . p y
# ======================================================================
"An object for the Advent of Code 2018 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            Observation
# ======================================================================


class Observation(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Classification"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text
        self.before = []
        self.instruction = []
        self.after = []

        # 2. Process text (if any)
        if text is not None and len(text) == 3:
            self.add_line(text[0])
            self.add_line(text[1])
            self.add_line(text[2])

    def add_line(self, line):

        if line.startswith('Before: '):
            return self.add_before(line)
        if line.startswith('After: '):
            return self.add_after(line)
        return self.add_instruction(line)

    def add_before(self, line):
        if not line.startswith('Before: ['):
            return False
        if not line.endswith(']'):
            return False
        cleaned = line[9:-1].replace(',', '').split(' ')
        if len(cleaned) != 4:
            return False
        self.before = [int(x) for x in cleaned]
        return True

    def add_after(self, line):
        if not line.startswith('After:  ['):
            return False
        if not line.endswith(']'):
            return False
        cleaned = line[9:-1].replace(',', '').split(' ')
        if len(cleaned) != 4:
            return False
        self.after = [int(x) for x in cleaned]
        return True

    def add_instruction(self, line):
        cleaned = line.split(' ')
        if len(cleaned) != 4:
            return False
        self.instruction = [int(x) for x in cleaned]
        return True



# ======================================================================
#                                                           Observations
# ======================================================================


class Observations(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Classification"

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text
        self.data = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.processText(text)

    def processText(self, text):
        # 1. Keep track of blank lines and collected lines
        previous_blank = False
        collected = []
        # 2. Loop for all lines of the text
        for line in text:
            if not line:
                if previous_blank:
                    break
                else:
                    if len(collected) == 3:
                        self.data.append(Observation(text=collected))
                        collected = []
                    previous_blank = True
            else:
                collected.append(line)
                previous_blank = False

    def __getitem__(self, index):
        out = self.data[index]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def append(self, item):
        self.data.append(item)

    def __iter__(self):
        return iter(self.data)

# ----------------------------------------------------------------------
# module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
        pass

# ======================================================================
# end                 o b s e r v a t i o n s . p y                  end
# ======================================================================
