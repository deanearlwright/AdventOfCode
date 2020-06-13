/* eslint-disable linebreak-style */
// ======================================================================
// Let It Snow
//   Advent of Code 2015 Day 25 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      m a c h i n e . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 25 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc25 = require('./aoc_25');
const machine = require('./machine');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
To continue, please consult the code grid in the manual.  Enter the code at row 4, column 2.`;

const EXAMPLES_PART_ONE = {
  11: 20151125,
  12: 18749137,
  13: 17289845,
  14: 30943339,
  15: 10071777,
  16: 33511524,
  21: 31916031,
  22: 21629792,
  23: 16929656,
  24: 7726640,
  25: 15514188,
  26: 4041754,
  31: 16080970,
  32: 8057251,
  33: 1601130,
  34: 7981243,
  35: 11661866,
  36: 16474243,
  41: 24592653,
  42: 32451966,
  43: 21345942,
  44: 9380097,
  45: 10600672,
  46: 31527494,
  51: 77061,
  52: 17552253,
  53: 28094349,
  54: 6899651,
  55: 9250759,
  56: 31663883,
  61: 33071741,
  62: 6796745,
  63: 25397450,
  64: 24659492,
  65: 1534922,
  66: 27995004,
};

const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 32451966;
const PART_TWO_RESULT = null;

// ======================================================================
//                                                            TestMachine
// ======================================================================

describe('Machine', () => {
  test('Test the default Machine creation', () => {
    // 1. Create default Machine object
    const myobj = new machine.Machine({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.row).toBe(0);
    expect(myobj.col).toBe(0);
  });

  test('Test the Machine object creation from text', () => {
    // 1. Create Machine object from text
    const myobj = new machine.Machine({ text: aoc25.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.row).toBe(4);
    expect(myobj.col).toBe(2);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Machine object using the key as text
      const myobj = new machine.Machine({ text: [` row ${key[0]}, column ${key[1]}.`] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.row).toBe(parseInt(key[0], 10));
      expect(myobj.col).toBe(parseInt(key[1], 10));
      // 3. Make sure it has the expected value
      expect(myobj.code(false)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Machine object using the key as text
      const myobj = new machine.Machine({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.machine(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Machine object', () => {
    // 1. Create Machine object from text
    const myobj = new machine.Machine({ text: aoc25.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Machine object', () => {
    // 1. Create Machine object from text
    const myobj = new machine.Machine({ part2: true, text: aoc25.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  m a c h i n e . t e s t . j s                 end
// ======================================================================
