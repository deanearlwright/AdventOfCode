// ======================================================================
// Binary Boarding
//   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p h o n e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_05';
import { Phone } from './phone';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 820;
const PART_TWO_RESULT = 819;

// ======================================================================
//                                                              TestPhone
// ======================================================================

describe('Phone', () => {
  test('Test the default Phone creation', () => {
    // 1. Create default Phone object
    const myobj = new Phone([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.passes).toHaveLength(0);
  });

  test('Test the Phone object creation from text', () => {
    // 1. Create Phone object from text
    const myobj = new Phone(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.passes).toHaveLength(3);

    // 3. Check Methods
    expect(myobj.highestSeat()).toBe(820);
  });

  test('Test part one example of Phone object', () => {
    // 1. Create Phone object from text
    const myobj = new Phone(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Phone object', () => {
    // 1. Create Phone object from text
    const myobj = new Phone(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    p h o n e . t e s t . t s                   end
// ======================================================================
