"use strict";
// ======================================================================
// Crab Combat
//   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Game = void 0;
// ======================================================================
//                           g a m e . t s
//
// A solver for the Advent of Code 2020 Day 22 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
var player_1 = require("./player");
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
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
        this.players = [];
        this.winner = NaN;
        this.previous = new Set();
        // 2. Process text (if any)
        if (this.text.length !== 0) {
            this.processText(this.text);
        }
    }
    Game.prototype.processText = function (text) {
        // Convert the text into players
        // 1. Start with nothing
        var player = null;
        // 2. Loop for all of the lines of text
        for (var indx = 0; indx < text.length; indx += 1) {
            var line = text[indx];
            // 3. If Player line, start a new player
            if (line.startsWith('Player')) {
                player = new player_1.Player([line]);
                this.players.push(player);
            }
            else if (player) {
                // 4. Otherwise add a card to the player
                player.addCard(parseInt(line, 10));
            }
            else {
                console.log("Unable to process line " + indx + ": " + line);
            }
        }
    };
    Game.prototype.whoWon = function () {
        // Return the index of the winner, or NaN if there isn't one
        // 1. If there is a saved winner, return it
        if (this.winner) {
            return this.winner;
        }
        // 2. If someone has run out of cards, the other one is the winner
        if (this.players[0].isEmpty()) {
            this.winner = this.players[1].id;
        }
        else if (this.players[1].isEmpty()) {
            this.winner = this.players[0].id;
        }
        // 3. Return the winner or no one yet
        return this.winner;
    };
    Game.prototype.getPlayerById = function (id) {
        // Given a player id, return the player object
        // 1. Loop for all of the players
        for (var indx = 0; indx < this.players.length; indx += 1) {
            if (id === this.players[indx].id) {
                return this.players[indx];
            }
        }
        // 2. Not found, oh well
        return new player_1.Player([]);
    };
    Game.prototype.oneRound = function () {
        // Play one round of the game
        // 1. Get a card from each player
        var card0 = this.players[0].getTopCard();
        var card1 = this.players[1].getTopCard();
        // 2. Determine who won the round and gets to keep the cards
        if (card0 > card1) {
            this.players[0].keep(card0, card1);
        }
        else {
            this.players[1].keep(card1, card0);
        }
    };
    Game.prototype.score = function () {
        // Return the score for the winning player (the other player has zero)
        return this.players[0].score() + this.players[1].score();
    };
    Game.prototype.play = function () {
        // Play until there is a winner and return the winning score
        // 1. Loop until there is a winner
        while (Number.isNaN(this.whoWon())) {
            // 2. Play one round
            this.oneRound();
        }
        // 3. Return the winning score
        return this.score();
    };
    Game.prototype.oneRoundRecursive = function () {
        // Play one round of the game
        // 1. Infinate game prevention
        var current = this.hash();
        if (this.previous.has(current)) {
            this.winner = this.players[0].id;
            return;
        }
        this.previous.add(current);
        // 2. Get a card from each player
        var card0 = this.players[0].getTopCard();
        var card1 = this.players[1].getTopCard();
        // 3. Check if going down the recursive hole
        if (this.isRecursive(card0, card1)) {
            // 4. Play out a recursive subgame
            var subWinner = this.playSubGame(card0, card1);
            if (subWinner === this.players[0].id) {
                this.players[0].keep(card0, card1);
            }
            else {
                this.players[1].keep(card1, card0);
            }
            // 5. Otherwise, play out this round using normal rules
        }
        else if (card0 > card1) {
            this.players[0].keep(card0, card1);
        }
        else {
            this.players[1].keep(card1, card0);
        }
    };
    Game.prototype.playRecursive = function () {
        // Play until there is a winner and return the winning score
        // 1. Loop until there is a winner
        while (Number.isNaN(this.whoWon())) {
            // 2. Play one round
            this.oneRoundRecursive();
        }
        // 3. Return the winning score
        return this.score();
    };
    Game.prototype.hash = function () {
        // Return a 'hash' of the state of the two players
        return this.players[0].toString() + "; " + this.players[1].toString();
    };
    Game.prototype.playSubGame = function (card0, card1) {
        // Play a new sub game and return the number of the winner
        // 1. Create a new Game
        var subGame = new Game([], true);
        // 2. Clone the players but with limited cards
        var player0 = this.players[0].clone(card0);
        var player1 = this.players[1].clone(card1);
        subGame.players.push(player0);
        subGame.players.push(player1);
        // 1. Loop until there is a winner
        while (Number.isNaN(subGame.whoWon())) {
            // 2. Play one round
            subGame.oneRoundRecursive();
        }
        // 3. Return the winning score
        return subGame.winner;
    };
    Game.prototype.isRecursive = function (card0, card1) {
        // Return true if a recursive subgame should be player (both players have enough cards)
        return this.players[0].hasAtLeast(card0) && this.players[1].hasAtLeast(card1);
    };
    Game.prototype.solution = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        if (verbose)
            console.log("solution: " + limit);
        if (this.part2) {
            return this.playRecursive();
        }
        return this.play();
    };
    Game.prototype.partOne = function (verbose, limit) {
        // Returns the solution for part one
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        return this.solution(verbose, limit);
    };
    Game.prototype.partTwo = function (verbose, limit) {
        // Returns the solution for part two
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // 1. Return the solution for part two
        return this.solution(verbose, limit);
    };
    return Game;
}());
exports.Game = Game;
// ======================================================================
// end                          g a m e . t s                         end
// ======================================================================
