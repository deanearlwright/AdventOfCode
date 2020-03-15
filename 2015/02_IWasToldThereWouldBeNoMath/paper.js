/* eslint-disable linebreak-style */
// ======================================================================
// I Was Told There Would Be No Math
//   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a p e r . j s
//
// A solver for the Advent of Code 2015 Day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Paper
// ======================================================================

class Paper {
  // Object for I Was Told There Would Be No Math

  constructor(options) {
    // Create a Paper object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.wrapping = 0;
    this.ribbon = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText();
    }
  }

  static calculateWrapping(present) {
    // Calculate the amount of wrapping paper needed for this present

    // 1. Break the present description into sides
    const [l, w, h] = present.split('x');

    // 2. Determine the paper to cover the box
    const box = 2 * l * w + 2 * w * h + 2 * h * l;

    // 3. Determine the smallest side
    const side = Math.min(l * w, w * h, h * l);

    // 4. Return the paper needed plus the slack
    return box + side;
  }

  static calculateRibbon(present) {
    // Calculate the length of ribbon paper needed for this present

    // 1. Break the present description into sides
    const [l, w, h] = present.split('x');

    // 2. Determine the ribbon to wrap the box
    const box = 2 * (Number(l) + Number(w) + Number(h) - Math.max(l, w, h));

    // 3. Determine the amount necessary for the bow
    const bow = l * w * h;

    // 4. Return the ribbon needed for this present
    return box + bow;
  }

  processText() {
    // Process all of the present sizes

    // 1. Loop for all of the presents
    this.text.forEach((present) => {
      // 2. Accumulate the abount of paper for this present
      this.wrapping += Paper.calculateWrapping(present);

      // 3. Accumulate the amount of ribbon for this present
      this.ribbon += Paper.calculateRibbon(present);
    });
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.wrapping;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.ribbon;
  }
}

module.exports.Paper = Paper;
// ======================================================================
// end                         p a p e r . j s                        end
// ======================================================================
