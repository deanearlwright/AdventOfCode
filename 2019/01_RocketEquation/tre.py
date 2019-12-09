
# ======================================================================
# The Tyranny of the Rocket Equation
#   Advent of Code 2019 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                               t r e . p y
# ======================================================================
"Solve the Rocket Equation problem of day 01 of Advent of Code 2019"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'The Tyranny of the Rocket Equation - day 01 of Advent of Code 2018'
    sample = 'sample: python mcm.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-t', '--max-time', action='store', default=0, type=int,
                        dest='maxtime', help='Maximum timer ticks before quitting')
    parser.add_argument('filepath', metavar='ticks', action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                          fuel_required
# ----------------------------------------------------------------------
def fuel_required(mass):
    "Calculate the fuel required for a given mass"

    return mass // 3 - 2

# ----------------------------------------------------------------------
#                                                fuel_required_with_fuel
# ----------------------------------------------------------------------
def fuel_required_with_fuel(mass):
    "Calculate the fuel required for a given mass"

    # 1. Start with no fuel required
    total_fuel = 0

    # 2. Determine the base fuel required for this mass
    fuel = fuel_required(mass)

    # 3. Loop until no additional fuel is required
    while fuel > 0:

        # 4. Add this fuel to the total fuel needed
        total_fuel += fuel

        # 5. Calculate additional fuel needed for the fuel
        fuel = fuel_required(fuel)

    # 6. Return the total_fuel required
    return total_fuel

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. We start at zero
    solution = 0

    # 2. Loop for all of the lines of input_text (one module per line)
    for line in input_lines:

        # 3. Determine the fuel requirement of this module
        module_mass = int(line)
        module_fuel = fuel_required(module_mass)
        if args.verbose:
            print("The fuel required for a module of mass %d is %d" %
                  (module_mass, module_fuel))

        # 4. Accumulate the total fuel required
        solution += module_fuel

    # 4. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % args.maxtime)
    else:
        print("The solution is %s" % (solution))

    # 5. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. We start at zero
    solution = 0

    # 2. Loop for all of the lines of input_text (one module per line)
    for line in input_lines:

        # 3. Determine the fuel requirement of this module
        module_mass = int(line)
        module_fuel = fuel_required_with_fuel(module_mass)
        if args.verbose:
            print("The fuel required for a module of mass %d with fuel is %d" %
                  (module_mass, module_fuel))

        # 4. Accumulate the total fuel required
        solution += module_fuel

    # 4. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % args.maxtime)
    else:
        print("The solution is %s" % (solution))

    # 5. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                              from_file
# ----------------------------------------------------------------------


def from_file(filepath):
    "Read the file"

    return from_text(open(filepath).read())

# ----------------------------------------------------------------------
#                                                              from_text
# ----------------------------------------------------------------------


def from_text(text):
    "Break the text into trimed, non-comment lines"

    # 1. We start with no lines
    lines = []

    # 2. Loop for lines in the text
    for line in text.split('\n'):

        # 3. But ignore blank and comment lines
        line = line.rstrip(' \r')
        if not line:
            continue
        if line.startswith('#'):
            continue

        # 4. Add the line
        lines.append(line)

    # 5. Return a list of clean lines
    return lines

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    """Read a The Tyranny of the Rocket Equation puzzle and solve it"""

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
    if result is not None:
        sys.exit(0)
    sys.exit(2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ======================================================================
# end                           t r e . p y                          end
# ======================================================================
