// ======================================================================
// Security Through Obscurity
//   Advent of Code 2016 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           e n c r y p t e d . t s
//
// A solver for the Advent of Code 2016 Day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type roomType = {
  text: string
  sector: number
  checksum: string
  decoy: boolean
  plain: string
}

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';
const ALPHABET2 = ALPHABET + ALPHABET;

// ======================================================================
//                                                              Encrypted
// ======================================================================

export class Encrypted {
  // Object for Security Through Obscurity
  text: string[];

  part2: boolean;

  rooms: roomType[];

  constructor(text: string[], part2 = false) {
    // Create a Encrypted object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rooms = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.rooms = [];
    const re = /^([a-z-]+)-([0-9]+)\[([a-z][a-z][a-z][a-z][a-z])]$/;
    // 2. Loop for all the lines in the text
    this.text.forEach((line) => {
      const parts = line.match(re);
      if (parts === null) {
        console.log(`Invalid format for ${line}`);
      } else {
        const room = {
          text: parts[1],
          sector: parseInt(parts[2], 10),
          checksum: parts[3],
          decoy: Encrypted.isDecoy(parts[1], parts[3]),
          plain: '',
        };
        this.rooms.push(room);
      }
    });
  }

  static isDecoy(text: string, checksum: string): boolean {
    return checksum !== Encrypted.computeChecksum(text);
  }

  static computeChecksum(text: string): string {
    // 1. Get the count for each letter in the string
    const counts: Map<string, number> = new Map();
    text.split('').forEach((letter) => {
      if (letter !== '-') {
        const value = counts.get(letter) || 0;
        counts.set(letter, value + 1);
      }
    });
    // 2. Start with nothing in the result
    let result = '';
    // 3. Loop from highest number of occurances to lowest
    for (let occurances = text.length; occurances > 0; occurances -= 1) {
      // 4. Get the letters with number of occurances
      let letters = '';
      counts.forEach((value, key) => {
        if (value === occurances) letters += key;
      });
      if (letters.length > 0) {
        const sorted = letters.split('').sort().join('');
        result += sorted;
        // console.log(`Loop: ${text} ${occurances} ${letters} ${sorted} ${result}`);
        if (result.length >= 5) break;
      }
    }
    if (result.length > 5) result = result.substring(0, 5);
    // console.log(`Result ${text} ${result}`);
    return result.padEnd(5, '?');
  }

  sumIfReal(verbose = false, limit = 0): number {
    if (verbose) console.log(`sumIfReal: ${limit}`);
    // 1. Start with nothing
    let result = 0;
    // 2. Loop for all the rooms
    this.rooms.forEach((room) => {
      // 3. Add the sector IDs if a the real rooms
      if (!room.decoy) result += room.sector;
    });
    // 4. Return the sum of the sectors of the real rooms
    return result;
  }

  static decrypt(room: roomType): string {
    // 1. Determine the rotate amount
    const shift = room.sector % 26;
    // 2. Start with nothing
    let result = '';
    // 3. Loop for every letter in the encrypted text
    room.text.split('').forEach((letter) => {
      // 4. Decrypt the letter
      if (letter === '-') {
        result += ' ';
      } else {
        result += ALPHABET2[shift + ALPHABET.indexOf(letter)];
      }
    });
    // 5. Return the plain text
    return result;
  }

  decryptIfReal(verbose = false, limit = 0): void {
    if (verbose) console.log(`decryptIfReal: ${limit}`);
    // 1. Loop for all the rooms
    for (let index = 0; index < this.rooms.length; index += 1) {
      // 2. Decrypt if it is a real rooms
      if (!this.rooms[index].decoy) {
        this.rooms[index].plain = Encrypted.decrypt(this.rooms[index]);
        if (verbose) console.log(`${this.rooms[index].plain}`);
      }
    }
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return NaN;
  }

  findNorthPoleObject(verbose = false, limit = 0): number {
    if (verbose) console.log(`findNorthPoleObject: ${limit}`);
    // 1. Assume the worst
    let result = NaN;
    // 2. What to look for
    const re = /(north|pole|object|star|santa)/;
    // 3. Loop for all of the rooms
    this.rooms.forEach((room) => {
      // 4. Check if this is the one
      if (re.test(room.plain)) {
        if (verbose) console.log(`Likely Match: ${room.plain} ${room.sector} ${room.text}`);
        result = room.sector;
      }
    });
    // 5. Return the sector number if found
    return result;
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.sumIfReal(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    this.decryptIfReal(false, limit);
    return this.findNorthPoleObject(verbose, limit);
  }
}

// ======================================================================
// end                      e n c r y p t e d . t s                   end
// ======================================================================
