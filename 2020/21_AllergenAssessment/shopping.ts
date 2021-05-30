// ======================================================================
// Allergen Assessment
//   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s h o p p i n g . t s
//
// A solver for the Advent of Code 2020 Day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Label } from './label';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type AllergenToIngredient = Record<string, Set<string>>;

// ======================================================================
//                                                               Shopping
// ======================================================================

export class Shopping {
  // Object for Allergen Assessment
  text: string[];

  part2: boolean;

  labels: Label[];

  ingredients: Set<string>;

  allergens: Set<string>;

  mapping: AllergenToIngredient;

  constructor(text: string[], part2 = false) {
    // Create a Shopping object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.labels = [];
    this.ingredients = new Set();
    this.allergens = new Set();
    this.mapping = {};

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string[]) {
    // Assign values from text

    // 1. Loop for each line of text
    for (let tindx = 0; tindx < text.length; tindx += 1) {
      // 2. Create a label from the text and add it to the list
      this.labels.push(new Label(text[tindx], this.part2));
    }

    // 2. Get complete list of ingredients
    for (let lindx = 0; lindx < this.labels.length; lindx += 1) {
      const ingredients = this.labels[lindx].getIngredients();
      for (let indx = 0; indx < ingredients.length; indx += 1) {
        this.ingredients.add(ingredients[indx]);
      }
    }

    // 3. Get complete list of alergens
    for (let lindx = 0; lindx < this.labels.length; lindx += 1) {
      const allergens = this.labels[lindx].getAllergens();
      for (let indx = 0; indx < allergens.length; indx += 1) {
        this.allergens.add(allergens[indx]);
      }
    }

    // 4. Create mapping of allergens to ingredients
    for (let lindx = 0; lindx < this.labels.length; lindx += 1) {
      const label = this.labels[lindx];
      const allergens = label.getAllergens();
      for (let aindx = 0; aindx < allergens.length; aindx += 1) {
        const allergen = allergens[aindx];
        if (this.mapping[allergen] === undefined) {
          this.mapping[allergen] = new Set(label.ingredients);
        } else {
          const ingredients = Array.from(this.mapping[allergen]);
          for (let indx = 0; indx < ingredients.length; indx += 1) {
            const ingredient = ingredients[indx];
            if (!label.ingredients.has(ingredient)) {
              this.mapping[allergen].delete(ingredient);
            }
          }
        }
      }
    }
  }

  notSafe(): Set<string> {
    // Return set of ingredients that have allergens

    // 1. Start with nothing
    const result: Set<string> = new Set();

    // 2. Loop for all of the allergens map to ingredients
    const allergins = Array.from(this.allergens);
    for (let aindx = 0; aindx < allergins.length; aindx += 1) {
      const allergin = allergins[aindx];
      // 3. Loop for all of the ingredients possible for that allergen
      const ingredients = Array.from(this.mapping[allergin]);
      for (let indx = 0; indx < ingredients.length; indx += 1) {
        // 4. Add the unsave ingredients to the result
        result.add(ingredients[indx]);
      }
    }
    // 5. Return the set of ingredients that have allergins
    return result;
  }

  safe(): Set<string> {
    // Returns set of ingredients that don't have allergens

    // 1. Start with the set of all ingrdents
    const result = new Set(this.ingredients);

    // 2. Get an array of ingredients with allergens
    const unsafe = Array.from(this.notSafe());

    // 3. Remove the unsage ingredients from the result
    for (let indx = 0; indx < unsafe.length; indx += 1) {
      result.delete(unsafe[indx]);
    }

    // 4. Return the remaining ingredients
    return result;
  }

  countIngredient(ingredient: string): number {
    // Return the number of labels on which the ingredient appears

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the labels
    for (let indx = 0; indx < this.labels.length; indx += 1) {
      const label = this.labels[indx];

      // 3. If this label has the ingredient, increment count
      if (label.ingredients.has(ingredient)) {
        result += 1;
      }
    }

    // 4. Return the number of labels with the ingredient
    return result;
  }

  countIngredients(ingredients: string[]): number {
    // Return the total number of labels on which the ingredients appears

    // 1. Start with nothing
    let result = 0;

    // 2. Loop fpr all of the ingredients given
    for (let indx = 0; indx < ingredients.length; indx += 1) {
      // 3. Add in the number of times this ingrdient appears
      result += this.countIngredient(ingredients[indx]);
    }
    // 4. Return total label count
    return result;
  }

  resolveAllergens(): boolean {
    // Returns true if we could resolve the allergens to thier ingredients

    // 1. Get a list of the known allergens
    const allergens = Array.from(this.allergens);

    // 2. Impose a limit
    for (let limit = 0; limit < 10; limit += 1) {
      let done = true;
      // 3 Once we find an allergin that can be in only one ingredient ...
      for (let aindx = 0; aindx < allergens.length; aindx += 1) {
        const allergen = allergens[aindx];
        const ingredients = Array.from(this.mapping[allergen]);
        if (ingredients.length === 1) {
          const ingredient = ingredients[0];
          // 4. We can remove that ingredient from the other allergen lists
          for (let indx = 0; indx < allergens.length; indx += 1) {
            if (indx !== aindx) {
              this.mapping[allergens[indx]].delete(ingredient);
            }
          }
        } else {
          done = false;
        }
      }
      // 5. if all allergens have only one ingredient, we are done
      if (done) {
        return true;
      }
    }
    // 6. All that work and nothing to show for it
    return false;
  }

  sortedIngredients(): string[] {
    // Returns the list of ingredients sorted by allergens

    // 1. Start with nothing
    const result: string[] = [];

    // 2. Get the allergens in sorted order
    const allergens = Array.from(this.allergens);
    allergens.sort();

    // 3. Loop for the sorted allergens
    for (let indx = 0; indx < allergens.length; indx += 1) {
      // 4. Get the single ingredient
      const ingredient = Array.from(this.mapping[allergens[indx]])[0];
      // 5. Add it to the result
      result.push(ingredient);
    }
    // 6. Return the ingredients sorted by allergens
    return result;
  }

  solution(verbose = false, limit = 0): number|string {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      if (!this.resolveAllergens()) {
        return NaN;
      }
      return this.sortedIngredients().join(',');
    }
    return this.countIngredients(Array.from(this.safe()));
  }

  partOne(verbose = false, limit = 0): number|string {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number|string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      s h o p p i n g . t s                     end
// ======================================================================
