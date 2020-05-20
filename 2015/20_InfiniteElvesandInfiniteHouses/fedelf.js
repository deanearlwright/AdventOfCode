/* eslint-disable linebreak-style */
// ======================================================================
// Infinite Elves and Infinite Houses
//   Advent of Code 2015 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           f e d e l f . j s
//
// A solver for the Advent of Code 2015 Day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Fedelf
// ======================================================================

class Fedelf {
  // Object for Infinite Elves and Infinite Houses

  constructor(options) {
    // Create a Fedelf object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.presents = null;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.presents = parseInt(this.text[0], 10);
    }
  }

  static inHouse(hnum) {
    // 1. Start with nothing
    let presents = 0;
    // 2. Loop for all possible elves
    for (let elf = 1; elf <= hnum; elf += 1) {
      // 3. If the elf delivers presents to this house, do so
      if (hnum % elf === 0) {
        presents += elf;
      }
    }
    // 4. Return the number of presents
    return presents * 10;
  }

  static firstHouse(presents) {
    // 1. Loop for all the possible houses
    for (let house = 1; house <= presents; house += 1) {
      // 2. Determine how many presents were delivered to that house
      const received = Fedelf.inHouse(house);
      // 3. Are there enough presents?
      if (received >= presents) {
        return house;
      }
    }
    // 4. So sorry
    return null;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return Fedelf.firstHouse(this.presents);
  }

  static inHouse2(hnum, elves) {
    // 1. Start with nothing
    let presents = 0;
    const newElves = { ...elves };
    // 2. Loop for all possible elves
    for (let elf = 1; elf <= hnum; elf += 1) {
      // 3. If the elf could deliver presents to this house ...
      if (hnum % elf === 0) {
        // 4. Check if the elf is off the clock (already delivered 50 presents)
        if (elf in newElves) {
          newElves[elf] += 1;
        } else {
          newElves[elf] = 1;
        }
        if (newElves[elf] <= 50) {
          presents += elf;
        }
      }
    }
    // 5. Elf 'presents' has the number of presents
    newElves.presents = presents * 11;
    return newElves;
  }

  static firstHouse2(presents) {
    // 1. Reset the elves
    const elves = {};
    // 1. Loop for all the possible houses
    for (let house = 1; house <= presents; house += 1) {
      // 2. Add the elf that starts with this house
      elves[house] = 0;
      // 3. Determine how many presents were delivered to that house
      // 3a. Start with nothing
      let delivered = 0;
      // 3b. Loop for all possible elves
      Object.keys(elves).forEach((elf) => {
        // 3c. If the elf could deliver presents to this house ...
        if (house % elf === 0) {
          // 3d. Deliver the present
          delivered += parseInt(elf, 10);
          elves[elf] += 1;
          // 3e. If this the last one present for this elf, his/her work is done
          if (elves[elf] === 50) {
            delete elves[elf];
          }
        }
      });
      delivered *= 11;
      // eslint-disable-next-line no-console
      console.log(`house ${house} gets ${delivered}`);
      if (delivered >= presents) {
        return house;
      }
    }
    // 4. So sorry
    return null;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return Fedelf.firstHouse2(this.presents);
  }
}

module.exports.Fedelf = Fedelf;
// ======================================================================
// end                         f e d e l f . j s                      end
// ======================================================================
