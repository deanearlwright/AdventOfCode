/* eslint-disable linebreak-style */
// ======================================================================
// No Time for a Taxicab
//   Advent of Code 2016 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t a x i c a b . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 01 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_01';

import { Taxicab } from './taxicab';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
R5, L5, R5, R3
`;

interface exampleTests {
  text: string;
  result: number;
  instLen: number;
}

const EXAMPLES_PART_ONE: exampleTests[] = [
  { text: 'R2, L3', result: 5, instLen: 2 },
  { text: 'R2, R2, R2', result: 2, instLen: 3 },
  { text: 'R5, L5, R5, R3', result: 12, instLen: 4 },
];

const EXAMPLES_PART_TWO: exampleTests[] = [
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = `
R8, R4, R4, R8
`;

const PART_ONE_RESULT = 12;
const PART_TWO_RESULT = 4;

// ======================================================================
//                                                            TestTaxicab
// ======================================================================

describe('Taxicab', () => {
  test('Test the default Taxicab creation', () => {
    // 1. Create default Taxicab object
    const myobj = new Taxicab([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.instructions).toHaveLength(0);
  });

  test('Test the Taxicab object creation from text', () => {
    // 1. Create Taxicab object from text
    const myobj = new Taxicab(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.instructions).toHaveLength(4);
    expect(myobj.instructions[0].direction).toBe('R');
    expect(myobj.instructions[0].blocks).toBe(5);
    expect(myobj.instructions[1].direction).toBe('L');
    expect(myobj.instructions[1].blocks).toBe(5);
    expect(myobj.instructions[2].direction).toBe('R');
    expect(myobj.instructions[2].blocks).toBe(5);
    expect(myobj.instructions[3].direction).toBe('R');
    expect(myobj.instructions[3].blocks).toBe(3);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Taxicab object
      const myobj = new Taxicab([test.text]);
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.instructions).toHaveLength(test.instLen);
      // 3. Make sure it has the expected value
      expect(myobj.routeDistance(false, 0)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Taxicab object using the key as text
      const myobj = new Taxicab(fromText(test.text), true);
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      // expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Taxicab object', () => {
    // 1. Create Taxicab object from text
    const myobj = new Taxicab(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Taxicab object', () => {
    // 1. Create Taxicab object from text
    const myobj = new Taxicab(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   t a x i c a b . t e s t . t s                end
// ======================================================================
