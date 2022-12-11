# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ p y t h o n . p y
# ======================================================================
"Generates python base programming source files for Advent of Code"

AOC_DD_PY = """
# ======================================================================
# TITLE
#   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ D D . p y
# ======================================================================
"Solve the puzzles for Advent of Code YYYY day DD"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

import MODULE

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                     parse_command_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'TITLE - Day DD of Advent of Code YYYY'
    sample = 'sample: python aoc_DD.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, dest='verbose',
                        help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-l', '--limit', action='store', default=0, type=int,
                        dest='limit',
                        help='Maximum (time, size, depth) before stopping')
    parser.add_argument('filepath', metavar='FILENAME',
                        action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. Create the puzzle solver
    my_solver = MODULE.CLASS(part2=False, text=input_lines)

    # 2. Determine the solution for part one
    solution = my_solver.part_one(verbose=args.verbose, limit=args.limit)
    if solution is None:
        print("There is no solution")
    else:
        print(f"The solution for part one is {solution}")

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Create the puzzle solver
    my_solver = MODULE.CLASS(part2=True, text=input_lines)

    # 2. Determine the solution for part two
    solution = my_solver.part_two(verbose=args.verbose, limit=args.limit)
    if solution is None:
        print("There is no solution")
    else:
        print(f"The solution for part two is {solution}")


    # 3. Return result
    return solution is not None


# ----------------------------------------------------------------------
#                                                              from_file
# ----------------------------------------------------------------------


def from_file(filepath, keep_blank=False):
    "Read the file"

    return from_text(open(filepath).read(), keep_blank)

# ----------------------------------------------------------------------
#                                                              from_text
# ----------------------------------------------------------------------


def from_text(text, keep_blank=False):
    "Break the text into trimed, non-comment lines"

    # 1. We start with no lines
    lines = []

    # 2. Loop for lines in the text
    for line in text.splitlines():

        # 3. But ignore blank and comment lines
        line = line.rstrip()
        if (not line) and (not keep_blank):
            continue
        if line.startswith('!'):
            continue

        # 4. Add the line
        lines.append(line)

    # 5. Return a list of clean lines
    return lines

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    "Read the Advent of Code problem and solve it"

    # 1. Get the command line options
    args = parse_command_line()

    # 2. Read the puzzle file
    input_text = from_file(args.filepath)

    # 3. Process the appropiate part of the puzzle
    if args.part == 1:
        result = part_one(args, input_text)
    else:
        result = part_two(args, input_text)

    # 5. Set return code (0 if solution found, 2 if not)
    if result:
        sys.exit(0)
    sys.exit(2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ======================================================================
# end                         a o c _ D D . p y                      end
# ======================================================================
"""

MODULE_PY = """
# ======================================================================
# TITLE
#   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         M O D U L E . p y
# ======================================================================
"A solver for the Advent of Code YYYY Day DD puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  CLASS
# ======================================================================


class CLASS(object):   # pylint: disable=R0902, R0205
    "Object for TITLE"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return None


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      M O D U L E . p y                     end
# ======================================================================
"""

TEST_MODULE_PY = """
# ======================================================================
# TITLE
#   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ M O D U L E . p y
# ======================================================================
"Test solver for Advent of Code YYYY day DD, TITLE"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_DD
import MODULE

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                              TestCLASS
# ======================================================================


class TestCLASS(unittest.TestCase):  # pylint: disable=R0904
    "Test CLASS object"

    def test_empty_init(self):
        "Test the default CLASS creation"

        # 1. Create default CLASS object
        myobj = MODULE.CLASS()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the CLASS object creation from text"

        # 1. Create CLASS object from text
        myobj = MODULE.CLASS(text=aoc_DD.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

    def test_part_one(self):
        "Test part one example of CLASS object"

        # 1. Create CLASS object from text
        myobj = MODULE.CLASS(text=aoc_DD.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of CLASS object"

        # 1. Create CLASS object from text
        myobj = MODULE.CLASS(part2=True,
                             text=aoc_DD.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ M O D U L E . p y                end
# ======================================================================
"""

PART_ONE_TXT = """Advent of Code YYYY Day DD Part One

From https://adventofcode.com/YYYY/day/DD by Eric Wastl

----- Day DD: TITLE -----

----- Part One -----

"""

PART_TWO_TXT = """Advent of Code YYYY Day DD Part Two

From https://adventofcode.com/YYYY/day/DD by Eric Wastl

----- Day DD: TITLE -----

----- Part Two -----

"""

WINGWARE_PY = """#!wing
#!version=7.0
##################################################################
# Wing project file                                              #
##################################################################
[project attributes]
proj.file-list = [loc('aoc_DD.py'),
                  loc('part_one.txt'),
                  loc('part_two.txt'),
                  loc('MODULE.py'),
                  loc('test_MODULE.py')]
proj.file-type = 'shared'
proj.launch-config = {loc('aoc_DD.py'): ('project',
        (u'-p1 -v input.txt',
         ''))}
"""

EXTRA_PY = """
# ======================================================================
# TITLE
#   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         E X T R A . p y
# ======================================================================
"OTHER for the Advent of Code YYYY Day DD puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 OTHER
# ======================================================================


class OTHER(object):   # pylint: disable=R0902, R0205
    "Object for TITLE"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      E X T R A . p y                     end
# ======================================================================
"""

TEST_EXTRA_PY = """
# ======================================================================
# TITLE
#   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ E X T R A . p y
# ======================================================================
"Test OTHER for Advent of Code YYYY day DD, TITLE"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import EXTRA

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                             TestOTHER
# ======================================================================


class TestOTHER(unittest.TestCase):  # pylint: disable=R0904
    "Test OTHER object"

    def test_empty_init(self):
        "Test the default OTHER creation"

        # 1. Create default OTHER object
        myobj = EXTRA.OTHER()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the OTHER object creation from text"

        # 1. Create OTHER object from text
        myobj = EXTRA.OTHER(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ E X T R A . p y                end
# ======================================================================
"""

PYTHON_FILES = {
    'aoc_DD.py': AOC_DD_PY,
    'MODULE.py': MODULE_PY,
    'test_MODULE.py': TEST_MODULE_PY,
    'aoc_DD.wpr': WINGWARE_PY,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
}

PYTHON_EXTRA = {
    'EXTRA.py': EXTRA_PY,
    'test_EXTRA.py': TEST_EXTRA_PY,
}


def python_before(args):
    "Build text converters"

    # 0. Precondition axioms
    assert args

    # 1. Start with simple conversions
    result = {
        "YYYY": f"{args.year:4d}",
        "DD": f"{args.day:2d}",
        "D D": ' '.join(list(f"{args.day:2d}")),
        "TITLE": ' '.join(args.title),
        "MODULE": args.cname.lower(),
        "CLASS": args.cname.capitalize(),
        "M O D U L E": ' '.join(list(args.cname.lower())),
        "EXTRA": args.ename.lower(),
        "OTHER": args.ename.capitalize(),
        "E X T R A": ' '.join(list(args.ename.lower())),
    }

    # 9. Return the text converters
    return result


def python_after(args, converters, text):
    "Cleanup text"

    # 0. Precondition axioms
    assert args
    assert converters
    assert text

    # 9. Return the input text
    return text

# ======================================================================
# end                      a o c _ p y t h o n . p y                 end
# ======================================================================
