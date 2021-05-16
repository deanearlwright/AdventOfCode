"use strict";
// ======================================================================
// Allergen Assessment
//   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Label = void 0;
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
var Label = /** @class */ (function () {
    function Label(text, part2) {
        // Create a Label object
        if (part2 === void 0) { part2 = false; }
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
    Label.prototype.processText = function (text) {
        // Assign values from text
        // 1. Divide the text at contains
        var cleaned = text.replace('(', '').replace(')', '');
        var _a = cleaned.split(' contains '), ingredients = _a[0], allergens = _a[1];
        // 2. Add the ingredients
        var ingredientList = ingredients.split(' ');
        for (var indx = 0; indx < ingredientList.length; indx += 1) {
            this.ingredients.add(ingredientList[indx]);
        }
        // 3. Add the allergens
        var allergenList = allergens.split(' ');
        for (var indx = 0; indx < allergenList.length; indx += 1) {
            var allergen = allergenList[indx].replace(',', '');
            this.allergens.add(allergen);
        }
    };
    Label.prototype.hasIngredient = function (ingredient) {
        // Return true if the label lists the ingredient
        return this.ingredients.has(ingredient);
    };
    Label.prototype.hasAllergen = function (allergen) {
        // Return true if the label lists the allergen
        return this.allergens.has(allergen);
    };
    Label.prototype.getIngredients = function () {
        // Returns a list of ingredients
        return Array.from(this.ingredients);
    };
    Label.prototype.getAllergens = function () {
        // Returns a list of allergens
        return Array.from(this.allergens);
    };
    return Label;
}());
exports.Label = Label;
// ======================================================================
// end                         l a b e l . t s                        end
// ======================================================================
