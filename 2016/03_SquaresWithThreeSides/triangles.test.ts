// ======================================================================
// Squares With Three Sides
//   Advent of Code 2016 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t r i a n g l e s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 03 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_03';
import { Triangles } from './triangles';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
5 10 25
3 4 5
18 80 81
 18  80  81
`;

interface exampleTests {
  text: string;
  result: boolean;
}

const EXAMPLES_PART_ONE: exampleTests[] = [
  { text: '\n2 7 12', result: false },
  { text: '\n5 10 25', result: false },
  { text: '\n3 4 5', result: true },
  { text: '\n18 80 81', result: true },
  { text: '\n 18  80  81 ', result: true },
];

const EXAMPLES_PART_TWO: exampleTests[] = [
  { text: '\n101 102 103', result: true },
  { text: '\n201 202 203', result: true },
  { text: '\n301 302 303', result: true },
  { text: '\n401 402 403', result: true },
  { text: '\n501 502 503', result: true },
  { text: '\n601 602 603', result: true },
  { text: '\n101 301 501', result: false },
  { text: '\n102 302 502', result: false },
  { text: '\n103 303 503', result: false },
  { text: '\n201 401 601', result: true },
  { text: '\n202 402 602', result: true },
  { text: '\n203 403 603', result: true },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = `
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
`;

const PART_ONE_RESULT = 3;
const PART_TWO_RESULT = 6;

// ======================================================================
//                                                          TestTriangles
// ======================================================================

describe('Triangles', () => {
  test('Test the default Triangles creation', () => {
    // 1. Create default Triangles object
    const myobj = new Triangles([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Triangles object creation from text', () => {
    // 1. Create Triangles object from text
    const myobj = new Triangles(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Triangles object
      const myobj = new Triangles(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(Triangles.isTriangle(myobj.sides[0])).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Triangles object using the key as text
      const myobj = new Triangles(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      // console.log(`${test.text} ${Triangles.isTriangle(myobj.sides[0])}`);
      expect(Triangles.isTriangle(myobj.sides[0])).toBe(test.result);
    });
  });

  test('Test part one example of Triangles object', () => {
    // 1. Create Triangles object from text
    const myobj = new Triangles(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Triangles object', () => {
    // 1. Create Triangles object from text
    const myobj = new Triangles(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                t r i a n g l e s . t e s t . t s               end
// ======================================================================
