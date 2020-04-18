/* eslint-disable linebreak-style */
// ======================================================================
// Elves Look Elves Say
//   Advent of Code 2015 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                  l o o k a n d s a y . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 10 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc10 = require('./aoc_10');
const lookandsay = require('./lookandsay');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '1\n';

const EXAMPLES_PART_ONE = {
  1: '11',
  11: '21',
  21: '1211',
  1211: '111221',
  111221: '312211',
};
const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 82350;
const PART_TWO_RESULT = 1166642;

// ======================================================================
//                                                         TestLookandsay
// ======================================================================

describe('Lookandsay', () => {
  test('Test the default Lookandsay creation', () => {
    // 1. Create default Lookandsay object
    const myobj = new lookandsay.Lookandsay({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Lookandsay object creation from text', () => {
    // 1. Create Lookandsay object from text
    const myobj = new lookandsay.Lookandsay({ text: aoc10.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Lookandsay object using the key as text
      const myobj = new lookandsay.Lookandsay({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.nextPhrase()).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Lookandsay object using the key as text
      const myobj = new lookandsay.Lookandsay({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.lookandsay(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Lookandsay object', () => {
    // 1. Create Lookandsay object from text
    const myobj = new lookandsay.Lookandsay({ text: aoc10.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Lookandsay object', () => {
    // 1. Create Lookandsay object from text
    const myobj = new lookandsay.Lookandsay({ part2: true, text: aoc10.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                t e s t _ l o o k a n d s a y . j s             end
// ======================================================================
