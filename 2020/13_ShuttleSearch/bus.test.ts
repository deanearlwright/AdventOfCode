// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b u s . t e s t . t s
//
// Test Bus for Advent of Code 2020 day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Bus } from './bus';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                TestBus
// ======================================================================

describe('Bus', () => {
  test('Test the default Bus creation', () => {
    // 1. Create default Bus object
    const myobj = new Bus();
    // 2. Make sure it has the default values
    expect(myobj.bid).toBe(0);
    expect(myobj.offset).toBe(0);
  });

  test('Test the Bus object creation from values', () => {
    // 1. Create Bus object from text
    const myobj = new Bus(13, 1);
    // 2. Make sure it has the expected values
    expect(myobj.bid).toBe(13);
    expect(myobj.offset).toBe(1);
    // 3. Check methods
    expect(myobj.nextDeparture(929)).toBe(936);
    expect(myobj.nextDeparture(936)).toBe(936);
    expect(myobj.nextDeparture(939)).toBe(949);
  });
});

// ======================================================================
// end                      b u s . t e s t . t s                     end
// ======================================================================
