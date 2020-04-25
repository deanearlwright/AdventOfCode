/* eslint-disable linebreak-style */
// ======================================================================
// Reindeer Olympics
//   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           o l y m p i c s . j s
//
// A solver for the Advent of Code 2015 Day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const reindeer = require('./reindeer');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const FINAL_TICK = 2503;

// ======================================================================
//                                                               Olympics
// ======================================================================

class Olympics {
  // Object for Reindeer Olympics

  constructor(options) {
    // Create a Olympics object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.reindeer = [];

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.reindeer = [];

    // 2. Loop for each line of the input
    text.forEach((line) => {
      // 3. Create a new reindeer from this text
      const deer = new reindeer.Reindeer({ text: line });
      // 4. Add the attendee
      this.reindeer.push(deer);
    });
  }

  startAll() {
    // 1. Start all the reindeers
    this.reindeer.forEach((deer) => {
      deer.start();
    });
  }

  gotoAll(tick) {
    // 1. Advance all the reindeers to tick
    this.reindeer.forEach((deer) => {
      deer.goto(tick);
    });
  }

  furthest() {
    // 1. Start with nothing
    let furthestDistance = 0;
    let furthestDeer = null;
    // 2. Loop for all of the reindeer
    this.reindeer.forEach((deer) => {
      // 3. If this one has traveled further, save it
      if (deer.distance > furthestDistance) {
        furthestDistance = deer.distance;
        furthestDeer = deer;
      }
    });
    // 4. Return the furthest deer
    return furthestDeer;
  }

  race(endTick) {
    // 1. Start all the reindeer
    this.startAll();
    // 2. Have the all fly
    this.gotoAll(endTick);
    // 3. Return the one that went the furthest
    return this.furthest();
  }

  highest() {
    // 1. Start with nothing
    let highestPoints = 0;
    let highestDeer = null;
    // 2. Loop for all of the reindeer
    this.reindeer.forEach((deer) => {
      // 3. If this one has received more rewards, save it
      if (deer.points > highestPoints) {
        highestPoints = deer.points;
        highestDeer = deer;
      }
    });
    // 4. Return the highest deer
    return highestDeer;
  }

  race2(endTick) {
    // 1. Start all the reindeer
    this.startAll();
    let raceTick = 0;
    // 2. do it a tick at a time
    while (raceTick < endTick) {
      raceTick += 1;
      // 3. Let each reindeer advance one tick
      this.reindeer.forEach((deer) => {
        deer.tick();
      });
      // 4. Find the furthest distance
      const furthestDeer = this.furthest();
      // 5. Give all deer at that distance a point
      if (furthestDeer !== null) {
        this.reindeer.forEach((deer) => {
          if (deer.distance === furthestDeer.distance) {
            deer.reward();
          }
        });
      }
    }
    // 6. Return the deer with the highest score
    return this.highest();
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    const deer = this.race(FINAL_TICK);
    if (deer === null) {
      return null;
    }
    return deer.distance;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    const deer = this.race2(FINAL_TICK);
    if (deer === null) {
      return null;
    }
    return deer.points;
  }
}

module.exports.Olympics = Olympics;
// ======================================================================
// end                      o l y m p i c s . j s                     end
// ======================================================================
