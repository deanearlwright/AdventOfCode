// ======================================================================
// A Maze of Twisty Little Cubicles
//   Advent of Code 2016 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           c u b i c l e s . t s
//
// A solver for the Advent of Code 2016 Day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Location = number;
type Directions = 0 | 1 | 2 | 3;

type NextCube = [number, number, number, number];
interface Cube {
  location: Location;
  next: NextCube;
  previous: Location;
  fromStart: number;
}
type Cubes = Record<Location, Cube>;

type XY = [number, number];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const locationConstant = 1000;
const startX = 1;
const startY = 1;
const finishX = 31;
const finishY = 39;
const badNext: Location = -1;
const north: Directions = 0;
const east: Directions = 1;
const south: Directions = 2;
const west: Directions = 3;

const dirNames = ['North', 'East', 'South', 'West'];
const deltas = [-1, locationConstant, 1, -locationConstant];
const reverse = [south, west, north, east];

// ======================================================================
//                                                               Cubicles
// ======================================================================

export class Cubicles {
  // Object for A Maze of Twisty Little Cubicles
  text: string[];

  part2: boolean;

  start: Location;

  finish: Location;

  cubes: Cubes;

  favorite: number;

  wall: number;

  furthest: number;

  constructor(text: string[], part2 = false) {
    // Create a Cubicles object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.start = Cubicles.xyToLocation(startX, startY);
    this.finish = Cubicles.xyToLocation(finishX, finishY);
    this.cubes = {};
    this.cubes[this.start] = this.initialLocation();
    this.favorite = 0;
    this.wall = 100;
    this.furthest = 200;
    if (this.part2) this.furthest = 50;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.favorite = parseInt(this.text[0], 10);
    }
  }

  static initializeLocation(loc: Location): Cube {
    const [x, y] = Cubicles.locationToXY(loc);
    const nextCube: NextCube = [NaN, NaN, NaN, NaN];
    if (x === 0) nextCube[west] = badNext;
    if (y === 0) nextCube[north] = badNext;
    return {
      location: loc,
      next: nextCube,
      previous: NaN,
      fromStart: 0,
    };
  }

  initialLocation(): Cube {
    return Cubicles.initializeLocation(this.start);
  }

  static xyToLocation(x: number, y: number): Location {
    return x * locationConstant + y;
  }

  static locationToXY(loc: Location): XY {
    return [Math.trunc(loc / locationConstant), loc % locationConstant];
  }

  isItCube(loc: Location): boolean {
    if (loc in this.cubes) return true;
    const [x, y] = Cubicles.locationToXY(loc);
    if (x < 0 || y < 0) return false;
    if (x > this.wall || y > this.wall) return false;
    const sum = x * x + 3 * x + 2 * x * y + y + y * y + this.favorite;
    const bits = sum.toString(2).replace(/0/g, '').length;
    return bits % 2 === 0;
  }

  stepsTo(verbose = false, limit = 0): number {
    if (verbose) console.log(`Finding steps from ${this.start} to ${this.finish}, limit=${limit}`);
    // 1. Start with nothing at the start
    let result = 99999999;
    if (this.furthest > 0) result = this.furthest;
    let currentLoc = this.start;
    let steps = 0;
    // 2. Loop until we run out of options or take too long.
    while (!Number.isNaN(currentLoc)
    && (limit === 0 || steps < limit)) {
      steps += 1;
      let nextLoc = this.cubes[currentLoc].previous;
      if (currentLoc === this.finish) {
        if (Number.isNaN(result) || this.cubes[currentLoc].fromStart < result) {
          result = this.cubes[currentLoc].fromStart;
        }
        if (verbose) console.log(`Reached finished ${this.finish} steps=${result}`);
        if (verbose) console.log(`Backtracking from ${currentLoc} to ${nextLoc} due to finding finish`);
      } else if (this.cubes[currentLoc].fromStart >= result) {
        if (verbose) console.log(`Backtracking from ${currentLoc} to ${nextLoc} due to reashing result limit`);
      } else {
        nextLoc = this.nextCube(currentLoc);
        if (nextLoc === badNext) {
          nextLoc = this.cubes[currentLoc].previous;
          if (verbose) console.log(`Backtracking from ${currentLoc} to ${nextLoc} due to getting badNext`);
        } else if (verbose) {
          console.log(`Moving from ${currentLoc} to ${nextLoc}`);
        }
      }
      currentLoc = nextLoc;
    }
    return result;
  }

  nextCube(loc: Location): Location {
    // 0. Prexisting conditions
    if (loc === badNext) return badNext;
    if (!(loc in this.cubes)) return badNext;
    const cube = this.cubes[loc];
    // 1. look for a unexplored direction
    for (let direction = 0; direction < dirNames.length; direction += 1) {
      if (Number.isNaN(cube.next[direction])) {
        // 2. Haven't been this way from here
        const nextLoc = Cubicles.deltaLoc(loc, direction);
        // 3. Is it a wall or cube;
        if (this.isItCube(nextLoc)) {
          // 3a. A cube
          this.cubes[loc].next[direction] = nextLoc;
          // 4. If we never been here before, create it
          if (!(nextLoc in this.cubes)) {
            const newCube = Cubicles.initializeLocation(nextLoc);
            newCube.fromStart = cube.fromStart + 1;
            newCube.next[reverse[direction]] = loc;
            newCube.previous = loc;
            this.cubes[nextLoc] = newCube;
            return nextLoc;
          }
          // 5. Been here before
          if (this.cubes[nextLoc].fromStart > cube.fromStart + 1) {
            // console.log(`From ${loc} going ${dirNames[direction]} been to ${nextLoc} before; Changing steps from ${this.cubes[nextLoc].fromStart} to ${cube.fromStart + 1}`);
            this.cubes[nextLoc].next = [NaN, NaN, NaN, NaN];
            this.cubes[nextLoc].fromStart = cube.fromStart + 1;
            this.cubes[nextLoc].next[reverse[direction]] = loc;
            this.cubes[nextLoc].previous = loc;
            return nextLoc;
          }
        } else {
          // 3b. A wall
          this.cubes[loc].next[direction] = badNext;
        }
      }
    }
    return badNext;
  }

  static deltaLoc(loc: Location, direction: number): Location {
    return loc + deltas[direction];
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      this.finish = 9999999;
      this.stepsTo(verbose, limit);
      return Object.keys(this.cubes).length;
    }
    return this.stepsTo(verbose, limit);
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
// end                      c u b i c l e s . t s                     end
// ======================================================================
