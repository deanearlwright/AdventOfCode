// ======================================================================
// Dragon Checksum
//   Advent of Code 2016 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s e c u r i t y . t s
//
// A solver for the Advent of Code 2016 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const FIRST_DISK_SIZE = 272;
const SECOND_DISK_SIZE = 35651584;

// ======================================================================
//                                                               Security
// ======================================================================

export class Security {
  // Object for Dragon Checksum
  text: string[];

  part2: boolean;

  initial: string;

  diskSize: number;

  constructor(text: string[], part2 = false) {
    // Create a Security object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.initial = '';
    this.diskSize = this.part2 ? SECOND_DISK_SIZE : FIRST_DISK_SIZE;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      [this.initial] = this.text;
    }
  }

  static stringReverse(str: string): string {
    return str.split('').reverse().join('');
  }

  static stringFlip(str: string): string {
    return str.replace(/0/g, 'O').replace(/1/g, '0').replace(/O/g, '1');
  }

  static oneDragon(str: string): string {
    return `${str}0${Security.stringFlip(Security.stringReverse(str))}`;
  }

  longDragon(): string {
    let dragon = this.initial;
    while (dragon.length < this.diskSize) {
      console.log(`longDragon length=${dragon.length}`);
      dragon = Security.oneDragon(dragon);
    }
    return dragon.substring(0, this.diskSize);
  }

  static pairs(str: string): string {
    const result: string[] = [];
    for (let index = 0; index < str.length - 1; index += 2) {
      result.push((str[index] === str[index + 1]) ? '1' : '0');
    }
    return result.join('');
  }

  static checksum(str: string): string {
    let result = Security.pairs(str);
    while (result.length % 2 === 0) {
      console.log(`checksum length=${result.length}`);
      result = Security.pairs(result);
    }
    return result;
  }

  solution(verbose = false, limit = 0): string {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return Security.checksum(this.longDragon());
    }
    return Security.checksum(this.longDragon());
  }

  partOne(verbose = false, limit = 0): string {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      s e c u r i t y . t s                     end
// ======================================================================
