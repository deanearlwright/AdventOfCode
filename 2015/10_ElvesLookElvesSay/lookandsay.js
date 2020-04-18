/* eslint-disable linebreak-style */
// ======================================================================
// Elves Look Elves Say
//   Advent of Code 2015 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                      l o o k a n d s a y . j s
//
// A solver for the Advent of Code 2015 Day 10 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                             Lookandsay
// ======================================================================

class Lookandsay {
  // Object for Elves Look Elves Say

  constructor(options) {
    // Create a Lookandsay object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.phrase = '';
    this.count = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      [this.phrase] = this.text;
    }
  }

  nextPhrase() {
    if (this.phrase) {
      let nextPhrase = '';
      let lastChar = null;
      let count = 0;
      for (let i = 0; i < this.phrase.length; i += 1) {
        const c = this.phrase.charAt(i);
        if (c !== lastChar) {
          if (lastChar && count) {
            nextPhrase += count + lastChar;
          }
          lastChar = c;
          count = 1;
        } else {
          count += 1;
        }
      }
      if (lastChar && count) {
        nextPhrase += count + lastChar;
      }
      this.phrase = nextPhrase;
    }
    this.count += 1;
    return this.phrase;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Generate lots of phrases
    while (this.count < 40) {
      this.nextPhrase();
    }
    // 2. Return the solution for part one
    return this.phrase.length;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    // 1. Generate lots of phrases
    while (this.count < 50) {
      this.nextPhrase();
    }
    // 2. Return the solution for part two
    return this.phrase.length;
  }
}

module.exports.Lookandsay = Lookandsay;
// ======================================================================
// end                    l o o k a n d s a y . j s                   end
// ======================================================================
