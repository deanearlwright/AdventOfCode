// ======================================================================
// Handheld Halting
//   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c o n s o l e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_08';
import { Console } from './console';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 5;
const PART_TWO_RESULT = 8;

// ======================================================================
//                                                            TestConsole
// ======================================================================

describe('Console', () => {
  test('Test the default Console creation', () => {
    // 1. Create default Console object
    const myobj = new Console([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.instructions).toHaveLength(0);
    expect(myobj.pc).toBe(1);
    expect(myobj.acc).toBe(0);
  });

  test('Test the Console object creation from text', () => {
    // 1. Create Console object from text
    const myobj = new Console(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(9);
    expect(myobj.instructions).toHaveLength(10);
    expect(myobj.pc).toBe(1);
    expect(myobj.acc).toBe(0);

    // 3. Check methods
    expect(myobj.infinite_loop()).toBe(5);
    expect(myobj.fix_the_program()).toBe(8);
  });

  test('Not Test part one example of Console object', () => {
    // 1. Create Console object from text
    const myobj = new Console(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Not Test part two example of Console object', () => {
    // 1. Create Console object from text
    const myobj = new Console(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  c o n s o l e . t e s t . t s                 end
// ======================================================================
