// ======================================================================
// Rambunctious Recitation
//   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           m e m o r y . t s
//
// Memory for the Advent of Code 2020 Day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Spoken = Record<number, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_NUM = RegExp('[0-9]+', 'g');

// ======================================================================
//                                                                 Memory
// ======================================================================

export class Memory {
  // Object for Rambunctious Recitation
  text: string;

  part2: boolean;

  age: number;

  turn: number;

  numbers: Spoken;

  constructor(text: string, part2 = false) {
    // Create a Memory object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.age = -1;
    this.turn = 0;
    this.numbers = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      const matches = Array.from(this.text.matchAll(RE_NUM), (m) => m[0]);
      for (let indx = 0; indx < matches.length; indx += 1) {
        this.add(parseInt(matches[indx], 10));
      }
    }
  }

  add_last_spoken() {
    // Add the last number spoken
    this.add(this.age);
  }

  add(num: number) {
    // Add a number to the memory

    // 1. Increment the turn number
    this.turn += 1;

    // 2. If the number is new, the age is 0
    if (undefined === this.numbers[num]) {
      this.age = 0;
    } else {
      // 3. Else the age is calculated from when last seen
      this.age = this.turn - this.numbers[num];
    }

    // 4. Save when the number was last seen
    this.numbers[num] = this.turn;
  }
}

// ======================================================================
// end                        m e m o r y . t s                       end
// ======================================================================
