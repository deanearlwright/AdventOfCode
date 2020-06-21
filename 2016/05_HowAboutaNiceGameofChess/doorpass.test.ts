// ======================================================================
// How About a Nice Game of Chess
//   Advent of Code 2016 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      d o o r p a s s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_05';
import { Doorpass } from './doorpass';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
abc
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = '18f47a30';
const PART_TWO_RESULT = '05ace8e3';

// ======================================================================
//                                                           TestDoorpass
// ======================================================================

describe('Doorpass', () => {
  test('Test the default Doorpass creation', () => {
    // 1. Create default Doorpass object
    const myobj = new Doorpass([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.id).toBe('');
  });

  test('Test the Doorpass object creation from text', () => {
    // 1. Create Doorpass object from text
    const myobj = new Doorpass(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.id).toBe('abc');
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Doorpass object
      const myobj = new Doorpass(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution(false, 0)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Doorpass object using the key as text
      const myobj = new Doorpass(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Doorpass object', () => {
    // 1. Create Doorpass object from text
    const myobj = new Doorpass(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Doorpass object', () => {
    // 1. Create Doorpass object from text
    const myobj = new Doorpass(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(true, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 d o o r p a s s . t e s t . t s                end
// ======================================================================
