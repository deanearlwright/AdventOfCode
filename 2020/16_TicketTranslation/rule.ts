// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r u l e . t s
//
// Rule for the Advent of Code 2020 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_NUM = /[0-9]+/g;

// ======================================================================
//                                                                   Rule
// ======================================================================

export class Rule {
  // Object for Ticket Translation
  text: string;

  part2: boolean;

  name: string;

  numbers: number[];

  positions: number[];

  constructor(text: string, part2 = false) {
    // Create a Rule object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.name = '';
    this.numbers = [];
    this.positions = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string) {
    // Populate the rule from rule

    // 1. Get the name
    this.name = text.substr(0, text.indexOf(':'));

    // 2. Get the numbers
    const nums = Array.from(this.text.matchAll(RE_NUM), (m) => m[0]);
    for (let indx = 0; indx < nums.length; indx += 1) {
      this.numbers.push(parseInt(nums[indx], 10));
    }
  }

  isValid(num: number): boolean {
    // Returns true if number matches the rule

    // 1. Check the number against the first range
    if (num >= this.numbers[0] && num <= this.numbers[1]) {
      return true;
    }
    // 2. Check the number against the second range
    if (num >= this.numbers[2] && num <= this.numbers[3]) {
      return true;
    }

    // 3. So sorry
    return false;
  }

  allValid(nums: number[]): boolean {
    // Return false is there is an invalid number

    // 1. Loop for all of the numbers
    for (let indx = 0; indx < nums.length; indx += 1) {
      const num = nums[indx];

      // 2. Return false if the number is invalid
      if (!this.isValid(num)) {
        return false;
      }
    }

    // 3. All are valid
    return true;
  }

  singleton(): boolean {
    // Return true is there is only one position for this rule
    return this.positions.length === 1;
  }

  resolved(): boolean {
    // Return true if the rule is resolved to a single field
    return this.positions.length === 1;
  }

  ticketIndex(): number {
    // Return the position of the ticket for this field (-1 if unknown)

    if (this.positions.length !== 1) {
      return -1;
    }
    return this.positions[0];
  }

  remove(num: number) {
    // Return the number from the positions (if it is there)
    // 1. Is the number in the positions array?
    const indx = this.positions.indexOf(num);

    // 2. If it is remove it
    if (indx !== -1) {
      this.positions.splice(indx, 1);
    }
  }
}

// ======================================================================
// end                          r u l e . t s                         end
// ======================================================================
