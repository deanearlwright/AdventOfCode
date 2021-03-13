// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b u s e s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_13';
import { Buses } from './buses';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
939
7,13,x,x,59,x,31,19
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 295;
const PART_TWO_RESULT = 1068781;

// ======================================================================
//                                                              TestBuses
// ======================================================================

describe('Buses', () => {
  test('Test the default Buses creation', () => {
    // 1. Create default Buses object
    const myobj = new Buses([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.earliest).toBe(0);
    expect(myobj.buses).toHaveLength(0);
  });

  test('Test the Buses object creation from text', () => {
    // 1. Create Buses object from text
    const myobj = new Buses(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.earliest).toBe(939);
    expect(myobj.buses).toHaveLength(5);
    // 3. Test methods
    expect(myobj.waiting()).toBe(295);
  });

  test('Test part one example of Buses object', () => {
    // 1. Create Buses object from text
    const myobj = new Buses(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Buses object', () => {
    // 1. Create Buses object from text
    const myobj = new Buses(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   b u s e s . t e s t . t s                  end
// ======================================================================
