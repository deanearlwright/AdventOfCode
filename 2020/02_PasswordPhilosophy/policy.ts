// ======================================================================
// Password Philosophy
//   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p o l i c y . t s
//
// Policy for the Advent of Code 2020 Day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Policy
// ======================================================================

export class Policy {
  // Object for Password Philosophy
  text: string;

  part2: boolean;

  low: number;

  high: number;

  letter: string;

  pswd: string;

  constructor(text: string, part2 = false) {
    // Create a Policy object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.low = 0;
    this.high = 0;
    this.letter = '';
    this.pswd = '';

    // 2. If there is a text, populate the policy and password
    if (text.length > 0) {
      const found = text.match(/(\d+)-(\d+) ([a-z]): ([a-z]+)/);
      if (found) {
        this.low = +found[1];
        this.high = +found[2];
        [this.letter, this.pswd] = found.slice(3, 5);
      } else {
        console.log(`Invalid policy text='${text}'`);
      }
    }
  }

  is_valid(): boolean {
    // Return true if the pswd is valid for the policy

    // 1. For part 1, we need the occurances of the letter to be in the specified range
    if (!this.part2) {
      // 1a. How many times does the letter appear in pswd?
      const re = RegExp(this.letter, 'g');
      const matches = Array.from(this.pswd.matchAll(re));
      const knt = matches.length;

      // 1b. Check that the letter appears the correct number of times
      return knt >= this.low && knt <= this.high;
    }

    // 2. For part 2, we the letter to be in one (but not both) of the given positions
    // 2a. Check for the letter at the two positions
    const atLow = this.letter === this.pswd.substr(this.low - 1, 1);
    const atHigh = this.letter === this.pswd.substr(this.high - 1, 1);
    // 2b. There can be only one
    return (atLow && !atHigh) || (atHigh && !atLow);
  }
}

// ======================================================================
// end                        p o l i c y . t s                       end
// ======================================================================
