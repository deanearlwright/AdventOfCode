/* eslint-disable linebreak-style */
// ======================================================================
// I Was Told There Would Be No Math
//   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a p e r . j s
//
// A solver for the Advent of Code 2015 Day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Paper
// ======================================================================


class Paper {
  // Object for I Was Told There Would Be No Math

  constructor(options) {
    // Create a Paper object

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

module.exports.Paper = Paper;
// ======================================================================
// end                         p a p e r . j s                        end
// ======================================================================
