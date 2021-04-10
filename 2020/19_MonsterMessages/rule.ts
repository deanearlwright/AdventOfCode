// ======================================================================
// Monster Messages
//   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r u l e . t s
//
// Rule for the Advent of Code 2020 Day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_RULE = /^([0-9]+): ([0-9a-z"| ]+)$/;

// ======================================================================
//                                                                   Rule
// ======================================================================

export class Rule {
  // Object for Monster Messages
  text: string;

  part2: boolean;

  number: number;

  definition: string;

  constructor(text: string, part2 = false) {
    // Create a Rule object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.number = 0;
    this.definition = '';

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string) {
    // Assign values from text

    // 1. Match the text against the regex
    const match = text.match(RE_RULE);
    if (match === null) {
      console.log(`Malformed rule (${text})`);
    } else {
      // 2. Save the rule number and definition
      const [, num, def] = match;
      this.number = parseInt(num, 10);
      this.definition = def;
    }
  }

  isConstant(): boolean {
    // Return true if the rule is for a constant
    return this.definition.startsWith('"');
  }

  letter(): string {
    // Return the letter for a constant rule
    if (this.isConstant()) {
      return this.definition[1];
    }
    return '';
  }

  alternatives(): string[] {
    // Return the subrules of the rule

    // 1. Constants have no alternatives
    if (this.isConstant()) {
      return [];
    }

    // 2. Return the whole definition if there are no alternatives
    if (this.definition.indexOf('|') === -1) {
      return [this.definition];
    }

    // 3. Return the alternatives
    return this.definition.split(' | ');
  }
}

// ======================================================================
// end                          r u l e . t s                         end
// ======================================================================
