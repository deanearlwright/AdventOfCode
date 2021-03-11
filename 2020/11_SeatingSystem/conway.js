"use strict";
// ======================================================================
// Seating System
//   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.Conway = void 0;
// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
var SEAT_FLOOR = '.';
var SEAT_EMPTY = 'L';
var SEAT_OCCUPIED = '#';
var SEAT_BEYOND = ' ';
var NEIGHBORS = [
    [-1, -1], [-1, 0], [-1, 1],
    [+0, -1], /*    */ [+0, 1],
    [+1, -1], [+1, 0], [+1, 1],
];
// ======================================================================
//                                                                 Conway
// ======================================================================
var Conway = /** @class */ (function () {
    function Conway(text, part2) {
        // Create a Conway object
        if (part2 === void 0) { part2 = false; }
        // 1. Set the initial values
        this.text = text === undefined ? [] : text;
        this.part2 = part2 === undefined ? false : part2;
        this.seats = [];
        this.leave = this.part2 ? 5 : 4;
        // 2. Process text (if any)
        if (this.text.length !== 0) {
            this.processText();
        }
    }
    Conway.prototype.processText = function () {
        // Process the text into seats
        // 1. Loop for every row in the text
        for (var rindx = 0; rindx < this.text.length; rindx += 1) {
            var textRow = this.text[rindx];
            // 2. Start with an empty row
            var seatrow = [];
            // 3. Loop for every character in the text row
            for (var cindx = 0; cindx < textRow.length; cindx += 1) {
                var textCol = textRow.substr(cindx, 1);
                if (textCol !== SEAT_FLOOR && textCol !== SEAT_EMPTY) {
                    console.log("Unexpected character " + textCol + " at row " + rindx + " column " + cindx);
                    textCol = SEAT_FLOOR;
                }
                // 4. Add the seat text to the seat row
                seatrow.push(textCol);
            }
            // 5. Add the row of seats to seats
            this.seats.push(seatrow);
        }
    };
    Conway.prototype.countOccupied = function () {
        // Returns number of occupied seats
        // 1.Start with nothing
        var result = 0;
        // 2. Loop for all of the rows
        for (var rindx = 0; rindx < this.seats.length; rindx += 1) {
            var row = this.seats[rindx];
            // 3. Loop for all of the columns
            for (var cindx = 0; cindx < row.length; cindx += 1) {
                var col = row[cindx];
                // 4. If someone is in the chair, increment count
                if (col === SEAT_OCCUPIED) {
                    result += 1;
                }
            }
        }
        // 5. Return the number of occupied seats
        return result;
    };
    Conway.prototype.seat = function (row, col) {
        // Return the status of the specified seat
        return this.seats[row][col];
    };
    Conway.prototype.neighbor = function (row, col, delta) {
        // Return the status of a nearby seat
        // 1. Compute the seat number
        var deltaRow = row + delta[0];
        var deltaCol = col + delta[1];
        // 2. If off the seating plane, return beyond
        if (deltaRow < 0 || deltaCol < 0
            || deltaRow >= this.seats.length || deltaCol >= this.seats.length) {
            return SEAT_BEYOND;
        }
        // 3. Return the seat status
        return this.seat(deltaRow, deltaCol);
    };
    Conway.prototype.neighbors = function (row, col) {
        // Return number of occupied seats nearby
        // 1. Start with nothing
        var result = 0;
        // 2. Loop for all of the neighbors
        for (var nindx = 0; nindx < NEIGHBORS.length; nindx += 1) {
            var delta = NEIGHBORS[nindx];
            // 3. Get the status of the nearby seat
            var nbor = this.neighbor(row, col, delta);
            // 4. If the seat is occupied, increment count
            if (nbor === SEAT_OCCUPIED) {
                result += 1;
                // 5. If part two, we look until the next seat
            }
            else if (this.part2 && nbor === SEAT_FLOOR) {
                var slnbor = this.sightLineNeighbor(row, col, delta);
                if (slnbor === SEAT_OCCUPIED) {
                    result += 1;
                }
            }
        }
        // 6. Return the number of occupied seats
        return result;
    };
    Conway.prototype.nextRound = function () {
        // Advance seat occupation, return true if something changed
        // 1. Start with nothing
        var future = [];
        var changed = false;
        // 2. Loop for all of the rows and the seats in the row
        for (var rindx = 0; rindx < this.seats.length; rindx += 1) {
            var currentRow = this.seats[rindx];
            var futureRow = [];
            for (var cindx = 0; cindx < currentRow.length; cindx += 1) {
                var futureSeat = currentRow[cindx];
                // 3. Get the number of occupied seats
                var numOccupied = 0;
                if (futureSeat !== SEAT_FLOOR) {
                    numOccupied = this.neighbors(rindx, cindx);
                }
                // 4. An empty seat becomes occupied if there are no nearby occupied seats
                //    And an occupied seat become empty if there to many people nearby
                switch (futureSeat) {
                    case SEAT_EMPTY:
                        if (numOccupied === 0) {
                            futureSeat = SEAT_OCCUPIED;
                            changed = true;
                        }
                        break;
                    case SEAT_OCCUPIED:
                        if (numOccupied >= this.leave) {
                            futureSeat = SEAT_EMPTY;
                            changed = true;
                        }
                        break;
                    default:
                        break;
                }
                // 5. Set the future seat in the future row
                futureRow.push(futureSeat);
            }
            // 6. Set the future row
            future.push(futureRow);
        }
        // 7. The future is now
        this.seats = future;
        // 8. Return true is a seat occupation changed
        return changed;
    };
    Conway.prototype.untilStable = function () {
        // Return the number of seats occupied when things settle down
        // 1. Loop until there are no changes
        while (this.nextRound()) {
            // empty
        }
        // 2. Return the count of occupied seats
        return this.countOccupied();
    };
    Conway.prototype.sightLineNeighbor = function (row, col, delta) {
        // Returns the next seat in the sight line
        // 1. Start with the floor
        var nbor = SEAT_FLOOR;
        var deltaRow = row + delta[0];
        var deltaCol = col + delta[1];
        // 2. Loop until we are not at a floor space
        while (nbor === SEAT_FLOOR) {
            // 3. Check the next space
            nbor = this.neighbor(deltaRow, deltaCol, delta);
            // 4. Advance
            deltaRow += delta[0];
            deltaCol += delta[1];
        }
        // 5. Return the non-floor value
        return nbor;
    };
    Conway.prototype.solution = function (verbose, limit) {
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        if (verbose)
            console.log("solution: " + limit);
        return this.untilStable();
    };
    Conway.prototype.partOne = function (verbose, limit) {
        // Returns the solution for part one
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        return this.solution(verbose, limit);
    };
    Conway.prototype.partTwo = function (verbose, limit) {
        // Returns the solution for part two
        if (verbose === void 0) { verbose = false; }
        if (limit === void 0) { limit = 0; }
        // 1. Return the solution for part two
        return this.solution(verbose, limit);
    };
    return Conway;
}());
exports.Conway = Conway;
// ======================================================================
// end                      c o n w a y . t s                     end
// ======================================================================
