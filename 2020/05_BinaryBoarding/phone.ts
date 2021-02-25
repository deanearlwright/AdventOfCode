// ======================================================================
// Binary Boarding
//   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p h o n e . t s
//
// A solver for the Advent of Code 2020 Day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Bpass } from './bpass';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Phone
// ======================================================================

export class Phone {
  // Object for Binary Boarding
  text: string[];

  part2: boolean;

  passes: Bpass[];

  constructor(text: string[], part2 = false) {
    // Create a Phone object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.passes = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      for (let indx = 0; indx < this.text.length; indx += 1) {
        this.passes.push(new Bpass(this.text[indx], this.part2));
      }
    }
  }

  highestSeat(): number {
    // Returns the number of the highest seat
    // 1. Start with nothing
    let result = -1;

    // 2. Loop for all of the boarding passes
    for (let indx = 0; indx < this.passes.length; indx += 1) {
      // 3. If the seat number of the boarding pass is higher, save the seat number
      if (this.passes[indx].seat > result) {
        result = this.passes[indx].seat;
      }
    }
    // 4. Return the higest seat number
    return result;
  }

  findSeat(): number {
    // Returns the number of the seat no one else has
    // 1. What is the highest seat number
    const highest = this.highestSeat();

    // 2. Work down to find your seat
    for (let seat = highest; seat > 0; seat -= 1) {
      let found = false;

      // 3. Loop for all of the boarding passes
      for (let indx = 0; indx < this.passes.length; indx += 1) {
        if (seat === this.passes[indx].seat) {
          found = true;
        }
      }

      // 4. If there is no boarding pass for this seat, it is ours
      if (!found) {
        return seat;
      }
    }

    // 5. That's odd
    return -1;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.findSeat();
    }
    return this.highestSeat();
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
// end                         p h o n e . t s                        end
// ======================================================================
