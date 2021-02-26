// ======================================================================
// Custom Customs
//   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      g r o u p s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_06';
import { Groups } from './groups';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
abc

a
b
c

ab
ac

a
a
a
a

b
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 11;
const PART_TWO_RESULT = 6;

// ======================================================================
//                                                              TestGroups
// ======================================================================

describe('Groups', () => {
  test('Test the default Groups creation', () => {
    // 1. Create default Groups object
    const myobj = new Groups([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.groups).toHaveLength(0);
  });

  test('Test the Groups object creation from text', () => {
    // 1. Create Groups object from text
    const myobj = new Groups(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(17);
    expect(myobj.groups).toHaveLength(5);
  });

  test('Test part one example of Groups object', () => {
    // 1. Create Groups object from text
    const myobj = new Groups(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Groups object', () => {
    // 1. Create Groups object from text
    const myobj = new Groups(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   g r o u p s . t e s t . t s                  end
// ======================================================================
