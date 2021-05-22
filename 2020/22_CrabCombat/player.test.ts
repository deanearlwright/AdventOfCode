// ======================================================================
// Crab Combat
//   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p l a y e r . t e s t . t s
//
// Test Player for Advent of Code 2020 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Player } from './player';
import { fromText } from './aoc_22';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Player 1:
9
2
6
3
1
`;

// ======================================================================
//                                                             TestPlayer
// ======================================================================

describe('Player', () => {
  test('Test the default Player creation', () => {
    // 1. Create default Player object
    const myobj = new Player([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.id).toBe(0);
    expect(myobj.cards).toHaveLength(0);
  });

  test('Test the Player object creation from text', () => {
    // 1. Create Player object from text
    const myobj = new Player(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.id).toBe(1);
    expect(myobj.cards).toHaveLength(5);
    expect(myobj.cards[0]).toBe(9);
    expect(myobj.cards[4]).toBe(1);
    // 3. Check methods
    expect(myobj.score()).toBe(45 + 8 + 18 + 6 + 1);
    expect(myobj.toString()).toBe('1: 9, 2, 6, 3, 1 = 78');
    expect(myobj.getTopCard()).toBe(9);
    expect(myobj.cards).toHaveLength(4);
    myobj.keep(9, 5);
    expect(myobj.cards).toHaveLength(6);
    expect(myobj.score()).toBe(12 + 30 + 12 + 3 + 18 + 5);
    expect(myobj.isEmpty()).toBe(false);
    expect(myobj.toString()).toBe('1: 2, 6, 3, 1, 9, 5 = 80');
    expect(myobj.getTopCard()).toBe(2);
    expect(myobj.getTopCard()).toBe(6);
    expect(myobj.getTopCard()).toBe(3);
    expect(myobj.getTopCard()).toBe(1);
    expect(myobj.getTopCard()).toBe(9);
    expect(myobj.getTopCard()).toBe(5);
    expect(myobj.isEmpty()).toBe(true);
    expect(myobj.toString()).toBe('1:  = 0');
  });

  test('Test the Player cloning', () => {
    // 1. Create Player object from text
    const myobj = new Player(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.id).toBe(1);
    expect(myobj.cards).toHaveLength(5);
    expect(myobj.cards[0]).toBe(9);
    expect(myobj.cards[4]).toBe(1);
    expect(myobj.toString()).toBe('1: 9, 2, 6, 3, 1 = 78');
    // 3. Clone that player
    const clone = myobj.clone(3);
    expect(clone.part2).toBe(false);
    expect(clone.text).toHaveLength(0);
    expect(clone.id).toBe(1);
    expect(clone.cards).toHaveLength(3);
    expect(clone.cards[0]).toBe(9);
    expect(clone.cards[2]).toBe(6);
    expect(clone.toString()).toBe('1: 9, 2, 6 = 37');
  });
});

// ======================================================================
// end                   p l a y e r . t e s t . t s                  end
// ======================================================================
