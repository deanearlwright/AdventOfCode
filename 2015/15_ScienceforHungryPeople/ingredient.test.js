/* eslint-disable linebreak-style */
// ======================================================================
// Science for Hungry People
//   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                     i n g r e d i e n t . t e s t . j s
// Test the cookie ingredient for Advent of Code 2015 day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const ingredient = require('./ingredient');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8';

// ======================================================================
//                                                         TestIngredient
// ======================================================================

describe('Ingredient', () => {
  test('Test the default Ingredient creation', () => {
    // 1. Create default Ingredient object
    const myobj = new ingredient.Ingredient({});
    // 2. Make sure it has the default values
    expect(myobj.name).toBe(null);
    expect(myobj.capacity).toBe(null);
    expect(myobj.durability).toBe(null);
    expect(myobj.flavor).toBe(null);
    expect(myobj.texture).toBe(null);
    expect(myobj.calories).toBe(null);
    expect(myobj.text).toBe(null);
  });

  test('Test the Ingredient object creation from text', () => {
    // 1. Create Ingredient object from text
    const myobj = new ingredient.Ingredient({ text: EXAMPLE_TEXT });
    // 2. Make sure it has the expected values
    expect(myobj.name).toBe('Butterscotch');
    expect(myobj.capacity).toBe(-1);
    expect(myobj.durability).toBe(-2);
    expect(myobj.flavor).toBe(6);
    expect(myobj.texture).toBe(3);
    expect(myobj.calories).toBe(8);
    expect(myobj.text).toBe(EXAMPLE_TEXT);
    // 3. Test properties
    expect(myobj.properties()).toStrictEqual([-1, -2, 6, 3, 8]);
    expect(myobj.properties(44)).toStrictEqual([-44, -88, 264, 132, 352]);
  });
});

// ======================================================================
// end                i n g r e d i e n t . t e s t . j s             end
// ======================================================================
