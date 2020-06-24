// ======================================================================
// Two-Factor Authentication
//   Advent of Code 2016 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           d i s p l a y . t s
//
// A solver for the Advent of Code 2016 Day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const screenOn = '#';
const screenOff = '.';
const screenHeight = 6;
const screenWidth = 50;
const screenRowOff = screenOff.repeat(screenWidth);
const screenRowOn = screenOn.repeat(screenWidth);

// ======================================================================
//                                                                Display
// ======================================================================

export class Display {
  // Object for Two-Factor Authentication
  text: string[];

  part2: boolean;

  screen: string[];

  constructor(text: string[], part2 = false) {
    // Create a Display object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.screen = [];
    this.screenReset();

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  screenReset(): void {
    this.screen = [
      screenRowOff.slice(),
      screenRowOff.slice(),
      screenRowOff.slice(),
      screenRowOff.slice(),
      screenRowOff.slice(),
      screenRowOff.slice(),
    ];
  }

  processText(): void {
    // 1. Loop for every line of the text
    this.text.forEach((line) => {
      this.processLine(line);
      console.log(`${line}, count = ${this.count()}`);
      this.show();
    });
  }

  processLine(line: string): void {
    // 1. Break the line into words
    const words = line.split(' ');
    if (words.length < 2) {
      console.log(`Line too short: ${line}`);
    } else {
      switch (words[0]) {
        case 'rect':
          this.processRect(line, words);
          break;
        case 'rotate':
          switch (words[1]) {
            case 'column':
              this.processRotateColumn(line, words);
              break;
            case 'row':
              this.processRotateRow(line, words);
              break;
            default:
              console.log(`rotate not column or row: ${line}`);
          }
          break;
        default:
          console.log(`'Unknown command ${words[0]}: ${line}`);
      }
    }
  }

  processRect(line: string, words: string[]): void {
    // rect AxB turns on all of the pixels in a rectangle at the top-left of
    // the screen which is A wide and B tall.
    if (this.screen.length !== 6) console.log(`processRect ${line} ${words.join()}`);
    if (words.length !== 2) {
      console.log(`Unexpected number of words ${words.length} in rect command ${line}`);
    } else {
      const numbers = words[1].split('x');
      if (numbers.length !== 2) {
        console.log(`Unexpected AxB ${words[1]} in rect command ${line}`);
      } else {
        const wide = parseInt(numbers[0], 10);
        const tall = parseInt(numbers[1], 10);
        if (wide < 1 || wide > screenWidth) {
          console.log(`Unexpected width ${wide} for rect command ${line}`);
        } else if (tall < 1 || tall > screenHeight) {
          console.log(`Unexpected height ${tall} for rect command ${line}`);
        } else {
          for (let row = 0; row < tall; row += 1) {
            this.setRectRowOn(row, wide);
          }
        }
      }
    }
  }

  setRectRowOn(row: number, wide: number): void {
    if (this.screen.length !== screenHeight) console.log(`row = ${row} wide = ${wide}`);
    this.screen[row] = screenRowOn.slice(0, wide) + this.screen[row].slice(wide);
    if (this.screen[row].length !== screenWidth) console.log(`Mucked up rext ?x${wide} for row ${row} ${this.screen[row].length} ${this.screen[row]}`);
  }

  processRotateColumn(line: string, words: string[]): void {
    // rotate column x=A by B shifts all of the pixels in column A (0 is the
    // left column) down by B pixels. Pixels that would fall off the bottom
    // appear at the top of the column.
    if (this.screen.length !== screenHeight) console.log(`processRotateColumn ${line} ${words.join()}`);
    if (words.length !== 5) {
      console.log(`Unexpected number of words ${words.length} in rotate column command ${line}`);
    } else {
      const numbers = words[2].split('=');
      if (numbers.length !== 2 || !words[2].startsWith('x')) {
        console.log(`Unexpected x=A ${words[2]} in rotate column command ${line}`);
      } else if (words[3] !== 'by') {
        console.log(`Missing by in rotate column command ${line}`);
      } else {
        const col = parseInt(numbers[1], 10);
        const shift = parseInt(words[4], 10);
        if (col < 0 || col > screenWidth - 1) {
          console.log(`Unexpected col ${col} for rotate column command ${line}`);
        } else if (shift < 1 || shift > screenHeight - 1) {
          console.log(`Unexpected shift ${shift} for rotate column command ${line}`);
        } else {
          const column = [
            this.screen[0][col],
            this.screen[1][col],
            this.screen[2][col],
            this.screen[3][col],
            this.screen[4][col],
            this.screen[5][col],
          ].join('');
          this.setRotateColumn(col, shift, column);
        }
      }
    }
  }

  setRotateColumn(col: number, shift: number, column: string): void {
    if (this.screen.length !== screenHeight) console.log(`setRotateColumn ${col} ${shift} ${column}`);
    const shifted = (column + column).slice(6 - shift);
    for (let row = 0; row < screenHeight; row += 1) {
      this.screen[row] = this.screen[row].slice(0, col)
        + shifted[row] + this.screen[row].slice(col + 1, 60);
    }
  }

  processRotateRow(line: string, words: string[]): void {
    // rotate row y=A by B shifts all of the pixels in row A (0 is the top
    // row) right by B pixels. Pixels that would fall off the right end
    // appear at the left end of the row.
    if (this.screen.length !== screenHeight) console.log(`processRotateRow ${line} ${words.join()}`);
    if (words.length !== 5) {
      console.log(`Unexpected number of words ${words.length} in rotate row command ${line}`);
    } else {
      const numbers = words[2].split('=');
      if (numbers.length !== 2 || !words[2].startsWith('y')) {
        console.log(`Unexpected y=A ${words[2]} in rotate row command ${line}`);
      } else if (words[3] !== 'by') {
        console.log(`Missing by in rotate row command ${line}`);
      } else {
        const row = parseInt(numbers[1], 10);
        const shift = parseInt(words[4], 10);
        if (row < 0 || row > screenHeight - 1) {
          console.log(`Unexpected row ${row} for rotate row command ${line}`);
        } else if (shift < 1 || shift > screenWidth - 1) {
          console.log(`Unexpected shift ${shift} for rotate row command ${line}`);
        } else {
          this.screen[row] = (this.screen[row]
            + this.screen[row]).slice(screenWidth - shift, screenWidth + screenWidth - shift);
        }
      }
    }
  }

  show(): void {
    console.log(`${this.screen[0]}
${this.screen[1]}
${this.screen[2]}
${this.screen[3]}
${this.screen[4]}
${this.screen[5]}`);
  }

  count(): number {
    // 1. Start with nothing
    let result = 0;
    // 2. Loop for every row
    for (let row = 0; row < screenHeight; row += 1) {
      result += this.countRow(row);
    }
    return result;
  }

  countRow(rownum: number): number {
    // 1. Start with nothing
    let result = 0;
    // 2. For for every column in the row
    for (let col = 0; col < screenWidth; col += 1) {
      result += this.screen[rownum][col] === screenOn ? 1 : 0;
    }
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return this.count();
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
// end                       d i s p l a y . t s                      end
// ======================================================================
