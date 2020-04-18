/* eslint-disable linebreak-style */
// ======================================================================
// JSAbacusFramework.io
//   Advent of Code 2015 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           n u m b e r s . j s
//
// A solver for the Advent of Code 2015 Day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Numbers
// ======================================================================

class Numbers {
  // Object for JSAbacusFramework.io

  constructor(options) {
    // Create a Numbers object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.json = '';

    // 2. Process text (if any)
    if (this.text !== null) {
      [this.json] = this.text;
    }
  }

  static sum(json) {
    const re = /(-?[0-9]+)/g;
    const matches = json.match(re);
    const reducer = (acc, cur) => Number(acc) + Number(cur);
    if (matches === null) {
      return 0;
    }
    return Number(matches.reduce(reducer));
  }

  static nored(json) {
    const re = /:"red"/;
    let result = json.slice(0);
    let red = result.search(re);
    while (red !== -1) {
      const leftBrace = Numbers.findLeftBrace(result, red);
      const rightBrace = Numbers.findRightBrace(result, red);
      result = result.substring(0, leftBrace) + result.substring(rightBrace + 1);
      red = result.search(re);
    }
    return result;
  }

  static findLeftBrace(result, red) {
    let braceCount = 0;
    for (let i = red; i >= 0; i -= 1) {
      switch (result.charAt(i)) {
        case '{':
          if (braceCount === 0) {
            return i;
          }
          braceCount -= 1;
          break;
        case '}':
          braceCount += 1;
          break;
        default:
          /* Empty */
      }
    }
    return 0;
  }

  static findRightBrace(result, red) {
    let braceCount = 0;
    for (let i = red; i < result.length; i += 1) {
      switch (result.charAt(i)) {
        case '}':
          if (braceCount === 0) {
            return i;
          }
          braceCount -= 1;
          break;
        case '{':
          braceCount += 1;
          break;
        default:
          /* Empty */
      }
    }
    return result.length;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return Numbers.sum(this.json);
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    this.todo = 'TODO';

    // 1. Return the solution for part two
    return Numbers.sum(Numbers.nored(this.json));
  }
}

module.exports.Numbers = Numbers;
// ======================================================================
// end                       n u m b e r s . j s                      end
// ======================================================================
