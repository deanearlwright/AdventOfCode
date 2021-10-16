# ======================================================================
# Advent of Code Generator
#   for Advent of Code -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     a o c _ t y p e s c r i p t . p y
# ======================================================================
"Generates typescript base programming source files for Advent of Code"

AOC_DD_TS = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                             a o c _ D D . t s
//
// Solve the Advent of Code YYYY day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { readFileSync } from 'fs';

import { exit } from 'process';

import * as yargs from 'yargs';

import { CLASS } from './MODULE';

// ----------------------------------------------------------------------
//                                                        parseCommndLine
// ----------------------------------------------------------------------

interface Arguments {
  verbose: boolean;
  part: number;
  limit: number;
  filepath: string;
}

function parseCommandLine(): Arguments {
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

function partOne(args: Arguments, inputLines: string[]): boolean {
  // Process part one of the puzzle

  // 1. Create the puzzle solver
  const solver = new CLASS(inputLines, false);

  // 2. Determine the solution for part one
  const solution = solver.partOne(args.verbose, args.limit);
  if (RCHECK) {
    console.log('There is no solution for part one');
  } else {
    console.log('The solution for part one is', solution);
  }

  // 3. Return result
  return NOTCHK;
}

// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------

function partTwo(args: Arguments, inputLines: string[]): boolean {
  // Process part two of the puzzle

  // 1. Create the puzzle solver
  const solver = new CLASS(inputLines, true);

  // 2. Determine the solution for part two
  const solution = solver.partTwo(args.verbose, args.limit);
  if (RCHECK) {
    console.log('There is no solution for part two');
  } else {
    console.log('The solution for part two is', solution);
  }

  // 3. Return result
  return NOTCHK;
}

// ----------------------------------------------------------------------
//                                                              from_text
// ----------------------------------------------------------------------

export function fromText(text: string): string[] {
  // Break the text into trimed, non-comment lines"

  // 1. We start with no lines
  const lines: string[] = [];

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

function fromFile(filepath: string): string[] {
  // Read the file
  try {
    const data = readFileSync(filepath, 'utf8');
    return fromText(data);
  } catch (e: unknown) {
    if (e instanceof Error) {
      console.log('Error', e.stack); // eslint-disable-line no-console
    }
    return [];
  }
}

// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------

function main() {
  // Read the Advent of Code problem and solve it
  let result = false;

  // 1. Get the command line options
  const argv: Arguments = parseCommandLine();

  // 2. Read the puzzle file
  const inputText: string[] = fromFile(argv.filepath);

  // 3. Process the appropiate part of the puzzle
  if (argv.part === 1) {
    result = partOne(argv, inputText);
  } else {
    result = partTwo(argv, inputText);
  }

  // 5. Set return code (0 if solution found, 2 if not)
  if (result) {
    exit(0);
  }
  exit(2);
}

// ----------------------------------------------------------------------
//                                                  module initialization
// ----------------------------------------------------------------------
if (typeof require !== 'undefined' && require.main === module) {
  main();
}

// ======================================================================
// end                         a o c _ D D . t s                      end
// ======================================================================
"""

CLASS_TS = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           M O D U L E . t s
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

export class CLASS {
  // Object for TITLE
  text: string[];

  part2: boolean;

  numbers: number[];

  constructor(text: string[], part2 = false) {
    // Create a CLASS object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.numbers = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      for (let indx = 0; indx < this.text.length; indx += 1) {
        this.numbers.push(+this.text[indx]);
      }
    }
  }

  solution(verbose = false, limit = 0): RTYPE {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return RNONE;
    }
    return RNONE;
  }

  partOne(verbose = false, limit = 0): RTYPE {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): RTYPE {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      M O D U L E . t s                     end
// ======================================================================
"""

TEST_CLASS_TS = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      M O D U L E . t e s t . t s
//
// Test the solver for Advent of Code YYYY day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_DD';
import { CLASS } from './MODULE';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '';

interface ExampleTests {
  text: string;
  result: RTYPE;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = RNONE;
const PART_TWO_RESULT = RNONE;

// ======================================================================
//                                                              TestCLASS
// ======================================================================

describe('CLASS', () => {
  test('Test the default CLASS creation', () => {
    // 1. Create default CLASS object
    const myobj = new CLASS([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the CLASS object creation from text', () => {
    // 1. Create CLASS object from text
    const myobj = new CLASS(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create CLASS object
      const myobj = new CLASS(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create CLASS object using the key as text
      const myobj = new CLASS(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of CLASS object', () => {
    // 1. Create CLASS object from text
    const myobj = new CLASS(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of CLASS object', () => {
    // 1. Create CLASS object from text
    const myobj = new CLASS(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   M O D U L E . t e s t . t s                  end
// ======================================================================
"""
EXTRA_TS = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           E X T R A . t s
//
// OTHER for the Advent of Code YYYY Day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  OTHER
// ======================================================================

export class OTHER {
  // Object for TITLE
  text: string;

  part2: boolean;

  constructor(text: string, part2 = false) {
    // Create a OTHER object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      // TODO process the test
    }
  }
}

// ======================================================================
// end                      E X T R A . t s                     end
// ======================================================================
"""

EXTRA_TEST_TS = """// ======================================================================
// TITLE
//   Advent of Code YYYY Day DD -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      E X T R A . t e s t . t s
//
// Test OTHER for Advent of Code YYYY day DD problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { OTHER } from './EXTRA';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '';

// ======================================================================
//                                                              TestOTHER
// ======================================================================

describe('OTHER', () => {
  test('Test the default OTHER creation', () => {
    // 1. Create default OTHER object
    const myobj = new OTHER('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the OTHER object creation from text', () => {
    // 1. Create OTHER object from text
    const myobj = new OTHER(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });
});

// ======================================================================
// end                   E X T R A . t e s t . t s                  end
// ======================================================================
"""

PACKAGE_JSON_TS = """{
  "name": "DIRLOWER",
  "version": "1.0.0",
  "description": "Advent of Code YYYY Day DD, TITLE",
  "main": "aoc_DD.js",
  "scripts": {
    "lint": "eslint . --ext .ts",
    "test": "jest",
    "part1": "tsc -lib ES2020 aoc_DD.ts && node aoc_DD.js -p 1",
    "part2": "tsc -lib ES2020 aoc_DD.ts && node aoc_DD.js -p 2",
    "part1v": "tsc -lib ES2020 aoc_DD.ts && node aoc_DD.js -p 1 -v",
    "part2v": "tsc -lib ES2020 aoc_DD.ts && node aoc_DD.js -p 2 -v"
  },
  "keywords": ["Advent of Code"],
    "author": "Dr. Dean Earl Wright III",
  "license": "MIT",
  "repository": {
    "private": true
    },
  "devDependencies": {
    "@types/jest": "^27.0.2",
    "@types/node": "^16.11.0",
    "@typescript-eslint/eslint-plugin": "^4.33.0",
    "@typescript-eslint/parser": "^4.33.0",
    "eslint": "^7.32.0",
    "eslint-config-airbnb-base": "^14.2.1",
    "eslint-config-airbnb-typescript": "^14.0.1",
    "eslint-config-standard": "^16.0.2",
    "eslint-plugin-import": "^2.22.1",
    "eslint-plugin-jest": "^25.2.1",
    "eslint-plugin-node": "^11.1.0",
    "eslint-plugin-promise": "^5.1.0",
    "eslint-plugin-react": "^7.22.0",
    "jest": "^27.2.5",
    "ts-jest": "^27.0.6",
    "typescript": "^4.4.4"
  },
  "dependencies": {
    "yargs": "^17.2.1"
  },
  "jest": {
    "transform": {
      ".(ts|tsx)": "ts-jest"
    },
    "moduleFileExtensions": [
      "ts",
      "tsx",
      "js"
    ]
  }
}
"""

ESLINTRC_TS = """{
  "settings": {
    "'import/resolver": {
        "node": {
          "paths": ["."],
          "extensions": [".js", ".jsx", ".ts", ".tsx"],
          "moduleDirectory": ["node_modules", "."]
        }
    }
  },
  "root": true,
  "parser": "@typescript-eslint/parser",
  "extends": [
    "airbnb-base",
    "airbnb-typescript/base",
  ],
  "env": {
    "commonjs": true,
    "jest": true,
    "jest/globals": true
  },
  "plugins": [
    "jest",
    "@typescript-eslint"
  ],
  "globals": {
    "Atomics": "readonly",
    "SharedArrayBuffer": "readonly"
  },
  "parserOptions": {
    "project": "./tsconfig.json"
  },
  "rules": {
    "no-console": 0,
    "linebreak-style": 0,
    "import/prefer-default-export": 0,
    "import/extensions": "off",
    "jest/no-disabled-tests": "warn",
    "jest/no-focused-tests": "error",
    "jest/no-identical-title": "error",
    "jest/prefer-to-have-length": "warn",
    "jest/valid-expect": "error"
  }
}
"""

TSCONFIG_JSON = """{
  "compilerOptions": {
    "lib": [
        "es2020"
    ],
    "strict": true,
    "moduleResolution": "node",
    "baseUrl": "./",
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
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

TYPESCRIPT_FILES = {
    'aoc_DD.ts': AOC_DD_TS,
    'MODULE.ts': CLASS_TS,
    'MODULE.test.ts': TEST_CLASS_TS,
    'part_one.txt': PART_ONE_TXT,
    'part_two.txt': PART_TWO_TXT,
    'package.json': PACKAGE_JSON_TS,
    '.eslintrc': ESLINTRC_TS,
    'tsconfig.json': TSCONFIG_JSON,
}

TYPESCRIPT_EXTRA = {
    'EXTRA.ts': EXTRA_TS,
    'EXTRA.test.ts': EXTRA_TEST_TS,
}


def ts_before(args):
    "Build text converters"

    # 0. Precondition axioms
    assert args

    # 1. Result options
    if args.rtype == "int":
        rtype = "number"
        rnone = "NaN"
        rchk = "Number.isNaN(solution)"
        nrchk = "!Number.isNaN(solution)"
    if args.rtype == "str":
        rtype = "string"
        rnone = "''"
        rchk = "solution.length === 0"
        nrchk = "solution.length > 0"

    # 1. Start with simple conversions
    result = {
        "YYYY": "%4d" % args.year,
        "DD": "%02d" % args.day,
        "D D": ' '.join(list("%02d" % args.day)),
        "TITLE": ' '.join(args.title),
        "MODULE": args.cname.lower(),
        "CLASS": args.cname.capitalize(),
        "M O D U L E": ' '.join(list(args.cname.lower())),
        "DIRLOWER": "%02d_%s" % (args.day, ''.join(args.title).lower()),
        'RTYPE': rtype,
        'RNONE': rnone,
        'RCHECK': rchk,
        'NOTCHK': nrchk,
        "EXTRA": args.ename.lower(),
        "OTHER": args.ename.capitalize(),
        "E X T R A": ' '.join(list(args.ename.lower())),

    }

    # 9. Return the text converters
    return result


def ts_after(args, converters, text):
    "Cleanup text"

    # 0. Precondition axioms
    assert args
    assert converters
    assert text

    # 9. Return the input text
    return text

# ======================================================================
# end                 a o c _ t y p e s c r i p t . p y              end
# ======================================================================
