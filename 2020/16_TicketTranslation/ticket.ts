// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t i c k e t . t s
//
// Ticket for the Advent of Code 2020 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_NUM = /[0-9]+/g;

// ======================================================================
//                                                                 Ticket
// ======================================================================

export class Ticket {
  // Object for Ticket Translation
  text: string;

  part2: boolean;

  numbers: number[];

  valid: boolean;

  constructor(text: string, part2 = false) {
    // Create a Ticket object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.numbers = [];
    this.valid = true;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      const nums = Array.from(this.text.matchAll(RE_NUM), (m) => m[0]);
      for (let indx = 0; indx < nums.length; indx += 1) {
        this.numbers.push(parseInt(nums[indx], 10));
      }
    }
  }

  length(): number {
    // Return the number of numbers on the ticket
    return this.numbers.length;
  }
}

// ======================================================================
// end                        t i c k e t . t s                       end
// ======================================================================
