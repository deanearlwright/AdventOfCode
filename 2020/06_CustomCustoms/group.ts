// ======================================================================
// Custom Customs
//   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           g r o u p . t s
//
// Group for the Advent of Code 2020 Day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Answers = Record<string, boolean>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_ANSWERS = /[a-z]+/g;

// ======================================================================
//                                                                  Group
// ======================================================================

export class Group {
  // Object for Custom Customs
  text: string;

  part2: boolean;

  answers: Answers;

  constructor(text: string, part2 = false) {
    // Create a Group object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.answers = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
      if (this.part2) {
        this.fixupForAll();
      }
    }
  }

  processText() {
    // Ppopulate the questions from the text

    // 1. Loop for each person in the group
    const matches = Array.from(this.text.matchAll(RE_ANSWERS));
    for (let match = 0; match < matches.length; match += 1) {
      const answers = matches[match][0];

      // 2. Loop for all the person's answers
      for (let indx = 0; indx < answers.length; indx += 1) {
        const answer = answers[indx];

        // 3. Add record the yes answer
        this.answers[answer] = true;
      }
    }
  }

  yes(): number {
    // Return the number of combined yes answers
    return Object.keys(this.answers).length;
  }

  fixupForAll() {
    // Eliminate the answers that are not unanimous

    // 1. Loop for all of the answers
    const keys = Object.keys(this.answers);
    for (let indx = 0; indx < keys.length; indx += 1) {
      const question = keys[indx];
      let everyone = true;

      // 2. Loop for each person's answers
      const matches = Array.from(this.text.matchAll(RE_ANSWERS));
      for (let match = 0; match < matches.length; match += 1) {
        const answers = matches[match][0];

        // 3. If this person didn't say yes to the question, remember it
        if (answers.indexOf(question) === -1) {
          everyone = false;
        }
      }

      // 4. If not everyone answered yes, remove the answer
      if (!everyone) {
        delete this.answers[question];
      }
    }
  }
}

// ======================================================================
// end                      g r o u p . t s                     end
// ======================================================================
