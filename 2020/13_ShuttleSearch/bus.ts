// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b u s . t s
//
// Bus for the Advent of Code 2020 Day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                    Bus
// ======================================================================

export class Bus {
  // Object for Shuttle Search
  bid: number;

  offset: number;

  constructor(bid = 0, offset = 0) {
    // Create a Bus object

    // 1. Set the initial values
    this.bid = bid === undefined ? 0 : bid;
    this.offset = offset === undefined ? 0 : offset;
  }

  nextDeparture(time: number): number {
    // Returns the ext time the bus departs after the specified fime
    const delta = time % this.bid;
    if (delta === 0) {
      return time;
    }
    return time + this.bid - delta;
  }
}

// ======================================================================
// end                           b u s . t s                          end
// ======================================================================
