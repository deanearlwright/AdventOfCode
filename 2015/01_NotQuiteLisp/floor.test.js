/* eslint-disable linebreak-style */
// ======================================================================
// Not Quite Lisp
//   Advent of Code 2015 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                      f l o o r . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 01, Not Quite Lisp
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc01 = require('./aoc_01');
const floor = require('./floor');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\n(())\n';

const EXAMPLES_PART_ONE = {
  '(())': 0,
  '()()': 0,
  '(((': 3,
  '(()(()(': 3,
  '))(((((': 3,
  '())': -1,
  '))(': -1,
  ')))': -3,
  ')())())': -3,
};

const EXAMPLES_PART_TWO = {
  ')': 1,
  '()())': 5,
};

const PART_ONE_TEXT = '\n(()(()(\n';
const PART_TWO_TEXT = '\n()())\n';

const EXAMPLE_RESULT = 0;
const PART_ONE_RESULT = 3;
const PART_TWO_RESULT = 5;

// ======================================================================
//                                                              TestFloor
// ======================================================================

describe('Floor', () => {
  test('Test the default Floor creation', () => {
    const myobj = new floor.Floor({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.level).toBe(null);
    expect(myobj.toBasement).toBe(null);
    expect(myobj.directions).toBe('');
  });

  test('Test the Floor object creation from text', () => {
    // 1. Create Floor object from text
    const myobj = new floor.Floor({ text: aoc01.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.level).toBe(null);
    expect(myobj.toBasement).toBe(null);
    expect(myobj.directions).toHaveLength(4);
    // 3. Check methods
    myobj.followDirections();
    expect(myobj.level).toBe(EXAMPLE_RESULT);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Floor object using the key at text
      const myobj = new floor.Floor({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.level).toBe(null);
      expect(myobj.toBasement).toBe(null);
      expect(myobj.directions).toHaveLength(key.length);
      // 3. Follow the instructions
      myobj.followDirections();
      expect(myobj.level).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Floor object using the key at text
      const myobj = new floor.Floor({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.level).toBe(null);
      expect(myobj.toBasement).toBe(null);
      expect(myobj.directions).toHaveLength(key.length);
      // 3. Follow the instructions
      myobj.followDirections();
      expect(myobj.toBasement).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Floor object', () => {
    // 1. Create Floor object from text
    const myobj = new floor.Floor({ text: aoc01.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Floor object', () => {
    // 1. Create Floor object from text
    const myobj = new floor.Floor({ part2: true, text: aoc01.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    t e s t _ f l o o r . j s                 end
// ======================================================================
