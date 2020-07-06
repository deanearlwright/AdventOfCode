// ======================================================================
// One-Time Pad
//   Advent of Code 2016 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a d . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_14';
import { Pad } from './pad';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
abc
`;

interface ExampleTests {
  text: string;
  result: Number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 22728;
const PART_TWO_RESULT = 22551;

// ======================================================================
//                                                                TestPad
// ======================================================================

describe('Pad', () => {
  test('Test the default Pad creation', () => {
    // 1. Create default Pad object
    const myobj = new Pad([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.salt).toBe('');
    expect(myobj.text).toHaveLength(0);
    expect(myobj.hashes).toHaveLength(0);
  });

  test('Test the Pad object creation from text', () => {
    // 1. Create Pad object from text
    const myobj = new Pad(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.salt).toBe('abc');
    expect(myobj.hashes).toHaveLength(0);
    // 3. Get the first hash
    myobj.nextHash();
    expect(myobj.hashes).toHaveLength(1);
    expect(myobj.hashes[0].triple).toBe('');
    // 4. Get the first triple
    expect(myobj.nextTriple(0)).toBe(18);
    expect(myobj.hashes).toHaveLength(19);
    expect(myobj.hashes[18].triple).toBe('8');
    expect(myobj.foundPenta(18)).toBe(false);
    // 5. Get the second triple
    expect(myobj.nextTriple(19)).toBe(39);
    expect(myobj.hashes[39].triple).toBe('e');
    expect(myobj.foundPenta(39)).toBe(true);
    // 6. Get the next Key
    expect(myobj.nextKey(40)).toBe(92);
    expect(myobj.hashes[92].triple).toBe('9');
    expect(myobj.hashes[92].key).toBe(true);
  });

  test('Test the Pad object creation from text part two', () => {
    // 1. Create Pad object from text
    const myobj = new Pad(fromText(EXAMPLE_TEXT), true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.salt).toBe('abc');
    expect(myobj.hashes).toHaveLength(0);
    // 3. Get the first hash
    myobj.nextHash();
    expect(myobj.hashes).toHaveLength(1);
    expect(myobj.hashes[0].hash).toBe('a107ff634856bb300138cac6568c0f24');
    // 4. Get the first triple
    expect(myobj.nextTriple(0)).toBe(5);
    expect(myobj.hashes).toHaveLength(6);
    expect(myobj.hashes[5].triple).toBe('2');
    expect(myobj.foundPenta(5)).toBe(false);
    // 5. Get the second triple
    expect(myobj.nextTriple(6)).toBe(10);
    expect(myobj.hashes[10].triple).toBe('e');
    expect(myobj.foundPenta(10)).toBe(true);
    // 6. Get the first Key
    expect(myobj.nextKey(0)).toBe(10);
    expect(myobj.hashes[10].triple).toBe('e');
    expect(myobj.hashes[10].key).toBe(true);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Pad object
      const myobj = new Pad(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Pad object using the key as text
      const myobj = new Pad(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Pad object', () => {
    // 1. Create Pad object from text
    const myobj = new Pad(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Pad object', () => {
    // 1. Create Pad object from text
    const myobj = new Pad(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                      p a d . t e s t . t s                     end
// ======================================================================
