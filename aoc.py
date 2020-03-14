# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c . p y
# ======================================================================
"Generates base programming source files for Advent of Code"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import datetime
import os

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INPUT_FILE_NAME = 'input.txt'

# ----- python -----

AOC_DD_PY = """# ======================================================================
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
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'TITLE - Day DD of Advent of Code YYYY'
    sample = 'sample: python aoc_DD.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-l', '--limit', action='store', default=0, type=int,
                        dest='limit',
                        help='Maximum limit (e.g., time, size, recursion) before stopping')
    parser.add_argument('filepath', metavar='FILENAME', action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. Create the puzzle solver
    solver = MODULE.CLASS(part2=False, text=input_lines)

    # 2. Determine the solution for part one
    solution = solver.part_one(verbose=args.verbose, limit=args.limit)
    if solution is None:
        print("There is no solution")
    else:
        print("The solution for part one is %s" % (solution))

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Create the puzzle solver
    solver = MODULE.CLASS(part2=True, text=input_lines)

    # 2. Determine the solution for part two
    solution = solver.part_two(verbose=args.verbose, limit=args.limit)
    if solution is None:
        print("There is no solution")
    else:
        print("The solution for part two is %s" % (solution))


    # 3. Return result
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
    for line in text.split('\\n'):

        # 3. But ignore blank and non-claim lines
        line = line.rstrip(' \\r')
        if not line:
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

CLASS_PY = """# ======================================================================
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
        if text is not None:
            pass

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return None


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

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

TEST_CLASS_PY = """# ======================================================================
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
        self.assertEqual(myobj.text, EXAMPLE_TEXT)

    def test_part_one(self):
        "Test part one example of CLASS object"

        # 1. Create CLASS object from text
        myobj = MODULE.CLASS(text=aoc_DD.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of CLASS object"

        # 1. Create CLASS object from text
        myobj = MODULE.CLASS(part2=True, text=aoc_DD.from_text(PART_TWO_TEXT))

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

PYTHON_FILES = {
    'aoc_DD.py': AOC_DD_PY,
    'MODULE.py': CLASS_PY,
    'test_MODULE.py': TEST_CLASS_PY,
    'MODULE.wpr': WINGWARE_PY,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
}


def python_before(args):
    "Build text converters"

    # 0. Precondition axioms
    assert args

    # 1. Start with simple conversions
    result = {
        "YYYY": "%4d" % args.year,
        "DD": "%02d" % args.day,
        "D D": ' '.join(list("%02d" % args.day)),
        "TITLE": ' '.join(args.title),
        "MODULE": args.cname.lower(),
        "CLASS": args.cname.capitalize(),
        "M O D U L E": ' '.join(list(args.cname.lower())),
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

# ----- javascript -----


AOC_DD_JS = """/* eslint-disable linebreak-style */

// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                             a o c _ D D . j s
//
// Solve the Advent of Code YYYY day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const yargs = require('yargs');
const fs = require('fs');
const process = require('process');

const MODULE = require('./MODULE');

// ----------------------------------------------------------------------
//                                                        parseCommndLine
// ----------------------------------------------------------------------

function parseCommandLine() {
  // Parse the command line options"

  // 1. Create the command line parser
  const { argv } = yargs
    .command('aoc_DD', 'TITLE - Day DD of Advent of Code YYYY', { })
    .option('verbose', {
      alias: 'v',
      default: false,
      describe: 'Print status messages to stdout',
      type: 'boolean',
    })
    .option('part', {
      alias: 'p',
      default: 1,
      describe: 'Puzzle Part (1 or 2)',
      type: 'number',
    })
    .option('limit', {
      alias: 'l',
      default: 0,
      describe: 'Maximum limit (e.g., time, size, recursion) before stopping',
      type: 'number',
    })
    .option('filepath', {
      alias: 'f',
      default: 'input.txt',
      describe: 'Location of puzzle input',
      type: 'string',
    })
    .example('$0 -p 1 input.txt', 'Solve part one of the puzzle')
    .help()
    .alias('help', 'h');

  // 2. Get the options and arguments
  return argv;
}

// ----------------------------------------------------------------------
//                                                                partOne
// ----------------------------------------------------------------------

