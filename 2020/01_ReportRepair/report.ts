// ======================================================================
// Report Repair
//   Advent of Code 2020 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r e p o r t . t s
//
// A solver for the Advent of Code 2020 Day 01 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Report
// ======================================================================

export class Report {
  // Object for Report Repair
  text: string[];

  part2: boolean;

  numbers: number[];

  constructor(text: string[], part2 = false) {
    // Create a Report object

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

  two_entries(verbose = false, limit = 0): number {
    if (verbose) console.log(`two_entries: ${limit}`);

    // 1. Loop for all the numbers
    for (let indx1 = 0; indx1 < this.numbers.length; indx1 += 1) {
      if (verbose) console.log(`two_entries: indx1=${indx1}, ${this.numbers[indx1]}`);
      // 2. Loop for the rest of the numbers
      for (let indx2 = indx1 + 1; indx2 < this.numbers.length; indx2 += 1) {
        if (verbose) console.log(`two_entries: indx2=${indx2}, ${this.numbers[indx2]}`);
        // 3. If these two numbers add to 2020, return their product
        if (this.numbers[indx1] + this.numbers[indx2] === 2020) {
          return this.numbers[indx1] * this.numbers[indx2];
        }
      }
    }
    // 4. All those loops and we never found a match
    return NaN;
  }

  three_entries(verbose = false, limit = 0): number {
    if (verbose) console.log(`three_entries: ${limit}`);

    // 1. Loop for all the numbers
    for (let indx1 = 0; indx1 < this.numbers.length; indx1 += 1) {
      if (verbose) console.log(`two_entries: indx1=${indx1}, ${this.numbers[indx1]}`);
      // 2. Loop for the rest of the numbers
      for (let indx2 = indx1 + 1; indx2 < this.numbers.length; indx2 += 1) {
        if (verbose) console.log(`two_entries: indx2=${indx2}, ${this.numbers[indx2]}`);
        // 3. And again loop for the rest of the numbers
        for (let indx3 = indx2 + 1; indx3 < this.numbers.length; indx3 += 1) {
          if (verbose) console.log(`two_entries: indx3=${indx3}, ${this.numbers[indx3]}`);
          // 4. If these three numbers add to 2020, return their product
          if (this.numbers[indx1] + this.numbers[indx2] + this.numbers[indx3] === 2020) {
            return this.numbers[indx1] * this.numbers[indx2] * this.numbers[indx3];
          }
        }
      }
    }
    // 5. All those loops and we never found a match
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.three_entries(verbose, limit);
    }
    return this.two_entries(verbose, limit);
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
// end                         r e p o r t . t s                      end
// ======================================================================
