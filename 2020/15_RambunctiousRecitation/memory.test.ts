// ======================================================================
// Rambunctious Recitation
//   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      m e m o r y . t e s t . t s
//
// Test Memory for Advent of Code 2020 day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Memory } from './memory';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '0,3,6';
const EXAMPLE_AGES = [0, 3, 3, 1, 0, 4, 0];

// ======================================================================
//                                                             TestMemory
// ======================================================================

describe('Memory', () => {
  test('Test the default Memory creation', () => {
    // 1. Create default Memory object
    const myobj = new Memory('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.age).toBe(-1);
    expect(myobj.turn).toBe(0);
    expect(myobj.numbers).toStrictEqual({});
  });

  test('Test the Memory object creation from text', () => {
    // 1. Create Memory object from text
    const myobj = new Memory(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(5);
    expect(myobj.age).toBe(0);
    expect(myobj.turn).toBe(3);
    expect(myobj.numbers[0]).toBe(1);
    expect(myobj.numbers[3]).toBe(2);
    expect(myobj.numbers[6]).toBe(3);

    // 3. Speak some more numbers
    for (let indx = 0; indx < EXAMPLE_AGES.length; indx += 1) {
      const age = EXAMPLE_AGES[indx];
      expect(myobj.age).toBe(age);
      myobj.add(age);
    }

    // 4. Final check
    expect(myobj.age).toBe(2);
    expect(myobj.turn).toBe(10);
  });
});

// ======================================================================
// end                   m e m o r y . t e s t . t s                  end
// ======================================================================
