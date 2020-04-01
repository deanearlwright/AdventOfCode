/* eslint-disable linebreak-style */
// ======================================================================
// Some Assembly Required
//   Advent of Code 2015 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      g a t e s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc07 = require('./aoc_07');
const gates = require('./gates');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i\n';

const PART_ONE_TEXT = `${EXAMPLE_TEXT}d -> a`;
const PART_TWO_TEXT = `${EXAMPLE_TEXT}e -> a`;

const PART_ONE_RESULT = 72;
const PART_TWO_RESULT = 507;

// ======================================================================
//                                                              TestGates
// ======================================================================

describe('Gates', () => {
  test('Test the default Gates creation', () => {
    // 1. Create default Gates object
    const myobj = new gates.Gates({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Gates object creation from text', () => {
    // 1. Create Gates object from text
    const myobj = new gates.Gates({ text: aoc07.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(8);
    expect(Object.keys(myobj.instructions)).toHaveLength(8);
    expect(Object.keys(myobj.wires)).toHaveLength(2);
  });

  test('Test the instructions', () => {
    // 1. Create default Gates object
    const myobj = new gates.Gates({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    // 3. Try out some instructions
    myobj.executeInstruction('123 -> x');
    expect(myobj.wires.x).toBe(123);
    myobj.executeInstruction('456 -> y');
    expect(myobj.wires.y).toBe(456);
    myobj.executeInstruction('x AND y -> d');
    expect(myobj.wires.d).toBe(72);
    myobj.executeInstruction('x OR y -> e');
    expect(myobj.wires.e).toBe(507);
    myobj.executeInstruction('x LSHIFT 2 -> f');
    expect(myobj.wires.f).toBe(492);
    myobj.executeInstruction('y RSHIFT 2 -> g');
    expect(myobj.wires.g).toBe(114);
    myobj.executeInstruction('NOT x -> h');
    expect(myobj.wires.h).toBe(65412);
    myobj.executeInstruction('NOT y -> i');
    expect(myobj.wires.i).toBe(65079);
    myobj.executeInstruction('d -> a');
    expect(myobj.wires.a).toBe(72);
    myobj.executeInstruction('1 OR y -> j');
    expect(myobj.wires.j).toBe(457);
  });

  test('Test part one example of Gates object', () => {
    // 1. Create Gates object from text
    const myobj = new gates.Gates({ text: aoc07.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Gates object', () => {
    // 1. Create Gates object from text
    const myobj = new gates.Gates({ part2: true, text: aoc07.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                     t e s t _ g a t e s . j s                  end
// ======================================================================
