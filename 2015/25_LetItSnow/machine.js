/* eslint-disable linebreak-style */
// ======================================================================
// Let It Snow
//   Advent of Code 2015 Day 25 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           m a c h i n e . j s
//
// A solver for the Advent of Code 2015 Day 25 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Machine
// ======================================================================

class Machine {
  // Object for Let It Snow

  constructor(options) {
    // Create a Machine object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.row = 0;
    this.col = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    this.row = 0;
    this.col = 0;
    const re = /.* row ([0-9]+), column ([0-9]+)\./; // row 2947, column 3029.
    const result = re.exec(text[0]);
    if (result === null) {
      // eslint-disable-next-line no-console
      console.log(`Unable to parse input: ${text}`);
    } else {
      this.row = parseInt(result[1], 10);
      this.col = parseInt(result[2], 10);
    }
  }

  code(verbose) {
    // 1. Can't do much for these
    if (this.row <= 0 || this.col <= 0) return 0;
    // 2. Let's start at the very beginning,
    //    a very good place to start.
    //    When you read you begin with A, B, C.
    //    When you code you begin with 1, 1, 20151125.
    let [row, col, number] = [1, 1, 20151125];
    // 3. Loop until we reach the required row and column
    while (row !== this.row || col !== this.col) {
      // 4. Compute the next number
      number = (number * 252533) % 33554393;
      // 5. Determine where this number would go
      if (row === 1) {
        row = col + 1;
        col = 1;
        // eslint-disable-next-line no-console
        if (verbose) console.log(`Starting new row ${row}, looking for row ${this.row}, col ${this.col}`);
      } else {
        row -= 1;
        col += 1;
      }
    }
    return number;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.code();
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

module.exports.Machine = Machine;
// ======================================================================
// end                      m a c h i n e . j s                     end
// ======================================================================
