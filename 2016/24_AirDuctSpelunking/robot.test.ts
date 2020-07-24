// ======================================================================
// Air Duct Spelunking
//   Advent of Code 2016 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r o b o t . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_24';
import { Robot } from './robot';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '';

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = NaN;
const PART_TWO_RESULT = NaN;

// ======================================================================
//                                                              TestRobot
// ======================================================================

describe('Robot', () => {
  test('Test the default Robot creation', () => {
    // 1. Create default Robot object
    const myobj = new Robot([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Robot object creation from text', () => {
    // 1. Create Robot object from text
    const myobj = new Robot(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Robot object
      const myobj = new Robot(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Robot object using the key as text
      const myobj = new Robot(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Robot object', () => {
    // 1. Create Robot object from text
    const myobj = new Robot(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Robot object', () => {
    // 1. Create Robot object from text
    const myobj = new Robot(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   r o b o t . t e s t . t s                  end
// ======================================================================
