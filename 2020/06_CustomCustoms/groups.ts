// ======================================================================
// Custom Customs
//   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           g r o u p s . t s
//
// A solver for the Advent of Code 2020 Day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Group } from './group';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Groups
// ======================================================================

export class Groups {
  // Object for Custom Customs
  text: string[];

  part2: boolean;

  groups: Group[];

  constructor(text: string[], part2 = false) {
    // Create a Groups object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.groups = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText() {
    // Create groups from the input text

    // 1. Start with no answers for the group
    let answers = '';

    // 2. Loop for each line of the text
    for (let indx = 0; indx < this.text.length; indx += 1) {
      const line = this.text[indx];

      // 3. If this is a blank line, save the collected answers (if any)
      if (line.length === 0) {
        if (answers.length > 0) {
          this.groups.push(new Group(answers, this.part2));
          answers = '';
        }
      } else {
        // 4. For non-blank lines, accumulate answers
        answers = `${answers},${line}`;
      }
    }

    // 5. Add any final answers
    if (answers.length > 0) {
      this.groups.push(new Group(answers, this.part2));
    }
  }

  yes(): number {
    // Return the sum of yes answers

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all the groups
    for (let indx = 0; indx < this.groups.length; indx += 1) {
      const group = this.groups[indx];
      // 3. Add in the number of yes answers from this group
      result += group.yes();
    }

    // 4. Return the sum of yes answers
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.yes();
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
// end                        g r o u p s . t s                       end
// ======================================================================
