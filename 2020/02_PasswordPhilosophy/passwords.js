"use strict";
// ======================================================================
// Password Philosophy
//   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Passwords = void 0;
// ======================================================================
//                           p a s s w o r d s . t s
//
// A solver for the Advent of Code 2020 Day 02 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
var policy_1 = require("./policy");
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// ======================================================================
//                                                              Passwords
// ======================================================================
var Passwords = /** @class */ (function () {
    function Passwords(text, part2) {
        // Create a Passwords object
        if (part2 === void 0) { part2 = false; }
        // 1. Set the initial values
        this.text = text === undefined ? [] : text;
        this.part2 = part2 === undefined ? false : part2;
        this.policies = [];
        // 2. Process text (if any)
        if (this.text.length !== 0) {
            // 3. Loop for all of the lines of text
            for (var indx = 0; indx < this.text.length; indx += 1) {
                // 4. Create a policy object and add it in to the growing list
                this.policies.push(new policy_1.Policy(this.text[indx], this.part2));
            }
        }
    }
    Passwords.prototype.count_valid = function () {
        // Return the number of passwords that match the policy
        // 1. Start with nothing
        var result = 0;
        // 2. Loop for all of the policies
        for (var indx = 0; indx < this.policies.length; indx += 1) {
            // 3. If this password matches the policy, increment the result
            if (this.policies[indx].is_valid()) {
                result += 1;
            }
        }
        // 4. Return the number of good password/policy pairs
        return result;
    };
    Passwords.prototype.solution = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        if (verbose)
            console.log("solution: " + limit);
        return this.count_valid();
    };
    Passwords.prototype.partOne = function (verbose, limit) {
        // Returns the solution for part one
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        return this.solution(verbose, limit);
    };
    Passwords.prototype.partTwo = function (verbose, limit) {
        // Returns the solution for part two
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // 1. Return the solution for part two
        return this.solution(verbose, limit);
    };
    return Passwords;
}());
exports.Passwords = Passwords;
// ======================================================================
// end                    p a s s w o r d s . t s                     end
// ======================================================================
