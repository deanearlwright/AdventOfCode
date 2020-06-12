/* eslint-disable linebreak-style */
// ======================================================================
// It Hangs in the Balance
//   Advent of Code 2015 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a c k a g e s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc24 = require('./aoc_24');
const packages = require('./packages');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
1
2
3
4
5
7
8
9
10
11
`;

const EXAMPLES_PART_ONE = {};
const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 99;
const PART_TWO_RESULT = 44;

// ======================================================================
//                                                           TestPackages
// ======================================================================

describe('Packages', () => {
  test('Test the default Packages creation', () => {
    // 1. Create default Packages object
    const myobj = new packages.Packages({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.weights).toHaveLength(0);
    expect(myobj.compartments).toBe(3);
    expect(myobj.target).toBe(0);
  });

  test('Test the Packages object creation from text', () => {
    // 1. Create Packages object from text
    const myobj = new packages.Packages({ text: aoc24.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(10);
    expect(myobj.weights).toHaveLength(10);
    expect(myobj.compartments).toBe(3);
    expect(myobj.target).toBe(20);
    // 3. Get the quantum entanglement of the backing with the best legroom
    expect(myobj.solution(false, 0)).toBe(99);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Packages object using the key as text
      const myobj = new packages.Packages({ part2: false, text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.packages(key)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Packages object using the key as text
      const myobj = new packages.Packages({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.packages(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Packages object', () => {
    // 1. Create Packages object from text
    const myobj = new packages.Packages({ text: aoc24.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: true })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Packages object', () => {
    // 1. Create Packages object from text
    const myobj = new packages.Packages({ part2: true, text: aoc24.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: true })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 p a c k a g e s . t e s t . j s                end
// ======================================================================
