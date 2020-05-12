/* eslint-disable linebreak-style */
// ======================================================================
// Like a GIF For Your Yard
//   Advent of Code 2015 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           l i g h t s . j s
//
// A solver for the Advent of Code 2015 Day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const DEFAULT_SIZE = 100;
const SQUARE_ON = '#';
const SQUARE_OFF = '.';
const DEFAULT_STEPS = 100;

// ======================================================================
//                                                                 Lights
// ======================================================================

class Lights {
  // Object for Like a GIF For Your Yard

  constructor(options) {
    // Create a Lights object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.size = options.size === undefined ? DEFAULT_SIZE : options.size;
    this.steps = options.steps === undefined ? DEFAULT_STEPS : options.steps;
    this.step = 0;
    this.grid = this.newGrid();

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
      if (this.part2) {
        this.setCorners();
      }
    }
  }

  newGrid() {
    const grid = new Array(this.size);
    for (let index = 0; index < this.size; index += 1) {
      grid[index] = new Array(this.size).fill(0);
    }
    return grid;
  }

  setCorners() {
    const sizem1 = this.size - 1;
    this.grid[0][0] = 1;
    this.grid[0][sizem1] = 1;
    this.grid[sizem1][0] = 1;
    this.grid[sizem1][sizem1] = 1;
  }

  processText(text) {
    // 1. Initialize the grid
    this.grid = this.newGrid();
    // 2. Make sure there are the correct number of rows
    if (text.length !== this.size) {
      // eslint-disable-next-line no-console
      console.log(`Text length does not size, ${text.length} != ${this.size}`);
    } else {
      // 3. Loop for all the rows
      for (let row = 0; row < this.size; row += 1) {
        const textRow = text[row];
        // 4. Check the row length
        if (textRow.length !== this.size) {
          // eslint-disable-next-line no-console
          console.log(`Text length does not size, ${text.length} != ${this.size}`);
        } else {
          // 5. Convert text to integers
          const gridRow = new Array(this.size).fill(0);
          for (let col = 0; col < this.size; col += 1) {
            switch (textRow[col]) {
              case SQUARE_ON:
                gridRow[col] = 1;
                break;
              case SQUARE_OFF:
                gridRow[col] = 0;
                break;
              default:
                // eslint-disable-next-line no-console
                console.log(`Unexpected text char in row ${row} col ${col} (${textRow[col]})`);
            }
          }
          this.grid[row] = gridRow;
        }
      }
    }
  }

  show() {
    const result = new Array(this.size);
    for (let row = 0; row < this.size; row += 1) {
      const gridRow = this.grid[row];
      const oneRow = new Array(this.size);
      for (let col = 0; col < this.size; col += 1) {
        switch (gridRow[col]) {
          case 1:
            oneRow[col] = SQUARE_ON;
            break;
          case 0:
            oneRow[col] = SQUARE_OFF;
            break;
          default:
            // eslint-disable-next-line no-console
            console.log(`Unexpected value in row ${row} col ${col} (${oneRow[col]})`);
        }
      }
      result[row] = oneRow.join('');
    }
    return result.join('\n');
  }

  next() {
    const ng = this.newGrid();
    for (let row = 0; row < this.size; row += 1) {
      for (let col = 0; col < this.size; col += 1) {
        const sum = this.neighbors(row, col);
        if (this.grid[row][col] === 1) {
          if (sum === 2 || sum === 3) {
            ng[row][col] = 1;
          }
        } else if (sum === 3) {
          ng[row][col] = 1;
        }
      }
    }
    this.grid = ng;
    if (this.part2) {
      this.setCorners();
    }
    this.step += 1;
  }

  neighbors(row, col) {
    const sizem1 = this.size - 1;
    const minRow = row === 0 ? 0 : row - 1;
    const minCol = col === 0 ? 0 : col - 1;
    const maxRow = row === sizem1 ? sizem1 : row + 1;
    const maxCol = col === sizem1 ? sizem1 : col + 1;
    let result = this.grid[row][col] === 0 ? 0 : -1;
    for (let nRow = minRow; nRow <= maxRow; nRow += 1) {
      for (let nCol = minCol; nCol <= maxCol; nCol += 1) {
        result += this.grid[nRow][nCol];
      }
    }
    return result;
  }

  count() {
    const sum = (a, v) => a + v;
    let result = 0;
    for (let row = 0; row < this.size; row += 1) {
      const rowSum = this.grid[row].reduce(sum);
      result += rowSum;
    }
    return result;
  }

  animate() {
    while (this.step < this.steps) {
      this.next();
    }
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    this.todo = 'TODO';

    // 1. Animate the lights for the prescribed time
    this.animate();

    // 2. Return the solution for part one
    return this.count();
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Animate the lights for the prescribed time
    this.animate();

    // 2. Return the solution for part two
    return this.count();
  }
}

module.exports.Lights = Lights;
// ======================================================================
// end                        l i g h t s . j s                       end
// ======================================================================
