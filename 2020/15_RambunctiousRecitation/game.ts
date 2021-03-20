// ======================================================================
// Rambunctious Recitation
//   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           g a m e . t s
//
// A solver for the Advent of Code 2020 Day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Memory } from './memory';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                   Game
// ======================================================================

export class Game {
  // Object for Rambunctious Recitation
  text: string[];

  part2: boolean;

  memory: Memory;

  constructor(text: string[], part2 = false) {
    // Create a Game object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.memory = new Memory('', this.part2);

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.memory = new Memory(this.text[0], this.part2);
    }
  }

  number_spoken(turn: number): number {
    // Return the nth number spoken

    // 1. Loop until we get to the specified turn
    while (this.memory.turn < turn - 1) {
      this.memory.add_last_spoken();
    }

    // 2. Return the number spoken on that turn
    return this.memory.age;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.number_spoken(30000000);
    }
    return this.number_spoken(2020);
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
// end                          g a m e . t s                         end
// ======================================================================
