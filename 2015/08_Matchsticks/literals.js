/* eslint-disable linebreak-style */
// ======================================================================
// Matchsticks
//   Advent of Code 2015 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           l i t e r a l s . j s
//
// A solver for the Advent of Code 2015 Day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Literals
// ======================================================================

class Literals {
  // Object for Matchsticks

  constructor(options) {
    // Create a Literals object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.kntCode = null;
    this.kntChar = null;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.kntText();
    }
  }

  getLengths(text) {
    if (!this.part2) {
      if (text.indexOf('\\') === -1) {
        return [text.length, text.length - 2];
      }
      const pattern = new RegExp('(\\\\"|\\\\x[0-9a-f][0-9a-f]|\\\\\\\\)', 'g');
      const newtext = text.replace(pattern, '*');
      return [text.length, newtext.length - 2];
    }
    if (text.indexOf('\\') === -1) {
      return [text.length, text.length + 4];
    }
    const pattern = new RegExp('(\\\\"|\\\\x[0-9a-f]|\\\\\\\\)', 'g');
    const newtext = text.replace(pattern, '****');
    return [text.length, newtext.length + 4];
  }

  kntText() {
    this.kntCode = 0;
    this.kntChar = 0;
    this.text.forEach((line) => {
      const [xcode, xchar] = this.getLengths(line);
      this.kntCode += xcode;
      this.kntChar += xchar;
    });
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    this.todo = 'TODO';

    // 1. Return the solution for part one
    return this.kntCode === null ? null : this.kntCode - this.kntChar;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.kntCode === null ? null : this.kntChar - this.kntCode;
  }
}

module.exports.Literals = Literals;
// ======================================================================
// end                      l i t e r a l s . j s                     end
// ======================================================================
