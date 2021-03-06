// ======================================================================
// Leonardo's Monorail
//   Advent of Code 2016 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      a s s e m b u n n y . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_12';
import { Assembunny } from './assembunny';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a`;

interface ExampleTests {
  text: string;
  result: Number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 42;
const PART_TWO_RESULT = 42;

// ======================================================================
//                                                         TestAssembunny
// ======================================================================

describe('Assembunny', () => {
  test('Test the default Assembunny creation', () => {
    // 1. Create default Assembunny object
    const myobj = new Assembunny([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.instructions).toHaveLength(0);
    expect(Object.keys(myobj.registers)).toHaveLength(4);
    expect(myobj.registers.a).toBe(0);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.c).toBe(0);
    expect(myobj.registers.d).toBe(0);
    expect(myobj.pc).toBe(0);
  });

  test('Test the Assembunny object creation from text', () => {
    // 1. Create Assembunny object from text
    const myobj = new Assembunny(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.instructions).toHaveLength(6);
    expect(Object.keys(myobj.registers)).toHaveLength(4);
    expect(myobj.registers.a).toBe(0);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.c).toBe(0);
    expect(myobj.registers.d).toBe(0);
    expect(myobj.pc).toBe(0);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Assembunny object
      const myobj = new Assembunny(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Assembunny object using the key as text
      const myobj = new Assembunny(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Assembunny object', () => {
    // 1. Create Assembunny object from text
    const myobj = new Assembunny(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Assembunny object', () => {
    // 1. Create Assembunny object from text
    const myobj = new Assembunny(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end               a s s e m b u n n y . t e s t . t s              end
// ======================================================================
