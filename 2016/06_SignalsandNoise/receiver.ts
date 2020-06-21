// ======================================================================
// Signals and Noise
//   Advent of Code 2016 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r e c e i v e r . t s
//
// A solver for the Advent of Code 2016 Day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type CharCounts = Map<string, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Receiver
// ======================================================================

export class Receiver {
  // Object for Signals and Noise
  text: string[];

  part2: boolean;

  counts: CharCounts[];

  constructor(text: string[], part2 = false) {
    // Create a Receiver object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.counts = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Create empty counts
    this.counts = [];
    for (let index = 0; index < this.text[0].length; index += 1) {
      const counts: CharCounts = new Map();
      this.counts.push(counts);
    }
    // 2. Loop every line in the text
    let lineNum = 0;
    this.text.forEach((line) => {
      lineNum += 1;
      // 3. Check length of line
      if (line.length !== this.counts.length) {
        console.log(`Unexpected line length ${lineNum} ${line.length} !== ${this.counts.length} ${line}`);
      } else {
        // 4. Add the letters in the line to the column counts
        for (let index = 0; index < line.length; index += 1) {
          const letter = line[index];
          const value = this.counts[index].get(letter) || 0;
          this.counts[index].set(letter, value + 1);
        }
      }
    });
  }

  recoverMessage(verbose = false, limit = 0): string {
    if (verbose) console.log(`recoverMessage: ${limit}`);
    // 1. Start with nothing
    let result = '';
    // 2. Loop through the counts
    this.counts.forEach((charMap) => {
      // 3. Find the most frequent character in the column
      let char = '?';
      let frequency = 0;
      charMap.forEach((value, key) => {
        if (value > frequency) {
          frequency = value;
          char = key;
        }
      });
      // 4. Add the most frequent letter to the result
      result += char;
    });
    // 5. Return the recovered message
    return result;
  }

  recoverMessageTwo(verbose = false, limit = 0): string {
    if (verbose) console.log(`recoverMessage: ${limit}`);
    // 1. Start with nothing
    let result = '';
    // 2. Loop through the counts
    this.counts.forEach((charMap) => {
      // 3. Find the most frequent character in the column
      let char = '?';
      let frequency = this.text.length;
      charMap.forEach((value, key) => {
        if (value < frequency) {
          frequency = value;
          char = key;
        }
      });
      // 4. Add the most frequent letter to the result
      result += char;
    });
    // 5. Return the recovered message
    return result;
  }

  solution(verbose = false, limit = 0): string {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.recoverMessageTwo();
    }
    return this.recoverMessage();
  }

  partOne(verbose = false, limit = 0): string {
    // Returns the solution for part one

    return this.recoverMessage(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      r e c e i v e r . t s                     end
// ======================================================================
