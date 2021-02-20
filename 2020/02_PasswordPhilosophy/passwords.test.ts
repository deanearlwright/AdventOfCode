// ======================================================================
// Password Philosophy
//   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a s s w o r d s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_02';
import { Passwords } from './passwords';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 2;
const PART_TWO_RESULT = 1;

// ======================================================================
//                                                          TestPasswords
// ======================================================================

describe('Passwords', () => {
  test('Test the default Passwords creation', () => {
    // 1. Create default Passwords object
    const myobj = new Passwords([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.policies).toHaveLength(0);
  });

  test('Test the Passwords object creation from text', () => {
    // 1. Create Passwords object from text
    const myobj = new Passwords(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.policies).toHaveLength(3);
    // 3. Check methods
    expect(myobj.count_valid()).toBe(2);
  });

  test('Test part one example of Passwords object', () => {
    // 1. Create Passwords object from text
    const myobj = new Passwords(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Passwords object', () => {
    // 1. Create Passwords object from text
    const myobj = new Passwords(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                p a s s w o r d s . t e s t . t s               end
// ======================================================================
