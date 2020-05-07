/* eslint-disable linebreak-style */
// ======================================================================
// Aunt Sue
//   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s u e . j s
//
// A solver for the Advent of Code 2015 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                    Sue
// ======================================================================

class Sue {
  // Object for Aunt Sue

  constructor(options) {
    // Create a Sue object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.number = null;
    this.attributes = {};

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Regular Expression parser for single tickertape line
    const pattern = /Sue ([0-9]+): ([a-z0-9:, ]+)+/;

    // 2. Decompose input line
    const match = text.match(pattern);
    if (match) {
      this.number = parseInt(match[1], 10);
      // 3. Loop for all of the attributes given
      const csv = match[2].split(',');
      for (let i = 0; i < csv.length; i += 1) {
        const parts = csv[i].split(':');
        const name = parts[0].trim();
        const amount = parseInt(parts[1], 10);
        // 4. Add the attribute
        this.attributes[name] = amount;
      }
    } else {
      // eslint-disable-next-line no-console
      console.log('Unable to parse input "%s"', text);
    }
  }

  checkAttribute(attribute, number) {
    // 1. Return true if it has the right number or "can't remember"
    if (attribute in this.attributes) {
      return number === this.attributes[attribute];
    }
    return true;
  }

  checkRetroencabulatorAttribute(attribute, number) {
    // 1. Return true if it has the right number or "can't remember"
    if (attribute in this.attributes) {
      // 2. But the right number is dependent on the attribute
      switch (attribute) {
        case 'cats':
        case 'trees':
          return number < this.attributes[attribute];
        case 'pomeranians':
        case 'goldfish':
          return number > this.attributes[attribute];
        default:
          return number === this.attributes[attribute];
      }
    }
    return true;
  }
}

module.exports.Sue = Sue;
// ======================================================================
// end                          s u e . j s                           end
// ======================================================================
