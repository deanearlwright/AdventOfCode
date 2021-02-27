// ======================================================================
// Handy Haversacks
//   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r u l e . t s
//
// Rule for the Advent of Code 2020 Day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type BagRecord = Record<string, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_MATCH = /^([a-z ]+) bags contain ([0-9a-z, ]+).$/;
const RE_BAG = /([0-9]+) ([a-z ]+) bag/g;

// ======================================================================
//                                                                   Rule
// ======================================================================

export class Rule {
  // Object for Handy Haversacks
  text: string;

  part2: boolean;

  bag: string;

  bags: BagRecord;

  constructor(text: string, part2 = false) {
    // Create a Rule object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.bag = '';
    this.bags = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText() {
    // Use regular expressions to split up the input text

    // 1. Break up the text into the parts before and after "contains"
    const matched = this.text.match(RE_MATCH);
    if (!matched) {
      console.log(`Unable to parse: ${this.text}`);
      return;
    }
    // eslint-disable-next-line prefer-destructuring
    this.bag = matched[1];
    const bags = matched[2];

    // 2. Loop for the containing bags
    const matches = Array.from(bags.matchAll(RE_BAG));
    for (let match = 0; match < matches.length; match += 1) {
      const bagNumber = matches[match][1];
      const bagColor = matches[match][2];

      // 3. Save the interier bag
      this.bags[bagColor] = parseInt(bagNumber, 10);
    }
  }

  contains(color: string): number {
    // Return the number of bags of that color that the bag contains
    if (this.bags[color]) {
      return this.bags[color];
    }
    return 0;
  }

  inside(): number {
    // Return the number of bags inside this bag
    // 1. Start with nothing
    let result = 0;
    // 2. Loop for all of the bags
    const values = Object.values(this.bags);
    for (let indx = 0; indx < values.length; indx += 1) {
      // 3. Add in the number of bags
      result += values[indx];
    }
    // 4. Return the number of bags inside this bag
    return result;
  }
}

// ======================================================================
// end                          r u l e . t s                         end
// ======================================================================
