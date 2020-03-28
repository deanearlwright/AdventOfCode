/* eslint-disable linebreak-style */
// ======================================================================
// Probably a Fire Hazard
//   Advent of Code 2015 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      l i g h t s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc06 = require('./aoc_06');
const lights = require('./lights');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'turn on 0,0 through 999,999\ntoggle 0,0 through 999,0\nturn off 499,499 through 500,500';

const EXAMPLES_PART_ONE = {
  'turn on 0,0 through 999,999': 1000000,
  'toggle 0,0 through 999,0': 1000,
  'turn off 499,499 through 500,500': 0,
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 1000000 - 1004;
const PART_TWO_RESULT = 1000000 + 2000 - 4;

// ======================================================================
//                                                              TestLights
// ======================================================================

describe('Lights', () => {
  test('Test the default Lights creation', () => {
    // 1. Create default Lights object
    const myobj = new lights.Lights({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.howManyAre(1)).toBe(0);
  });

  test('Test the Lights object creation from text', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({ text: aoc06.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    // 3. And the expected answer
    expect(myobj.howManyAre(1)).toBe(PART_ONE_RESULT);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Lights object using the key at text
      const myobj = new lights.Lights({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Check out how many lights are on
      expect(myobj.howManyAre(1)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test part one example of Lights object', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({ text: aoc06.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Lights object', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({ part2: true, text: aoc06.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    t e s t _ l i g h t s . j s                 end
// ======================================================================
