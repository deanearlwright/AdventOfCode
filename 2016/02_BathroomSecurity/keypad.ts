// ======================================================================
// Bathroom Security
//   Advent of Code 2016 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           k e y p a d . t s
//
// A solver for the Advent of Code 2016 Day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type matrixType = Array<Array<string>>

interface locationType {
  row: number
  col: number
}

type deltaType = Record<string, locationType>

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const keypadOne: matrixType = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9'],
];

const keypadTwo: matrixType = [
  ['.', '.', '1', '.', '.'],
  ['.', '2', '3', '4', '.'],
  ['5', '6', '7', '8', '9'],
  ['.', 'A', 'B', 'C', '.'],
  ['.', '.', 'D', '.', '.'],
];

const movement: deltaType = {
  U: { row: -1, col: 0 },
  D: { row: 1, col: 0 },
  L: { row: 0, col: -1 },
  R: { row: 0, col: 1 },
};

// ======================================================================
//                                                                 Keypad
// ======================================================================

export class Keypad {
  // Object for Bathroom Security
  text: string[];

  part2: boolean;

  keypad: matrixType;

  start: locationType;

  constructor(text: string[], part2 = false) {
    // Create a Keypad object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;

    // 2. Keypad and start
    this.keypad = this.part2 ? keypadTwo : keypadOne;
    this.start = this.part2 ? { row: 2, col: 0 } : { row: 1, col: 1 };
  }

  solution(verbose = false, limit = 0): string {
    if (verbose) console.log(`solution: limit ${limit}`);
    if (this.part2) {
      return '';
    }
    return '';
  }

  static newLoc(location: locationType, delta: locationType): locationType {
    return { row: location.row + delta.row, col: location.col + delta.col };
  }

  onPad(location: locationType): boolean {
    // Return true if the location is on the keypad
    if (location.row < 0 || location.row >= this.keypad.length) return false;
    if (location.col < 0 || location.col >= this.keypad[location.row].length) return false;
    if (this.keypad[location.row][location.col] === '.') return false;
    return true;
  }

  determineCode(verbose = false, limit = 0): string {
    if (verbose) console.log(`determineCode: limit ${limit}`);
    // 1. Start with no code at the center of the keypad
    let loc: locationType = this.start;
    let result = '';
    this.text.forEach((line) => {
      line.split('').forEach((dir) => {
        const delta = movement[dir];
        const nextLoc = Keypad.newLoc(loc, delta);
        if (this.onPad(nextLoc)) loc = nextLoc;
        if (verbose) console.log(`${line} ${dir} ${loc.row} ${loc.col}`);
      });
      result += this.keypad[loc.row][loc.col];
      if (verbose) console.log(`${line} ${result}`);
    });
    return result;
  }

  partOne(verbose = false, limit = 0): string {
    // Returns the solution for part one

    return this.determineCode(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.determineCode(verbose, limit);
  }
}

// ======================================================================
// end                      k e y p a d . t s                         end
// ======================================================================
