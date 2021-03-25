// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r u l e s . t e s t . t s
//
// Test Rules for Advent of Code 2020 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Rules } from './rules';
import { fromText } from './aoc_16';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
`;

// ======================================================================
//                                                              TestRules
// ======================================================================

describe('Rules', () => {
  test('Test the default Rules creation', () => {
    // 1. Create default Rules object
    const myobj = new Rules([]);

    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.rules).toHaveLength(0);
  });

  test('Test the Rules object creation from text', () => {
    // 1. Create Rules object from text
    const myobj = new Rules(fromText(EXAMPLE_TEXT));

    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(10);
    expect(myobj.rules).toHaveLength(3);
    expect(myobj.rules[0].name).toBe('class');
    expect(myobj.rules[1].name).toBe('row');
    expect(myobj.rules[2].name).toBe('seat');
    expect(myobj.rules[0].numbers[0]).toBe(1);
    expect(myobj.rules[1].numbers[0]).toBe(6);
    expect(myobj.rules[2].numbers[0]).toBe(13);

    // 3. Check methods
    expect(myobj.isValid(0)).toBe(false);
    expect(myobj.isValid(2)).toBe(true);
    expect(myobj.isValid(4)).toBe(false);
    expect(myobj.isValid(55)).toBe(false);
    expect(myobj.isValid(12)).toBe(false);
    expect(myobj.isValid(7)).toBe(true);
    expect(myobj.isValid(3)).toBe(true);
    expect(myobj.isValid(47)).toBe(true);

    expect(myobj.allValid([7, 3, 47])).toBe(true);
    expect(myobj.allValid([40, 4, 50])).toBe(false);
    expect(myobj.allValid([55, 2, 20])).toBe(false);
    expect(myobj.allValid([38, 6, 12])).toBe(false);
  });
});

// ======================================================================
// end                    r u l e s . t e s t . t s                   end
// ======================================================================
