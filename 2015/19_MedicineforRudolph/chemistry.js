/* eslint-disable linebreak-style */
// ======================================================================
// Medicine for Rudolph
//   Advent of Code 2015 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           c h e m i s t r y . j s
//
// A solver for the Advent of Code 2015 Day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                              Chemistry
// ======================================================================

class Chemistry {
  // Object for Medicine for Rudolph

  constructor(options) {
    // Create a Chemistry object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.replacements = {};
    this.molecule = '';
    this.kntRep = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.replacements = {};
    this.molecule = '';
    this.kntRep = 0;
    const pattern = /([A-Za-z]+) => ([A-Za-z]+)/;

    // 2. Loop for each line of the input
    text.forEach((line) => {
      // 3. Decompose input line into cities and distance
      const match = line.match(pattern);
      if (match) {
        const before = match[1];
        const after = match[2];

        // 4. Add to replacements dictionary
        if (!(before in this.replacements)) {
          this.replacements[before] = [];
          this.kntRep += 1;
        }
        this.replacements[before].push(after);
      } else if (this.molecule === '') {
        this.molecule = line;
      } else {
        // eslint-disable-next-line no-console
        console.log('Unable to parse input', line);
      }
    });
  }

  oneOff(start) {
    // 1. Start with nothing
    const molecules = {};
    // 2. Loop for all of the the replacements
    Object.keys(this.replacements).forEach((key) => {
      // 3. Loop for all of the places this replacement is in the molecule
      let index = start.indexOf(key);
      while (index >= 0) {
        // 4. Split the sting here
        const before = start.substring(0, index);
        const after = start.substring(index + key.length);
        // eslint-disable-next-line no-console
        // console.log(`${this.molecule}:${index}=${before}-${key}-${after}`);
        // 5. Loop for all of the replacement values
        const replacements = this.replacements[key];
        replacements.forEach((changeTo) => {
          // 6. Remember this new(ish) molecule
          const newMolecule = `${before}${changeTo}${after}`;
          molecules[newMolecule] = true;
        });
        // 7. Advence to the next place the key is found
        index = start.indexOf(key, index + 1);
      }
    });
    // 8. Return the different molecules created
    return molecules;
  }

  severalOff(starts) {
    // 1. Start with nothing
    const result = {};
    // 2. Loop for the starting molecules
    Object.keys(starts).forEach((start) => {
      // 3. Determine the molecules that this one can make
      const nextGen = this.oneOff(start);
      // 4. Add all of these new molecules to the result
      Object.keys(nextGen).forEach((nextOne) => {
        result[nextOne] = true;
      });
    });
    // 5. Return the all of the different new molecules created
    return result;
  }

  calibrate() {
    return Object.keys(this.oneOff(this.molecule)).length;
  }

  prune(molecules) {
    // 1. Start with nothing
    const result = {};
    const len = this.molecule.length;
    // 2. Loop for all the molecules;
    Object.keys(molecules).forEach((one) => {
      // 3. Keep only the ones less than or the same length as the goal
      if (one.length <= len) {
        result[one] = true;
      }
    });
    // 4. Return the right sized molecules
    return result;
  }

  medicine() {
    // 1. Start with just e
    let molecules = { e: true };
    let steps = 0;
    // 2. Loop until we get to the medicine
    while (molecules[this.molecule] === undefined) {
      // 3. Expand the existing molecules
      molecules = this.severalOff(molecules);
      // 4. Eliminate molecules that have grown too large
      molecules = this.prune(molecules);
      // 5. Increment the number of steps
      steps += 1;
    }
    // 5. Return the number of steps needed to make the medicine
    return steps;
  }

  tokens() {
    // 2. Get counts of terminals
    //    If we were going with a general solution (which we are not)
    //    then we should be determine the terminals by checking the grammar.
    const kntRn = (this.molecule.match(/Rn/g) || []).length;
    const kntAr = (this.molecule.match(/Ar/g) || []).length;
    const kntY = (this.molecule.match(/Y/g) || []).length;
    // 2. Get count of tokens in the string
    const kntTokens = (this.molecule.match(/[A-Z]/g) || []).length;
    // 3. Return the token counts
    return {
      Rn: kntRn,
      Ar: kntAr,
      Y: kntY,
      tokens: kntTokens,
    };
  }

  medicine2() {
    const counts = this.tokens();
    return counts.tokens - (counts.Rn + counts.Ar + counts.Y + counts.Y + 1);
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.calibrate();
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.medicine2();
  }
}

module.exports.Chemistry = Chemistry;
// ======================================================================
// end                     c h e m i s t r y . j s                    end
// ======================================================================
