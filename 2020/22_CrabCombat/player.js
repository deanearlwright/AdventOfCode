"use strict";
// ======================================================================
// Crab Combat
//   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Player = void 0;
// ======================================================================
//                           p l a y e r . t s
//
// Player for the Advent of Code 2020 Day 22 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// ======================================================================
//                                                                 Player
// ======================================================================
var Player = /** @class */ (function () {
    function Player(text, part2) {
        // Create a Player object
        if (part2 === void 0) { part2 = false; }
        // 1. Set the initial values
        this.text = text === undefined ? [] : text;
        this.part2 = part2 === undefined ? false : part2;
        this.id = 0;
        this.cards = [];
        // 2. Process Text
        if (this.text.length > 0) {
            this.processText(this.text);
        }
    }
    Player.prototype.processText = function (text) {
        // Get player number and cards
        // 1. Loop for all of the lines of text
        for (var indx = 0; indx < text.length; indx += 1) {
            var line = text[indx];
            // 2. If this is the player line, save id
            if (line.startsWith('Player')) {
                this.id = parseInt(line.substr(7, 1), 10);
            }
            else {
                // 3. Otherwise save the card
                this.addCard(parseInt(line, 10));
            }
        }
    };
    Player.prototype.addCard = function (card) {
        // Add a card to the player
        this.cards.push(card);
    };
    Player.prototype.addCards = function (cards) {
        // Add multiple cards to the player
        this.cards = this.cards.concat(cards);
    };
    Player.prototype.getTopCard = function () {
        // Returns the top card from the player's deck
        return this.cards.shift() || 0;
    };
    Player.prototype.isEmpty = function () {
        // Returns true if the player has no more cards in the deck
        return this.cards.length === 0;
    };
    Player.prototype.keep = function (high, low) {
        // Keep the cards from a round of the game
        this.addCard(high);
        this.addCard(low);
    };
    Player.prototype.score = function () {
        // Return the score for these cards
        // 1. Start with nothing
        var result = 0;
        var multiplier = this.cards.length;
        // 2. Loop for all of the cards
        for (var indx = 0; indx < this.cards.length; indx += 1) {
            var card = this.cards[indx];
            // 3. Add in the score for this card
            result += card * multiplier;
            // 4. The next card is not worth as much
            multiplier -= 1;
        }
        // 5. Return the total score
        return result;
    };
    Player.prototype.toString = function () {
        // Return the important information for this player
        return this.id + ": " + this.cards.join(', ') + " = " + this.score();
    };
    Player.prototype.hasAtLeast = function (amount) {
        // Does the play have at least the specified number of cards?
        return this.cards.length >= amount;
    };
    Player.prototype.clone = function (amount) {
        // Create a copy of the player with the top n cards
        // 1. Create a basic player
        var cloned = new Player([], this.part2);
        cloned.id = this.id;
        // 2. Copy the top few cards
        for (var indx = 0; indx < amount; indx += 1) {
            cloned.addCard(this.cards[indx]);
        }
        // 3. Return the new micro-Player
        return cloned;
    };
    return Player;
}());
exports.Player = Player;
// ======================================================================
// end                        p l a y e r . t s                       end
// ======================================================================
