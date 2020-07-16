// ======================================================================
// Firewall Rules
//   Advent of Code 2016 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b l a c k l i s t . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_20';
import { Blacklist } from './blacklist';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
5-8
0-2
4-7
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 3;
const PART_TWO_RESULT = 4294967295 + 2 - 9;

// ======================================================================
//                                                          TestBlacklist
// ======================================================================

describe('Blacklist', () => {
  test('Test the default Blacklist creation', () => {
    // 1. Create default Blacklist object
    const myobj = new Blacklist([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.ranges).toHaveLength(0);
    expect(myobj.sorted).toHaveLength(0);
  });

  test('Test the Blacklist object creation from text', () => {
    // 1. Create Blacklist object from text
    const myobj = new Blacklist(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.ranges).toHaveLength(3);
    expect(myobj.ranges[0].low).toBe(5);
    expect(myobj.ranges[2].high).toBe(7);
    expect(myobj.sorted).toHaveLength(3);
    expect(myobj.sorted[0].low).toBe(0);
    expect(myobj.sorted[2].high).toBe(8);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Blacklist object
      const myobj = new Blacklist(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Blacklist object using the key as text
      const myobj = new Blacklist(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Blacklist object', () => {
    // 1. Create Blacklist object from text
    const myobj = new Blacklist(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Blacklist object', () => {
    // 1. Create Blacklist object from text
    const myobj = new Blacklist(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                b l a c k l i s t . t e s t . t s               end
// ======================================================================
