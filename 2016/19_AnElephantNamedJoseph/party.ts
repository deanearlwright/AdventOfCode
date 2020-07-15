// ======================================================================
// An Elephant Named Joseph
//   Advent of Code 2016 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a r t y . t s
//
// A solver for the Advent of Code 2016 Day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Party
// ======================================================================

export class Party {
  // Object for An Elephant Named Joseph
  text: string[];

  part2: boolean;

  numElves: number;

  elves: number[];

  constructor(text: string[], part2 = false) {
    // Create a Party object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.numElves = 0;
    this.elves = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.numElves = parseInt(this.text[0], 10);
      for (let elf = 0; elf < this.numElves; elf += 1) {
        this.elves.push(1);
      }
    }
  }

  whoIsToTheLeft(elf: number): number {
    for (let left = elf + 1; left < this.numElves; left += 1) {
      if (this.elves[left] > 0) {
        return left;
      }
    }
    for (let left = 0; left < elf; left += 1) {
      if (this.elves[left] > 0) {
        return left;
      }
    }
    return elf;
  }

  stealPresents(starting: number): number {
    let elf = starting;
    let left = this.whoIsToTheLeft(elf);
    while (elf !== left) {
      this.elves[elf] += this.elves[left];
      this.elves[left] = 0;
      elf = this.whoIsToTheLeft(elf);
      left = this.whoIsToTheLeft(elf);
    }
    return elf + 1;
  }

  whoIsAcross(elf: number, kntElves: number): number {
    const half = Math.floor(kntElves / 2);
    let result = elf;
    for (let knt = 0; knt < half; knt += 1) {
      result = this.whoIsToTheLeft(result);
    }
    return result;
  }

  stealPresentsTwo(starting: number): number {
    let kntElves = this.elves.length;
    let elf = starting;
    while (kntElves > 1) {
      const across = this.whoIsAcross(elf, kntElves);
      this.elves[elf] += this.elves[across];
      this.elves[across] = 0;
      kntElves -= 1;
      elf = this.whoIsToTheLeft(elf);
    }
    return elf + 1;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.stealPresentsTwo(0);
    }
    return this.stealPresents(0);
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
// end                         p a r t y . t s                        end
// ======================================================================
