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
const EXAMPLE_TEXT = '';
const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = null;
const PART_TWO_RESULT = null;

// ======================================================================
//                                                              TestFloor
// ======================================================================

describe('Floor', () => {
  test('Test the default Floor creation', () => {
    const myobj = new floor.Floor({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Floor object creation from text', () => {
    // 1. Create Floor object from text
    const myobj = new floor.Floor({ text: aoc01.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
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
