/* eslint-disable linebreak-style */
// ======================================================================
// Probably a Fire Hazard
//   Advent of Code 2015 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           l i g h t s . j s
//
// A solver for the Advent of Code 2015 Day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Lights
// ======================================================================

class Lights {
  // Object for Probably a Fire Hazard

  constructor(options) {
    // Create a Lights object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.size = 1000;
    this.lights = Array(this.size).fill().map(() => Array(this.size).fill(0));

    // 2. Process text (if any)
    if (this.text !== null) {
      this.text.forEach((line) => this.processInstruction(line));
    }
  }

  processInstruction(line) {
    const pattern = /(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)/;
    const inst = pattern.exec(line);
    switch (inst[1]) {
      case 'turn on':
        this.turn(1, Number(inst[2]), Number(inst[3]), Number(inst[4]), Number(inst[5]));
        break;
      case 'turn off':
        this.turn(0, Number(inst[2]), Number(inst[3]), Number(inst[4]), Number(inst[5]));
        break;
      case 'toggle':
        this.toggle(Number(inst[2]), Number(inst[3]), Number(inst[4]), Number(inst[5]));
        break;
      default:
        // eslint-disable-next-line no-console
        console.log('Bad instruction', inst);
    }
  }

  turn(onOrOff, lrow, lcol, urow, ucol) {
    for (let row = lrow; row <= urow; row += 1) {
      const theRow = this.lights[row];
      for (let col = lcol; col <= ucol; col += 1) {
        if (this.part2) {
          if (onOrOff === 1) {
            theRow[col] += 1;
          } else {
            theRow[col] += theRow[col] === 0 ? 0 : -1;
          }
        } else {
          theRow[col] = onOrOff;
        }
      }
      this.lights[row] = theRow;
    }
  }

  toggle(lrow, lcol, urow, ucol) {
    for (let row = lrow; row <= urow; row += 1) {
      const theRow = this.lights[row];
      for (let col = lcol; col <= ucol; col += 1) {
        if (this.part2) {
          theRow[col] += 2;
        } else {
          theRow[col] = theRow[col] === 1 ? 0 : 1;
        }
      }
      this.lights[row] = theRow;
    }
  }

  howManyAre(onOrOff) {
    // 1. Start with none
    let knt = 0;
    for (let row = 0; row < this.lights.length; row += 1) {
      const theRow = this.lights[row];
      for (let col = 0; col < theRow.length; col += 1) {
        if (theRow[col] === onOrOff) {
          knt += 1;
        }
      }
    }
    return knt;
  }

  totalBrightness() {
    // 1. Start with none
    let knt = 0;
    for (let row = 0; row < this.lights.length; row += 1) {
      const theRow = this.lights[row];
      for (let col = 0; col < theRow.length; col += 1) {
        knt += theRow[col];
      }
    }
    return knt;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.howManyAre(1);
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.totalBrightness();
  }
}

module.exports.Lights = Lights;
// ======================================================================
// end                      l i g h t s . j s                     end
// ======================================================================
