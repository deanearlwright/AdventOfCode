// ======================================================================
// Handy Haversacks
//   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r u l e . t e s t . t s
//
// Test Rule for Advent of Code 2020 day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Rule } from './rule';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'light red bags contain 1 bright white bag, 2 muted yellow bags.';

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
    expect(myobj.bag).toBe('');
    expect(Object.keys(myobj.bags)).toHaveLength(0);
  });

  test('Test the Rule object creation from text', () => {
    // 1. Create Rule object from text
    const myobj = new Rule(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(EXAMPLE_TEXT.length);
    expect(myobj.bag).toBe('light red');
    expect(Object.keys(myobj.bags)).toHaveLength(2);

    // 3. Check methods
    expect(myobj.contains('bright white')).toBe(1);
    expect(myobj.contains('muted yellow')).toBe(2);
    expect(myobj.contains('puke yellow')).toBe(0);

    expect(myobj.inside()).toBe(3);
  });
});

// ======================================================================
// end                   r u l e . t e s t . t s                  end
// ======================================================================
