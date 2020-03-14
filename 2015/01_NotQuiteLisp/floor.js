/* eslint-disable linebreak-style */
// ======================================================================
// Not Quite Lisp
//   Advent of Code 2015 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ========================================================================

// ======================================================================
//                           f l o o r . j s
//
// A solver for the Advent of Code 2015 Day 01 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Floor
// ======================================================================

class Floor {
  // Object for Not Quite Lisp

  constructor(options) {
    // Create a Floor object

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

module.exports.Floor = Floor;
// ======================================================================
// end                         f l o o r . j s                        end
// ======================================================================
