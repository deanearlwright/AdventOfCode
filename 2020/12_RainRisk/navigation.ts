// ======================================================================
// Rain Risk
//   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           n a v i g a t i o n . t s
//
// A solver for the Advent of Code 2020 Day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Ferry } from './ferry';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                             Navigation
// ======================================================================

export class Navigation {
  // Object for Rain Risk
  text: string[];

  part2: boolean;

  ferry: Ferry;

  constructor(text: string[], part2 = false) {
    // Create a Navigation object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.ferry = new Ferry(this.part2);
  }

  executeAll(): number {
    // Execute all of the instructions

    // 1. Loop for each line of test
    for (let indx = 0; indx < this.text.length; indx += 1) {
      const instruction = this.text[indx];

      // 2. Execute the instruction
      this.ferry.execute(instruction);
      // console.log(`${indx + 1} inst ${instruction} loc ${this.ferry.loc}
      //              waypoint ${ this.ferry.waypoint }`);
    }

    // 3. Return the manhattan (taxi-cab) distance
    return this.ferry.manhattanDistance();
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.executeAll();
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
// end                    n a v i g a t i o n . t s                   end
// ======================================================================
