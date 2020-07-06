// ======================================================================
// Timing is Everything
//   Advent of Code 2016 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           d i s c s . t s
//
// A solver for the Advent of Code 2016 Day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
interface Disc {
  num: number;
  positions: number;
  time0: number;
  now: number;
}
type Stack = Disc[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const disc0: Disc = {
  num: 0,
  positions: 1,
  time0: 0,
  now: 0,
};

// ======================================================================
//                                                                  Discs
// ======================================================================

export class Discs {
  // Object for Timing is Everything
  text: string[];

  part2: boolean;

  stack: Stack;

  time: number;

  constructor(text: string[], part2 = false) {
    // Create a Discs object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.stack = [disc0];
    this.time = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    this.stack = [disc0];
    const reTrash = /(#|,|\.|;)/g;
    this.text.forEach((line) => {
      const parts = line.replace(reTrash, '').split(' ');
      const disc:Disc = {
        num: parseInt(parts[1], 10),
        positions: parseInt(parts[3], 10),
        time0: parseInt(parts[11], 10),
        now: parseInt(parts[11], 10),
      };
      this.stack.push(disc);
    });
  }

  drop(atTime: number): number {
    this.reset();
    while (this.time < atTime) this.advance();
    for (let index = 0; index < this.stack.length; index += 1) {
      if (this.stack[index].now !== 0) return index;
      this.advance();
    }
    return 0;
  }

  reset(): void {
    this.time = 0;
    for (let index = 0; index < this.stack.length; index += 1) {
      this.stack[index].now = this.stack[index].time0;
    }
  }

  advance(): void {
    this.time += 1;
    for (let index = 0; index < this.stack.length; index += 1) {
      this.stack[index].now += 1;
      if (this.stack[index].now === this.stack[index].positions) {
        this.stack[index].now = 0;
      }
    }
  }

  firstDrop(verbose = false, limit = 0): number {
    const maxTime = limit === 0 ? 99999999999 : limit;
    if (verbose) console.log(`firstDrop: limit = ${maxTime}`);
    for (let time = 0; time < maxTime; time += 1) {
      const disc = this.drop(time);
      if (verbose) console.log(`firstDrop: time = ${time} disc=${disc}`);
      if (disc === 0) return time;
    }
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return this.firstDrop(verbose, limit);
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
// end                         d i s c s . t s                        end
// ======================================================================
