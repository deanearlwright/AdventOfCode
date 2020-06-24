// ======================================================================
// Two-Factor Authentication
//   Advent of Code 2016 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      d i s p l a y . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_08';
import { Display } from './display';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1';

interface ExampleTests {
  text: string;
  result: Number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: 'rect 3x2\n', result: 6 },
  { text: 'rect 3x2\nrotate column x=1 by 1', result: 6 },
  { text: 'rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4', result: 6 },
  { text: 'rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1', result: 6 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 6;
const PART_TWO_RESULT = NaN;

// ======================================================================
//                                                            TestDisplay
// ======================================================================

describe('Display', () => {
  test('Test the default Display creation', () => {
    // 1. Create default Display object
    const myobj = new Display([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.screen).toHaveLength(6);
    expect(myobj.screen[0]).toHaveLength(50);
    expect(myobj.screen[0][0]).toBe('.');
  });

  test('Test the Display object creation from text', () => {
    // 1. Create Display object from text
    const myobj = new Display(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.screen).toHaveLength(6);
    expect(myobj.screen[0]).toHaveLength(50);
    expect(myobj.screen[0][0]).toBe('.');
    expect(myobj.screen[1][0]).toBe('#');
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Display object
      const myobj = new Display(fromText(test.text));
      expect(myobj.part2).toBe(false);
      // 3. Make sure it has the expected value
      myobj.show();
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Display object using the key as text
      const myobj = new Display(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Display object', () => {
    // 1. Create Display object from text
    const myobj = new Display(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Display object', () => {
    // 1. Create Display object from text
    const myobj = new Display(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  d i s p l a y . t e s t . t s                 end
// ======================================================================
