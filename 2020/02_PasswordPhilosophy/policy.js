"use strict";
// ======================================================================
// Password Philosophy
//   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Policy = void 0;
// ======================================================================
//                           p o l i c y . t s
//
// Policy for the Advent of Code 2020 Day 02 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// ======================================================================
//                                                                 Policy
// ======================================================================
var Policy = /** @class */ (function () {
    function Policy(text, part2) {
        // Create a Policy object
        var _a;
        if (part2 === void 0) { part2 = false; }
        // 1. Set the initial values
        this.text = text === undefined ? '' : text;
        this.part2 = part2 === undefined ? false : part2;
        this.low = 0;
        this.high = 0;
        this.letter = '';
        this.pswd = '';
        // 2. If there is a text, populate the policy and password
        if (text.length > 0) {
            var found = text.match(/(\d+)-(\d+) ([a-z]): ([a-z]+)/);
            if (found) {
                this.low = +found[1];
                this.high = +found[2];
                _a = found.slice(3, 5), this.letter = _a[0], this.pswd = _a[1];
            }
            else {
                console.log("Invalid policy text='" + text + "'");
            }
        }
    }
    Policy.prototype.is_valid = function () {
        // Return true if the pswd is valid for the policy
        // 1. For part 1, we need the occurances of the letter to be in the specified range
        if (!this.part2) {
            // 1a. How many times does the letter appear in pswd?
            var re = RegExp(this.letter, 'g');
            var matches = Array.from(this.pswd.matchAll(re));
            var knt = matches.length;
            // 1b. Check that the letter appears the correct number of times
            return knt >= this.low && knt <= this.high;
        }
        // 2. For part 2, we the letter to be in one (but not both) of the given positions
        // 2a. Check for the letter at the two positions
        var atLow = this.letter === this.pswd.substr(this.low - 1, 1);
        var atHigh = this.letter === this.pswd.substr(this.high - 1, 1);
        // 2b. There can be only one
        return (atLow && !atHigh) || (atHigh && !atLow);
    };
    return Policy;
}());
exports.Policy = Policy;
// ======================================================================
// end                        p o l i c y . t s                       end
// ======================================================================
