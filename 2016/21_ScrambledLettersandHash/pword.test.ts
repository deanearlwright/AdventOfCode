// ======================================================================
// Scrambled Letters and Hash
//   Advent of Code 2016 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p w o r d . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_21';
import { Pword } from './pword';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step 
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
`;

interface ExampleTests {
  text: string;
  start: string;
  result: string;
}

interface ExampleTwoTests {
  text: string;
  result: string;
  finish: string;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: 'swap position 4 with position 0', start: 'abcde', result: 'ebcda' },
  { text: 'swap letter d with letter b', start: 'ebcda', result: 'edcba' },
  { text: 'reverse positions 0 through 4', start: 'edcba', result: 'abcde' },
  { text: 'rotate left 1 step', start: 'abcde', result: 'bcdea' },
  { text: 'move position 1 to position 4', start: 'bcdea', result: 'bdeac' },
  { text: 'move position 3 to position 0', start: 'bdeac', result: 'abdec' },
  { text: 'rotate based on position of letter b', start: 'abdec', result: 'ecabd' },
  { text: 'rotate based on position of letter d', start: 'ecabd', result: 'decab' },
];
const EXAMPLES_PART_TWO: ExampleTwoTests[] = [
  { text: 'swap position 4 with position 0', result: 'abcde', finish: 'ebcda' },
  { text: 'swap letter d with letter b', result: 'ebcda', finish: 'edcba' },
  { text: 'reverse positions 0 through 4', result: 'edcba', finish: 'abcde' },
  { text: 'rotate left 1 step', result: 'abcde', finish: 'bcdea' },
  { text: 'move position 1 to position 4', result: 'bcdea', finish: 'bdeac' },
  { text: 'move position 3 to position 0', result: 'bdeac', finish: 'abdec' },
  { text: 'rotate based on position of letter b', result: 'abdec', finish: 'ecabd' },
  { text: 'rotate based on position of letter d', result: 'ecabd', finish: 'decab' },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_START = 'abcde';
const PART_TWO_FINISH = 'decab';

const PART_ONE_RESULT = 'decab';
const PART_TWO_RESULT = 'abcde';

// ======================================================================
//                                                              TestPword
// ======================================================================

describe('Pword', () => {
  test('Test the default Pword creation', () => {
    // 1. Create default Pword object
    const myobj = new Pword([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.start).toBe('abcdefgh');
    expect(myobj.finish).toBe('fbgdceah');
    expect(myobj.instructions).toHaveLength(0);
  });

  test('Test the Pword object creation from text', () => {
    // 1. Create Pword object from text
    const myobj = new Pword(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(8);
    expect(myobj.start).toBe('abcdefgh');
    expect(myobj.finish).toBe('fbgdceah');
    expect(myobj.instructions).toHaveLength(8);
    expect(myobj.instructions[0].action).toBe('swap position');
    expect(myobj.instructions[0].op1).toBe('4');
    expect(myobj.instructions[0].op2).toBe('0');
    expect(myobj.instructions[7].action).toBe('rotate based');
    expect(myobj.instructions[7].op1).toBe('d');
    expect(myobj.instructions[7].op2).toBe('X');
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Pword object
      const myobj = new Pword(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      myobj.start = test.start;
      expect(myobj.scramble(false)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Pword object using the key as text
      const myobj = new Pword(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      myobj.finish = test.finish;
      expect(myobj.solution(false)).toBe(test.result);
    });
  });

  test('Test part one example of Pword object', () => {
    // 1. Create Pword object from text
    const myobj = new Pword(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    myobj.start = PART_ONE_START;
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Pword object', () => {
    // 1. Create Pword object from text
    const myobj = new Pword(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    myobj.finish = PART_TWO_FINISH;
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    p w o r d . t e s t . t s                   end
// ======================================================================
