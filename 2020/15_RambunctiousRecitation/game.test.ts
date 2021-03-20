// ======================================================================
// Rambunctious Recitation
//   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      g a m e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 15 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_15';
import { Game } from './game';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
0,3,6
`;

interface ExampleTests {
  text: string;
  spoken: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: '0,3,6', spoken: 436 },
  { text: '1,3,2', spoken: 1 },
  { text: '2,1,3', spoken: 10 },
  { text: '1,2,3', spoken: 27 },
  { text: '2,3,1', spoken: 78 },
  { text: '3,2,1', spoken: 438 },
  { text: '3,1,2', spoken: 1836 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: '0,3,6', spoken: 175594 },
  { text: '1,3,2', spoken: 2578 },
  { text: '2,1,3', spoken: 3544142 },
  { text: '1,2,3', spoken: 261214 },
  { text: '2,3,1', spoken: 6895259 },
  { text: '3,2,1', spoken: 18 },
  { text: '3,1,2', spoken: 362 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 436;
const PART_TWO_RESULT = 175594;

// ======================================================================
//                                                              TestGame
// ======================================================================

describe('Game', () => {
  test('Test the default Game creation', () => {
    // 1. Create default Game object
    const myobj = new Game([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Game object creation from text', () => {
    // 1. Create Game object from text
    const myobj = new Game(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Game object
      const myobj = new Game(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.spoken);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Game object using the key as text
      const myobj = new Game(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      // expect(myobj.solution()).toBe(test.spoken);
    });
  });

  test('Test part one example of Game object', () => {
    // 1. Create Game object from text
    const myobj = new Game(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Game object', () => {
    // 1. Create Game object from text
    const myobj = new Game(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   g a m e . t e s t . t s                  end
// ======================================================================
