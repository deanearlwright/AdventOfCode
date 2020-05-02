/* eslint-disable linebreak-style */
// ======================================================================
// Science for Hungry People
//   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                        i n g r e d i e n t . j s
//
// A cookie ingredient for the Advent of Code 2015 Day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// ======================================================================
//                                                             Ingredient
// ======================================================================

class Ingredient {
  // Object for a single cookie ingredient

  constructor(options) {
    // Create a IngredientReindeet object

    // 1. Set the initial values
    this.name = options.name === undefined ? null : options.name;
    this.capacity = options.capacity === undefined ? null : options.capacity;
    this.durability = options.durability === undefined ? null : options.durability;
    this.flavor = options.flavor === undefined ? null : options.flavor;
    this.texture = options.texture === undefined ? null : options.texture;
    this.calories = options.calories === undefined ? null : options.calories;
    this.text = options.text === undefined ? null : options.text;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Regular Expression parser for ingredient
    // Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    const pattern = /([A-Z][a-z]+): capacity (-?[0-9]+), durability (-?[0-9]+), flavor (-?[0-9]+), texture (-?[0-9]+), calories ([0-9]+)/;

    // 2. Decompose input line
    const match = text.match(pattern);
    if (match) {
      // 3. Set ingredient values
      [, this.name, this.capacity, this.durability,
        this.flavor, this.texture, this.calories] = match;
      this.capacity = parseInt(this.capacity, 10);
      this.durability = parseInt(this.durability, 10);
      this.flavor = parseInt(this.flavor, 10);
      this.texture = parseInt(this.texture, 10);
      this.calories = parseInt(this.calories, 10);
    } else {
      // eslint-disable-next-line no-console
      console.log('Unable to parse input', text);
    }
  }

  properties(amount = 1) {
    return [this.capacity * amount, this.durability * amount,
      this.flavor * amount, this.texture * amount, this.calories * amount];
  }
}

module.exports.Ingredient = Ingredient;
// ======================================================================
// end                   i n g r e d i e n t . j s                    end
// ======================================================================
