// ======================================================================
// Docking Data
//   Advent of Code 2020 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b i t m a s k . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_14';
import { Bitmask } from './bitmask';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
`;

const EXAMPLE_TWO = `
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TWO;

const PART_ONE_RESULT = 165;
const PART_TWO_RESULT = 208;

// ======================================================================
//                                                            TestBitmask
// ======================================================================

describe('Bitmask', () => {
  test('Test the default Bitmask creation', () => {
    // 1. Create default Bitmask object
    const myobj = new Bitmask([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.bitmask).toBe('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
    expect(myobj.memory).toStrictEqual({});
  });

  test('Test the Bitmask object creation from text', () => {
    // 1. Create Bitmask object from text
    const myobj = new Bitmask(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.bitmask).toBe('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
    expect(myobj.memory).toStrictEqual({});
  });

  test('Test part one example of Bitmask object', () => {
    // 1. Create Bitmask object from text
    const myobj = new Bitmask(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Bitmask object', () => {
    // 1. Create Bitmask object from text
    const myobj = new Bitmask(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  b i t m a s k . t e s t . t s                 end
// ======================================================================
