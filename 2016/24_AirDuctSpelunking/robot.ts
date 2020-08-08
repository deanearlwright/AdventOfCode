// ======================================================================
// Air Duct Spelunking
//   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r o b o t . t s
//
// A solver for the Advent of Code 2016 Day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Location = number;
type Point = number;
type Distance = number;
type Moves = Location[];
type Distances = Distance[];
type Points = Location[];
interface Hall {
  location: Location;
  point: Point;
  moves: Moves;
  previous: Location;
  explore: Moves;
  steps: Distance;
}
type Halls = Record<string, Hall>;
type DMatrix = Distances[];
type PMatrix = Points[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const MAZE_WALL = '#';
const MAZE_HALL = '.';

// const REVERSE = {
//   N: 'S',
//   S: 'N',
//   W: 'E',
//   E: 'W',
// };

// const DIRS = ['N', 'S', 'W', 'E'];
// const RDIR = ['S', 'N', 'E', 'W'];

const DELTA = [-1000, 1000, -1, 1];

// const WALL_MOVE = -1;

const ROW_MULT = 1000;

const INITIAL_MOVES: Moves = [NaN, NaN, NaN, NaN];

// ======================================================================
//                                                                  Robot
// ======================================================================

export class Robot {
  // Object for Air Duct Spelunking
  text: string[];

  part2: boolean;

  points: Points;

  halls: Halls;

  constructor(text: string[], part2 = false) {
    // Create a Robot object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.points = [];
    this.halls = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.points = [];
    this.halls = {};
    // 2. Loop for all rows of the text
    for (let row = 0; row < this.text.length; row += 1) {
      const mazeRow = this.text[row];
      let mazeRC = row * ROW_MULT - 1;
      // 3. Loop for all of the columns of the row
      for (let col = 0; col < mazeRow.length; col += 1) {
        mazeRC += 1;
        const mazeAT = this.text[row][col];
        // 4. If it is a number, save location
        if (mazeAT !== MAZE_WALL && mazeAT !== MAZE_HALL) {
          this.points[parseInt(mazeAT, 10)] = mazeRC;
        }
        // 5. If not a wall, save square
        if (mazeAT !== MAZE_WALL) {
          this.halls[mazeRC] = Robot.mazeHall(mazeRC, mazeAT);
        }
      }
    }
    // 6. Adjust moves in halls
    this.adjustHallMoves();
  }

  static mazeHall(loc: Location, point: string): Hall {
    // 1. Create the base record
    const hall: Hall = {
      location: loc,
      point: point === '.' ? NaN : parseInt(point, 10),
      moves: INITIAL_MOVES.slice(),
      previous: NaN,
      explore: INITIAL_MOVES.slice(),
      steps: 0,
    };
    // 2. Loop for all of the possible exits
    for (let index = 0; index < DELTA.length; index += 1) {
      // 3. Determine if we can move in that direction
      hall.moves[index] = loc + DELTA[index];
    }
    return hall;
  }

  adjustHallMoves(): void {
    // 1. Loop for all of the hall elements
    const keys = Object.keys(this.halls);
    for (let kindex = 0; kindex < keys.length; kindex += 1) {
      const key = keys[kindex];
      const { moves } = this.halls[key];
      // 2. Loop for all of the possible places from this location
      for (let index = 0; index < DELTA.length; index += 1) {
        // 3. Mark walls with NaN instead of location
        if (!(keys.includes(moves[index].toString()))) {
          moves[index] = NaN;
        }
      }
      // 4. Save the adjusted move array
      this.halls[key].moves = moves;
      this.halls[key].explore = moves.slice();
    }
  }

  resetExplore(): void {
    // 1. Loop for all of the hall elements
    const keys = Object.keys(this.halls);
    for (let kindex = 0; kindex < keys.length; kindex += 1) {
      const key = keys[kindex];
      // 2. Copy moves to explore
      this.halls[key].explore = this.halls[key].moves.slice();
      // 3. Forget the previous previous
      this.halls[key].previous = NaN;
      // 4. And how long it took to get here
      this.halls[key].steps = 0;
    }
  }

  findAllDistances(verbose = false, limit = 0): DMatrix {
    // 1. Start with nothing
    const result: DMatrix = [];
    // 2. Loop for all points
    for (let point = 0; point < this.points.length; point += 1) {
      // 3. Get the distances from this point
      this.resetExplore();
      const distances = this.findDistancesFromPoint(point, verbose, limit);
      // 4. Save them as a row of the matrix
      result.push(distances);
    }
    // 5. Return all the distances
    return result;
  }

  findDistancesFromPoint(point: Point, verbose = false, limit = 0): Distances {
    // 1. Start at the indicated point
    const start: Location = this.points[point];
    let loc = start;
    if (verbose) console.log(`findDistancesFromPoint: point=${point} loc=${loc} limit=${limit}`);
    // 2. Not all who wander are lost
    while (!Number.isNaN(loc)) {
      loc = this.step(start, loc);
      if (!Number.isNaN(loc)) {
        const { explore, previous, steps } = this.halls[loc];
        if (verbose) console.log(`prev=${previous} loc=${loc} steps=${steps} exp=${explore}`);
        if (limit > 0 && steps > limit) {
          loc = NaN;
        }
      }
    }
    // 3. Start out with no distances
    const distances = new Array(this.points.length);
    distances.fill(NaN);
    // 4. Loop for all the points
    for (let pindex = 0; pindex < this.points.length; pindex += 1) {
      distances[pindex] = this.halls[this.points[pindex]].steps;
    }
    // 5. Return the distances found
    // console.log(distances);
    return distances;
  }

  step(start: Location, loc: Location): Location {
    // 1. See what moves are available to explore
    const { explore, previous, steps } = this.halls[loc];
    // 2. Find the first unexplored location
    let next = NaN;
    for (let eindex = 0; eindex < explore.length; eindex += 1) {
      next = explore[eindex];
      // 3. If there is one go to that location
      if (!Number.isNaN(next) && next !== start) {
        this.halls[loc].explore[eindex] = NaN;
        // 4. Unless we have already been here and got there by a shorter path
        if (Number.isNaN(this.halls[next].previous) || this.halls[next].steps > steps + 1) {
          this.halls[next].previous = loc;
          this.halls[next].steps = steps + 1;
          const nexplore = this.halls[next].moves.slice();
          for (let nindex = 0; nindex < nexplore.length; nindex += 1) {
            if (nexplore[nindex] === loc) {
              nexplore[nindex] = NaN;
            }
          }
          this.halls[next].explore = nexplore;
          return next;
        }
      }
    }
    // 5. No way forward, so we must go back
    return previous;
  }

  static getAllPermutations(string: string): string[] {
    // 0. Based on https://initjs.org/all-permutations-of-a-set-f1be174c79f8
    // 1. Start with nothing
    const results = [];
    // 2. Singleton is base case output = [input]
    if (string.length === 1) {
      results.push(string);
      return results;
    }
    // 3. Loop for all of the characters in the string
    for (let i = 0; i < string.length; i += 1) {
      // 4. Isolate the first character and all the rest
      const firstChar = string[i];
      const charsLeft = string.substring(0, i) + string.substring(i + 1);
      // 5. Permutation the remaining characters
      const innerPermutations = Robot.getAllPermutations(charsLeft);
      // 6. Add the first character to all of those permutations
      for (let j = 0; j < innerPermutations.length; j += 1) {
        results.push(firstChar + innerPermutations[j]);
      }
    }
    // 7. Return an array of permutations
    return results;
  }

  pointPermutations(): string[] {
    // 1. Result is easy if there are no points
    if (this.points.length < 1) {
      return [];
    }
    // 2. Make string of point numbers
    const points = '123456789'.slice(0, this.points.length - 1);
    // 3. Return the permutated numbers
    return Robot.getAllPermutations(points);
  }

  getTotalSteps(points: string, distances: DMatrix): number {
    // 1. Start with nothing and at nowhere
    let result = 0;
    let point = 0;
    // 2. Loop through the points
    for (let index = 0; index < points.length; index += 1) {
      // 2. Get the next point in the path
      const next = parseInt(points[index], 10);
      // 3. Accumulate the steps
      result += distances[point][next];
      // 4. The next point becomes the current point in the path
      point = next;
    }
    // 5. For part2, we need to head home
    if (this.part2) {
      result += distances[point][0];
    }
    // 6. Return the length of the path (and posiblily return to the origin)
    return result;
  }

  getFewestSteps(paths: string[], distances: DMatrix): number {
    // 0. Ignore very small mazes
    if (paths.length < 1) {
      return 0;
    }
    // 1. Start with the steps on the first path
    let result = this.getTotalSteps(paths[0], distances);
    if (paths.length === 1) {
      return result;
    }
    // 2. Loop for all of the other paths
    for (let index = 1; index < paths.length; index += 1) {
      // 3. Get the number of steps for this path
      const steps = this.getTotalSteps(paths[index], distances);
      // 4. Keep only the number of steps of the shortest path
      if (steps < result) {
        result = steps;
      }
    }
    // 5. Return the number of steps in the shortest path
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    const distances = this.findAllDistances(false, 99999);
    const paths = this.pointPermutations();
    return this.getFewestSteps(paths, distances);
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
// end                         r o b o t . t s                        end
// ======================================================================
