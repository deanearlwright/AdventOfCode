// ======================================================================
// Passport Processing
//   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a s s p o r t . t e s t . t s
//
// Test Passport for Advent of Code 2020 day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Passport } from './passport';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm';

// ======================================================================
//                                                           TestPassport
// ======================================================================

describe('Passport', () => {
  test('Test the default Passport creation', () => {
    // 1. Create default Passport object
    const myobj = new Passport('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.numFields).toBe(0);
  });

  test('Test the Passport object creation from text', () => {
    // 1. Create Passport object from text
    const myobj = new Passport(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(EXAMPLE_TEXT.length);
    expect(myobj.numFields).toBe(8);
    // 3. Check methods
    expect(myobj.is_valid()).toBe(true);
    expect(myobj.is_field_valid('ecl')).toBe(true);
    expect(myobj.is_field_valid('pid')).toBe(true);
    expect(myobj.is_field_valid('eyr')).toBe(true);
    expect(myobj.is_field_valid('hcl')).toBe(true);
    expect(myobj.is_field_valid('byr')).toBe(true);
    expect(myobj.is_field_valid('iyr')).toBe(true);
    expect(myobj.is_field_valid('cid')).toBe(true);
    expect(myobj.is_field_valid('hgt')).toBe(true);
  });
});

// ======================================================================
// end                 p a s s p o r t . t e s t . t s                end
// ======================================================================
