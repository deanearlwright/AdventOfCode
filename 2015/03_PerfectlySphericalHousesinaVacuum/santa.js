/* eslint-disable linebreak-style */
// ======================================================================
// Perfectly Spherical Houses in a Vacuum
//   Advent of Code 2015 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s a n t a . j s
//
// A solver for the Advent of Code 2015 Day 03 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const DELTA = {
  '^': [0, 1],
  v: [0, -1],
  '<': [-1, 0],
  '>': [1, 0],
};

// ======================================================================
//                                                                  Santa
// ======================================================================

class Santa {
  // Object for Perfectly Spherical Houses in a Vacuum

  constructor(options) {
    // Create a Santa object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.houses = 0;
    this.location = [0, 0];
    this.visited = {};

    // 2. Process text (if any)
    if (this.text !== null) {
      // TODO process the test
      [this.directions] = this.text;
    } else {
      this.directions = '';
    }
  }

  followDirection(location, direction) {
    // 1. Determine the next house
    const delta = DELTA[direction];
    const nextLocation = [delta[0] + location[0], delta[1] + location[1]];
    // 2. If this is an old house, deliver another prexent
    if (nextLocation in this.visited) {
      this.visited[nextLocation] += 1;
    // 3. Otherwise, deliver the first present to this house
    } else {
      this.visited[nextLocation] = 1;
      this.houses += 1;
    }
    // 4. Keep track of number of presents delivered
    this.presents += 1;

    // 5. Return the new location
    return nextLocation;
  }

  followDirections() {
    // 1. Deliver to the first house
    this.location = [0, 0];
    this.presents = 1;
    this.houses = 1;
    this.visited[this.location] = 1;

    // 2. Loop for each character in the instructions
    this.directions.split('').forEach((direction) => {
      // 3. Process that direction
      this.location = this.followDirection(this.location, direction);
    });
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Follow the directions
    this.followDirections();

    // 2. Return the number of houses visited
    return this.houses;
  }

  followDirectionsTwo() {
    // 1. Deliver to the first house by both Santa and robo-Santa
    this.location = [0, 0];
    this.presents = 2;
    this.houses = 1;
    this.visited[this.location] = 2;

    // 2. Santa follows the first instruction
    let isSanta = true;
    let roboLocation = [0, 0];

    // 3. Loop for each character in the instructions
    this.directions.split('').forEach((direction) => {
      // 4. Santa does half the deliveries
      if (isSanta) {
        this.location = this.followDirection(this.location, direction);
      } else {
        roboLocation = this.followDirection(roboLocation, direction);
      }
      // 5. Switch off
      isSanta = !isSanta;
    });
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Follow the directions
    this.followDirectionsTwo();

    // 2. Return the number of houses visited
    return this.houses;
  }
}

module.exports.Santa = Santa;
// ======================================================================
// end                         s a n t a . j s                        end
// ======================================================================
