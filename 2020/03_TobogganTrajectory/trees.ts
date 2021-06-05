// ======================================================================
// Toboggan Trajectory
//   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t r e e s . t s
//
// A solver for the Advent of Code 2020 Day 03 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const TREE = '#';

// ======================================================================
//                                                                  Trees
// ======================================================================

export class Trees {
  // Object for Toboggan Trajectory
  text: string[];

  part2: boolean;

  rows = 0;

  cols = 0;

  constructor(text: string[], part2 = false) {
    // Create a Trees object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rows = 0;
    this.cols = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.rows = this.text.length;
      this.cols = this.text[0].length;
    }
  }

  is_tree(col: number, row: number): boolean {
    // Returns true if there is a tree at (col, row)

    // 1. There are no trees below the forest
    if (this.is_below(row)) {
      return false;
    }

    // 2. Check the forest square
    const mcol = col % this.cols;
    if (TREE === this.text[row][mcol]) {
      return true;
    }

    // 4. There is no spoon
    return false;
  }

  is_below(row: number): boolean {
    // Returns true if beyond the forest
    return row >= this.rows;
  }

  count_trees(delta_col: number, delta_row: number): number {
    // Return number of trees hit in toboggen ride

    // 1. Start at the very beginning
    let col = 0;
    let row = 0;
    let knt = 0;

    // 2. Loop until we are out of the forest
    do {
      // 3. If this is a tree, count it
      if (this.is_tree(col, row)) {
        knt += 1;
      }

      // 4. Advent to the next location
      col += delta_col;
      row += delta_row;
    } while (!this.is_below(row));

    // 5. Return the number of trees hit
    return knt;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      // 1. Get the counts from multiple toboggan runs
      const kntOneOne = this.count_trees(1, 1);
      const kntThreeOne = this.count_trees(3, 1);
      const kntFiveOne = this.count_trees(5, 1);
      const kntSevenOne = this.count_trees(7, 1);
      const kntOneTwo = this.count_trees(1, 2);
      // 2. Return the product of the trees encountered
      return kntOneOne * kntThreeOne * kntFiveOne * kntSevenOne * kntOneTwo;
    }
    return this.count_trees(3, 1);
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
// end                         t r e e s . t s                        end
// ======================================================================
