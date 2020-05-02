/* eslint-disable linebreak-style */
// ======================================================================
// Science for Hungry People
//   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r e c i p e . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc15 = require('./aoc_15');
const recipe = require('./recipe');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_BS = 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8';
const EXAMPLE_CN = 'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3';
const EXAMPLE_TEXT = `\n${EXAMPLE_BS}\n${EXAMPLE_CN}\n`;

const EXAMPLES_PART_ONE = {};
const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 62842880;
const PART_TWO_RESULT = 57600000;

// ======================================================================
//                                                             TestRecipe
// ======================================================================

describe('Recipe', () => {
  test('Test the default Recipe creation', () => {
    // 1. Create default Recipe object
    const myobj = new recipe.Recipe({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.ingredients).toHaveLength(0);
    expect(myobj.number).toBe(0);
  });

  test('Test the Recipe object creation from text', () => {
    // 1. Create Recipe object from text
    const myobj = new recipe.Recipe({ text: aoc15.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.ingredients).toHaveLength(2);
    expect(myobj.number).toBe(2);
    // 3. Check scoring
    expect(myobj.scoreRecipe([44, 56])).toBe(62842880);
    // 4. Check tooMuch() and justRight()
    expect(recipe.Recipe.tooMuch([44, 0])).toBe(false);
    expect(recipe.Recipe.tooMuch([44, 56])).toBe(false);
    expect(recipe.Recipe.tooMuch([44, 57])).toBe(true);
    expect(recipe.Recipe.justRight([44, 0])).toBe(false);
    expect(recipe.Recipe.justRight([44, 56])).toBe(true);
    expect(recipe.Recipe.justRight([44, 57])).toBe(false);
    // 5. Check bestRecipe()
    expect(myobj.bestRecipe()).toStrictEqual([44, 56]);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Recipe object using the key as text
      const myobj = new recipe.Recipe({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.recipe(key)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Recipe object using the key as text
      const myobj = new recipe.Recipe({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.recipe(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Recipe object', () => {
    // 1. Create Recipe object from text
    const myobj = new recipe.Recipe({ text: aoc15.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Recipe object', () => {
    // 1. Create Recipe object from text
    const myobj = new recipe.Recipe({ part2: true, text: aoc15.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   r e c i p e . t e s t . j s                  end
// ======================================================================
