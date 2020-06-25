// ======================================================================
// Explosives in Cyberspace
//   Advent of Code 2016 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      d e c o m p r e s s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 09 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_09';
import { Decompress } from './decompress';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
ADVENT
A(1x5)BC
(3x3)XYZ
A (2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABC Y
`;

interface ExampleTests {
  text: string;
  result: Number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: 'ADVENT  ', result: 6 },
  { text: '  A(1x5)BC', result: 7 },
  { text: '(3x3)XYZ', result: 9 },
  { text: 'A (2x2)BCD(2x2)EFG', result: 11 },
  { text: '(6x1)(1x3)A', result: 6 },
  { text: 'X(8x2)(3x3)ABC Y', result: 18 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: 'ADVENT', result: 6 },
  { text: 'A(1x5)BC', result: 7 },
  { text: '(3x3)XYZ', result: 9 },
  { text: 'X(8x2)(3x3)ABCY', result: 20 },
  { text: '(27x12)(20x12)(13x14)(7x10)(1x12)A', result: 241920 },
  { text: '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', result: 445 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = '\nX(8x2)(3x3)ABCY';

const PART_ONE_RESULT = 6 + 7 + 9 + 11 + 6 + 18;
const PART_TWO_RESULT = 20;

// ======================================================================
//                                                         TestDecompress
// ======================================================================

describe('Decompress', () => {
  test('Test the default Decompress creation', () => {
    // 1. Create default Decompress object
    const myobj = new Decompress([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Decompress object creation from text', () => {
    // 1. Create Decompress object from text
    const myobj = new Decompress(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Decompress object
      const myobj = new Decompress(fromText(`\n${test.text}`));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Decompress object using the key as text
      const myobj = new Decompress(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Decompress object', () => {
    // 1. Create Decompress object from text
    const myobj = new Decompress(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Decompress object', () => {
    // 1. Create Decompress object from text
    const myobj = new Decompress(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end               d e c o m p r e s s . t e s t . t s              end
// ======================================================================
