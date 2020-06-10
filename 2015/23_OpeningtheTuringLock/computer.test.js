/* eslint-disable linebreak-style */
// ======================================================================
// Opening the Turing Lock
//   Advent of Code 2015 Day 23 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c o m p u t e r . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 23 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc23 = require('./aoc_23');
const computer = require('./computer');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
inc a
jio a, +2
tpl a
inc a
`;

const EXAMPLES_PART_ONE = {
  'inc a;0;0': { a: 1, b: 0, pc: 1 },
  'inc a;1;0': { a: 2, b: 0, pc: 1 },
  'inc a;20;0': { a: 21, b: 0, pc: 1 },
  'jio a, +2;0;0': { a: 0, b: 0, pc: 1 },
  'jio a, +2;1;0': { a: 1, b: 0, pc: 2 },
  'jio a, +20;0;0': { a: 0, b: 0, pc: 1 },
  'jio a, +20;1;0': { a: 1, b: 0, pc: 20 },
  'tpl a;0;0': { a: 0, b: 0, pc: 1 },
  'tpl a;1;0': { a: 3, b: 0, pc: 1 },
  'tpl a;2;0': { a: 6, b: 0, pc: 1 },
  'tpl a;20;0': { a: 60, b: 0, pc: 1 },
  'hlf a;0;0': { a: 0, b: 0, pc: 1 },
  'hlf a;1;0': { a: 0, b: 0, pc: 1 },
  'hlf a;2;0': { a: 1, b: 0, pc: 1 },
  'hlf a;20;0': { a: 10, b: 0, pc: 1 },
  'jmp +2;0;0': { a: 0, b: 0, pc: 2 },
  'jmp -2;1;0': { a: 1, b: 0, pc: -2 },
  'jmp +20;0;0': { a: 0, b: 0, pc: 20 },
  'jmp +0;1;0': { a: 1, b: 0, pc: 0 },
  'jie a, -1;0;0': { a: 0, b: 0, pc: -1 },
  'jie a, +2;1;0': { a: 1, b: 0, pc: 1 },
  'jie a, +3;2;0': { a: 2, b: 0, pc: 3 },
  'jie a, +4;3;0': { a: 3, b: 0, pc: 1 },
};
const EXAMPLES_PART_TWO = {
  'inc a;0;0': { a: 1, b: 0, pc: 1 },
  'inc a;1;0': { a: 2, b: 0, pc: 1 },
  'inc a;20;0': { a: 21, b: 0, pc: 1 },
  'jio a, +2;0;0': { a: 0, b: 0, pc: 1 },
  'jio a, +2;1;0': { a: 1, b: 0, pc: 2 },
  'jio a, +20;0;0': { a: 0, b: 0, pc: 1 },
  'jio a, +20;1;0': { a: 1, b: 0, pc: 20 },
  'tpl a;0;0': { a: 0, b: 0, pc: 1 },
  'tpl a;1;0': { a: 3, b: 0, pc: 1 },
  'tpl a;2;0': { a: 6, b: 0, pc: 1 },
  'tpl a;20;0': { a: 60, b: 0, pc: 1 },
  'hlf a;0;0': { a: 0, b: 0, pc: 1 },
  'hlf a;1;0': { a: 0, b: 0, pc: 1 },
  'hlf a;2;0': { a: 1, b: 0, pc: 1 },
  'hlf a;20;0': { a: 10, b: 0, pc: 1 },
  'jmp +2;0;0': { a: 0, b: 0, pc: 2 },
  'jmp -2;1;0': { a: 1, b: 0, pc: -2 },
  'jmp +20;0;0': { a: 0, b: 0, pc: 20 },
  'jmp +0;1;0': { a: 1, b: 0, pc: 0 },
  'jie a, -1;0;0': { a: 0, b: 0, pc: -1 },
  'jie a, +2;1;0': { a: 1, b: 0, pc: 1 },
  'jie a, +3;2;0': { a: 2, b: 0, pc: 3 },
  'jie a, +4;3;0': { a: 3, b: 0, pc: 1 },
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 0;
const PART_TWO_RESULT = 0;

// ======================================================================
//                                                           TestComputer
// ======================================================================

describe('Computer', () => {
  test('Test the default Computer creation', () => {
    // 1. Create default Computer object
    const myobj = new computer.Computer({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.registers.a).toBe(0);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.pc).toBe(0);
  });

  test('Test the Computer object creation from text', () => {
    // 1. Create Computer object from text
    const myobj = new computer.Computer({ text: aoc23.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.registers.a).toBe(0);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.pc).toBe(0);
    expect(myobj.instructions).toHaveLength(4);
    expect(myobj.instructions[0].opcode).toBe('inc');
    expect(myobj.instructions[0].op1).toBe('a');
    expect(myobj.instructions[1].opcode).toBe('jio');
    expect(myobj.instructions[1].op1).toBe('a');
    expect(myobj.instructions[1].op2).toBe(2);
    expect(myobj.instructions[2].opcode).toBe('tpl');
    expect(myobj.instructions[2].op1).toBe('a');
    expect(myobj.instructions[3].opcode).toBe('inc');
    expect(myobj.instructions[3].op1).toBe('a');
    // 3. Run the program
    expect(myobj.registers).toStrictEqual({ a: 0, b: 0, pc: 0 });
    myobj.run({});
    expect(myobj.registers).toStrictEqual({ a: 2, b: 0, pc: 4 });
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Computer object using the key as text, and initial values of a and b
      // eslint-disable-next-line no-console
      // console.log(key);
      const [inst, a, b] = key.split(';');
      const myobj = new computer.Computer({ text: [inst] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      myobj.registers.a = parseInt(a, 10);
      myobj.registers.b = parseInt(b, 10);
      // 3. Make sure it has the expected value
      expect(myobj.step()).toBe(false);
      expect(myobj.registers).toStrictEqual(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test the Computer object creation from text for part 2', () => {
    // 1. Create Computer object from text
    const myobj = new computer.Computer({ part2: true, text: aoc23.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.registers.a).toBe(0);
    expect(myobj.registers.b).toBe(0);
    expect(myobj.registers.pc).toBe(0);
    expect(myobj.instructions).toHaveLength(4);
    expect(myobj.instructions[0].opcode).toBe('inc');
    expect(myobj.instructions[0].op1).toBe('a');
    expect(myobj.instructions[1].opcode).toBe('jio');
    expect(myobj.instructions[1].op1).toBe('a');
    expect(myobj.instructions[1].op2).toBe(2);
    expect(myobj.instructions[2].opcode).toBe('tpl');
    expect(myobj.instructions[2].op1).toBe('a');
    expect(myobj.instructions[3].opcode).toBe('inc');
    expect(myobj.instructions[3].op1).toBe('a');
    // 3. Run the program
    expect(myobj.registers).toStrictEqual({ a: 0, b: 0, pc: 0 });
    myobj.registers.a = 1;
    expect(myobj.registers).toStrictEqual({ a: 1, b: 0, pc: 0 });
    myobj.run({ verbose: true });
    expect(myobj.registers).toStrictEqual({ a: 7, b: 0, pc: 4 });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Computer object using the key as text
      const [inst, a, b] = key.split(';');
      const myobj = new computer.Computer({ part2: true, text: [inst] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      myobj.registers.a = parseInt(a, 10);
      myobj.registers.b = parseInt(b, 10);
      // 3. Make sure it has the expected value
      expect(myobj.step()).toBe(false);
      expect(myobj.registers).toStrictEqual(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Computer object', () => {
    // 1. Create Computer object from text
    const myobj = new computer.Computer({ text: aoc23.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Computer object', () => {
    // 1. Create Computer object from text
    const myobj = new computer.Computer({ part2: true, text: aoc23.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: true })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 c o m p u t e r . t e s t . j s                end
// ======================================================================
