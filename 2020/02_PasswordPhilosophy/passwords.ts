// ======================================================================
// Password Philosophy
//   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a s s w o r d s . t s
//
// A solver for the Advent of Code 2020 Day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Policy } from './policy';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                              Passwords
// ======================================================================

export class Passwords {
  // Object for Password Philosophy
  text: string[];

  part2: boolean;

  policies: Policy[];

  constructor(text: string[], part2 = false) {
    // Create a Passwords object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.policies = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      // 3. Loop for all of the lines of text
      for (let indx = 0; indx < this.text.length; indx += 1) {
        // 4. Create a policy object and add it in to the growing list
        this.policies.push(new Policy(this.text[indx], this.part2));
      }
    }
  }

  count_valid(): number {
    // Return the number of passwords that match the policy

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the policies
    for (let indx = 0; indx < this.policies.length; indx += 1) {
      // 3. If this password matches the policy, increment the result
      if (this.policies[indx].is_valid()) {
        result += 1;
      }
    }

    // 4. Return the number of good password/policy pairs
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.count_valid();
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
// end                    p a s s w o r d s . t s                     end
// ======================================================================
