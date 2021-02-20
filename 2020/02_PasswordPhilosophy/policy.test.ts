// ======================================================================
// Password Philosophy
//   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p o l i c y . t e s t . t s
//
// Test Policy for Advent of Code 2020 day 02 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Policy } from './policy';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '1-3 a: abcde';
const EXAMPLE_FAIL1 = '2-4 b: cdefg';
const EXAMPLE_FAIL2 = '2-9 c: ccccccccc';

// ======================================================================
//                                                             TestPolicy
// ======================================================================

describe('Policy', () => {
  test('Test the default Policy creation', () => {
    // 1. Create default Policy object
    const myobj = new Policy('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.low).toBe(0);
    expect(myobj.high).toBe(0);
    expect(myobj.letter).toBe('');
    expect(myobj.pswd).toBe('');
  });

  test('Test the Policy object creation from text', () => {
    // 1. Create Policy object from text
    const myobj = new Policy(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(EXAMPLE_TEXT.length);
    expect(myobj.low).toBe(1);
    expect(myobj.high).toBe(3);
    expect(myobj.letter).toBe('a');
    expect(myobj.pswd).toBe('abcde');
    // 3. Test methods
    expect(myobj.is_valid()).toBe(true);
  });

  test('Test the Policy object with bad password', () => {
    // 1. Create Policy object from text
    const myobj = new Policy(EXAMPLE_FAIL1);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(EXAMPLE_FAIL1.length);
    expect(myobj.low).toBe(2);
    expect(myobj.high).toBe(4);
    expect(myobj.letter).toBe('b');
    expect(myobj.pswd).toBe('cdefg');
    // 3. Test methods
    expect(myobj.is_valid()).toBe(false);
  });

  test('Test the Policy object creation from text [part 2]', () => {
    // 1. Create Policy object from text
    const myobj = new Policy(EXAMPLE_TEXT, true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(EXAMPLE_TEXT.length);
    expect(myobj.low).toBe(1);
    expect(myobj.high).toBe(3);
    expect(myobj.letter).toBe('a');
    expect(myobj.pswd).toBe('abcde');
    // 3. Test methods
    expect(myobj.is_valid()).toBe(true);
  });

  test('Test the Policy object with bad password [part2]', () => {
    // 1. Create Policy object from text
    const myobj = new Policy(EXAMPLE_FAIL2, true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(EXAMPLE_FAIL2.length);
    expect(myobj.low).toBe(2);
    expect(myobj.high).toBe(9);
    expect(myobj.letter).toBe('c');
    expect(myobj.pswd).toBe('ccccccccc');
    // 3. Test methods
    expect(myobj.is_valid()).toBe(false);
  });
});

// ======================================================================
// end                   p o l i c y . t e s t . t s                  end
// ======================================================================
