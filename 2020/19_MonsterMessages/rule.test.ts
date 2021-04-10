// ======================================================================
// Monster Messages
//   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r u l e . t e s t . t s
//
// Test Rule for Advent of Code 2020 day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Rule } from './rule';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '1: 2 3 | 3 2';
const EXAMPLE_TEXT4 = '4: "a"';

// ======================================================================
//                                                               TestRule
// ======================================================================

describe('Rule', () => {
  test('Test the default Rule creation', () => {
    // 1. Create default Rule object
    const myobj = new Rule('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.number).toBe(0);
    expect(myobj.definition).toHaveLength(0);
  });

  test('Test the Rule object creation from text', () => {
    // 1. Create Rule object from text
    const myobj = new Rule(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(12);
    expect(myobj.number).toBe(1);
    expect(myobj.definition).toBe('2 3 | 3 2');
    // 3. Test methods
    expect(myobj.isConstant()).toBe(false);
    expect(myobj.alternatives()).toStrictEqual(['2 3', '3 2']);
  });

  test('Test the Rule object creation for constant', () => {
    // 1. Create Rule object from text
    const myobj = new Rule(EXAMPLE_TEXT4);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.number).toBe(4);
    expect(myobj.definition).toBe('"a"');
    // 3. Test methods
    expect(myobj.isConstant()).toBe(true);
    expect(myobj.letter()).toBe('a');
  });
});

// ======================================================================
// end                     r u l e . t e s t . t s                    end
// ======================================================================
