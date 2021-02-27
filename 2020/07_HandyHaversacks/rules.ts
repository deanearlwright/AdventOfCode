// ======================================================================
// Handy Haversacks
//   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r u l e s . t s
//
// A solver for the Advent of Code 2020 Day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Rule } from './rule';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type RuleRecord = Record<string, Rule>;
type Bags = Record<string, string>;
type Known = Record<string, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const THE_BAG = 'shiny gold';

// ======================================================================
//                                                                  Rules
// ======================================================================

export class Rules {
  // Object for Handy Haversacks
  text: string[];

  part2: boolean;

  rules: RuleRecord;

  known: Known;

  constructor(text: string[], part2 = false) {
    // Create a Rules object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rules = {};
    this.known = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      for (let indx = 0; indx < this.text.length; indx += 1) {
        const rule = new Rule(this.text[indx], this.part2);
        this.rules[rule.bag] = rule;
      }
    }
  }

  can_hold(color: string): Bags {
    // Returns the bags that can hold the specified color
    // 1. Start with nothing
    const bags: Bags = {};

    // 2. Loop for every rule
    const keys = Object.keys(this.rules);
    for (let indx = 0; indx < keys.length; indx += 1) {
      const key = keys[indx];
      const rul = this.rules[key];

      // 3. If the rule can contain a bag of the specified color, add it
      if (rul.contains(color) > 0) {
        bags[key] = color;
      }
    }

    // 4. Return the bags that can hold the specified color
    return bags;
  }

  can_contain(color: string): number {
    // Return number of bags that can contain the specified colored bag

    // 1. Start with the bags that can directly contain the colored bag
    const bags = this.can_hold(color);

    // 2. Expand that list until it doesn't get any larger
    let previous = 0;
    let howMany = Object.keys(bags).length;
    while (previous !== howMany) {
      // 3. Loop for all of the current bags
      const keys = Object.keys(bags);
      for (let indx = 0; indx < keys.length; indx += 1) {
        const want = keys[indx];

        // 4. Find the bags that can hold this one
        const more = this.can_hold(want);

        // 5. Add them to the bags we have
        const mkeys = Object.keys(more);
        for (let mindx = 0; mindx < mkeys.length; mindx += 1) {
          const mkey = mkeys[mindx];
          bags[mkey] = want;
        }
      }
      // 6. Update counts
      previous = howMany;
      howMany = Object.keys(bags).length;
    }
    return howMany;
  }

  required_inside(color: string): number {
    // Return how many bags are required within the specified bag

    // 1. If we already know the answer, just return it
    if (this.known[color] === null) {
      return this.known[color];
    }

    // 2. If there is no rule for this color, return 0
    if (this.rules[color] === null) {
      this.known[color] = 0;
      return 0;
    }

    // 3. If this color bag contains no other, return 0
    if (this.rules[color].inside() === 0) {
      return 0;
    }

    // 4. Otherwise accumulate the number of needed bags
    let result = 0;

    // 5. Loop for all of the inner bags
    const { bags } = this.rules[color];
    const colors = Object.keys(bags);
    for (let indx = 0; indx < colors.length; indx += 1) {
      const icolor = colors[indx];
      const inumber = bags[icolor];

      // 6. Add in the number of bags of this color
      result = result + inumber + inumber * this.required_inside(icolor);
    }

    // 7. Remember the number of bags needed for this color
    this.known[color] = result;

    // 8. Return the number of bags requires within the specified bag
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.required_inside(THE_BAG);
    }
    return this.can_contain(THE_BAG);
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      r u l e s . t s                     end
// ======================================================================
