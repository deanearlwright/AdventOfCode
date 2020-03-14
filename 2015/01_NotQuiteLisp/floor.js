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
    this.level = null;
    this.directions = '';
    this.toBasement = null;

    // 2. Process text (if any)
    if (this.text !== null) {
      [this.directions] = this.text;
    }
  }

  followDirections() {
    // 1. Start at the ground floor
    let number = 0;
    this.level = 0;
    // 2. Loop for each character in the instructions
    this.directions.split('').forEach((paren) => {
      number += 1;
      // 3. Go up or down a level
      if (paren === '(') {
        this.level += 1;
      } else if (paren === ')') {
        this.level -= 1;
        // 4. Remenber when we enter the basement
        if (this.level < 0 && this.toBasement === null) {
          this.toBasement = number;
        }
      } else {
        console.log('Unexpected direction ', paren); // eslint-disable-line no-console
      }
    });
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Follow the directions
    this.followDirections();

    // 2. Return the solution for part one
    return this.level;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Follow the directions
    this.followDirections();

    // 2. Return the solution for part one
    return this.toBasement;
  }
}

module.exports.Floor = Floor;
// ======================================================================
// end                         f l o o r . j s                        end
// ======================================================================
