"use strict";
// ======================================================================
// Encoding Error
//   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Cypher = void 0;
// ======================================================================
//                           c y p h e r . t s
//
// A solver for the Advent of Code 2020 Day 09 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// ======================================================================
//                                                                 Cypher
// ======================================================================
var Cypher = /** @class */ (function () {
    function Cypher(text, part2, preamble) {
        // Create a Cypher object
        if (part2 === void 0) { part2 = false; }
        if (preamble === void 0) { preamble = 25; }
        // 1. Set the initial values
        this.text = text === undefined ? [] : text;
        this.part2 = part2 === undefined ? false : part2;
        this.numbers = [];
        this.preamble = preamble === undefined ? 25 : preamble;
        // 2. Process text (if any)
        if (this.text.length !== 0) {
            for (var indx = 0; indx < this.text.length; indx += 1) {
                this.numbers.push(+this.text[indx]);
            }
        }
    }
    Cypher.prototype.rogue_number = function () {
        // Find the number that doesn't follow the rules
        // 1. Set index based on the preamble
        var testStart = this.preamble;
        var testEnd = this.numbers.length;
        var result = NaN;
        // 2. Loop for all of the number to test
        for (var indx = testStart; indx < testEnd; indx += 1) {
            var test_1 = this.numbers[indx];
            result = test_1;
            // 3. Loop for the last bunch of number
            for (var pindx = indx - this.preamble; pindx < indx - 1; pindx += 1) {
                var previous = this.numbers[pindx];
                // 4. Loop for the remaining previous numbers
                for (var rindx = pindx + 1; rindx < indx; rindx += 1) {
                    var remaining = this.numbers[rindx];
                    // 5. Check if this pair of previous number is equal to the test number
                    if ((previous + remaining) === test_1) {
                        // 6. The test number is fine, we will need to find another
                        result = NaN;
                    }
                }
            }
            // 7. If this number is not the result of two of the previous numbers, return it
            if (!Number.isNaN(result)) {
                return result;
            }
            // 8. Well then, try to find another
        }
        // 9. Every number satisified
        return NaN;
    };
    Cypher.prototype.weakness = function () {
        // Find the weakness in the XMAS code, returning min+max
        // 1. Need the rule breaker from part 1
        var ruleBreaker = this.rogue_number();
        // 2. Loop for all the numbers (except the last)
        for (var bindx = 0; bindx < this.numbers.length - 1; bindx += 1) {
            var bottom = this.numbers[bindx];
            var rangeMin = bottom;
            var rangeMax = bottom;
            var rangeSum = bottom;
            // 3. Loop for all of the remaining numbers
            for (var indx = bindx + 1; indx < this.numbers.length; indx += 1) {
                var current = this.numbers[indx];
                rangeSum += current;
                rangeMin = Math.min(rangeMin, current);
                rangeMax = Math.max(rangeMax, current);
                // 4. Have we found the range we were looking for?
                if (rangeSum === ruleBreaker) {
                    // 5. If so, return the min plus max of the range
                    return rangeMin + rangeMax;
                }
                // 6. If the sum is greater than the rule breaker, we need a new beginning
                if (rangeSum > ruleBreaker) {
                    indx = this.numbers.length;
                }
            }
        }
        // 7. Never did find a range that added up to the rule breaker
        return NaN;
    };
    Cypher.prototype.solution = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        if (verbose)
            console.log("solution: " + limit);
        if (this.part2) {
            return this.weakness();
        }
        return this.rogue_number();
    };
    Cypher.prototype.partOne = function (verbose, limit) {
        // Returns the solution for part one
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        return this.solution(verbose, limit);
    };
    Cypher.prototype.partTwo = function (verbose, limit) {
        // Returns the solution for part two
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // 1. Return the solution for part two
        return this.solution(verbose, limit);
    };
    return Cypher;
}());
exports.Cypher = Cypher;
// ======================================================================
// end                        c y p h e r . t s                       end
// ======================================================================
