/* eslint-disable linebreak-style */
// ======================================================================
// Aunt Sue
//   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           m f c s a m . j s
//
// A CSI machine for the Advent of Code 2015 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Mfcsam
// ======================================================================

class Mfcsam {
  // Object for My First Crime Scene Analysis Machine

  constructor(options) {
    // Create a Mfcsam object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.compounds = {};

    // 2. Process text (if any)
    if (this.text !== null) {
      this.text.forEach((line) => this.processText(line));
    }
  }

  processText(text) {
    // 1. Regular Expression parser for single tickertape line
    const pattern = /([a-z]+): ([0-9]+)/;

    // 2. Decompose input line
    const match = text.match(pattern);
    if (match) {
      const name = match[1];
      const amount = parseInt(match[2], 10);

      // 3. Add to compounds list
      this.compounds[name] = amount;
    } else {
      // eslint-disable-next-line no-console
      console.log('Unable to parse input "%s"', text);
    }
  }
}

module.exports.Mfcsam = Mfcsam;
// ======================================================================
// end                        m f c s a m . j s                       end
// ======================================================================
