// ======================================================================
// How About a Nice Game of Chess
//   Advent of Code 2016 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           d o o r p a s s . t s
//
// A solver for the Advent of Code 2016 Day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Md5 } from 'ts-md5/dist/md5';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Doorpass
// ======================================================================

export class Doorpass {
  // Object for How About a Nice Game of Chess
  text: string[];

  part2: boolean;

  id: string;

  constructor(text: string[], part2 = false) {
    // Create a Doorpass object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.id = '';

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.id = this.text[0].trim();
    }
  }

  passwordFromID(verbose = false, limit = 0): string {
    if (verbose) console.log(`passwordFromID: ${limit}`);
    // 1. Start with nothing
    let result = '';
    let index = 0;
    // 2. Loop until we compute the eight character password
    while (result.length < 8 && (limit === 0 || index < limit)) {
      // 3. Check if the hash of the id and the index starts with five zeroes
      const idhash = Md5.hashStr(this.id + index).toString();
      if (idhash.startsWith('00000')) {
        result += idhash[5];
        if (verbose) console.log(`${this.id} ${index} ${result}`);
      }
      index += 1;
    }
    return result;
  }

  passwordFromIDTwo(verbose = false, limit = 0): string {
    if (verbose) console.log(`passwordFromIDTwo: ${limit}`);
    // 1. Start with nothing
    let result = '________';
    let index = 0;
    // 2. Loop until we compute the eight character password
    while (result.indexOf('_') !== -1 && (limit === 0 || index < limit)) {
      // 3. Check if the hash of the id and the index starts with five zeroes
      const idhash = Md5.hashStr(this.id + index).toString();
      if (idhash.startsWith('00000')) {
        const offset = parseInt(idhash[5], 16);
        const letter = idhash[6];
        if (offset < 8 && result[offset] === '_') {
          const letters = result.split('');
          letters[offset] = letter;
          result = letters.join('');
        }
        if (verbose) console.log(`${this.id} ${index} ${result} ${offset} ${letter}`);
      }
      index += 1;
    }
    return result;
  }

  solution(verbose = false, limit = 0): string {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return '';
    }
    return '';
  }

  partOne(verbose = false, limit = 0): string {
    // Returns the solution for part one

    return this.passwordFromID(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.passwordFromIDTwo(verbose, limit);
  }
}

// ======================================================================
// end                      d o o r p a s s . t s                     end
// ======================================================================
