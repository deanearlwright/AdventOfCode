// ======================================================================
// One-Time Pad
//   Advent of Code 2016 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a d . t s
//
// A solver for the Advent of Code 2016 Day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Md5 } from 'ts-md5/dist/md5';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

interface Hash {
  hash: string;
  key: boolean;
  triple: string;
  penta: string;
}

type Hashes = Hash[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// const digits = '0123456789abcdef'.split('');
const tripleDigits = [
  '000', '111', '222', '333', '444', '555', '666', '777',
  '888', '999', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff',
];
const pentaDigits = [
  '00000', '11111', '22222', '33333',
  '44444', '55555', '66666', '77777',
  '88888', '99999', 'aaaaa', 'bbbbb',
  'ccccc', 'ddddd', 'eeeee', 'fffff',
];

// ======================================================================
//                                                                    Pad
// ======================================================================

export class Pad {
  // Object for One-Time Pad
  text: string[];

  part2: boolean;

  salt: string;

  hashes: Hashes;

  constructor(text: string[], part2 = false) {
    // Create a Pad object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.salt = '';
    this.hashes = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      [this.salt] = this.text;
    }
  }

  nextHash(): void {
    const index = this.hashes.length;
    let md5Hash = <string> Md5.hashStr(this.salt + index);
    if (this.part2) md5Hash = Pad.extendHash(md5Hash);
    const triple = Pad.firstTriple(md5Hash);
    const penta = Pad.allPentas(md5Hash);
    const hash = {
      hash: md5Hash,
      key: false,
      triple,
      penta,
    };
    // console.log(`index=${index} hash=${md5Hash} triple=${triple} penta=${penta}`);
    this.hashes.push(hash);
  }

  static extendHash(hash: string): string {
    let result = hash;
    for (let index = 0; index < 2016; index += 1) {
      result = <string> Md5.hashStr(result);
    }
    return result;
  }

  static firstTriple(hash: string): string {
    let first = 9999;
    tripleDigits.forEach((triple) => {
      const index = hash.indexOf(triple);
      if (index !== -1 && index < first) first = index;
    });
    return first < 9999 ? hash[first] : '';
  }

  static allPentas(hash: string): string {
    const result: string[] = [];
    pentaDigits.forEach((penta) => {
      const index = hash.indexOf(penta);
      if (index !== -1) result.push(penta[0]);
    });
    return result.join('');
  }

  nextTriple(index: number): number {
    console.log(`Looking for triple starting at ${index}`);
    while (index + 1 > this.hashes.length) {
      this.nextHash();
    }
    let result = index;
    while (this.hashes[result].triple === '') {
      result += 1;
      if (result + 1 > this.hashes.length) this.nextHash();
    }
    console.log(`Found triple of ${this.hashes[result].triple} at ${result}`);
    return result;
  }

  foundPenta(index: number): boolean {
    const lookForTriple = this.hashes[index].triple;
    const limit = index + 1001;
    console.log(`Looking for penta of ${lookForTriple} from ${index + 1} to ${limit}`);
    for (let check = index + 1; check < limit; check += 1) {
      if (check + 1 > this.hashes.length) this.nextHash();
      if (this.hashes[check].penta.indexOf(lookForTriple) !== -1) {
        console.log(`Found penta of ${lookForTriple} at ${check}`);
        return true;
      }
    }
    console.log(`No penta of ${lookForTriple} from ${index + 1} to ${limit}`);
    return false;
  }

  nextKey(index: number): number {
    console.log(`Looking for key starting at ${index}`);
    let result = index;
    let gotKey = false;
    while (!gotKey) {
      result = this.nextTriple(result);
      if (this.foundPenta(result)) {
        this.hashes[result].key = true;
        gotKey = true;
      } else {
        result += 1;
      }
    }
    console.log(`Found Key at ${result}`);
    return result;
  }

  get64Keys(): number {
    this.hashes = [];
    let result = 0;
    for (let index = 0; index < 64; index += 1) {
      result = this.nextKey(result) + 1;
    }
    return result - 1;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.get64Keys();
    }
    return this.get64Keys();
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
// end                           p a d . t s                          end
// ======================================================================
