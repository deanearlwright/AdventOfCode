// ======================================================================
// Grid Computing
//   Advent of Code 2016 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           n o d e s . t s
//
// A solver for the Advent of Code 2016 Day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type NodeStore = {
  name: string;
  x: number;
  y: number;
  size: number;
  used: number;
  avail: number;
  percent: number;
};

type GridStore = Record<string, NodeStore>;

type NodeStores = NodeStore[];

type Corners = {
  minX: number,
  minY: number;
  maxX: number;
  maxY: number;
};

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const NO_CORNERS = {
  minX: 0,
  minY: 0,
  maxX: 0,
  maxY: 0,
};

// ======================================================================
//                                                                  Nodes
// ======================================================================

export class Nodes {
  // Object for Grid Computing
  text: string[];

  part2: boolean;

  storage: GridStore;

  corners: Corners;

  used: NodeStores;

  avail: NodeStores;

  constructor(text: string[], part2 = false) {
    // Create a Nodes object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.storage = {};
    this.corners = { ...NO_CORNERS };
    this.used = [];
    this.avail = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.storage = {};
    this.corners = { ...NO_CORNERS };
    this.used = [];
    this.avail = [];
    // 2. Loop for all lines of text
    this.text.forEach((line) => {
      // 3. Process storage information
      if (line[0] === '/') {
        const parts = line.replace(/ +/g, ' ').split(' ');
        const xy = parts[0].split('-');
        const x = parseInt(xy[1].substring(1), 10);
        const y = parseInt(xy[2].substring(1), 10);
        const name = Nodes.nodeName(x, y);
        const size = parseInt(parts[1].substring(0, parts[1].length - 1), 10);
        const used = parseInt(parts[2].substring(0, parts[2].length - 1), 10);
        const avail = parseInt(parts[3].substring(0, parts[3].length - 1), 10);
        const percent = parseInt(parts[4].substring(0, parts[4].length - 1), 10);
        const node: NodeStore = {
          name,
          x,
          y,
          size,
          used,
          avail,
          percent,
        };
        this.storage[name] = node;
        this.used.push(node);
        this.avail.push(node);
      }
    });
    // 4. Sort used and avail lists
    this.used.sort((a, b) => a.used - b.used);
    this.avail.sort((a, b) => a.avail - b.avail);
    // 5. Find the corners
    this.used.forEach((node) => {
      if (this.corners.minX > node.x) {
        this.corners.minX = node.x;
      }
      if (this.corners.minY > node.y) {
        this.corners.minY = node.y;
      }
      if (this.corners.maxX < node.x) {
        this.corners.maxX = node.x;
      }
      if (this.corners.maxY < node.y) {
        this.corners.maxY = node.y;
      }
    });
  }

  static nodeName(x: number, y: number): string {
    return `node-x${x}-y${y}`;
  }

  whoHasAvail(need: number): number {
    // 1. Loop until we find enough space
    for (let index = 0; index < this.avail.length; index += 1) {
      if (this.avail[index].avail >= need) {
        return index;
      }
    }
    // 2. Never did
    return -1;
  }

  numberViablePairs(verbose = false, limit = 0): number {
    if (verbose) console.log(`numberViablePairs: ${limit}`);
    // 1. Start with nothing
    let result = 0;
    // 2. Loop for all of the nodes in order of need
    for (let index = 0; index < this.used.length; index += 1) {
      const { name, used, avail } = this.used[index];
      if (used > 0) {
        // 3. Is there any one who can receive this much space?
        const availLowest = this.whoHasAvail(used);
        if (availLowest >= 0) {
          result += (this.avail.length - availLowest);
          if (avail >= used) {
            result -= 1;
          }
          if (verbose) console.log(`nVP ${index} ${name} ${used} ${availLowest} ${result}`);
        } else {
          break;
        }
      }
    }
    // 9. Return number of pairs found
    return result;
  }

  printGrid(): number {
    const grid: string[] = [];
    for (let row = this.corners.minY; row <= this.corners.maxY; row += 1) {
      const gridRow: string[] = [];
      for (let col = this.corners.minX; col <= this.corners.maxX; col += 1) {
        let char = '.';
        if (row === 0 && col === 0) {
          char = '!';
        } else if (row === 0 && col === this.corners.maxX) {
          char = 'G';
        } else {
          const name = Nodes.nodeName(col, row);
          if (this.storage[name].used === 0) {
            char = 'E';
          } else if (this.storage[name].used > 100) {
            char = '#';
          }
        }
        gridRow.push(char);
      }
      grid.push(gridRow.join(''));
    }
    console.log(grid.join('\n'));
    //
    // !...................................G
    // .....................................
    // ...............######################
    // .....................................
    // .....................................
    // .....................................
    // ....................E................
    // .....................................
    // .....................................
    // .....................................
    // 1 = (0,0), G = (36, 0), E = (20, 6)
    // The wall is from 15 to 36 on row 2.
    // Distance = 36-20+6 = 22.
    // To get past wall = 6 cols = 22+12=34
    // Five step cycle = 5 * 35 = 175.
    // Total moves = 34 + 175 = 209.
    return 209;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      this.printGrid();
      return NaN;
    }
    return this.numberViablePairs(verbose, limit);
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
// end                         n o d e s . t s                        end
// ======================================================================
