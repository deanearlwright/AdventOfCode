/* eslint-disable linebreak-style */
// ======================================================================
// I Was Told There Would Be No Math
//   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a p e r . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc02 = require('./aoc_02');
const paper = require('./paper');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '';
const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = null;
const PART_TWO_RESULT = null;

// ======================================================================
//                                                              TestPaper
// ======================================================================

describe('Paper', () => {
  test('Test the default Paper creation', () => {
    // 1. Create default Paper object
    const myobj = new paper.Paper({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Paper object creation from text', () => {
    // 1. Create Paper object from text
    const myobj = new paper.Paper({ text: aoc02.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test part one example of Paper object', () => {
    // 1. Create Paper object from text
    const myobj = new paper.Paper({ text: aoc02.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Paper object', () => {
    // 1. Create Paper object from text
    const myobj = new paper.Paper({ part2: true, text: aoc02.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                     t e s t _ p a p e r . j s                  end
// ======================================================================
