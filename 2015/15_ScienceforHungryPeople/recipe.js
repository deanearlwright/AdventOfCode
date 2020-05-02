/* eslint-disable linebreak-style */
// ======================================================================
// Science for Hungry People
//   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r e c i p e . j s
//
// A solver for the Advent of Code 2015 Day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const ingredient = require('./ingredient');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const INGREDIENT_TOTAL = 100;
const DESIRED_CALORIES = 500;
const PROPERTY_CALORIES = 4;

// ======================================================================
//                                                                 Recipe
// ======================================================================

class Recipe {
  // Object for Science for Hungry People

  constructor(options) {
    // Create a Recipe object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.ingredients = [];
    this.number = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    text.forEach((line) => {
      const item = new ingredient.Ingredient({ text: line });
      this.ingredients.push(item);
      this.number += 1;
    });
  }

  static tooMuch(counts) {
    const sum = (a, v) => a + v;
    const result = counts.reduce(sum);
    return result > INGREDIENT_TOTAL;
  }

  static justRight(counts) {
    const sum = (a, v) => a + v;
    const result = counts.reduce(sum);
    return result === INGREDIENT_TOTAL;
  }

  scoreRecipe(counts) {
    // 1. Start out with (almost) nothing
    let result = 1;
    let calories = 0;
    // 2. Get all of the ingredient properties
    const ingredientScores = [];
    for (let i = 0; i < this.number; i += 1) {
      ingredientScores.push(this.ingredients[i].properties(counts[i]));
      // 2a. Accumulate calories for part2
      calories += ingredientScores[i][PROPERTY_CALORIES];
    }
    // 3. Loop for all the attributes
    for (let a = 0; a < PROPERTY_CALORIES; a += 1) {
      // 3. Attribute score is sum of ingredient attributes
      let attributeScore = 0;
      for (let i = 0; i < this.number; i += 1) {
        attributeScore += ingredientScores[i][a];
      }
      // 4. Attribute score is zero if less than zero
      if (attributeScore < 0) {
        attributeScore = 0;
      }
      // 5. Multiple the attributes together
      //    (now do you see why we started with 1 ?)
      result *= attributeScore;
    }
    // 6. If this is part2, we need it to be the right number of calories
    if (this.part2 && calories !== DESIRED_CALORIES) {
      result = 0;
    }
    // 7. Return the multiplication of the sum of the ingredient properties
    return result;
  }

  bestRecipe() {
    // 1. Start with a pretty poor "best" score
    let bestScore = 0;
    let bestCounts = new Array(this.number).fill(0);
    // 2. This is how we know how much we have
    const counts = new Array(this.number).fill(0);
    const sum = (a, v) => a + v;

    function nextIngredient(index, last, maximum, outer) {
      // 1. If this is the last ingredient, use the maximum
      if (index === last) {
        counts[index] = maximum;
        // 2. Calculate the score
        const score = outer.scoreRecipe(counts);
        // 3. If this score is better, save it
        if (score > bestScore) {
          bestScore = score;
          bestCounts = counts.slice();
        }
      } else {
        // 4. Loop for every possible amount of that ingredient
        for (let amount = 0; amount <= maximum; amount += 1) {
          counts[index] = amount;
          const total = counts.reduce(sum);
          // 5. Get more ingredients
          nextIngredient(index + 1, last, INGREDIENT_TOTAL - total, outer);
        }
      }
      // 6. We are done with this ingredient
      counts[index] = 0;
    }
    // 3. Test all the ingredient combinations
    nextIngredient(0, this.number - 1, INGREDIENT_TOTAL, this);
    // 4. Return the best ingredient counts
    return bestCounts;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    const bestCounts = this.bestRecipe();
    const result = this.scoreRecipe(bestCounts);
    return result;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    const bestCounts = this.bestRecipe();
    const result = this.scoreRecipe(bestCounts);
    return result;
  }
}

module.exports.Recipe = Recipe;
// ======================================================================
// end                        r e c i p e . j s                       end
// ======================================================================
