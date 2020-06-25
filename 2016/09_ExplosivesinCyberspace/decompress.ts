// ======================================================================
// Explosives in Cyberspace
//   Advent of Code 2016 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           d e c o m p r e s s . t s
//
// A solver for the Advent of Code 2016 Day 09 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                             Decompress
// ======================================================================

export class Decompress {
  // Object for Explosives in Cyberspace
  text: string[];

  part2: boolean;

  decompressed: string[];

  constructor(text: string[], part2 = false) {
    // Create a Decompress object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.decompressed = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Loop for all of them lines of text
    this.text.forEach((line) => {
      if (this.part2) {
        this.decompressed.push(Decompress.lengthOfExpanded(line));
      } else {
        this.decompressed.push(Decompress.expandText(line));
      }
    });
  }

  static expandText(line: string): string {
    let result = '';
    let remainder = 0;
    let left = line.indexOf('(', remainder);
    while (left >= 0) {
      const right = line.indexOf(')', left);
      if (right > 0) {
        const cross = line.indexOf('x', left);
        if (cross > 0 && cross < right) {
          const numbers = line.substring(left + 1, right).split('x');
          const chars = parseInt(numbers[0], 10);
          const times = parseInt(numbers[1], 10);
          const once = line.substring(right + 1, right + 1 + chars);
          const expanded = once.repeat(times);
          // console.log(`left=${left}, cross=${cross}, right=${right},
          // chars = ${ chars }, times = ${ times }, once = ${ once }, expanded = ${ expanded }`);
          result = `${result}${line.substring(remainder, left)}${expanded}`;
          remainder = right + 1 + chars;
          // console.log(`result=${result}, remainder=${remainder}`);
        } else {
          result = `${result}(`;
          remainder += 1;
        }
      } else {
        result = `${result}(`;
        remainder += 1;
      }
      left = line.indexOf('(', remainder);
    }
    result = `${result}${line.substring(remainder)}`;
    // console.log(`expand ${line}, ${result}`);
    return result;
  }

  static lengthOfExpanded(line: string): string {
    return `#${Decompress.lengthOfPart(line)}`;
  }

  static lengthOfPart(line: string): number {
    let result = 0;
    let remainder = 0;
    let left = line.indexOf('(', remainder);
    while (left >= 0) {
      const right = line.indexOf(')', left);
      if (right > 0) {
        const cross = line.indexOf('x', left);
        if (cross > 0 && cross < right) {
          const numbers = line.substring(left + 1, right).split('x');
          const chars = parseInt(numbers[0], 10);
          const times = parseInt(numbers[1], 10);
          const once = line.substring(right + 1, right + 1 + chars);
          const expanded = Decompress.lengthOfPart(once);
          // console.log(`left=${left}, cross=${cross}, right=${right}, chars=${chars},
          //  times=${times}, once=${once}, expanded=${expanded}`);
          result += (left - remainder) + times * expanded;
          remainder = right + 1 + chars;
          // console.log(`result=${result}, remainder=${remainder}`);
        } else {
          result += 1;
          remainder += 1;
        }
      } else {
        result += 1;
        remainder += 1;
      }
      left = line.indexOf('(', remainder);
    }
    result += line.length - remainder;
    // console.log(`lengthOfPart: result=${result} line=${line}`);
    return result;
  }

  countChars(): number {
    let result = 0;
    const re = / /g;
    this.decompressed.forEach((line) => {
      if (line.startsWith('#')) {
        result += parseInt(line.substring(1), 10);
      } else {
        result += line.replace(re, '').length;
      }
    });
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.countChars();
    }
    return this.countChars();
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
// end                    d e c o m p r e s s . t s                   end
// ======================================================================
