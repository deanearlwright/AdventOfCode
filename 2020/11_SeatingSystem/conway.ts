// ======================================================================
// Seating System
//   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           c o n w a y . t s
//
// A solver for the Advent of Code 2020 Day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Seat = '.' | 'L' | '#' | ' ';
type SeatRow = Seat[];
type Seats = SeatRow[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const SEAT_FLOOR: Seat = '.';
const SEAT_EMPTY: Seat = 'L';
const SEAT_OCCUPIED: Seat = '#';
const SEAT_BEYOND: Seat = ' ';

const NEIGHBORS = [
  [-1, -1], [-1, 0], [-1, 1],
  [+0, -1], /*    */ [+0, 1],
  [+1, -1], [+1, 0], [+1, 1],
];

// ======================================================================
//                                                                 Conway
// ======================================================================

export class Conway {
  // Object for Seating System
  text: string[];

  part2: boolean;

  seats: Seats;

  leave: number;

  constructor(text: string[], part2 = false) {
    // Create a Conway object

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

  processText() {
    // Process the text into seats
    // 1. Loop for every row in the text
    for (let rindx = 0; rindx < this.text.length; rindx += 1) {
      const textRow = this.text[rindx];

      // 2. Start with an empty row
      const seatrow: SeatRow = [];

      // 3. Loop for every character in the text row
      for (let cindx = 0; cindx < textRow.length; cindx += 1) {
        let textCol = textRow.substr(cindx, 1) as Seat;
        if (textCol !== SEAT_FLOOR && textCol !== SEAT_EMPTY) {
          console.log(`Unexpected character ${textCol} at row ${rindx} column ${cindx}`);
          textCol = SEAT_FLOOR;
        }

        // 4. Add the seat text to the seat row
        seatrow.push(textCol);
      }
      // 5. Add the row of seats to seats
      this.seats.push(seatrow);
    }
  }

  countOccupied() {
    // Returns number of occupied seats

    // 1.Start with nothing
    let result = 0;

    // 2. Loop for all of the rows
    for (let rindx = 0; rindx < this.seats.length; rindx += 1) {
      const row = this.seats[rindx];

      // 3. Loop for all of the columns
      for (let cindx = 0; cindx < row.length; cindx += 1) {
        const col = row[cindx];

        // 4. If someone is in the chair, increment count
        if (col === SEAT_OCCUPIED) {
          result += 1;
        }
      }
    }

    // 5. Return the number of occupied seats
    return result;
  }

  seat(row: number, col: number): Seat {
    // Return the status of the specified seat
    return this.seats[row][col];
  }

  neighbor(row: number, col: number, delta: number[]): Seat {
    // Return the status of a nearby seat

    // 1. Compute the seat number
    const deltaRow = row + delta[0];
    const deltaCol = col + delta[1];

    // 2. If off the seating plane, return beyond
    if (deltaRow < 0 || deltaCol < 0
      || deltaRow >= this.seats.length || deltaCol >= this.seats.length) {
      return SEAT_BEYOND;
    }

    // 3. Return the seat status
    return this.seat(deltaRow, deltaCol);
  }

  neighbors(row: number, col: number): number {
    // Return number of occupied seats nearby

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the neighbors
    for (let nindx = 0; nindx < NEIGHBORS.length; nindx += 1) {
      const delta = NEIGHBORS[nindx];

      // 3. Get the status of the nearby seat
      const nbor = this.neighbor(row, col, delta);

      // 4. If the seat is occupied, increment count
      if (nbor === SEAT_OCCUPIED) {
        result += 1;
        // 5. If part two, we look until the next seat
      } else if (this.part2 && nbor === SEAT_FLOOR) {
        const slnbor = this.sightLineNeighbor(row, col, delta);
        if (slnbor === SEAT_OCCUPIED) {
          result += 1;
        }
      }
    }

    // 6. Return the number of occupied seats
    return result;
  }

  nextRound(): boolean {
    // Advance seat occupation, return true if something changed

    // 1. Start with nothing
    const future: Seats = [];
    let changed = false;

    // 2. Loop for all of the rows and the seats in the row
    for (let rindx = 0; rindx < this.seats.length; rindx += 1) {
      const currentRow = this.seats[rindx];
      const futureRow: SeatRow = [];
      for (let cindx = 0; cindx < currentRow.length; cindx += 1) {
        let futureSeat = currentRow[cindx];

        // 3. Get the number of occupied seats
        let numOccupied = 0;
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
  }

  untilStable(): number {
    // Return the number of seats occupied when things settle down

    // 1. Loop until there are no changes
    while (this.nextRound()) {
      // empty
    }

    // 2. Return the count of occupied seats
    return this.countOccupied();
  }

  sightLineNeighbor(row: number, col: number, delta: number[]): Seat {
    // Returns the next seat in the sight line

    // 1. Start with the floor
    let nbor = SEAT_FLOOR;
    let deltaRow = row + delta[0];
    let deltaCol = col + delta[1];

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
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.untilStable();
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      c o n w a y . t s                     end
// ======================================================================
