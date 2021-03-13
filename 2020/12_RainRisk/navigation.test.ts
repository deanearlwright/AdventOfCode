// ======================================================================
// Rain Risk
//   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      n a v i g a t i o n . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_12';
import { Navigation } from './navigation';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
F10
N3
F7
R90
F11
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 25;
const PART_TWO_RESULT = 286;

// ======================================================================
//                                                         TestNavigation
// ======================================================================

describe('Navigation', () => {
  test('Test the default Navigation creation', () => {
    // 1. Create default Navigation object
    const myobj = new Navigation([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Navigation object creation from text', () => {
    // 1. Create Navigation object from text
    const myobj = new Navigation(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(5);
  });

  test('Test part one example of Navigation object', () => {
    // 1. Create Navigation object from text
    const myobj = new Navigation(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Navigation object', () => {
    // 1. Create Navigation object from text
    const myobj = new Navigation(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end               n a v i g a t i o n . t e s t . t s              end
// ======================================================================
