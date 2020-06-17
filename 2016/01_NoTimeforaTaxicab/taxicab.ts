// ======================================================================
// No Time for a Taxicab
//   Advent of Code 2016 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t a x i c a b . t s
//
// A solver for the Advent of Code 2016 Day 01 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
interface instructionType {
  direction: string;
  blocks: number;
}

interface directionType {
  left: string;
  right: string;
}

type facingType = Record<string, directionType>

interface locationType {
  we: number;
  sn: number;
}

type deltaType = Record<string, locationType>

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const facings: facingType = {
  N: { left: 'W', right: 'E' },
  S: { left: 'E', right: 'W' },
  E: { left: 'N', right: 'S' },
  W: { left: 'S', right: 'N' },
};

const deltas: deltaType = {
  N: { we: 0, sn: 1 },
  S: { we: 0, sn: -1 },
  E: { we: 1, sn: 0 },
  W: { we: -1, sn: 0 },
};

// ======================================================================
//                                                                Taxicab
// ======================================================================

export class Taxicab {
  // Object for No Time for a Taxicab
  text: string[];

  part2: boolean;

  instructions: instructionType[];

  constructor(text: string[], part2 = false) {
    // Create a Taxicab object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.instructions = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.instructions = [];
    // 2. Break up the input line
    const parts: string[] = this.text[0].split(',');
    // 3. Loop for all of the comma seperated parts
    parts.forEach((single: string) => {
      const trimed = single.trim();
      const direction: string = trimed[0];
      const blocks: number = parseInt(trimed.substr(1), 10);
      const instruction: instructionType = { direction, blocks };
      this.instructions.push(instruction);
    });
  }

  routeDistance(verbose: boolean, limit: number): number {
    if (verbose) console.log(`routeDistance limit=${limit}`);
    // 1. Start at the very beginning
    let we = 0;
    let sn = 0;
    let dir = 'N';
    let steps = 0;
    // 2. Loop for all of the instructions
    for (let index = 0; index < this.instructions.length; index += 1) {
      const instruction = this.instructions[index];
      // 3. Check that we haven't gone too far
      steps += 1;
      if (limit > 0 && steps > limit) {
        console.log(`Stopped after ${steps} instructions`);
        break;
      }
      // 4. Get new facing
      const newDir = instruction.direction === 'R' ? facings[dir].right : facings[dir].left;
      // 5. Move in that direction
      switch (newDir) {
        case 'E':
          we += instruction.blocks;
          break;
        case 'W':
          we -= instruction.blocks;
          break;
        case 'N':
          sn += instruction.blocks;
          break;
        case 'S':
          sn -= instruction.blocks;
          break;
        default:
          console.log(`Invalid direction after ${instruction.direction}${instruction.blocks}`);
      }
      if (verbose) console.log(`${steps} ${dir} ${instruction.direction}${instruction.blocks} ${newDir} ${we} ${sn}`);
      dir = newDir;
    }
    return Math.abs(we) + Math.abs(sn);
  }

  static visitedBefore(locations: locationType[], location: locationType): boolean {
    // 1. loop for all locations
    for (let index = 0; index < locations.length; index += 1) {
      if (locations[index].we === location.we && locations[index].sn === location.sn) return true;
    }
    return false;
  }

  visitTwice(verbose = true, limit = 0): number {
    if (verbose) console.log(`visitTwice limit=${limit}`);
    // 1. Start at the very beginning
    let we = 0;
    let sn = 0;
    let dir = 'N';
    let steps = 0;
    let found = false;
    const visited: locationType[] = [];
    // 2. Helper functions
    function visitedBefore(xwe: number, xsn: number): boolean {
      // a. loop for all locations
      for (let vindex = 0; vindex < visited.length; vindex += 1) {
        // b. If we have been here before, return true
        if (visited[vindex].we === xwe && visited[vindex].sn === xsn) return true;
      }
      // c. Else return false
      return false;
    }
    function addLocation(xwe: number, xsn: number): void {
      // a. Remember where we have been
      const loc: locationType = { we: xwe, sn: xsn };
      visited.push(loc);
    }
    // 3. Remember being at the start
    addLocation(we, sn);
    // 4. Loop for all of the instructions
    for (let index = 0; index < this.instructions.length; index += 1) {
      const instruction = this.instructions[index];
      // 5. Check that we haven't gone too far
      steps += 1;
      if (limit > 0 && steps > limit) {
        console.log(`Stopped after ${steps} instructions`);
        break;
      }
      // 6. Get new facing
      const newDir = instruction.direction === 'R' ? facings[dir].right : facings[dir].left;
      // 7. Move in that direction
      const delta = deltas[newDir];
      for (let block = 0; block < instruction.blocks; block += 1) {
        we += delta.we;
        sn += delta.sn;
        if (visitedBefore(we, sn)) {
          found = true;
          break;
        }
        addLocation(we, sn);
      }
      if (verbose) console.log(`${steps} ${dir} ${instruction.direction}${instruction.blocks} ${newDir} ${we} ${sn} ${found}`);
      dir = newDir;
      if (found) break;
    }
    if (found) return Math.abs(we) + Math.abs(sn);
    return NaN;
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.routeDistance(verbose, limit);
  }

  partTwo(verbose = true, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.visitTwice(verbose, limit);
  }
}

// ======================================================================
// end                       t a x i c a b . t s                      end
// ======================================================================
