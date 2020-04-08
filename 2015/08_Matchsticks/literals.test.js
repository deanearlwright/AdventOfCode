/* eslint-disable linebreak-style */
// ======================================================================
// Matchsticks
//   Advent of Code 2015 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      l i t e r a l s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc08 = require('./aoc_08');
const literals = require('./literals');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\n""\n"abc"\n"aaa\\"aaa"\n"\\x27"';

const EXAMPLES_PART_ONE = {
  '""': [2, 0],
  '"abc"': [5, 3],
  '"aaa\\"aaa"': [10, 7],
  '"\\x27"': [6, 1],
  '"\\\\"': [4, 1],
  '"aaa\\"aaa\\x27aaa\\\\aaa"': [2 + 12 + 2 + 4 + 2, 12 + 1 + 1 + 1],
};

const EXAMPLES_PART_TWO = {
  '""': [2, 6],
  '"abc"': [5, 9],
  '"aaa\\"aaa"': [10, 16],
  '"\\x27"': [6, 11],
  '"\\\\"': [4, 10],
  '"aaa\\"aaa\\x27aaa\\\\aaa"': [2 + 12 + 2 + 4 + 2, 12 + 4 + 4 + 7 + 4],
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 23 - 11;
const PART_TWO_RESULT = 42 - 23;

// ======================================================================
//                                                           TestLiterals
// ======================================================================

describe('Literals', () => {
  test('Test the default Literals creation', () => {
    // 1. Create default Literals object
    const myobj = new literals.Literals({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Literals object creation from text', () => {
    // 1. Create Literals object from text
    const myobj = new literals.Literals({ text: aoc08.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Literals object using the key at text
      const myobj = new literals.Literals({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3.  Make sure it has the expected values
      expect(myobj.getLengths(key)).toStrictEqual(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Literals object using the key at text
      const myobj = new literals.Literals({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected values
      expect(myobj.getLengths(key)).toStrictEqual(EXAMPLES_PART_TWO[key]);
    });
  });


  test('Test part one example of Literals object', () => {
    // 1. Create Literals object from text
    const myobj = new literals.Literals({ text: aoc08.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Literals object', () => {
    // 1. Create Literals object from text
    const myobj = new literals.Literals({ part2: true, text: aoc08.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  t e s t _ l i t e r a l s . j s               end
// ======================================================================
