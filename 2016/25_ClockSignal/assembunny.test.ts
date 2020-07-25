// ======================================================================
// Clock Signal
//   Advent of Code 2016 Day 25 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      a s s e m b u n n y . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 25 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_25';
import { Assembunny } from './assembunny';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT_INITIALIZATION = `
cpy a d
cpy 15 c
cpy 170 b
inc d
dec b
jnz b -2
dec c
jnz c -5
`;

const EXAMPLE_TEXT_COMPLETE = `
cpy a d
cpy 15 c
cpy 170 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT_COMPLETE;
const PART_TWO_TEXT = '';

const PART_ONE_RESULT = 180;
const PART_TWO_RESULT = NaN;

// ======================================================================
//                                                              TestAssembunny
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
    const myobj = new Assembunny(fromText(EXAMPLE_TEXT_INITIALIZATION));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(8);
    expect(myobj.instructions).toHaveLength(8);
    expect(Object.keys(myobj.registers)).toHaveLength(4);
    expect(myobj.registers.a).toBe(0);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.c).toBe(0);
    expect(myobj.registers.d).toBe(0);
    expect(myobj.pc).toBe(0);
    // 3. Set register a to 1 and run until stopped
    myobj.registers.a = 1;
    myobj.run(false, 9999);
    expect(myobj.registers.a).toBe(1);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.c).toBe(0);
    expect(myobj.registers.d).toBe(1 + 15 * 170);
    expect(myobj.pc).toBe(8);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Assembunny object
      const myobj = new Assembunny(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution(false)).toBe(test.result);
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
    expect(myobj.partOne(true, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Assembunny object', () => {
    // 1. Create Assembunny object from text
    const myobj = new Assembunny(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   a s s e m b u n n y . t e s t . t s                  end
// ======================================================================
