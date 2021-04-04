// ======================================================================
// Operation Order
//   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      e x p r e s s i o n . t e s t . t s
//
// Test Expression for Advent of Code 2020 day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Expression } from './expression';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '1 + 2 * 3 + 4 * 5 + 6';

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: '1', result: 1 },
  { text: '123', result: 123 },
  { text: '1 + 2', result: 3 },
  { text: '2 * 3', result: 6 },
  { text: '1 + 2 * 3 + 4 * 5 + 6', result: 71 },
  { text: '1 + (2 * 3) + (4 * (5 + 6))', result: 51 },
  { text: '2 * 3 + (4 * 5)', result: 26 },
  { text: '5 + (8 * 3 + 9 + 3 * 4 * 3)', result: 437 },
  { text: '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', result: 12240 },
  { text: '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', result: 13632 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: '1', result: 1 },
  { text: '123', result: 123 },
  { text: '1 + 2', result: 3 },
  { text: '2 * 3', result: 6 },
  { text: '1 + 2 * 3 + 4 * 5 + 6', result: 231 },
  { text: '1 + (2 * 3) + (4 * (5 + 6))', result: 51 },
  { text: '2 * 3 + (4 * 5)', result: 46 },
  { text: '5 + (8 * 3 + 9 + 3 * 4 * 3)', result: 1445 },
  { text: '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', result: 669060 },
  { text: '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', result: 23340 },

];

// ======================================================================
//                                                         TestExpression
// ======================================================================

describe('Expression', () => {
  test('Test the default Expression creation', () => {
    // 1. Create default Expression object
    const myobj = new Expression('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.tokens).toHaveLength(0);
  });

  test('Test the Expression object creation from text', () => {
    // 1. Create Expression object from text
    const myobj = new Expression(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(21);
    expect(myobj.tokens).toHaveLength(11);
  });
});

test('Test all of the part one examples', () => {
  // 1. Loop for all of the examples
  EXAMPLES_PART_ONE.forEach((test) => {
    // 2. Create Homework object
    const myobj = new Expression(test.text);
    expect(myobj.part2).toBe(false);
    // 3. Make sure it has the expected value
    expect(myobj.evaluate()).toBe(test.result);
  });
});

test('Test all of the part two examples', () => {
  // 1. Loop for all of the examples for the second part
  EXAMPLES_PART_TWO.forEach((test) => {
    // 2. Create Homework object using the key as text
    const myobj = new Expression(test.text, true);
    expect(myobj.part2).toBe(true);
    // 3. Make sure it has the expected value
    expect(myobj.evaluate()).toBe(test.result);
  });
});
// ======================================================================
// end                e x p r e s s i o n . t e s t . t s             end
// ======================================================================
