// ======================================================================
// Encoding Error
//   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c y p h e r . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 09 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_09';
import { Cypher } from './cypher';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 127;
const PART_TWO_RESULT = 62;

// ======================================================================
//                                                             TestCypher
// ======================================================================

describe('Cypher', () => {
  test('Test the default Cypher creation', () => {
    // 1. Create default Cypher object
    const myobj = new Cypher([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.numbers).toHaveLength(0);
    expect(myobj.preamble).toBe(25);
  });

  test('Test the Cypher object creation from text', () => {
    // 1. Create Cypher object from text
    const myobj = new Cypher(fromText(EXAMPLE_TEXT), false, 5);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(20);
    expect(myobj.numbers).toHaveLength(20);
    expect(myobj.preamble).toBe(5);

    // 3. Check methods
    expect(myobj.rogue_number()).toBe(127);
    expect(myobj.weakness()).toBe(62);
  });

  test('Test part one example of Cypher object', () => {
    // 1. Create Cypher object from text
    const myobj = new Cypher(fromText(PART_ONE_TEXT), false, 5);
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Cypher object', () => {
    // 1. Create Cypher object from text
    const myobj = new Cypher(fromText(PART_TWO_TEXT), true, 5);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   c y p h e r . t e s t . t s                  end
// ======================================================================
