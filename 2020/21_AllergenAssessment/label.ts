// ======================================================================
// Allergen Assessment
//   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           l a b e l . t s
//
// Label for the Advent of Code 2020 Day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Label
// ======================================================================

export class Label {
  // Object for Allergen Assessment
  text: string;

  part2: boolean;

  ingredients: Set<string>;

  allergens: Set<string>;

  constructor(text: string, part2 = false) {
    // Create a Label object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.ingredients = new Set();
    this.allergens = new Set();

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string) {
    // Assign values from text

    // 1. Divide the text at contains
    const cleaned = text.replace('(', '').replace(')', '');
    const [ingredients, allergens] = cleaned.split(' contains ');

    // 2. Add the ingredients
    const ingredientList = ingredients.split(' ');
    for (let indx = 0; indx < ingredientList.length; indx += 1) {
      this.ingredients.add(ingredientList[indx]);
    }

    // 3. Add the allergens
    const allergenList = allergens.split(' ');
    for (let indx = 0; indx < allergenList.length; indx += 1) {
      const allergen = allergenList[indx].replace(',', '');
      this.allergens.add(allergen);
    }
  }

  hasIngredient(ingredient: string): boolean {
    // Return true if the label lists the ingredient
    return this.ingredients.has(ingredient);
  }

  hasAllergen(allergen: string): boolean {
    // Return true if the label lists the allergen
    return this.allergens.has(allergen);
  }

  getIngredients(): string[] {
    // Returns a list of ingredients
    return Array.from(this.ingredients);
  }

  getAllergens(): string[] {
    // Returns a list of allergens
    return Array.from(this.allergens);
  }
}

// ======================================================================
// end                         l a b e l . t s                        end
// ======================================================================
