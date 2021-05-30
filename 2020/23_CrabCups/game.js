"use strict";
// ======================================================================
// Crab Cups
//   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Game = void 0;
// ======================================================================
//                           g a m e . t s
//
// A solver for the Advent of Code 2020 Day 23 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
var ONE_MILLION = 1000000;
var TEN_MILLION = 10000000;
// ======================================================================
//                                                                   Game
// ======================================================================
var Game = /** @class */ (function () {
    function Game(text, part2) {
        // Create a Game object
        if (part2 === void 0) { part2 = false; }
        // 1. Set the initial values
        this.text = text === undefined ? [] : text;
        this.part2 = part2 === undefined ? false : part2;
        this.cups = {};
        this.current = 0;
        this.maximum = 0;
        // 2. Process text (if any)
        if (this.text.length !== 0) {
            this.processText(this.text[0]);
        }
    }
    Game.prototype.processText = function (text) {
        // Create cups from the input text line
        // 1. Start with nothing
        var values = [0];
        // 2. Loop for the characters in the text, adding the values
        for (var indx = 0; indx < text.length; indx += 1) {
            values.push(parseInt(text[indx], 10));
        }
        // 3. Loop for (most) of the values
        for (var indx = 1; indx < values.length - 1; indx += 1) {
            // 4. Make a linked list of the values
            this.cups[values[indx]] = values[indx + 1];
        }
        // 5. Make it a circular list
        // eslint-disable-next-line prefer-destructuring
        this.cups[values[values.length - 1]] = values[1];
        // 6. Save the maximum cup value
        this.maximum = values.length - 1;
        // 7. The first cup is the current cup (don't you worry anymore)
        // eslint-disable-next-line prefer-destructuring
        this.current = values[1];
        // 8. For part two, add more cups
        if (this.part2) {
            this.addMoreCups(values);
        }
    };
    Game.prototype.addMoreCups = function (values) {
        // Add many more cups
        // 1. Point the last cup to the new cup
        this.cups[values[values.length - 1]] = this.maximum + 1;
        // 2. Loop for the rest of the cups
        for (var value = this.maximum + 1; value <= ONE_MILLION; value += 1) {
            // 3. Add another  cup
            this.cups[value] = value + 1;
        }
        // 4. Make it circular
        // eslint-disable-next-line prefer-destructuring
        this.cups[ONE_MILLION] = values[1];
        // 5. Now we have a much larger maximum
        this.maximum = ONE_MILLION;
    };
    Game.prototype.toString = function () {
        // Return the game object as a string
        // 1. Start with cups: and the current value
        var result = "cups: (" + this.current + ")";
        if (this.current === 0) {
            return result;
        }
        // 2. Loop for all of the cups
        var nxt = this.cups[this.current];
        while (nxt !== this.current) {
            // 3. Add the number to the result
            result = result + " " + nxt + " ";
            // 4. Advance to the next cup
            nxt = this.cups[nxt];
        }
        // 5. Return the formated object
        return result;
    };
    Game.prototype.move = function () {
        // Make one move of the cups
        // 1. Pick up three cups
        var picked1 = this.cups[this.current];
        var picked2 = this.cups[picked1];
        var picked3 = this.cups[picked2];
        var after = this.cups[picked3];
        // 2. Select the destination cup
        var destination = this.current - 1;
        while (destination < 1
            || destination === picked1
            || destination === picked2
            || destination === picked3) {
            if (destination < 1) {
                destination = this.maximum;
            }
            else {
                destination -= 1;
            }
        }
        // console.log(this.current, this.maximum, picked1, picked2, picked3, after, destination);
        // 3. Place the picked cups after the destination
        //    Before: ... -> c -> p1 -> p2 -> p3 -> a -> ...
        //            ... -> d -> x -> ...
        //    After:  ... -> c -> a -> ...
        //            ... -> d -> p1 -> p2 -> p3 -> x -> ...
        this.cups[this.current] = after;
        this.cups[picked3] = this.cups[destination];
        this.cups[destination] = picked1;
        // 4. Select the new current cup
        this.current = this.cups[this.current];
    };
    Game.prototype.labels = function () {
        // Return the cup labels (after 1) as a string
        // 1. Start with nothing
        var result = '';
        if (this.current === 0) {
            return result;
        }
        // 2. Loop for all of the cups
        var nxt = this.cups[1];
        while (nxt !== 1) {
            // 3. Add the number to the result
            result = "" + result + nxt;
            // 4. Advance to the next cup
            nxt = this.cups[nxt];
        }
        // 5. Return the cup labels
        return result;
    };
    Game.prototype.manyMoves = function (count) {
        // Simulate many moves in the game
        for (var indx = 0; indx < count; indx += 1) {
            this.move();
        }
    };
    Game.prototype.starCups = function () {
        // Return product of the labels on the star cups
        // 1. Start with nothing
        var values = [];
        var where = 1;
        // 2. Loop twice
        for (var indx = 1; indx < 3; indx += 1) {
            where = this.cups[where];
            values.push(where);
        }
        // 3. Return the product
        return values[0] * values[1];
    };
    Game.prototype.partOne = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // Returns the solution for part one
        if (verbose) {
            console.log(limit);
        }
        this.manyMoves(100);
        return this.labels();
    };
    Game.prototype.partTwo = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // Returns the solution for part two
        if (verbose) {
            console.log(limit);
        }
        this.manyMoves(TEN_MILLION);
        return this.starCups();
    };
    return Game;
}());
exports.Game = Game;
// ======================================================================
// end                          g a m e . t s                         end
// ======================================================================
