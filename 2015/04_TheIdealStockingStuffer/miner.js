/* eslint-disable linebreak-style */
// ======================================================================
// The Ideal Stocking Stuffer
//   Advent of Code 2015 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           m i n e r . j s
//
// A solver for the Advent of Code 2015 Day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const md5 = require('md5');
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Miner
// ======================================================================

class Miner {
  // Object for The Ideal Stocking Stuffer

  constructor(options) {
    // Create a Miner object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.base = '';

    // 2. Process text (if any)
    if (this.text !== null) {
      [this.base] = this.text;
    }
  }

  generateHash(number) {
    // 1. Construct a message from the base and the number
    const message = this.base + number;
    // 2. Return a has of the message
    return md5(message);
  }

  findAdventCoin() {
    // 1. Generate the required prefix
    const prefix = '0'.repeat(this.part2 ? 6 : 5);
    // 2. Loop until we find the number that has the prefix
    let number = 1;
    for (; ; number += 1) {
      // 3. Create a hash using this number
      const hash = this.generateHash(number);
      // 4. Is this the one we have been looking for?
      if (hash.startsWith(prefix)) {
        break;
      }
    }
    // 5. Return the magic number
    return number;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the number of the generated coin
    return this.findAdventCoin();
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the number of the generated coin
    return this.findAdventCoin();
  }
}

module.exports.Miner = Miner;
// ======================================================================
// end                         m i n e r . j s                        end
// ======================================================================
