// ======================================================================
// An Elephant Named Joseph
//   Advent of Code 2016 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a r t y . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_19';
import { Party } from './party';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
5
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: '1', result: 1 },
  { text: '2', result: 1 },
  { text: '3', result: 3 },
  { text: '4', result: 1 },
  { text: '5', result: 3 },
  { text: '6', result: 5 },
  { text: '7', result: 7 },
  { text: '8', result: 1 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: '1', result: 1 },
  { text: '2', result: 1 },
  { text: '3', result: 3 },
  { text: '4', result: 1 },
  { text: '5', result: 2 },
  { text: '6', result: 3 },
  { text: '7', result: 5 },
  { text: '8', result: 7 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 3;
const PART_TWO_RESULT = 2;

// ======================================================================
//                                                              TestParty
// ======================================================================

describe('Party', () => {
  test('Test the default Party creation', () => {
    // 1. Create default Party object
    const myobj = new Party([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.numElves).toBe(0);
    expect(myobj.elves).toHaveLength(0);
  });

  test('Test the Party object creation from text', () => {
    // 1. Create Party object from text
    const myobj = new Party(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.numElves).toBe(5);
    expect(myobj.elves).toHaveLength(5);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Party object
      const myobj = new Party(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Party object using the key as text
      const myobj = new Party(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Party object', () => {
    // 1. Create Party object from text
    const myobj = new Party(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Party object', () => {
    // 1. Create Party object from text
    const myobj = new Party(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    p a r t y . t e s t . t s                   end
// ======================================================================
