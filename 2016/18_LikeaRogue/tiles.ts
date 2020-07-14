// ======================================================================
// Like a Rogue
//   Advent of Code 2016 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t i l e s . t s
//
// A solver for the Advent of Code 2016 Day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

type Tile = '.' | '^';
type TileArray = Tile[];
type TileRow = string; // of Tiles
type NextRow = string; // of Tiles

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const NEXT_TRAP: NextRow[] = [
  '^^.',
  '.^^',
  '^..',
  '..^',
];

const PART1_NUMBER_ROWS = 40;
const PART2_NUMBER_ROWS = 400000;
// ======================================================================
//                                                                  Tiles
// ======================================================================

export class Tiles {
  // Object for Like a Rogue
  text: string[];

  part2: boolean;

  rows: TileRow[];

  numRows: number;

  constructor(text: string[], part2 = false) {
    // Create a Tiles object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rows = [];
    this.numRows = this.part2 ? PART2_NUMBER_ROWS : PART1_NUMBER_ROWS;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.rows.push(`${this.text[0]}`);
    }
  }

  static nextRow(row: TileRow): TileRow {
    // 1. Start with nothing
    const result: TileArray = [];
    // 2. Loop for every position in the row
    for (let position = 0; position < row.length; position += 1) {
      // 3. Compute and save the position in the next row
      result.push(Tiles.nextTile(row, position));
    }
    // 4. Return the next row
    return result.join('');
  }

  static nextTile(row: TileRow, pos: number): Tile {
    // 1. Center is easy
    const center = <Tile>row[pos];
    // 3. Problem for left if pos is 0
    const left = <Tile>(pos === 0 ? '.' : row[pos - 1]);
    // 4. Problem for right if at end of row
    const right = <Tile>(pos < row.length - 1 ? row[pos + 1] : '.');
    // 5. Put them all together
    const lcr = `${left}${center}${right}`;
    // 6. Return the tile computed from left, center, right
    return NEXT_TRAP.indexOf(lcr) === -1 ? '.' : '^';
  }

  static countSafeRow(row: TileRow): number {
    return row.replace(/\^/g, '').length;
  }

  fillRows(numRows: number): void {
    for (let index = 1; index < numRows; index += 1) {
      this.rows.push(Tiles.nextRow(this.rows[index - 1]));
    }
  }

  countSafe(): number {
    let result = 0;
    for (let index = 0; index < this.rows.length; index += 1) {
      result += Tiles.countSafeRow(this.rows[index]);
    }
    return result;
  }

  fillAndCount(numRows: number): number {
    this.fillRows(numRows);
    return this.countSafe();
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.fillAndCount(this.numRows);
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
