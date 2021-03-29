// ======================================================================
// Conway Cubes
//   Advent of Code 2020 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p o c k e t . t s
//
// A solver for the Advent of Code 2020 Day 17 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ACTIVE = '#';
const INACTIVE = '.';
const RE_NUM = /[0-9-]+/g;

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Active = '#';
type Inactive = '.';
type Cube = Active | Inactive;
type Index = string;
type Cubes = Record<Index, Cube>;
type Indexes = Index[];

// ======================================================================
//                                                                 Pocket
// ======================================================================

export class Pocket {
  // Object for Conway Cubes
  text: string[];

  part2: boolean;

  cycle: number;

  current: Cubes;

  constructor(text: string[], part2 = false) {
    // Create a Pocket object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.cycle = 0;
    this.current = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText() {
    // Assign values from text

    // 1. Loop for each line of text
    for (let rindx = 0; rindx < this.text.length; rindx += 1) {
      const line = this.text[rindx];
      // 2. loop for each character of the line
      for (let cindx = 0; cindx < line.length; cindx += 1) {
        const cube = line.charAt(cindx) as Cube;
        // 3. If active add it to the current cubes
        if (cube === ACTIVE) {
          if (this.part2) {
            this.current[`${rindx},${cindx},0,0`] = cube;
          } else {
            this.current[`${rindx},${cindx},0`] = cube;
          }
        } else if (cube !== INACTIVE) {
          console.log(`Invalid character ${cube} in line ${rindx}`);
        }
      }
    }
  }

  active(): number {
    // Return the number of active conway cubes

    // 1. Start with nothing
    let result = 0;

    // 2. Get all of the keys
    const keys = Object.keys(this.current);

    // 3. Loop for all of the keys
    for (let kindx = 0; kindx < keys.length; kindx += 1) {
      const key = keys[kindx];

      // 4. If the value is active, increment the count
      if (this.current[key] === ACTIVE) {
        result += 1;
      }
    }

    /// 5. Return the number of active conway cubes
    return result;
  }

  isActive(index: Index) {
    // Returns true if the index conway cube is currently active
    return (this.current[index] === ACTIVE);
  }

  neighbors(index: Index): Indexes {
    // Return a list of the nearby locations

    // 1. Start with nothing
    const result: string[] = [];

    // 2. Convert index to table location
    const loc: number[] = Array.from(index.matchAll(RE_NUM), (m) => parseInt(m[0], 10));

    // 3. Loop for the three dimensions
    for (let x = -1; x < 2; x += 1) {
      for (let y = -1; y < 2; y += 1) {
        for (let z = -1; z < 2; z += 1) {
          // 4. Part 1 only need three dimensions
          if (!this.part2) {
            // 5. Don't include the center location
            if (x !== 0 || y !== 0 || z !== 0) {
              result.push(`${x + loc[0]},${y + loc[1]},${z + loc[2]}`);
            }
          } else {
            // 6. Part 2 needs four dimenstion
            for (let w = -1; w < 2; w += 1) {
              if (x !== 0 || y !== 0 || z !== 0 || w !== 0) {
                result.push(`${x + loc[0]},${y + loc[1]},${z + loc[2]},${w + loc[3]}`);
              }
            }
          }
        }
      }
    }
    // 7. Return the neighbors
    return result;
  }

  countNearby(index: Index): number {
    // Return the count of nearby active conway cubes

    // 1. Start with nothing
    let result = 0;

    // 2. Get all of the neighbors
    const nearby = this.neighbors(index);

    // 3. Loop for all of the neighbors
    for (let nindx = 0; nindx < nearby.length; nindx += 1) {
      const neighbor = nearby[nindx];

      // 4. If the nearby neighbor is active, increase count
      if (this.isActive(neighbor)) {
        result += 1;
      }
    }

    // 5. Return the count of nearby active neighbors
    return result;
  }

  oneCycle() {
    // Simulate the conway cubes for one cycle

    // 1. Start with nothing
    const nextActive: Cubes = {};
    const nextChecked: Cubes = {};

    // 2. Loop for all of the active cells
    const keys = Object.keys(this.current);
    for (let kindx = 0; kindx < keys.length; kindx += 1) {
      const key = keys[kindx];
      if (this.current[key] === ACTIVE) {
        // 3. Determine if it will remain active
        const activeNearby = this.countNearby(key);
        if (activeNearby === 2 || activeNearby === 3) {
          // console.log(`cube ${key} with count of ${activeNearby} will remain active`);
          nextActive[key] = ACTIVE;
        } else {
          // console.log(`cube ${key} with count of ${activeNearby} will become inactive`);
        }
        // 4. For all of the neighbors of the active cell
        const actNearby = this.neighbors(key);
        for (let nindx = 0; nindx < actNearby.length; nindx += 1) {
          const neighbor = actNearby[nindx];
          // 5. Ignore neighbors that are active or have been checked
          if (neighbor !== key && !this.isActive(neighbor) && undefined === nextChecked[neighbor]) {
            // 6. Determine if the neighbor will become active
            const neighborNearby = this.countNearby(neighbor);
            if (neighborNearby === 3) {
              // console.log(`cube ${neighbor} with count of ${neighborNearby} will become active`);
              nextActive[neighbor] = ACTIVE;
            }
            // 7. Remember we checked this nearby location
            nextChecked[neighbor] = ACTIVE;
          }
        }
      }
    }
    // 8. The future is now
    this.current = nextActive;
    // 9. Update the cycle count
    this.cycle += 1;
  }

  runUntil(cycle: number) {
    // Return count of active cubes after the specified cycle

    // 1. Loop until we reach the specified cycle
    while (this.cycle < cycle) {
      // 2. Execute the next cycle
      this.oneCycle();
    }
    // 3. Return the count of active cubes
    return this.active();
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.runUntil(6);
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit); // 213
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit); // 1624
  }
}

// ======================================================================
// end                        p o c k e t . t s                       end
// ======================================================================
