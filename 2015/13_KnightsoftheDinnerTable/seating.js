/* eslint-disable linebreak-style */
// ======================================================================
// Knights of the Dinner Table
//   Advent of Code 2015 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s e a t i n g . j s
//
// A solver for the Advent of Code 2015 Day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Seating
// ======================================================================

class Seating {
  // Object for Knights of the Dinner Table

  constructor(options) {
    // Create a Seating object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.attendees = {};
    this.number = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }

    // 3. For part2, the host is included
    if (this.part2) {
      this.number += 1;
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.attendees = {};
    this.number = 0;
    const pattern = /([A-Z][A-Za-z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([A-Z][A-Za-z]+)\./;

    // 2. Loop for each line of the input
    text.forEach((line) => {
      // 3. Decompose input line into cities and distance
      const match = line.match(pattern);
      if (match) {
        const personOne = match[1];
        const gainLoss = match[2];
        let amount = parseInt(match[3], 10);
        const personTwo = match[4];

        // 4. Gain or loss
        if (gainLoss === 'lose') {
          amount = -amount;
        }

        // 5. Add the attendee
        this.addAttendee(personOne, amount, personTwo);
      } else {
        // eslint-disable-next-line no-console
        console.log('Unable to parse input', line);
      }
    });
  }

  addAttendee(personOne, amount, personTwo) {
    if (!(personOne in this.attendees)) {
      this.attendees[personOne] = {};
      this.number += 1;
    }
    this.attendees[personOne][personTwo] = amount;
  }

  nextTo(personOne, personTwo) {
    let happiness = 0;
    if (personOne in this.attendees && personTwo in this.attendees[personOne]) {
      happiness += this.attendees[personOne][personTwo];
    }
    if (personTwo in this.attendees && personOne in this.attendees[personTwo]) {
      happiness += this.attendees[personTwo][personOne];
    }
    return happiness;
  }

  totalHappiness(table) {
    if (table === null || table.length !== this.number) {
      return null;
    }
    let happiness = this.nextTo(table[0], table[this.number - 1]);
    for (let i = 0; i < this.number - 1; i += 1) {
      happiness += this.nextTo(table[i], table[i + 1]);
    }
    return happiness;
  }

  maximizeHappiness() {
    // 1. Start with nothing
    let bestTable = null;
    let bestHappiness = null;
    // 2. Get the names of the attendees and vary all but the host
    const keys = Object.keys(this.attendees);
    let host = keys[0];
    let others = keys.slice(1);
    if (this.part2) {
      host = 'yourself';
      others = keys;
    }
    // 3. Get variations of the others
    const variations = Seating.permutator(others);
    // 4. Loop for all of the variations
    for (let i = 0; i < variations.length; i += 1) {
      // 5. Determine the happiness from this table arrangement
      const table = [host].concat(variations[i]);
      const happiness = this.totalHappiness(table);
      // 6. If the first or better than all the previous save it
      if (bestHappiness === null || happiness > bestHappiness) {
        bestHappiness = happiness;
        bestTable = table;
      }
    }
    // 7. Return the most happy of arrangements
    return bestTable;
  }

  // Derived from https://stackoverflow.com/questions/9960908/permutations-in-javascript
  static permutator(inputArr) {
    const result = [];
    const permute = (arr, m = []) => {
      if (arr.length === 0) {
        result.push(m);
      } else {
        for (let i = 0; i < arr.length; i += 1) {
          const curr = arr.slice();
          const next = curr.splice(i, 1);
          permute(curr.slice(), m.concat(next));
        }
      }
    };
    permute(inputArr);
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
    return this.totalHappiness(this.maximizeHappiness());
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.totalHappiness(this.maximizeHappiness());
  }
}

module.exports.Seating = Seating;
// ======================================================================
// end                       s e a t i n g . j s                      end
// ======================================================================
