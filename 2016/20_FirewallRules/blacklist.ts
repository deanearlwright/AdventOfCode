// ======================================================================
// Firewall Rules
//   Advent of Code 2016 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b l a c k l i s t . t s
//
// A solver for the Advent of Code 2016 Day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

type Range = {
  low: number,
  high: number,
};
type Ranges = Range[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const IP_LOW = 0;
const IP_HIGH = 4294967295;

// ======================================================================
//                                                              Blacklist
// ======================================================================

export class Blacklist {
  // Object for Firewall Rules
  text: string[];

  part2: boolean;

  ranges: Ranges;

  sorted: Ranges;

  constructor(text: string[], part2 = false) {
    // Create a Blacklist object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.ranges = [];
    this.sorted = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
      this.sorted = this.ranges.slice();
      this.sorted.sort((a, b) => a.low - b.low);
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.ranges = [];
    // 2. Loop every line of text
    this.text.forEach((line) => {
      const [low, high] = line.split('-');
      // 3. Add it to the ranges
      this.ranges.push({ low: parseInt(low, 10), high: parseInt(high, 10) });
    });
  }

  findLowestAddress(): number {
    // 1. You have to start somewhere
    let lowest = IP_LOW;
    // 2. Loop for all of the sorted ranges
    for (let index = 0; index < this.sorted.length; index += 1) {
      if (lowest < this.sorted[index].low) {
        return lowest;
      }
      if (lowest < this.sorted[index].high) {
        lowest = this.sorted[index].high + 1;
      }
    }
    return lowest;
  }

  findNumberAddresses(): number {
    // 1. You have to start somewhere
    let count = 0;
    let lowest = IP_LOW;
    // 2. Loop for all of the sorted ranges
    for (let index = 0; index < this.sorted.length; index += 1) {
      if (lowest < this.sorted[index].low) {
        count += this.sorted[index].low - lowest;
      }
      if (lowest < this.sorted[index].high) {
        lowest = this.sorted[index].high + 1;
      }
    }
    if (lowest < IP_HIGH) {
      count += IP_HIGH - lowest;
    }
    return count;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.findNumberAddresses();
    }
    return this.findLowestAddress();
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
// end                     b l a c k l i s t . t s                    end
// ======================================================================
