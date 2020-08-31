# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           c a v e . p y
# ======================================================================
"Goblins, and Elves, and Walls (Oh my!) for the AoC 2018 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import person

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Cave
# ======================================================================


class Cave(object):   # pylint: disable=R0902, R0205
    "Goblins, and Elves, and Walls (Oh my!) for Beverage Bandits"

    def __init__(self, text=None, elf_attack=3):

        # 1. Set the initial values
        self.text = text
        self.items = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.processText(text, elf_attack)

    def processText(self, text, elf_attack=3):
        # 1. Set initial values
        self.items = {
            '#': person.People(letter='#'),
            'E': person.People(letter='E'),
            'G': person.People(letter='G'),
            }

        # 2. Loop for each line of text
        for row, line in enumerate(text):

            # 3. Loop for each character in the line
            for col, char in enumerate(line):

                # 4. Save the non-space items
                if char == '#':
                    self.items[char].add(person.Person(letter=char,
                                                       location=person.row_col_to_loc(row, col)))
                elif char == 'E':
                    self.items[char].add(person.Person(letter=char,
                                                       location=person.row_col_to_loc(row, col),
                                                       attack=elf_attack))
                elif char == 'G' :
                    self.items[char].add(person.Person(letter=char,
                                                       location=person.row_col_to_loc(row, col)))

    def get_by_location(self, loc):
        for which in '#EG':
            if loc in self.items[which]:
                return self.items[which][loc]
        return None

    def max_loc(self, letter='#'):
        return max(self.items[letter].locations())

    def __str__(self):
        max_row, max_col = person.loc_to_row_col(self.max_loc())
        result = []
        for row in range(max_row + 1):
            line = []
            for col in range(max_col + 1):
                who = self.get_by_location(person.row_col_to_loc(row, col))
                if who == None:
                    line.append('.')
                else:
                    line.append(who.letter)
            result.append(''.join(line))
        return '\n'.join(result)

    def __getitem__(self, letter):
        if letter in self.items:
            return self.items[letter]
        else:
            raise AttributeError("No such letter: " + letter)

    def __len__(self):
        return len(self.items)

    def hitpoints(self):
        return self.items['E'].hitpoints() + self.items['G'].hitpoints()

    def map_with_hitpoints(self):
        max_row, max_col = person.loc_to_row_col(self.max_loc())
        result = []
        for row in range(max_row + 1):
            line = []
            units = []
            for col in range(max_col + 1):
                who = self.get_by_location(person.row_col_to_loc(row, col))
                if who == None:
                    line.append('.')
                else:
                    line.append(who.letter)
                    if who.letter != '#':
                        units.append('%s(%d)' % (who.letter, who.hitpoints))
            line_out = ''.join(line)
            if len(units) > 0:
                line_out = line_out + '   ' + ', '.join(units)
            result.append(line_out)
        return '\n'.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                            c a v e . p y                       end
# ======================================================================