function partOne(args, inputLines) {
  // Process part one of the puzzle

  // 1. Create the puzzle solver
  const solver = new MODULE.CLASS({ part2: false, text: inputLines });

  // 2. Determine the solution for part two
  const solution = solver.partOne({ verbose: args.verbose, limit: args.limit });
  if (solution == null) {
    console.log('There is no solution for part one'); // eslint-disable-line no-console
  } else {
    console.log('The solution for part one is', solution); // eslint-disable-line no-console
  }

  // 3. Return result
  return solution != null;
}

// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------

function partTwo(args, inputLines) {
  // Process part two of the puzzle

  // 1. Create the puzzle solver
  const solver = new MODULE.CLASS({ part2: true, text: inputLines });

  // 2. Determine the solution for part two
  const solution = solver.partTwo({ verbose: args.verbose, limit: args.limit });
  if (solution == null) {
    console.log('There is no solution for part two'); // eslint-disable-line no-console
  } else {
    console.log('The solution for part two is', solution); // eslint-disable-line no-console
  }

  // 3. Return result
  return solution != null;
}

// ----------------------------------------------------------------------
//                                                              from_text
// ----------------------------------------------------------------------

function fromText(text) {
  // Break the text into trimed, non-comment lines"

  // 1. We start with no lines
  const lines = [];

  // 2. Loop for lines in the text
  text.split(/\\r?\\n/).forEach((line) => {
    // 3. But ignore blank and non-claim lines
    const cleaned = line.trimEnd();
    if (cleaned.length > 0 && !cleaned.startsWith('!')) {
      // 4. Add the line
      lines.push(cleaned);
    }
  });

  // 5. Return a list of clean lines
  return lines;
}

// ----------------------------------------------------------------------
//                                                              from_file
// ----------------------------------------------------------------------

function fromFile(filepath) {
  // Read the file
  try {
    const data = fs.readFileSync(filepath, 'utf8');
    return fromText(data);
  } catch (e) {
    console.log('Error', e.stack); // eslint-disable-line no-console
    return '';
  }
}

// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------

function main() {
  // Read the Advent of Code problem and solve it
  let result = null;

  // 1. Get the command line options
  const argv = parseCommandLine();

  // 2. Read the puzzle file
  const inputText = fromFile(argv.filepath);

  // 3. Process the appropiate part of the puzzle
  if (argv.part === 1) {
    result = partOne(argv, inputText);
  } else {
    result = partTwo(argv, inputText);
  }

  // 5. Set return code (0 if solution found, 2 if not)
  if (result != null) {
    process.exit(0);
  }
  process.exit(2);
}

// ----------------------------------------------------------------------
//                                                  module initialization
// ----------------------------------------------------------------------
if (typeof require !== 'undefined' && require.main === module) {
  main();
}

// ----------------------------------------------------------------------
//                                                                 export
// ----------------------------------------------------------------------

module.exports.fromText = fromText;

// ======================================================================
// end                         a o c _ D D . j s                      end
// ======================================================================

"""

CLASS_JS = """/* eslint-disable linebreak-style */
// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           M O D U L E . j s
//
// A solver for the Advent of Code YYYY Day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  CLASS
// ======================================================================


A
class CLASS {
  // Object for TITLE

  constructor(options) {
    // Create a CLASS object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;

    // 2. Process text (if any)
    if (this.text === null) {
      // TODO process the test
    }
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    this.todo = 'TODO';

    // 1. Return the solution for part one
    return null;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    this.todo = 'TODO';

    // 1. Return the solution for part two
    return null;
  }
}

module.exports.CLASS = CLASS;
// ======================================================================
// end                      M O D U L E . j s                     end
// ======================================================================
"""

TEST_CLASS_JS = """/* eslint-disable linebreak-style */
// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      M O D U L E . t e s t . j s
//
// Test the solver for Advent of Code YYYY day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aocDD = require('./aoc_DD');
const MODULE = require('./MODULE');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '';
const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = null;
const PART_TWO_RESULT = null;

// ======================================================================
//                                                              TestCLASS
// ======================================================================

