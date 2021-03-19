// ======================================================================
// Docking Data
//   Advent of Code 2020 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b i t m a s k . t s
//
// A solver for the Advent of Code 2020 Day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Memory = Record<number, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const DEFAULT_MASK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const RE_MEM = /mem\[([0-9]+)\] = ([0-9]+)/;

// ======================================================================
//                                                                Bitmask
// ======================================================================

export class Bitmask {
  // Object for Docking Data
  text: string[];

  part2: boolean;

  bitmask: string;

  memory: Memory;

  constructor(text: string[], part2 = false) {
    // Create a Bitmask object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.bitmask = DEFAULT_MASK;
    this.memory = {};
  }

  execute(): number {
    // Run the initialization code and return the sum of the memory locations

    // 1. Loop fpr all instructions in the initialization code
    for (let indx = 0; indx < this.text.length; indx += 1) {
      const inst = this.text[indx];

      // 2. Execute the mask or mem instruction
      if (inst.substr(0, 4) === 'mask') {
        this.saveMask(inst);
      } else {
        this.saveMem(inst);
      }
    }

    // 3. Return the sum of all of the memory locations
    let result = 0;
    const values = Object.values(this.memory) as Array<number>;
    for (let indx = 0; indx < values.length; indx += 1) {
      result += values[indx];
    }
    return result;
  }

  saveMask(inst: string) {
    // Save a new mask value
    const newMask = inst.substr(7);
    if (newMask.length !== 36) {
      console.log(`Invalid mask instruction: ${inst}`);
    } else {
      this.bitmask = newMask;
    }
  }

  saveMem(inst: string) {
    // Save a masked value at a single place in memory

    // 1. Parse the instruction line
    const found = inst.match(RE_MEM);
    if (found === null) {
      console.log(`Bad mem instruction: ${inst}`);
      return;
    }
    const loc = parseInt(found[1], 10);
    const value = parseInt(found[2], 10);

    // 2. If part2, things get wierd
    if (this.part2) {
      const maskedLoc = this.applyMaskToLocation(loc);
      this.saveMultiLocations(maskedLoc, value);
      return;
    }

    // 3. Get the masked value
    const masked = this.applyMaskToValue(value);

    // 4. Save the value in the specified location
    this.memory[loc] = masked;
  }

  applyMaskToValue(value: number): number {
    // Return the value with the mask applied

    // 1. Get the value as 36 character bits
    const value36 = value.toString(2).padStart(36, '0');

    // 2. Apply the mask
    const bits: string[] = [];
    for (let indx = 0; indx < 36; indx += 1) {
      const mask = this.bitmask.substr(indx, 1);
      const bit = value36.substr(indx, 1);
      switch (mask) {
        case '0':
          bits.push('0');
          break;
        case '1':
          bits.push('1');
          break;
        case 'X':
          bits.push(bit);
          break;
        default:
          console.log(`Unexpected value ${mask} in mask ${this.bitmask}`);
      }
    }

    // 3. Return the masked value as an integer
    const maskedBits = bits.join('');
    return parseInt(maskedBits, 2);
  }

  applyMaskToLocation(loc: number): string {
    // Return the location with the mask applied

    // 1. Get the value as 36 character bits
    const loc36 = loc.toString(2).padStart(36, '0');

    // 2. Apply the mask
    const bits: string[] = [];
    for (let indx = 0; indx < 36; indx += 1) {
      const mask = this.bitmask.substr(indx, 1);
      const bit = loc36.substr(indx, 1);
      switch (mask) {
        case '0':
          bits.push(bit);
          break;
        case '1':
          bits.push(mask);
          break;
        case 'X':
          bits.push(mask);
          break;
        default:
          console.log(`Unexpected value ${mask} in mask ${this.bitmask}`);
      }
    }

    // 3. Return the masked location as an integer
    return bits.join('');
  }

  saveMultiLocations(maskedLoc: string, value: number) {
    // Save the value to multiple locations

    // 1. Locate the first floating bit in the masked location
    const firstX = maskedLoc.indexOf('X');

    // 2. If there aren't any, save the value at the location
    if (firstX === -1) {
      const loc = parseInt(maskedLoc, 2);
      this.memory[loc] = value;
      return;
    }

    // 3. Replace the floating bit with a 0 and with a 1
    const mask0 = maskedLoc.replace('X', '0');
    const mask1 = maskedLoc.replace('X', '1');

    // 4. Save the value at those two locations (which may further expand)
    this.saveMultiLocations(mask0, value);
    this.saveMultiLocations(mask1, value);
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.execute();
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
// end                       b i t m a s k . t s                      end
// ======================================================================
