// ======================================================================
// Balance Bots
//   Advent of Code 2016 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b o t s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 10 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_10';
import { Bots } from './bots';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

interface ExampleTests {
  value1: number;
  value2: number;
  result: number;
}

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
`;

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { value1: 2, value2: 5, result: 2 },
  { value1: 5, value2: 2, result: 2 },
  { value1: 2, value2: 3, result: 1 },
  { value1: 3, value2: 5, result: 0 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = NaN;
const PART_TWO_RESULT = 30;

// ======================================================================
//                                                               TestBots
// ======================================================================

describe('Bots', () => {
  test('Test the default Bots creation', () => {
    // 1. Create default Bot object
    const myobj = new Bots([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.goes).toHaveLength(0);
    expect(myobj.hasTwo).toHaveLength(0);
  });

  test('Test the Bots object creation from text', () => {
    // 1. Create Bot object from text
    const myobj = new Bots(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    // value 5 goes to bot 2
    // value 3 goes to bot 1
    // value 2 goes to bot 2
    expect(myobj.goes).toHaveLength(3);
    expect(myobj.goes[0].value).toBe(5);
    expect(myobj.goes[0].bot).toBe(2);
    expect(myobj.goes[1].value).toBe(3);
    expect(myobj.goes[1].bot).toBe(1);
    expect(myobj.goes[2].value).toBe(2);
    expect(myobj.goes[2].bot).toBe(2);
    expect(myobj.hasTwo).toHaveLength(0);
    // bot 0 gives low to output 2 and high to output 0
    // bot 1 gives low to output 1 and high to bot 0
    // bot 2 gives low to bot 1 and high to bot 0
    expect(myobj.gives[0].low.which).toBe('output');
    expect(myobj.gives[0].low.num).toBe(2);
    expect(myobj.gives[0].high.which).toBe('output');
    expect(myobj.gives[0].high.num).toBe(0);
    expect(myobj.gives[1].low.which).toBe('output');
    expect(myobj.gives[1].low.num).toBe(1);
    expect(myobj.gives[1].high.which).toBe('bot');
    expect(myobj.gives[1].high.num).toBe(0);
    expect(myobj.gives[2].low.which).toBe('bot');
    expect(myobj.gives[2].low.num).toBe(1);
    expect(myobj.gives[2].high.which).toBe('bot');
    expect(myobj.gives[2].high.num).toBe(0);
    // 3. Make the initial distribution
    myobj.initialDistribution();
    expect(myobj.hasTwo).toHaveLength(1);
    expect(myobj.hasTwo[0]).toBe(2);
    expect(myobj.bots[1]).toStrictEqual([3]);
    expect(myobj.bots[2]).toStrictEqual([5, 2]);
    // 4. And now the comparison distributions
    expect(myobj.distribute(2, { high: 5, low: 2 })).toBe(true);
    expect(myobj.bots[0]).toStrictEqual([5]);
    expect(myobj.bots[1]).toStrictEqual([3, 2]);
    expect(myobj.bots[2]).toStrictEqual([]);
    expect(myobj.distribute(1, { high: 5, low: 2 })).toBe(false);
    expect(myobj.bots[0]).toStrictEqual([5, 3]);
    expect(myobj.bots[1]).toStrictEqual([]);
    expect(myobj.bots[2]).toStrictEqual([]);
    expect(myobj.outs[1]).toStrictEqual([2]);
    expect(myobj.distribute(0, { high: 5, low: 2 })).toBe(false);
    expect(myobj.bots[0]).toStrictEqual([]);
    expect(myobj.bots[1]).toStrictEqual([]);
    expect(myobj.bots[2]).toStrictEqual([]);
    expect(myobj.outs[0]).toStrictEqual([5]);
    expect(myobj.outs[1]).toStrictEqual([2]);
    expect(myobj.outs[2]).toStrictEqual([3]);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Bot object
      const myobj = new Bots(fromText(EXAMPLE_TEXT));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(6);
      // 3. Make sure it has the expected value
      expect(myobj.whoCompares(test.value1, test.value2)).toBe(test.result);
    });
  });

  test('Test all of the part twos examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Bot object using the key as text
      const myobj = new Bots(fromText(EXAMPLE_TEXT), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Bots object', () => {
    // 1. Create Bot object from text
    const myobj = new Bots(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Bots object', () => {
    // 1. Create Bot object from text
    const myobj = new Bots(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                     b o t s . t e s t . t s                    end
// ======================================================================
