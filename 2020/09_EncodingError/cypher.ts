// ======================================================================
// Encoding Error
//   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           c y p h e r . t s
//
// A solver for the Advent of Code 2020 Day 09 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Cypher
// ======================================================================

export class Cypher {
  // Object for Encoding Error
  text: string[];

  part2: boolean;

  numbers: number[];

  preamble: number;

  constructor(text: string[], part2 = false, preamble = 25) {
    // Create a Cypher object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.numbers = [];
    this.preamble = preamble === undefined ? 25 : preamble;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      for (let indx = 0; indx < this.text.length; indx += 1) {
        this.numbers.push(+this.text[indx]);
      }
    }
  }

  rogue_number(): number {
    // Find the number that doesn't follow the rules

    // 1. Set index based on the preamble
    const testStart = this.preamble;
    const testEnd = this.numbers.length;
    let result = NaN;

    // 2. Loop for all of the number to test
    for (let indx = testStart; indx < testEnd; indx += 1) {
      const test = this.numbers[indx];
      result = test;

      // 3. Loop for the last bunch of number
      for (let pindx = indx - this.preamble; pindx < indx - 1; pindx += 1) {
        const previous = this.numbers[pindx];

        // 4. Loop for the remaining previous numbers
        for (let rindx = pindx + 1; rindx < indx; rindx += 1) {
          const remaining = this.numbers[rindx];

          // 5. Check if this pair of previous number is equal to the test number
          if ((previous + remaining) === test) {
            // 6. The test number is fine, we will need to find another
            result = NaN;
          }
        }
      }
      // 7. If this number is not the result of two of the previous numbers, return it
      if (!Number.isNaN(result)) {
        return result;
      }
      // 8. Well then, try to find another
    }
    // 9. Every number satisified
    return NaN;
  }

  weakness(): number {
    // Find the weakness in the XMAS code, returning min+max

    // 1. Need the rule breaker from part 1
    const ruleBreaker = this.rogue_number();

    // 2. Loop for all the numbers (except the last)
    for (let bindx = 0; bindx < this.numbers.length - 1; bindx += 1) {
      const bottom = this.numbers[bindx];
      let rangeMin = bottom;
      let rangeMax = bottom;
      let rangeSum = bottom;

      // 3. Loop for all of the remaining numbers
      for (let indx = bindx + 1; indx < this.numbers.length; indx += 1) {
        const current = this.numbers[indx];
        rangeSum += current;
        rangeMin = Math.min(rangeMin, current);
        rangeMax = Math.max(rangeMax, current);

        // 4. Have we found the range we were looking for?
        if (rangeSum === ruleBreaker) {
          // 5. If so, return the min plus max of the range
          return rangeMin + rangeMax;
        }

        // 6. If the sum is greater than the rule breaker, we need a new beginning
        if (rangeSum > ruleBreaker) {
          indx = this.numbers.length;
        }
      }
    }
    // 7. Never did find a range that added up to the rule breaker
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.weakness();
    }
    return this.rogue_number();
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
// end                        c y p h e r . t s                       end
// ======================================================================
