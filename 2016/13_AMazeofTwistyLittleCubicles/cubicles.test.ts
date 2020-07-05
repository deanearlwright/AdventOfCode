// ======================================================================
// A Maze of Twisty Little Cubicles
//   Advent of Code 2016 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c u b i c l e s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_13';
import { Cubicles } from './cubicles';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
10
`;

interface ExampleTests {
  input: number;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { input: 1, result: 1 },
  { input: 0, result: 2 },
  { input: 1002, result: 1 },
  { input: 4001, result: 5 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { input: 1, result: 3 },
  { input: 2, result: 3 + 2 },
  { input: 3, result: 3 + 2 + 1 },
  { input: 4, result: 3 + 2 + 1 + 3 },
  { input: 5, result: 3 + 2 + 1 + 3 + 2 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 11;
const PART_TWO_RESULT = 41;

// ======================================================================
//                                                           TestCubicles
// ======================================================================

describe('Cubicles', () => {
  test('Test the default Cubicles creation', () => {
    // 1. Create default Cubicles object
    const myobj = new Cubicles([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.start).toBe(1001);
    expect(myobj.finish).toBe(31039);
    expect(Object.keys(myobj.cubes)).toHaveLength(1);
    expect(1000 in myobj.cubes).toBe(false);
    expect(1001 in myobj.cubes).toBe(true);
    expect(myobj.cubes[1001].location).toBe(1001);
    expect(myobj.cubes[1001].previous).toBe(NaN);
    expect(myobj.cubes[1001].fromStart).toBe(0);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.favorite).toBe(0);
  });

  test('Test the Cubicles object creation from text', () => {
    // 1. Create Cubicles object from text
    const myobj = new Cubicles(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.start).toBe(1001);
    expect(myobj.finish).toBe(31039);
    expect(Object.keys(myobj.cubes)).toHaveLength(1);
    expect(1000 in myobj.cubes).toBe(false);
    expect(1001 in myobj.cubes).toBe(true);
    expect(myobj.cubes[1001].location).toBe(1001);
    expect(myobj.cubes[1001].previous).toBe(NaN);
    expect(myobj.cubes[1001].fromStart).toBe(0);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.favorite).toBe(10);
    // 3. Check walls vs. cubes
    expect(myobj.isItCube(0)).toBe(true);
    expect(myobj.isItCube(1)).toBe(true);
    expect(myobj.isItCube(2)).toBe(false);
    expect(myobj.isItCube(3)).toBe(false);
    expect(myobj.isItCube(1000)).toBe(false);
    expect(myobj.isItCube(1001)).toBe(true);
    expect(myobj.isItCube(1002)).toBe(true);
    expect(myobj.isItCube(1003)).toBe(false);
    expect(myobj.isItCube(2000)).toBe(true);
    expect(myobj.isItCube(2001)).toBe(false);
    expect(myobj.isItCube(2002)).toBe(true);
    expect(myobj.isItCube(2003)).toBe(false);
    expect(myobj.isItCube(3000)).toBe(false);
    expect(myobj.isItCube(3001)).toBe(true);
    expect(myobj.isItCube(3002)).toBe(true);
    expect(myobj.isItCube(3003)).toBe(true);
    expect(myobj.isItCube(7004)).toBe(true);
    // 4. Check making path
    expect(myobj.nextCube(myobj.start)).toBe(1002);
    expect(myobj.nextCube(myobj.start)).toBe(1);
    expect(myobj.nextCube(1002)).toBe(2002);
    expect(myobj.nextCube(2002)).toBe(3002);
    expect(myobj.nextCube(3002)).toBe(3001);
    expect(myobj.nextCube(3002)).toBe(4002);
    expect(myobj.nextCube(3002)).toBe(3003);
    expect(myobj.nextCube(3002)).toBe(-1);
    expect(myobj.nextCube(3003)).toBe(3004);
    expect(myobj.nextCube(3004)).toBe(4004);
    expect(myobj.nextCube(4004)).toBe(4005);
    expect(myobj.nextCube(4005)).toBe(5005);
    expect(myobj.nextCube(5005)).toBe(6005);
    expect(myobj.nextCube(6005)).toBe(6004);
    expect(myobj.nextCube(6004)).toBe(7004);
    expect(myobj.cubes[7004].fromStart).toBe(11);
    expect(myobj.cubes[7004].previous).toBe(6004);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Cubicles object
      const myobj = new Cubicles(fromText(EXAMPLE_TEXT));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      myobj.finish = test.input;
      myobj.wall = 10;
      // 3. Make sure it has the expected value
      expect(myobj.solution(false)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Cubicles object using the key as text
      const myobj = new Cubicles(fromText(EXAMPLE_TEXT), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      myobj.wall = 10;
      myobj.furthest = test.input;
      // 3. Make sure it has the expected value
      expect(myobj.solution(false, 1000)).toBe(test.result);
    });
  });

  test('Test part one example of Cubicles object', () => {
    // 1. Create Cubicles object from text
    const myobj = new Cubicles(fromText(PART_ONE_TEXT));
    myobj.finish = 7004;
    myobj.wall = 10;
    // 2. Check the part one result
    expect(myobj.partOne(false, 1000)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Cubicles object', () => {
    // 1. Create Cubicles object from text
    const myobj = new Cubicles(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 50)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 c u b i c l e s . t e s t . t s                end
// ======================================================================
