// ======================================================================
// Allergen Assessment
//   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      l a b e l . t e s t . t s
//
// Test Label for Advent of Code 2020 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Label } from './label';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)';

// ======================================================================
//                                                              TestLabel
// ======================================================================

describe('Label', () => {
  test('Test the default Label creation', () => {
    // 1. Create default Label object
    const myobj = new Label('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.ingredients.size).toBe(0);
    expect(myobj.allergens.size).toBe(0);
    // 3. Check methods
    expect(myobj.hasIngredient('mxmxvkd')).toBe(false);
    expect(myobj.hasIngredient('tuna')).toBe(false);
    expect(myobj.hasAllergen('fish')).toBe(false);
    expect(myobj.hasAllergen('seafood')).toBe(false);
    expect(myobj.getIngredients()).toHaveLength(0);
    expect(myobj.getAllergens()).toHaveLength(0);
  });

  test('Test the Label object creation from text', () => {
    // 1. Create Label object from text
    const myobj = new Label(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(47);
    expect(myobj.ingredients.size).toBe(4);
    expect(myobj.allergens.size).toBe(2);
    // 3. Check methods
    expect(myobj.hasIngredient('mxmxvkd')).toBe(true);
    expect(myobj.hasIngredient('kfcds')).toBe(true);
    expect(myobj.hasIngredient('sqjhc')).toBe(true);
    expect(myobj.hasIngredient('nhms')).toBe(true);
    expect(myobj.hasIngredient('tuna')).toBe(false);
    expect(myobj.hasAllergen('dairy')).toBe(true);
    expect(myobj.hasAllergen('fish')).toBe(true);
    expect(myobj.hasAllergen('seafood')).toBe(false);
    expect(myobj.getIngredients()).toHaveLength(4);
    expect(myobj.getAllergens()).toHaveLength(2);
  });
});

// ======================================================================
// end                    l a b e l . t e s t . t s                   end
// ======================================================================
