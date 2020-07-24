// ======================================================================
// Air Duct Spelunking
//   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r o b o t . t s
//
// A solver for the Advent of Code 2016 Day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Robot
// ======================================================================

export class Robot {
  // Object for Air Duct Spelunking
  text: string[];

  part2: boolean;

  constructor(text: string[], part2 = false) {
    // Create a Robot object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      // TODO process the test
    }
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return NaN;
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      r o b o t . t s                     end
// ======================================================================
