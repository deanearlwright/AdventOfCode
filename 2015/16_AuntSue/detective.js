/* eslint-disable linebreak-style */
// ======================================================================
// Aunt Detective
//   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                       d e t e c t i v e . j s
//
// A solver for the Advent of Code 2015 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const mfcsam = require('./mfcsam');
const sue = require('./sue');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const TT0 = 'children: 3';
const TT1 = 'cats: 7';
const TT2 = 'samoyeds: 2';
const TT3 = 'pomeranians: 3';
const TT4 = 'akitas: 0';
const TT5 = 'vizslas: 0';
const TT6 = 'goldfish: 5';
const TT7 = 'trees: 3';
const TT8 = 'cars: 2';
const TT9 = 'perfumes: 1';
const TICKER_TAPE = [TT0, TT1, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9];

// ======================================================================
//                                                              Detective
// ======================================================================

class Detective {
  // Object for Detective using MFCSAM to determine which Sue

  constructor(options) {
    // Create a Detective object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.CSI = new mfcsam.Mfcsam({ text: TICKER_TAPE });
    this.aunts = [];
    this.number = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    text.forEach((line) => {
      const aunt = new sue.Sue({ text: line });
      this.aunts.push(aunt);
      this.number += 1;
    });
  }

  checkAunt(aunt) {
    // 1. Assume aunt will match
    let include = true;
    // eslint-disable-next-line no-console
    console.log(aunt);
    // 2. Loop for each of the aunt's attribute
    Object.keys(aunt.attributes).forEach((k) => {
      // 3. If not a good match, don't retirm false
      if (this.part2) {
        if (!aunt.checkRetroencabulatorAttribute(k, this.CSI.compounds[k])) {
          include = false;
        }
      } else if (!aunt.checkAttribute(k, this.CSI.compounds[k])) {
        include = false;
      }
    });
    // 4. Return true only if aunt matches all attributes
    return include;
  }

  whichAunts() {
    // 1. If there are no aunts, there is no result
    if (!this.aunts) {
      return null;
    }
    // 2. Start with no aunts matching
    const result = [];
    // 3. Loop for all the aunts
    this.aunts.forEach((aunt) => {
      const matches = this.checkAunt(aunt);
      if (matches) {
        result.push(aunt);
      }
    });
    if (result.length === 0) {
      return null;
    }
    return result;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    const who = this.whichAunts();
    if (!who) {
      return null;
    }
    if (who.length > 1) {
      // eslint-disable-next-line no-console
      console.log('Found %d aunts', who.length);
      return null;
    }
    return who[0].number;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    const who = this.whichAunts();
    if (!who) {
      return null;
    }
    if (who.length > 1) {
      // eslint-disable-next-line no-console
      console.log('Found %d aunts', who.length);
      return null;
    }
    return who[0].number;
  }
}

module.exports.Detective = Detective;
// ======================================================================
// end                    d e t e c t i v e . j s                     end
// ======================================================================
