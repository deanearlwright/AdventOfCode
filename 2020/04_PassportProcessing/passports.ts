// ======================================================================
// Passport Processing
//   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a s s p o r t s . t s
//
// A solver for the Advent of Code 2020 Day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Passport } from './passport';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                              Passports
// ======================================================================

export class Passports {
  // Object for Passport Processing
  text: string[];

  part2: boolean;

  passports: Passport[];

  constructor(text: string[], part2 = false) {
    // Create a Passports object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.passports = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText() {
    // Read in the passports and create the passport objects

    // 1. Start with nothing
    let passportText = '';

    // 2. Loop for all if the lines in the text
    for (let indx = 0; indx < this.text.length; indx += 1) {
      const line = this.text[indx];

      // 3. If this is a blank line, create and add a passport if we have some fields
      if (line.length === 0 && passportText.length > 0) {
        this.passports.push(new Passport(passportText, this.part2));
        passportText = '';
      } else {
        // 4. Keep collecting fields
        passportText = `${passportText} ${line}`;
      }
    }

    // 5. Are there remaining passport fields?
    if (passportText.length > 0) {
      this.passports.push(new Passport(passportText, this.part2));
    }
  }

  count_valid(): number {
    // Returns the number of valid passports

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the passports
    for (let indx = 0; indx < this.passports.length; indx += 1) {
      const pspt = this.passports[indx];

      // 3. If the passport is valid, increment the count
      if (pspt.is_valid()) {
        result += 1;
      }
    }

    // 4. Return the count of valid passports
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.count_valid();
    }
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
// end                     p a s s p o r t s . t s                    end
// ======================================================================
