// ======================================================================
// Lobby Layout
//   Advent of Code 2020 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t i l e s . t s
//
// A solver for the Advent of Code 2020 Day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Delta = Record<string, number[]>;
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// const NUMBER_OF_DAYS = 100;

const DELTA: Delta = {
  E: [10, 0],
  W: [-10, 0],
  NE: [5, -5],
  SE: [5, 5],
  NW: [-5, -5],
  SW: [-5, 5],
};
const DELTA_KEYS = ['E', 'W', 'NE', 'SE', 'NW', 'SW'];

const CENTER = 10000;
const ROWMULT = 100000;

const RE_NW = RegExp('nw', 'g');
const RE_NE = RegExp('ne', 'g');
const RE_SW = RegExp('sw', 'g');
const RE_SE = RegExp('se', 'g');
const RE_W = RegExp('w', 'g');
const RE_E = RegExp('e', 'g');

const NUMBER_OF_DAYS = 100;

// ======================================================================
//                                                                  Tiles
// ======================================================================

export class Tiles {
  // Object for Lobby Layout
  text: string[];

  part2: boolean;

  tiles: Set<number>;

  constructor(text: string[], part2 = false) {
    // Create a Tiles object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.tiles = new Set();

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string[]) {
    // Assign values from text

    // 1. Loop for every line of the text
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];

      // 2. Determine the location of this tile
      const loc = this.location(line);

      // 3. Set (or reset) the tile
      if (this.tiles.has(loc)) {
        this.tiles.delete(loc);
      } else {
        this.tiles.add(loc);
      }
    }
  }

  // eslint-disable-next-line class-methods-use-this
  location(line: string): number {
    // Determine the location of the tile by following the direction instructions

    // 1. Isolate the instructions
    let instructions = line.replace(RE_NW, 'NW,');
    instructions = instructions.replace(RE_NE, 'NE,');
    instructions = instructions.replace(RE_SW, 'SW,');
    instructions = instructions.replace(RE_SE, 'SE,');
    instructions = instructions.replace(RE_W, 'W,');
    instructions = instructions.replace(RE_E, 'E,');
    const insts = instructions.split(',');

    // 2. Start at the reference tile
    const loc = [CENTER, CENTER];

    // 3. Loop for all of the instructions
    for (let indx = 0; indx < insts.length; indx += 1) {
      const inst = insts[indx];
      if (inst.length > 0) {
        // 4. Adjust the locations
        loc[0] += DELTA[inst][0];
        loc[1] += DELTA[inst][1];
      }
    }

    // 5. Return the final locations as a single number
    return loc[1] * ROWMULT + loc[0];
  }

  howManyBlack(): number {
    // Return count of black tiles
    return this.tiles.size;
  }

  isTileBlack(row: number, col: number): boolean {
    // Return true if the tile is black

    // 1. Covert the column and row number to an index
    const index = row * ROWMULT + col;

    // 2. If the tile is in the set of tiles then it is a black tile
    return this.tiles.has(index);
  }

  // eslint-disable-next-line class-methods-use-this
  neighbors(row: number, col: number): number[] {
    // Return the indexes of the tiles next to the specified tile

    // 1. Start with nothing
    const result = [];

    // 2. Loop for all of the neighbors
    for (let indx = 0; indx < DELTA_KEYS.length; indx += 1) {
      const delta = DELTA[DELTA_KEYS[indx]];

      // 3. Get the location of the neighborly tile
      const loc = (row + delta[1]) * ROWMULT + delta[0] + col;

      // 4. Add it to the result
      result.push(loc);
    }

    // 5. Return the locations of nearby files
    return result;
  }

  blackNeighbors(neighbors: number[]): number {
    // Return the number of black neighbots

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for the neighbor indexes
    for (let indx = 0; indx < neighbors.length; indx += 1) {
      const neighbor = neighbors[indx];

      // 3. If the neighboring tile is black, increment the cound
      if (this.tiles.has(neighbor)) {
        result += 1;
      }
    }

    // 4. Return the number of nearby black tiles
    return result;
  }

  nextDay(): boolean {
    // Advance tiles, returns true if something changed

    // 1. Start with nothing
    const future: Set<number> = new Set();
    const checked: Set<number> = new Set();
    let changed = false;

    // 2. Loop for all of the current black tiles
    const current = Array.from(this.tiles.values());
    for (let indx = 0; indx < current.length; indx += 1) {
      const curindx = +current[indx];

      // 3. Split out the row and column
      const col = curindx % ROWMULT;
      const row = Math.floor(curindx / ROWMULT);

      // 4. Get the number of black neighbors
      const neighbors = this.neighbors(row, col);
      const blackCount = this.blackNeighbors(neighbors);

      // 5. We keep a black tile if it has exactly one or two neighbors
      if (blackCount === 1 || blackCount === 2) {
        future.add(curindx);
      } else {
        changed = true;
      }

      // 6. Check the white tiles near the black one
      for (let nindx = 0; nindx < neighbors.length; nindx += 1) {
        const neighbor = +neighbors[nindx];
        if (!this.tiles.has(neighbor) && !checked.has(neighbor)) {
          const whiteCol = neighbor % ROWMULT;
          const whiteRow = Math.floor(neighbor / ROWMULT);
          const whiteNeighbors = this.neighbors(whiteRow, whiteCol);
          const whiteCount = this.blackNeighbors(whiteNeighbors);

          // 7. A white tile changes to black if there are exactly two black neighbors
          if (whiteCount === 2) {
            future.add(neighbor);
            changed = true;
          }

          // 8. We have checked this location for the future
          checked.add(neighbor);
        }
      }
    }

    // 9. The future is now
    this.tiles = future;

    // 10. Return true if any tile changed
    return changed;
  }

  multipleDays(days: number): number {
    // Advance several days and return the number of black tiles

    // 1. Loop for the number of days
    for (let day = 0; day < days; day += 1) {
      // 2. Advance one day
      this.nextDay();
    }
    // 3. Return the number of black tiles
    return this.howManyBlack();
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.multipleDays(NUMBER_OF_DAYS);
    }
    return this.howManyBlack();
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
// end                         t i l e s . t s                        end
// ======================================================================
