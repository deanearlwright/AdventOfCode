// ======================================================================
// Binary Boarding
//   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b p a s s . t s
//
// Bpass for the Advent of Code 2020 Day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_F = /F/g;
const RE_B = /B/g;
const RE_L = /L/g;
const RE_R = /R/g;

// ======================================================================
//                                                                  Bpass
// ======================================================================

export class Bpass {
  // Object for Binary Boarding
  text: string;

  part2: boolean;

  row: number;

  col: number;

  seat: number;

  constructor(text: string, part2 = false) {
    // Create a Bpass object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.row = 0;
    this.col = 0;
    this.seat = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      const binary = this.text.replace(RE_F, '0').replace(RE_B, '1').replace(RE_L, '0').replace(RE_R, '1');
      // console.log(`${this.text} ${binary} ${binary.substr(0, 7)} ${binary.substr(7, 3)}`);
      this.row = parseInt(binary.substr(0, 7), 2);
      this.col = parseInt(binary.substr(7, 3), 2);
      this.seat = this.row * 8 + this.col;
    }
  }
}

// ======================================================================
// end                         b p a s s . t s                        end
// ======================================================================
