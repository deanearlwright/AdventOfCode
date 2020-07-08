// ======================================================================
// Timing is Everything
//   Advent of Code 2016 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      d i s c s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_15';
import { Discs } from './discs';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
`;

interface ExampleTests {
  time: number;
  result: Number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { time: 0, result: 2 },
  { time: 1, result: 1 },
  { time: 2, result: 1 },
  { time: 3, result: 1 },
  { time: 4, result: 1 },
  { time: 5, result: 0 },
  { time: 6, result: 1 },
];

const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 5;
const PART_TWO_RESULT = 85;

// ======================================================================
//                                                              TestDiscs
// ======================================================================

describe('Discs', () => {
  test('Test the default Discs creation', () => {
    // 1. Create default Discs object
    const myobj = new Discs([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.time).toBe(0);
    expect(myobj.stack).toHaveLength(1);
    expect(myobj.stack[0].num).toBe(0);
    expect(myobj.stack[0].positions).toBe(1);
    expect(myobj.stack[0].time0).toBe(0);
    expect(myobj.stack[0].now).toBe(0);
  });

  test('Test the Discs object creation from text', () => {
    // 1. Create Discs object from text
    const myobj = new Discs(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.time).toBe(0);
    expect(myobj.stack).toHaveLength(3);
    expect(myobj.stack[0].num).toBe(0);
    expect(myobj.stack[0].positions).toBe(1);
    expect(myobj.stack[0].time0).toBe(0);
    expect(myobj.stack[0].now).toBe(0);
    expect(myobj.stack[1].num).toBe(1);
    expect(myobj.stack[1].positions).toBe(5);
    expect(myobj.stack[1].time0).toBe(4);
    expect(myobj.stack[1].now).toBe(4);
    expect(myobj.stack[2].num).toBe(2);
    expect(myobj.stack[2].positions).toBe(2);
    expect(myobj.stack[2].time0).toBe(1);
    expect(myobj.stack[2].now).toBe(1);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Discs object
      const myobj = new Discs(fromText(EXAMPLE_TEXT));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(2);
      // 3. Make sure it has the expected value
      expect(myobj.drop(test.time)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Discs object using the key as text
      const myobj = new Discs(fromText(EXAMPLE_TEXT), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(2);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Discs object', () => {
    // 1. Create Discs object from text
    const myobj = new Discs(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(true, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Discs object', () => {
    // 1. Create Discs object from text
    const myobj = new Discs(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(true, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    d i s c s . t e s t . t s                   end
// ======================================================================
