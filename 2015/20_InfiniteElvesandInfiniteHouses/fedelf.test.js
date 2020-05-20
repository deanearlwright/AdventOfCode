/* eslint-disable linebreak-style */
// ======================================================================
// Infinite Elves and Infinite Houses
//   Advent of Code 2015 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      f e d e l f . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc20 = require('./aoc_20');
const fedelf = require('./fedelf');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '125';

const EXAMPLES_PART_ONE_PPH = {
  1: 10,
  2: 30,
  3: 40,
  4: 70,
  5: 60,
  6: 120,
  7: 80,
  8: 150,
  9: 130,
};

const EXAMPLES_PART_ONE_FHP = {
  5: 1,
  10: 1,
  15: 2,
  20: 2,
  25: 2,
  30: 2,
  35: 3,
  40: 3,
  45: 4,
  50: 4,
  55: 4,
  60: 4,
  65: 4,
  70: 4,
  75: 6,
  80: 6,
  90: 6,
  100: 6,
  110: 6,
  120: 6,
  125: 8,
  130: 8,
  135: 8,
  140: 8,
  145: 8,
  150: 8,
};

const EXAMPLES_PART_TWO_PPH = {
  1: 11,
  2: 33,
  3: 44,
  4: 77,
  5: 66,
  6: 132,
  7: 88,
  8: 165,
  9: 143,
};

const EXAMPLES_PART_TWO_FHP = {
  5: 1,
  10: 1,
  15: 2,
  20: 2,
  25: 2,
  30: 2,
  35: 3,
  40: 3,
  45: 4,
  50: 4,
  55: 4,
  60: 4,
  65: 4,
  70: 4,
  75: 4,
  80: 6,
  90: 6,
  100: 6,
  110: 6,
  120: 6,
  125: 6,
  130: 6,
  135: 8,
  140: 8,
  145: 8,
  150: 8,
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 8;
const PART_TWO_RESULT = 6;

// ======================================================================
//                                                             TestFedelf
// ======================================================================

describe('Fedelf', () => {
  test('Test the default Fedelf creation', () => {
    // 1. Create default Fedelf object
    const myobj = new fedelf.Fedelf({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.presents).toBe(null);
  });

  test('Test the Fedelf object creation from text', () => {
    // 1. Create Fedelf object from text
    const myobj = new fedelf.Fedelf({ text: aoc20.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.presents).toBe(125);
  });

  test('Test all of the part one examples: Presents Per House', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE_PPH).forEach((key) => {
      // 3. Make sure it has the expected value
      expect(fedelf.Fedelf.inHouse(key)).toBe(EXAMPLES_PART_ONE_PPH[key]);
    });
  });

  test('Test all of the part one examples: First House with Presents', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE_FHP).forEach((key) => {
      // 3. Make sure it has the expected value
      expect(fedelf.Fedelf.firstHouse(key)).toBe(EXAMPLES_PART_ONE_FHP[key]);
    });
  });

  test('Test part one example of Fedelf object', () => {
    // 1. Create Fedelf object from text
    const myobj = new fedelf.Fedelf({ text: aoc20.fromText(PART_ONE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.presents).toBe(125);
    // 3. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test all of the part two examples: Presents Per House', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_TWO_PPH).forEach((key) => {
      // 3. Make sure it has the expected value
      expect(fedelf.Fedelf.inHouse2(key).presents).toBe(EXAMPLES_PART_TWO_PPH[key]);
    });
  });

  test('Test all of the part two examples: First House with Presents', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_TWO_FHP).forEach((key) => {
      // 3. Make sure it has the expected value
      expect(fedelf.Fedelf.firstHouse2(key)).toBe(EXAMPLES_PART_TWO_FHP[key]);
    });
  });

  test('Test part two example of Fedelf object', () => {
    // 1. Create Fedelf object from text
    const myobj = new fedelf.Fedelf({ part2: true, text: aoc20.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   f e d e l f . t e s t . j s                  end
// ======================================================================
