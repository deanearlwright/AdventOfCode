"use strict";
// ======================================================================
// Toboggan Trajectory
//   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Trees = void 0;
// ======================================================================
//                           t r e e s . t s
//
// A solver for the Advent of Code 2020 Day 03 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
var TREE = '#';
// ======================================================================
//                                                                  Trees
// ======================================================================
var Trees = /** @class */ (function () {
    function Trees(text, part2) {
        // Create a Trees object
        if (part2 === void 0) { part2 = false; }
        this.rows = 0;
        this.cols = 0;
        // 1. Set the initial values
        this.text = text === undefined ? [] : text;
        this.part2 = part2 === undefined ? false : part2;
        this.rows = 0;
        this.cols = 0;
        // 2. Process text (if any)
        if (this.text.length !== 0) {
            this.rows = this.text.length;
            this.cols = this.text[0].length;
        }
    }
    Trees.prototype.is_tree = function (col, row) {
        // Returns true if there is a tree at (col, row)
        // 1. There are no trees below the forest
        if (this.is_below(row)) {
            return false;
        }
        // 2. Check the forest square
        var mcol = col % this.cols;
        if (TREE === this.text[row][mcol]) {
            return true;
        }
        // 4. There is no spoon
        return false;
    };
    Trees.prototype.is_below = function (row) {
        // Returns true if beyond the forest
        return row >= this.rows;
    };
    Trees.prototype.count_trees = function (delta_col, delta_row) {
        // Return number of trees hit in toboggen ride
        // 1. Start at the very beginning
        var col = 0;
        var row = 0;
        var knt = 0;
        // 2. Loop until we are out of the forest
        do {
            // 3. If this is a tree, count it
            if (this.is_tree(col, row)) {
                knt += 1;
            }
            // 4. Advent to the next location
            col += delta_col;
            row += delta_row;
        } while (!this.is_below(row));
        // 5. Return the number of trees hit
        return knt;
    };
    Trees.prototype.solution = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        if (verbose)
            console.log("solution: " + limit);
        if (this.part2) {
            // 1. Get the counts from multiple toboggan runs
            var kntOneOne = this.count_trees(1, 1);
            var kntThreeOne = this.count_trees(3, 1);
            var kntFiveOne = this.count_trees(5, 1);
            var kntSevenOne = this.count_trees(7, 1);
            var kntOneTwo = this.count_trees(1, 2);
            // 2. Return the product of the trees encountered
            return kntOneOne * kntThreeOne * kntFiveOne * kntSevenOne * kntOneTwo;
        }
        return this.count_trees(3, 1);
    };
    Trees.prototype.partOne = function (verbose, limit) {
        // Returns the solution for part one
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        return this.solution(verbose, limit);
    };
    Trees.prototype.partTwo = function (verbose, limit) {
        // Returns the solution for part two
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // 1. Return the solution for part two
        return this.solution(verbose, limit);
    };
    return Trees;
}());
exports.Trees = Trees;
// ======================================================================
// end                      t r e e s . t s                     end
// ======================================================================
