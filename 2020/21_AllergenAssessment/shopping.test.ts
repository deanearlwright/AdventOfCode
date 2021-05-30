// ======================================================================
// Allergen Assessment
//   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      s h o p p i n g . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_21';
import { Shopping } from './shopping';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 5;
const PART_TWO_RESULT = 'mxmxvkd,sqjhc,fvjkl';

// ======================================================================
//                                                           TestShopping
// ======================================================================

describe('Shopping', () => {
  test('Test the default Shopping creation', () => {
    // 1. Create default Shopping object
    const myobj = new Shopping([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.labels).toHaveLength(0);
    expect(myobj.ingredients.size).toBe(0);
    expect(myobj.allergens.size).toBe(0);
  });

  test('Test the Shopping object creation from text', () => {
    // 1. Create Shopping object from text
    const myobj = new Shopping(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.labels).toHaveLength(4);
    expect(myobj.ingredients.size).toBe(7);
    expect(myobj.ingredients.has('kfcds')).toBe(true);
    expect(myobj.allergens.size).toBe(3);
    expect(myobj.mapping.soy.size).toBe(2);
    expect(myobj.mapping.soy.has('sqjhc')).toBe(true);
    expect(myobj.mapping.soy.has('fvjkl')).toBe(true);
    expect(myobj.mapping.dairy.size).toBe(1);
    expect(myobj.mapping.dairy.has('mxmxvkd')).toBe(true);
    expect(myobj.labels[0].ingredients.has('kfcds')).toBe(true);
    // 3. Check methods
    expect(myobj.countIngredient('mxmxvkd')).toBe(3);
    expect(myobj.countIngredient('kfcds')).toBe(1);
    expect(myobj.countIngredient('nhms')).toBe(1);
    expect(myobj.countIngredient('sbzzf')).toBe(2);
    expect(myobj.countIngredient('trh')).toBe(1);
    expect(myobj.countIngredients(['mxmxvkd'])).toBe(3);
    expect(myobj.countIngredients(['kfcds'])).toBe(1);
    expect(myobj.countIngredients(['nhms'])).toBe(1);
    expect(myobj.countIngredients(['sbzzf'])).toBe(2);
    expect(myobj.countIngredients(['trh'])).toBe(1);
    expect(myobj.countIngredients(['kfcds', 'nhms', 'sbzzf', 'trh'])).toBe(5);
    expect(myobj.notSafe().size).toBe(3);
    expect(myobj.safe().size).toBe(4);
    expect(myobj.countIngredients(Array.from(myobj.safe()))).toBe(5);
    expect(myobj.resolveAllergens()).toBe(true);
    expect(myobj.mapping.dairy.size).toBe(1);
    expect(myobj.mapping.soy.size).toBe(1);
    expect(myobj.mapping.fish.size).toBe(1);
    expect(myobj.mapping.dairy.has('mxmxvkd')).toBe(true);
    expect(myobj.mapping.soy.has('fvjkl')).toBe(true);
    expect(myobj.mapping.fish.has('sqjhc')).toBe(true);
    expect(myobj.sortedIngredients()).toStrictEqual(['mxmxvkd', 'sqjhc', 'fvjkl']);
  });

  test('Test part one example of Shopping object', () => {
    // 1. Create Shopping object from text
    const myobj = new Shopping(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Shopping object', () => {
    // 1. Create Shopping object from text
    const myobj = new Shopping(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 s h o p p i n g . t e s t . t s                end
// ======================================================================
