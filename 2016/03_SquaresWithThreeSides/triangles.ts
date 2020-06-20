// ======================================================================
// Squares With Three Sides
//   Advent of Code 2016 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t r i a n g l e s . t s
//
// A solver for the Advent of Code 2016 Day 03 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

type sidesTypes = [number, number, number];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                              Triangles
// ======================================================================

export class Triangles {
  // Object for Squares With Three Sides
  text: string[];

  part2: boolean;

  sides: sidesTypes[];

  constructor(text: string[], part2 = false) {
    // Create a Triangles object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.sides = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    const re = /\s+/;
    this.sides = [];
    this.text.forEach((line) => {
      const sides = line.trim().split(re);
      this.sides.push([parseInt(sides[0], 10), parseInt(sides[1], 10), parseInt(sides[2], 10)]);
    });
  }

  static isTriangle(sides: sidesTypes): boolean {
    return (sides[0] + sides[1] > sides[2])
      && (sides[0] + sides[2] > sides[1])
      && (sides[1] + sides[2] > sides[0]);
  }

  numTriangles(verbose: boolean, limit: number): number {
    if (verbose) console.log(`numTriangles ${limit}`);
    let result = 0;
    this.sides.forEach((sides) => {
      if (Triangles.isTriangle(sides)) {
        if (verbose) console.log(`${sides[0]} ${sides[1]} ${sides[2]} is a trangle`);
        result += 1;
      } else if (verbose) console.log(`${sides[0]} ${sides[1]} ${sides[2]} is not a trangle`);
    });
    return result;
  }

  numTrianglesInColumns(verbose: boolean, limit: number): number {
    if (verbose) console.log(`numTriangles ${limit}`);
    let result = 0;
    for (let triples = 0; triples < this.sides.length; triples += 3) {
      for (let index = 0; index < 3; index += 1) {
        const sides: sidesTypes = [this.sides[triples][index],
          this.sides[triples + 1][index],
          this.sides[triples + 2][index]];
        if (Triangles.isTriangle(sides)) {
          if (verbose) console.log(`${sides[0]} ${sides[1]} ${sides[2]} is a trangle`);
          result += 1;
        } else if (verbose) console.log(`${sides[0]} ${sides[1]} ${sides[2]} is not a trangle`);
      }
    }
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return NaN;
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.numTriangles(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.numTrianglesInColumns(verbose, limit);
  }
}

// ======================================================================
// end                     t r i a n g l e s . t s                    end
// ======================================================================
