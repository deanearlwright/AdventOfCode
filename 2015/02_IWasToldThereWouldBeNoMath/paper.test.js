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
const EXAMPLE_TEXT = '2x3x4';
const PART_ONE_TEXT = '2x3x4\n1x1x10\n';
const PART_TWO_TEXT = PART_ONE_TEXT;

const EXAMPLE_WRAPPING = 58;
const EXAMPLE_RIBBON = 34;
const PART_ONE_RESULT = 58 + 43;
const PART_TWO_RESULT = 34 + 14;

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
    expect(myobj.wrapping).toBe(0);
    expect(myobj.ribbon).toBe(0);
  });

  test('Test the Paper object creation from text', () => {
    // 1. Create Paper object from text
    const myobj = new paper.Paper({ text: aoc02.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.text[0]).toBe(EXAMPLE_TEXT);
    // 3. Check methods
    expect(paper.Paper.calculateWrapping('2x3x4')).toBe(58);
    expect(paper.Paper.calculateWrapping('1x1x10')).toBe(43);
    expect(myobj.wrapping).toBe(EXAMPLE_WRAPPING);
    expect(paper.Paper.calculateRibbon('2x3x4')).toBe(34);
    expect(paper.Paper.calculateRibbon('1x1x10')).toBe(14);
    expect(myobj.ribbon).toBe(EXAMPLE_RIBBON);
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
