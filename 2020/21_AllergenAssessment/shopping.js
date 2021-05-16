"use strict";
// ======================================================================
// Allergen Assessment
//   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Shopping = void 0;
// ======================================================================
//                           s h o p p i n g . t s
//
// A solver for the Advent of Code 2020 Day 21 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
var label_1 = require("./label");
// ======================================================================
//                                                               Shopping
// ======================================================================
var Shopping = /** @class */ (function () {
    function Shopping(text, part2) {
        // Create a Shopping object
        if (part2 === void 0) { part2 = false; }
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
    Shopping.prototype.processText = function (text) {
        // Assign values from text
        // 1. Loop for each line of text
        for (var tindx = 0; tindx < text.length; tindx += 1) {
            // 2. Create a label from the text and add it to the list
            this.labels.push(new label_1.Label(text[tindx], this.part2));
        }
        // 2. Get complete list of ingredients
        for (var lindx = 0; lindx < this.labels.length; lindx += 1) {
            var ingredients = this.labels[lindx].getIngredients();
            for (var indx = 0; indx < ingredients.length; indx += 1) {
                this.ingredients.add(ingredients[indx]);
            }
        }
        // 3. Get complete list of alergens
        for (var lindx = 0; lindx < this.labels.length; lindx += 1) {
            var allergens = this.labels[lindx].getAllergens();
            for (var indx = 0; indx < allergens.length; indx += 1) {
                this.allergens.add(allergens[indx]);
            }
        }
        // 4. Create mapping of allergens to ingredients
        for (var lindx = 0; lindx < this.labels.length; lindx += 1) {
            var label = this.labels[lindx];
            var allergens = label.getAllergens();
            for (var aindx = 0; aindx < allergens.length; aindx += 1) {
                var allergen = allergens[aindx];
                if (this.mapping[allergen] === undefined) {
                    this.mapping[allergen] = new Set(label.ingredients);
                }
                else {
                    var ingredients = Array.from(this.mapping[allergen]);
                    for (var indx = 0; indx < ingredients.length; indx += 1) {
                        var ingredient = ingredients[indx];
                        if (!label.ingredients.has(ingredient)) {
                            this.mapping[allergen]["delete"](ingredient);
                        }
                    }
                }
            }
        }
    };
    Shopping.prototype.notSafe = function () {
        // Return set of ingredients that have allergens
        // 1. Start with nothing
        var result = new Set();
        // 2. Loop for all of the allergens map to ingredients
        var allergins = Array.from(this.allergens);
        for (var aindx = 0; aindx < allergins.length; aindx += 1) {
            var allergin = allergins[aindx];
            // 3. Loop for all of the ingredients possible for that allergen
            var ingredients = Array.from(this.mapping[allergin]);
            for (var indx = 0; indx < ingredients.length; indx += 1) {
                // 4. Add the unsave ingredients to the result
                result.add(ingredients[indx]);
            }
        }
        // 5. Return the set of ingredients that have allergins
        return result;
    };
    Shopping.prototype.safe = function () {
        // Returns set of ingredients that don't have allergens
        // 1. Start with the set of all ingrdents
        var result = new Set(this.ingredients);
        // 2. Get an array of ingredients with allergens
        var unsafe = Array.from(this.notSafe());
        // 3. Remove the unsage ingredients from the result
        for (var indx = 0; indx < unsafe.length; indx += 1) {
            result["delete"](unsafe[indx]);
        }
        // 4. Return the remaining ingredients
        return result;
    };
    Shopping.prototype.countIngredient = function (ingredient) {
        // Return the number of labels on which the ingredient appears
        // 1. Start with nothing
        var result = 0;
        // 2. Loop for all of the labels
        for (var indx = 0; indx < this.labels.length; indx += 1) {
            var label = this.labels[indx];
            // 3. If this label has the ingredient, increment count
            if (label.ingredients.has(ingredient)) {
                result += 1;
            }
        }
        // 4. Return the number of labels with the ingredient
        return result;
    };
    Shopping.prototype.countIngredients = function (ingredients) {
        // Return the total number of labels on which the ingredients appears
        // 1. Start with nothing
        var result = 0;
        // 2. Loop fpr all of the ingredients given
        for (var indx = 0; indx < ingredients.length; indx += 1) {
            // 3. Add in the number of times this ingrdient appears
            result += this.countIngredient(ingredients[indx]);
        }
        // 4. Return total label count
        return result;
    };
    Shopping.prototype.resolveAllergens = function () {
        // Returns true if we could resolve the allergens to thier ingredients
        // 1. Get a list of the known allergens
        var allergens = Array.from(this.allergens);
        // 2. Impose a limit
        for (var limit = 0; limit < 10; limit += 1) {
            var done = true;
            // 3 Once we find an allergin that can be in only one ingredient ...
            for (var aindx = 0; aindx < allergens.length; aindx += 1) {
                var allergen = allergens[aindx];
                var ingredients = Array.from(this.mapping[allergen]);
                if (ingredients.length === 1) {
                    var ingredient = ingredients[0];
                    // 4. We can remove that ingredient from the other allergen lists
                    for (var indx = 0; indx < allergens.length; indx += 1) {
                        if (indx !== aindx) {
                            this.mapping[allergens[indx]]["delete"](ingredient);
                        }
                    }
                }
                else {
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
    };
    Shopping.prototype.sortedIngredients = function () {
        // Returns the list of ingredients sorted by allergens
        // 1. Start with nothing
        var result = [];
        // 2. Get the allergens in sorted order
        var allergens = Array.from(this.allergens);
        allergens.sort();
        // 3. Loop for the sorted allergens
        for (var indx = 0; indx < allergens.length; indx += 1) {
            // 4. Get the single ingredient
            var ingredient = Array.from(this.mapping[allergens[indx]])[0];
            // 5. Add it to the result
            result.push(ingredient);
        }
        // 6. Return the ingredients sorted by allergens
        return result;
    };
    Shopping.prototype.solution = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        if (verbose)
            console.log("solution: " + limit);
        if (this.part2) {
            if (!this.resolveAllergens()) {
                return NaN;
            }
            return this.sortedIngredients().join(',');
        }
        return this.countIngredients(Array.from(this.safe()));
    };
    Shopping.prototype.partOne = function (verbose, limit) {
        // Returns the solution for part one
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        return this.solution(verbose, limit);
    };
    Shopping.prototype.partTwo = function (verbose, limit) {
        // Returns the solution for part two
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // 1. Return the solution for part two
        return this.solution(verbose, limit);
    };
    return Shopping;
}());
exports.Shopping = Shopping;
// ======================================================================
// end                      s h o p p i n g . t s                     end
// ======================================================================
