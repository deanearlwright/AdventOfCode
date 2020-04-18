/* eslint-disable linebreak-style */
// ======================================================================
// Corporate Policy
//   Advent of Code 2015 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a s s w o r d . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc11 = require('./aoc_11');
const password = require('./password');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'abcdefgh\n';

const IS_VALID_PART_ONE = {
  hijklmmn: false,
  abbceffg: false,
  abbcegjk: false,
  abcdffaa: true,
  ghjaabcc: true,
};

const INCREMENT_PART_ONE = {
  abcdefgh: 'abcdefgj',
  ghijklmz: 'ghjaaaaa',
};

const EXAMPLE_PART_ONE = {
  abcdefgh: 'abcdffaa',
  ghijklmn: 'ghjaabcc',
};

const EXAMPLES_PART_TWO = {
  abcdefgh: 'abcdffbb',
  ghijklmn: 'ghjbbcdd',
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 'abcdffaa';
const PART_TWO_RESULT = 'abcdffbb';

// ======================================================================
//                                                           TestPassword
// ======================================================================

describe('Password', () => {
  test('Test the default Password creation', () => {
    // 1. Create default Password object
    const myobj = new password.Password({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Password object creation from text', () => {
    // 1. Create Password object from text
    const myobj = new password.Password({ text: aoc11.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
  });

  test('Test part one isValid', () => {
    // 1. Loop for all of the examples
    Object.keys(IS_VALID_PART_ONE).forEach((key) => {
      // 2. Create Password object using the key as text
      const myobj = new password.Password({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(password.Password.isValid(key)).toBe(IS_VALID_PART_ONE[key]);
    });
  });

  test('Test part one increment', () => {
    // 1. Loop for all of the examples
    Object.keys(INCREMENT_PART_ONE).forEach((key) => {
      // 2. Create Password object using the key as text
      const myobj = new password.Password({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(password.Password.increment(key)).toBe(INCREMENT_PART_ONE[key]);
    });
  });

  test('Test all of part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLE_PART_ONE).forEach((key) => {
      // 2. Create Password object using the key as text
      const myobj = new password.Password({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.partOne({})).toBe(EXAMPLE_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Password object using the key as text
      const myobj = new password.Password({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.partTwo({})).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Password object', () => {
    // 1. Create Password object from text
    const myobj = new password.Password({ text: aoc11.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Password object', () => {
    // 1. Create Password object from text
    const myobj = new password.Password({ part2: true, text: aoc11.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  t e s t _ p a s s w o r d . j s               end
// ======================================================================
