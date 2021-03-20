// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c r t . t e s t . t s
//
// Test CRT for Advent of Code 2020 day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { CRT } from './crt';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Testcrt
// ======================================================================

describe('crt', () => {
  test('Test the crt', () => {
    expect(CRT([3, 5, 7], [2, 3, 2])).toBe(23);
    expect(CRT([5, 13], [2, 3])).toBe(42);
    expect(CRT([11, 12, 13], [10, 4, 12])).toBe(1000);
    expect(CRT([5, 7, 9, 11], [1, 2, 3, 4])).toBe(1731);
    expect(CRT([7, 13, 59, 31, 19], [0, 12, 55, 25, 12])).toBe(1068781);
    expect(CRT([17, 13, 19], [0, 11, 16])).toBe(3417);
    expect(CRT([67, 7, 59, 61], [0, 6, 57, 58])).toBe(754018);
    expect(CRT([67, 7, 59, 61], [0, 5, 56, 57])).toBe(779210);
    expect(CRT([67, 7, 59, 61], [0, 6, 56, 57])).toBe(1261476);
    expect(CRT([1789, 37, 47, 1889], [0, 36, 45, 1886])).toBe(1202161486);
  });
});

// ======================================================================
// end                      c r t . t e s t . t s                     end
// ======================================================================
