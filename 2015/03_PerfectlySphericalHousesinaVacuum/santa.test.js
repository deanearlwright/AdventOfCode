/* eslint-disable linebreak-style */
// ======================================================================
// Perfectly Spherical Houses in a Vacuum
//   Advent of Code 2015 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      s a n t a . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 03 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc03 = require('./aoc_03');
const santa = require('./santa');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\n^>v<\n';

const EXAMPLES_PART_ONE = {
  '>': 2,
  '^>v<': 4,
  '^v^v^v^v^v': 2,
};

const EXAMPLES_PART_TWO = {
  '^v': 3,
  '^>v<': 3,
  '^v^v^v^v^v': 11,
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 4;
const PART_TWO_RESULT = 3;

// ======================================================================
//                                                              TestSanta
// ======================================================================

describe('Santa', () => {
  test('Test the default Santa creation', () => {
    // 1. Create default Santa object
    const myobj = new santa.Santa({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Santa object creation from text', () => {
    // 1. Create Santa object from text
    const myobj = new santa.Santa({ text: aoc03.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.directions).toHaveLength(4);
    // 3. Follow the directions
    myobj.followDirections();
    // 4. Check the results
    expect(myobj.presents).toBe(5);
    expect(myobj.houses).toBe(4);
    expect(myobj.location).toStrictEqual([0, 0]);
    expect(Object.keys(myobj.visited)).toHaveLength(4);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Santa object using the key at text
      const myobj = new santa.Santa({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Follow the instructions
      myobj.followDirections();
      expect(myobj.houses).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test part one example of Santa object', () => {
    // 1. Create Santa object from text
    const myobj = new santa.Santa({ text: aoc03.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Santa object using the key at text
      const myobj = new santa.Santa({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Follow the instructions
      myobj.followDirectionsTwo();
      expect(myobj.houses).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part two example of Santa object', () => {
    // 1. Create Santa object from text
    const myobj = new santa.Santa({ part2: true, text: aoc03.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                     t e s t _ s a n t a . j s                  end
// ======================================================================