describe('CLASS', () => {
  test('Test the default CLASS creation', () => {
    // 1. Create default CLASS object
    const myobj = new MODULE.CLASS({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the CLASS object creation from text', () => {
    // 1. Create CLASS object from text
    const myobj = new MODULE.CLASS({ text: aocDD.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test part one example of CLASS object', () => {
    // 1. Create CLASS object from text
    const myobj = new MODULE.CLASS({ text: aocDD.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of CLASS object', () => {
    // 1. Create CLASS object from text
    const myobj = new MODULE.CLASS({ part2: true, text: aocDD.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    t e s t _ M O D U L E . j s                 end
// ======================================================================
"""

PACKAGE_JSON = """
{
  "name": "DIRLOWER",
  "version": "1.0.0",
  "description": "Advent of Code YYYY Day DD, TITLE",
  "main": "aoc_DD.js",
  "scripts": {
    "test": "jest"
  },
  "keywords": ['Advent of Code'],
    "author": "Dr. Dean Earl Wright III",
  "license": "MIT",
  "devDependencies": {
    "eslint": "^6.8.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-config-standard": "^14.1.0",
    "eslint-plugin-import": "^2.20.1",
    "eslint-plugin-jest": "^23.8.2",
    "eslint-plugin-node": "^11.0.0",
    "eslint-plugin-promise": "^4.2.1",
    "eslint-plugin-standard": "^4.0.1",
    "jest": "^25.1.0"
  }
}
"""

ESLINTRC_JS = """
module.exports = {
  env: {
    commonjs: true,
    'jest/globals': true,
  },
  plugins: [
    'jest',
  ],
  extends: [
    'airbnb-base',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
  },
  rules: {
    "jest/no-disabled-tests": "warn",
    "jest/no-focused-tests": "error",
    "jest/no-identical-title": "error",
    "jest/prefer-to-have-length": "warn",
    "jest/valid-expect": "error"

  },
};
"""

JEST_CONFIG_JS = """
// For a detailed explanation regarding each configuration property, visit:
// https://jestjs.io/docs/en/configuration.html

module.exports = {
  testEnvironment: "Node",
};
"""

GITIGNORE_JS = """
node_modules/
"""

JAVASCRIPT_FILES = {
    'aoc_DD.js': AOC_DD_JS,
    'MODULE.js': CLASS_JS,
    'MODULE.test.js': TEST_CLASS_JS,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
    'package.json': PACKAGE_JSON,
    '.eslintrc.js': ESLINTRC_JS,
    'jest.config.js': JEST_CONFIG_JS,
    '.gitignore': GITIGNORE_JS,
}


def js_before(args):
    "Build text converters"

    # 0. Precondition axioms
    assert args

    # 1. Start with simple conversions
    result = {
        "YYYY": "%4d" % args.year,
        "DD": "%02d" % args.day,
        "D D": ' '.join(list("%02d" % args.day)),
        "TITLE": ' '.join(args.title),
        "MODULE": args.cname.lower(),
        "CLASS": args.cname.capitalize(),
        "M O D U L E": ' '.join(list(args.cname.lower())),
        "DIRLOWER": "%2d_%s" % (args.day, ''.join(args.title).lower())
    }

    # 9. Return the text converters
    return result


def js_after(args, converters, text):
    "Cleanup text"

    # 0. Precondition axioms
    assert args
    assert converters
    assert text

    # 9. Return the input text
    return text

# ----- languages


LANGUAGES = {
    'python': (PYTHON_FILES, python_before, python_after),
    'javascript': (JAVASCRIPT_FILES, js_before, js_after)
}

# ----- Substitions

SUBSTITUTIONS = {
    'DD': 'DD',
    'D D': 'D D',
    'DIR': 'DIR',
    'DIRLOWER': 'DIRLOWER',
    'YYYY': 'YYYY',
    'TITLE': 'TITLE',
    'CLASS': 'CLASS',
    'MODULE': 'MODULE',
    'M O D U L E': 'M O D U L E',
}

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Determine defaults for year and day
    today = datetime.date.today()
    if today.month == 12:
        default_year = today.year
        default_day = today.day
    else:
        default_year = None
        default_day = None
    default_dir = os.getcwd()

    # 2. Create the command line parser
    desc = 'Advent of Code source file generator'
    sample = 'sample: python aoc.py -d 17 My Little Programs'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help='Print status messages to stdout')
    parser.add_argument('-l', '--language', choices=['python', 'javascript'],
                        help='Programming language (python or javascript)')
    parser.add_argument('-i', '--input', action='store', default="", dest='inval',
                        help='Puzzle input from web page')
    parser.add_argument('-c', '--class', action='store', default="", dest='cname',
                        help='Name of class')
    parser.add_argument('-y', '--year', action='store', default=default_year,
                        help="Year of puzzle", dest='year', type=int)
    parser.add_argument('-d', '--day', action='store', default=default_day,
                        help="Day of puzzle", dest='day', type=int)
    parser.add_argument('-b', '--base', action='store', default=default_dir,
                        help="base direcotory of Advent of Code", dest='base')
    parser.add_argument('title', action='store', type=str, nargs='+',
                        help="Title of puzzle")
    parser.add_argument('-a', '--add', action='store_true', default=False,
                        dest='add', help='Add files to existing directory')
    parser.add_argument('--py', dest='language', action='store_const', const='python',
                        help='Programming language is python')
    parser.add_argument('--js', dest='language', action='store_const', const='javascript',
                        help='Programming language is javascript')

    # 3. Get the options and arguments
    args = parser.parse_args()

    # 4. Ensure we have required arguments (year, day, title, and language)
    if not args.title:
        parser.error("Puzzle title is required")
    if not args.year:
        parser.error("Puzzle year is required")
    if args.year > 2049 or args.year < 2015:
        parser.error("Year must be 2015-2049")
    if not args.day:
        parser.error("Puzzle day is required")
    if args.day > 25 or args.day < 1:
        parser.error("Day must be 1-25")
    if not args.language:
        parser.error("Programming language is required")

    # 5. Ensure base and year directories exist but not the day
    if not os.path.isdir(args.base):
        parser.error("Base directory (%s) does not exist" % (args.base))
    base_year = os.path.join(args.base, str(args.year))
    if not os.path.isdir(base_year):
        parser.error("Year directory (%s) does not exist" % (base_year))
    day_begins = '%02d_' % (args.day)
    with os.scandir(base_year) as it:
        for entry in it:
            if entry.name.startswith(day_begins) and entry.is_dir() and not args.add:
                parser.error("Day directory (%s) already exists" % (entry.name))

    # 6. If there is no class name, use last word in title
    if not args.cname:
        args.cname = args.title[-1]

    # 7. Return the arguments
    return args

# ----------------------------------------------------------------------
#                                                             copy_files
# ----------------------------------------------------------------------


def copy_files(args, day_directory):
    """Copy language files to day directory"""

    # 1. Get list of language specific files and pre and post converters
    files, conv_before, conv_after = LANGUAGES[args.language]

    # 2. Execute the build converter function for this language
    text_converters = conv_before(args)

    # 2. Loop for all the files
    for file_info in files.items():
        raw_file_name, raw_file_text = file_info

        # 3. Get full path of output file
        out_file_name = get_file_name(day_directory, raw_file_name, text_converters)

        # 4. Don't write if the file already exists
        if os.path.isfile(out_file_name):
            print("File %s already exists, skipping" % out_file_name)
            continue

        # 5. Convert the text for this file
        converted_text = convert_text(text_converters, raw_file_text)

        # 6. Do any final clear up on the file
        final_text = conv_after(args, text_converters, converted_text)

        # 7. Write file
        with open(out_file_name, 'w') as output_file:
            output_file.write(final_text)

# ----------------------------------------------------------------------
#                                                          get_file_name
# ----------------------------------------------------------------------


def get_file_name(day_directory, raw_file_name, converters):
    "Get full path name of file"

    # 1. Convert the raw file name
    converted_file_name = convert_text(converters, raw_file_name)

    # 2. Return the complete file name
    return os.path.join(day_directory, converted_file_name)

# ----------------------------------------------------------------------
#                                                           convert_text
# ----------------------------------------------------------------------


def convert_text(converters, raw_text):
    "Get processed text by successively applying converters"

    # 1. Start with the initial text
    result = raw_text

    # 2. Loop for all of the converters
    for conv_from, conv_to in converters.items():

        # 3. Make this replacement
        result = result.replace(conv_from, conv_to)

    # 4. Return the converted text
    return result

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    """Generate base programming files for Advent of Code solver"""

    # 1. Get the command line options
    args = parse_command_line()

    # 2. Create the day directory
    base_year_day = os.path.join(args.base, str(args.year),
                                 '%02d_%s' % (args.day, ''.join(args.title)))
    os.mkdir(base_year_day)

    # 3. Copy files to the day directory
    copy_files(args, base_year_day)

    # 4. Create input file for sepecified input (if any)
    if args.inval:
        with open(os.path(base_year_day, INPUT_FILE_NAME), 'w') as input_txt:
            input_txt.write(args.inval)
            input_txt.write('\n')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ======================================================================
# end                            a o c . p y                         end
# ======================================================================
