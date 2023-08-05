# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     a o c _ j a v a s c r i p t . p y
# ======================================================================
"Generates javascript base programming source files for Advent of Code"


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

const fs = require('fs');
const process = require('process');
const yargs = require('yargs');

const MODULE = require('./MODULE');

// ----------------------------------------------------------------------
//                                                       parseCommandLine
// ----------------------------------------------------------------------

function parseCommandLine() {
  // Parse the command line options

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
  const solution = solver.partOne({ verbose: args.verbose,
                                    limit: args.limit });
  if (solution == null) {
    // eslint-disable-next-line no-console
    console.log('There is no solution for part one');
  } else {
    // eslint-disable-next-line no-console
    console.log('The solution for part one is', solution);
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
  const solution = solver.partTwo({ verbose: args.verbose,
                                    limit: args.limit });
  if (solution == null) {
    // eslint-disable-next-line no-console
    console.log('There is no solution for part two');
  } else {
    // eslint-disable-next-line no-console
    console.log('The solution for part two is', solution);
  }

  // 3. Return result
  return solution != null;
}

// ----------------------------------------------------------------------
//                                                              from_text
// ----------------------------------------------------------------------

function fromText(text) {
  // Break the text into trimed, non-comment lines

  // 1. We start with no lines
  const lines = [];

  // 2. Loop for lines in the text
  text.split(/\\r?\\n/).forEach((line) => {
    // 3. But ignore blank and comment lines
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

class CLASS {
  // Object for TITLE

  constructor(options) {
    // Create a CLASS object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;

    // 2. Process text (if any)
    if (this.text !== null) {
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
// ======================================================================

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

const EXAMPLES_PART_ONE = {};
const EXAMPLES_PART_TWO = {};

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

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create CLASS object using the key as text
      const myobj = new MODULE.CLASS({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.MODULE(key)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create CLASS object using the key as text
      const myobj = new MODULE.CLASS({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.MODULE(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of CLASS object', () => {
    // 1. Create CLASS object from text
    const myobj = new MODULE.CLASS({ text: aocDD.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of CLASS object', () => {
    // 1. Create CLASS object from text
    const myobj = new MODULE.CLASS({ part2: true,
                                     text: aocDD.fromText(PART_TWO_TEXT)
                                   });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   M O D U L E . t e s t . j s                  end
// ======================================================================
"""

PACKAGE_JSON_JS = """
{
  "name": "DIRLOWER",
  "version": "1.0.0",
  "description": "Advent of Code YYYY Day DD, TITLE",
  "main": "aoc_DD.js",
  "scripts": {
    "lint": "eslint . --ext .js",
    "lint:fix": "npm run lint -- --fix",
    "test": "jest",
    "part1": "node aoc_DD.js -p 1",
    "part2": "node aoc_DD.js -p 2",
    "part1v": "node aoc_DD.js -p 1 -v",
    "part2v": "node aoc_DD.js -p 2 -v"
  },
  "keywords": ["Advent of Code"],
    "author": "Dr. Dean Earl Wright III",
  "license": "MIT",
"devDependencies": {
    "eslint": "^8.46.0",
    "eslint-config-airbnb-base": "^15.0.0",
    "eslint-config-standard": "^17.1.0",
    "eslint-plugin-import": "^2.28.0",
    "eslint-plugin-jest": "^27.2.3",
    "eslint-plugin-node": "^11.1.0",
    "eslint-plugin-promise": "^6.1.1",
    "eslint-plugin-react": "^7.33.1",
    "jest": "^29.6.2"
  },
  "dependencies": {
    "yargs": "^17.7.2"

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

JAVASCRIPT_FILES = {
    'aoc_DD.js': AOC_DD_JS,
    'MODULE.js': CLASS_JS,
    'MODULE.test.js': TEST_CLASS_JS,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
    'package.json': PACKAGE_JSON_JS,
    '.eslintrc.js': ESLINTRC_JS,
    'jest.config.js': JEST_CONFIG_JS,
}

JAVASCRIPT_EXTRA = {}


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


# ======================================================================
# end                a o c _ j a v a s c r i p t . p y               end
# ======================================================================
