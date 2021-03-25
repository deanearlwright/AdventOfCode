// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r u l e . t e s t . t s
//
// Test Rule for Advent of Code 2020 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Rule } from './rule';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'row: 6-11 or 33-44';

// ======================================================================
//                                                              TestRule
// ======================================================================

describe('Rule', () => {
  test('Test the default Rule creation', () => {
    // 1. Create default Rule object
    const myobj = new Rule('');

    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.name).toBe('');
    expect(myobj.numbers).toHaveLength(0);
    expect(myobj.positions).toHaveLength(0);
  });

  test('Test the Rule object creation from text', () => {
    // 1. Create Rule object from text
    const myobj = new Rule(EXAMPLE_TEXT);

    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(18);
    expect(myobj.name).toBe('row');
    expect(myobj.numbers).toHaveLength(4);
    expect(myobj.numbers[0]).toBe(6);
    expect(myobj.numbers[1]).toBe(11);
    expect(myobj.numbers[2]).toBe(33);
    expect(myobj.numbers[3]).toBe(44);
    expect(myobj.positions).toHaveLength(0);

    // 3. Check methods
    expect(myobj.isValid(0)).toBe(false);
    expect(myobj.isValid(5)).toBe(false);
    expect(myobj.isValid(6)).toBe(true);
    expect(myobj.isValid(8)).toBe(true);
    expect(myobj.isValid(11)).toBe(true);
    expect(myobj.isValid(12)).toBe(false);
    expect(myobj.isValid(15)).toBe(false);
    expect(myobj.isValid(32)).toBe(false);
    expect(myobj.isValid(33)).toBe(true);
    expect(myobj.isValid(38)).toBe(true);
    expect(myobj.isValid(44)).toBe(true);
    expect(myobj.isValid(45)).toBe(false);
    expect(myobj.isValid(55)).toBe(false);

    expect(myobj.allValid([])).toBe(true);
    expect(myobj.allValid([5])).toBe(false);
    expect(myobj.allValid([5, 8])).toBe(false);
    expect(myobj.allValid([8, 5])).toBe(false);
    expect(myobj.allValid([8, 38])).toBe(true);
  });
});

// ======================================================================
// end                   r u l e . t e s t . t s                  end
// ======================================================================
