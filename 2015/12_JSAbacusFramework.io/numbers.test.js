/* eslint-disable linebreak-style */
// ======================================================================
// JSAbacusFramework.io
//   Advent of Code 2015 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      n u m b e r s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc12 = require('./aoc_12');
const numbers = require('./numbers');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\n{"a":{"b":4},"c":-1}\n';

const EXAMPLES_PART_ONE = {
  '[1,2,3]': 6,
  '{"a":2,"b":4}': 6,
  '[[[3]]]': 3,
  '{"a":{"b":4},"c":-1}': 3,
  '{"a":[-1,1]}': 0,
  '[-1,{"a":1}]': 0,
  '[]': 0,
  '{}': 0,
  '[1,{"c":"red","b":2},3]': 6,
  '{"d":"red","e":[1,2,3,4],"f":5}': 15,
  '[1,"red",5]': 6,
};
const NORED_PART_TWO = {
  '[1,2,3]': '[1,2,3]',
  '{"a":2,"b":4}': '{"a":2,"b":4}',
  '[[[3]]]': '[[[3]]]',
  '{"a":{"b":4},"c":-1}': '{"a":{"b":4},"c":-1}',
  '{"a":[-1,1]}': '{"a":[-1,1]}',
  '[-1,{"a":1}]': '[-1,{"a":1}]',
  '[]': '[]',
  '{}': '{}',
  '[1,{"c":"red","b":2},3]': '[1,,3]',
  '{"d":"red","e":[1,2,3,4],"f":5}': '',
  '[1,"red",5]': '[1,"red",5]',
  '{"a":{[1,2]},"d":"red","e":[1,2,3,4],"f":5}': '',
};
const EXAMPLES_PART_TWO = {
  '[1,2,3]': 6,
  '{"a":2,"b":4}': 6,
  '[[[3]]]': 3,
  '{"a":{"b":4},"c":-1}': 3,
  '{"a":[-1,1]}': 0,
  '[-1,{"a":1}]': 0,
  '[]': 0,
  '{}': 0,
  '[1,{"c":"red","b":2},3]': 4,
  '{"d":"red","e":[1,2,3,4],"f":5}': 0,
  '[1,"red",5]': 6,
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = '\n[1,{"c":"red","b":2},3]';

const PART_ONE_RESULT = 3;
const PART_TWO_RESULT = 4;

// ======================================================================
//                                                            TestNumbers
// ======================================================================

describe('Numbers', () => {
  test('Test the default Numbers creation', () => {
    // 1. Create default Numbers object
    const myobj = new numbers.Numbers({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Numbers object creation from text', () => {
    // 1. Create Numbers object from text
    const myobj = new numbers.Numbers({ text: aoc12.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Numbers object using the key as text
      const myobj = new numbers.Numbers({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(numbers.Numbers.sum(key)).toBe(EXAMPLES_PART_ONE[key]);
      expect(myobj.partOne({})).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test nored examples for part two', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(NORED_PART_TWO).forEach((key) => {
      // 2. Create Numbers object using the key as text
      const myobj = new numbers.Numbers({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(numbers.Numbers.nored(key)).toBe(NORED_PART_TWO[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Numbers object using the key as text
      const myobj = new numbers.Numbers({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.partTwo({})).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Numbers object', () => {
    // 1. Create Numbers object from text
    const myobj = new numbers.Numbers({ text: aoc12.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Numbers object', () => {
    // 1. Create Numbers object from text
    const myobj = new numbers.Numbers({ part2: true, text: aoc12.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   t e s t _ n u m b e r s . j s                end
// ======================================================================
