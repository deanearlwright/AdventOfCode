// ======================================================================
// Operation Order
//   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      h o m e w o r k . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_18';
import { Homework } from './homework';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 26 + 437 + 12240 + 13632;
const PART_TWO_RESULT = 46 + 1445 + 669060 + 23340;

// ======================================================================
//                                                           TestHomework
// ======================================================================

describe('Homework', () => {
  test('Test the default Homework creation', () => {
    // 1. Create default Homework object
    const myobj = new Homework([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.expressions).toHaveLength(0);
  });

  test('Test the Homework object creation from text', () => {
    // 1. Create Homework object from text
    const myobj = new Homework(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.expressions).toHaveLength(4);

    // 3. Check methods
    expect(myobj.evaluateAll()).toBe(PART_ONE_RESULT);
  });

  test('Test part one example of Homework object', () => {
    // 1. Create Homework object from text
    const myobj = new Homework(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Homework object', () => {
    // 1. Create Homework object from text
    const myobj = new Homework(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 h o m e w o r k . t e s t . t s                end
// ======================================================================
