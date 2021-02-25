// ======================================================================
// Binary Boarding
//   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b p a s s . t e s t . t s
//
// Test Bpass for Advent of Code 2020 day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Bpass } from './bpass';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'FBFBBFFRLR';

// ======================================================================
//                                                              TestBpass
// ======================================================================

describe('Bpass', () => {
  test('Test the default Bpass creation', () => {
    // 1. Create default Bpass object
    const myobj = new Bpass('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.row).toBe(0);
    expect(myobj.col).toBe(0);
    expect(myobj.seat).toBe(0);
  });

  test('Test the Bpass object creation from text', () => {
    // 1. Create Bpass object from text
    const myobj = new Bpass(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(10);
    expect(myobj.row).toBe(44);
    expect(myobj.col).toBe(5);
    expect(myobj.seat).toBe(357);
  });
});

// ======================================================================
// end                    b p a s s . t e s t . t s                   end
// ======================================================================
