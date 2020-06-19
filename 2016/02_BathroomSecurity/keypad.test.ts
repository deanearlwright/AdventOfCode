// ======================================================================
// Bathroom Security
//   Advent of Code 2016 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      k e y p a d . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_02';
import { Keypad } from './keypad';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `ULL
RRDDD
LURDL
UUUUD`;

interface exampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: exampleTests[] = [];
const EXAMPLES_PART_TWO: exampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = '1985';
const PART_TWO_RESULT = '5DB3';

// ======================================================================
//                                                             TestKeypad
// ======================================================================

describe('Keypad', () => {
  test('Test the default Keypad creation', () => {
    // 1. Create default Keypad object
    const myobj = new Keypad([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Keypad object creation from text', () => {
    // 1. Create Keypad object from text
    const myobj = new Keypad(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    // 3. Get the code
    expect(myobj.determineCode(false, 0)).toBe('1985');
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Keypad object
      const myobj = new Keypad(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Keypad object using the key as text
      const myobj = new Keypad(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Keypad object', () => {
    // 1. Create Keypad object from text
    const myobj = new Keypad(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Keypad object', () => {
    // 1. Create Keypad object from text
    const myobj = new Keypad(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   k e y p a d . t e s t . t s                  end
// ======================================================================
