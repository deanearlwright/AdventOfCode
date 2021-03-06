// ======================================================================
// Adapter Array
//   Advent of Code 2020 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           j o l t s . t s
//
// A solver for the Advent of Code 2020 Day 10 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Arrangement = Record<number, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Jolts
// ======================================================================

export class Jolts {
  // Object for Adapter Array
  text: string[];

  part2: boolean;

  numbers: number[];

  device: number;

  constructor(text: string[], part2 = false) {
    // Create a Jolts object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.numbers = [];
    this.device = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      for (let indx = 0; indx < this.text.length; indx += 1) {
        const num = +this.text[indx];
        this.numbers.push(num);
        this.device = Math.max(num, this.device);
      }
      this.device += 3;
      this.numbers.sort((a, b) => a - b);
    }
  }

  count_diff(): number[] {
    // Return the count of adaptor differences

    // 1. Start with nothing
    let one = 0;
    let three = 0;
    let last = 0;

    // 2. Loop for all the adaptors (in sorted order)
    for (let indx = 0; indx < this.numbers.length; indx += 1) {
      const jolts = this.numbers[indx];
      // console.log(`one=${one} three=${three} last=${last} indx=${indx} jolts=${jolts}`);

      // 3. Compute and count the differences
      const diff = jolts - last;
      switch (diff) {
        case 1:
          one += 1;
          break;
        case 3:
          three += 1;
          break;
        default:
          console.log(`Unexpected difference from ${last} to ${jolts}`);
      }
      // 4. The current value is now the last
      last = jolts;
    }
    // 5. One more differernce to the device
    three += 1;

    // 6. Return the counts
    return [one, three];
  }

  count_arrangements(): number {
    // Returns the possible arrangement of adaptors

    // 1. Start with no arrangements
    const arrangements: Arrangement = {};
    let last = 0;
    // 2. Loop for all the adaptors (in sorted order)
    for (let indx = 0; indx < this.numbers.length; indx += 1) {
      const jolts = this.numbers[indx];

      // 3. Get the number of arrangments for the previous three joltages
      const minus3 = arrangements[jolts - 3] || 0;
      const minus2 = arrangements[jolts - 2] || 0;
      const minus1 = arrangements[jolts - 1] || 0;

      // 4. Can this be the initial adaptor?
      const initial = jolts <= 3 ? 1 : 0;

      // 5. The number of arrangements for this adaptor is the sum of those immediately below it
      arrangements[jolts] = minus3 + minus2 + minus1 + initial;
      last = jolts;
    }
    // 6. Return the total number of arrangements
    return arrangements[last];
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.count_arrangements();
    }
    const knts = this.count_diff();
    return knts[0] * knts[1];
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
// end                      j o l t s . t s                     end
// ======================================================================
