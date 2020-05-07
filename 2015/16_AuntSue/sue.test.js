/* eslint-disable linebreak-style */
// ======================================================================
// Aunt Sue
//   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                         s u e . t e s t . j s
//
// Test the Sue object for Advent of Code 2015 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc16 = require('./aoc_16');
const sue = require('./sue');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'Sue 1: children: 1, cars: 8, vizslas: 7';

// ======================================================================
//                                                                TestSue
// ======================================================================

describe('Sue', () => {
  test('Test the default Sue creation', () => {
    // 1. Create default Mfcsam object
    const myobj = new sue.Sue({});
    // 2. Make sure it has the default values
    expect(myobj.text).toBe(null);
    expect(myobj.number).toBe(null);
    expect(myobj.attributes).toStrictEqual({});
  });

  test('Test the Mfcsam object creation from text', () => {
    // 1. Create Mfcsam object from text
    const myobj = new sue.Sue({ text: EXAMPLE_TEXT });
    // 2. Make sure it has the expected values
    expect(myobj.text).toHaveLength(EXAMPLE_TEXT.length);
    expect(myobj.number).toBe(1);
    expect(Object.keys(myobj.attributes)).toHaveLength(3);
    expect(myobj.attributes.children).toBe(1);
    expect(myobj.attributes.cars).toBe(8);
    expect(myobj.attributes.vizslas).toBe(7);
    // 3. Check the attributes
    expect(myobj.checkAttribute('children', 0)).toBe(false);
    expect(myobj.checkAttribute('children', 1)).toBe(true);
    expect(myobj.checkAttribute('children', 2)).toBe(false);
    expect(myobj.checkAttribute('cars', 0)).toBe(false);
    expect(myobj.checkAttribute('cars', 1)).toBe(false);
    expect(myobj.checkAttribute('cars', 4)).toBe(false);
    expect(myobj.checkAttribute('cars', 8)).toBe(true);
    expect(myobj.checkAttribute('cars', 9)).toBe(false);
    expect(myobj.checkAttribute('cats', 0)).toBe(true);
    expect(myobj.checkAttribute('cats', 1)).toBe(true);
    expect(myobj.checkAttribute('cats', 4)).toBe(true);
    expect(myobj.checkAttribute('cats', 8)).toBe(true);
    expect(myobj.checkAttribute('cats', 9)).toBe(true);
  });
});

// ======================================================================
// end                       s u e . t e s t . j s                    end
// ======================================================================
