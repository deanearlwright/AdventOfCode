// ======================================================================
// Handheld Halting
//   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      i n s t r u c t i o n . t e s t . t s
//
// Test Instruction for Advent of Code 2020 day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Instruction } from './instruction';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'acc -99';

// ======================================================================
//                                                        TestInstruction
// ======================================================================

describe('Instruction', () => {
  test('Test the default Instruction creation', () => {
    // 1. Create default Instruction object
    const myobj = new Instruction('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.operation).toBe('');
    expect(myobj.argument).toBe(0);
    expect(myobj.visited).toBe(false);
  });

  test('Test the Instruction object creation from text', () => {
    // 1. Create Instruction object from text
    const myobj = new Instruction(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(7);
    expect(myobj.operation).toBe('acc');
    expect(myobj.argument).toBe(-99);
    expect(myobj.visited).toBe(false);

    // 3. Test methods
    expect(myobj.is_visited()).toBe(false);
    expect(myobj.execute(42)).toStrictEqual([-57, 1]);
    expect(myobj.is_visited()).toBe(true);
    myobj.reset();
    expect(myobj.is_visited()).toBe(false);
  });
});

// ======================================================================
// end              i n s t r u c t i o n . t e s t . t s             end
// ======================================================================
