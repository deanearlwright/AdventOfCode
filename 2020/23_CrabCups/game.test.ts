// ======================================================================
// Crab Cups
//   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      g a m e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 23 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_23';
import { Game } from './game';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
389125467
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = '67384529';
const PART_TWO_RESULT = 149245887792;

// ======================================================================
//                                                               TestGame
// ======================================================================

describe('Game', () => {
  test('Test the default Game creation', () => {
    // 1. Create default Game object
    const myobj = new Game([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(Object.keys(myobj.cups)).toHaveLength(0);
    expect(myobj.current).toBe(0);
    expect(myobj.maximum).toBe(0);
    // 3. Check methods
    expect(myobj.toString()).toBe('cups: (0)');
  });

  test('Test the Game object creation from text', () => {
    // 1. Create Game object from text
    const myobj = new Game(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(Object.keys(myobj.cups)).toHaveLength(9);
    expect(myobj.current).toBe(3);
    expect(myobj.maximum).toBe(9);
    expect(myobj.cups[3]).toBe(8);
    expect(myobj.cups[8]).toBe(9);
    expect(myobj.cups[6]).toBe(7);
    expect(myobj.cups[7]).toBe(3);
    // 3. Check methods
    expect(myobj.toString()).toBe('cups: (3) 8  9  1  2  5  4  6  7 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (2) 8  9  1  5  4  6  7  3 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (5) 4  6  7  8  9  1  3  2 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (8) 9  1  3  4  6  7  2  5 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (4) 6  7  9  1  3  2  5  8 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (1) 3  6  7  9  2  5  8  4 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (9) 3  6  7  2  5  8  4  1 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (2) 5  8  3  6  7  4  1  9 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (6) 7  4  1  5  8  3  9  2 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (5) 7  4  1  8  3  9  2  6 ');
    myobj.move();
    expect(myobj.toString()).toBe('cups: (8) 3  7  4  1  9  2  6  5 ');
    expect(myobj.labels()).toBe('92658374');
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
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(1);
    expect(Object.keys(myobj.cups)).toHaveLength(1000000);
    expect(myobj.current).toBe(3);
    expect(myobj.maximum).toBe(1000000);
    expect(myobj.cups[3]).toBe(8);
    expect(myobj.cups[8]).toBe(9);
    expect(myobj.cups[6]).toBe(7);
    expect(myobj.cups[7]).toBe(10);
    expect(myobj.cups[10]).toBe(11);
    expect(myobj.cups[999998]).toBe(999999);
    expect(myobj.cups[999999]).toBe(1000000);
    expect(myobj.cups[1000000]).toBe(3);
    // 3. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                     g a m e . t e s t . t s                    end
// ======================================================================
