// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b u s e s . t s
//
// A solver for the Advent of Code 2020 Day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Bus } from './bus';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Buses
// ======================================================================

export class Buses {
  // Object for Shuttle Search
  text: string[];

  part2: boolean;

  buses: Bus[];

  earliest: number;

  constructor(text: string[], part2 = false) {
    // Create a Buses object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.buses = [];
    this.earliest = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText() {
    // Read earliest time and bus arrival intervals

    // 1. Save earlist time
    this.earliest = parseInt(this.text[0], 10);
    // 2. Split up the bus IDs that are in service
    const busIDs = this.text[1].split(',');
    // 3. Loop for each bus in the text
    for (let indx = 0; indx < busIDs.length; indx += 1) {
      const busID = busIDs[indx];
      // 4. If not X, create and save bus
      if (busID !== 'x') {
        const aBus = new Bus(parseInt(busID, 10), indx);
        this.buses.push(aBus);
      }
    }
  }

  waiting(): number {
    // Return the ID of the next bus times the number of minutes waiting

    // 1. Start with nothing
    let bestBus = 0;
    let bestTime = this.earliest + 9999999;

    // 2. Loop for all of the buses
    for (let indx = 0; indx < this.buses.length; indx += 1) {
      const aBus = this.buses[indx];

      // 3. When is the earlist this bus will depart
      const busDeparts = aBus.nextDeparture(this.earliest);

      // 4. If this bus departs ealiet then the best time, use this bus
      if (busDeparts < bestTime) {
        bestTime = busDeparts;
        bestBus = aBus.bid;
      }
    }
    // 5. Return the bus ID times the minutes spent waiting
    return bestBus * (bestTime - this.earliest);
  }

  contest(): number {
    // Return the time that the first bus departs and all the rest in succession

    // 1. Start with nothing
    const ids: number[] = [];
    const offsets: number[] = [];

    // 2. Loop for all of the buses
    for (let indx = 0; indx < this.buses.length; indx += 1) {
      const aBus = this.buses[indx];

      // 3. Add to the mods and offset arrays
      ids.push(aBus.bid);
      offsets.push(aBus.offset);
    }

    // 4. Try to find the time
    //    Converted from C code of Ryan Palo because I couldn't get crt to work with large numbers
    //    https://dev.to/rpalo/advent-of-code-2020-solution-megathread-day-13-shuttle-search-313f
    let step = ids[0];
    let search = 1;
    for (let time = step; time < 999999999999999; time += step) {
      let success = true;
      for (let indx = 0; indx <= search; indx += 1) {
        if ((time + offsets[indx]) % ids[indx] !== 0) {
          success = false;
          break;
        }
      }
      if (success && search === ids.length - 1) {
        return time;
      }
      if (success) {
        step *= ids[search];
        search += 1;
      }
    }
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.contest();
    }
    return this.waiting();
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
// end                         b u s e s . t s                        end
// ======================================================================
