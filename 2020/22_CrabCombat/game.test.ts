// ======================================================================
// Crab Combat
//   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      g a m e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_22';
import { Game } from './game';

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

Player 2:
5
8
4
7
10
`;

const EXAMPLE_REVERSED = `
Player 1:
5
8
4
7
10

Player 2:
9
2
6
3
1
`;

const EXAMPLE_INFINITE = `
Player 1:
43
19

Player 2:
2
29
14
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;
const PART_ONE_RESULT = 306;
const PART_TWO_RESULT = 291;

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
    expect(myobj.players).toHaveLength(0);
    expect(myobj.winner).toBe(NaN);
  });

  test('Test the Game object creation from text', () => {
    // 1. Create Game object from text
    const myobj = new Game(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(12);
    expect(myobj.players).toHaveLength(2);
    expect(myobj.winner).toBe(NaN);
    // 3. Test methods
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 9, 2, 6, 3, 1 = 78');
    expect(myobj.players[1].toString()).toBe('2: 5, 8, 4, 7, 10 = 93');
    myobj.oneRound(); // 1
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 2, 6, 3, 1, 9, 5 = 80');
    expect(myobj.players[1].toString()).toBe('2: 8, 4, 7, 10 = 68');
    myobj.oneRound(); // 2
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 6, 3, 1, 9, 5 = 68');
    expect(myobj.players[1].toString()).toBe('2: 4, 7, 10, 8, 2 = 96');
    myobj.oneRound(); // 3
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 3, 1, 9, 5, 6, 4 = 90');
    expect(myobj.players[1].toString()).toBe('2: 7, 10, 8, 2 = 76');
  });

  test('Test the Game object creation from text part 2', () => {
    // 1. Create Game object from text for part2 recusive game
    const myobj = new Game(fromText(EXAMPLE_TEXT), true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(12);
    expect(myobj.players).toHaveLength(2);
    expect(myobj.winner).toBe(NaN);
    // 3. Test methods
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 9, 2, 6, 3, 1 = 78');
    expect(myobj.players[1].toString()).toBe('2: 5, 8, 4, 7, 10 = 93');
    myobj.oneRoundRecursive(); // 1
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 2, 6, 3, 1, 9, 5 = 80');
    expect(myobj.players[1].toString()).toBe('2: 8, 4, 7, 10 = 68');
    myobj.oneRoundRecursive(); // 2
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 6, 3, 1, 9, 5 = 68');
    expect(myobj.players[1].toString()).toBe('2: 4, 7, 10, 8, 2 = 96');
    myobj.oneRoundRecursive(); // 3
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 3, 1, 9, 5, 6, 4 = 90');
    expect(myobj.players[1].toString()).toBe('2: 7, 10, 8, 2 = 76');
    myobj.oneRoundRecursive(); // 4
    myobj.oneRoundRecursive(); // 5
    myobj.oneRoundRecursive(); // 6
    myobj.oneRoundRecursive(); // 7
    myobj.oneRoundRecursive(); // 8
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 4, 9, 8, 5, 2 = 92');
    expect(myobj.players[1].toString()).toBe('2: 3, 10, 1, 7, 6 = 78');
    myobj.oneRoundRecursive(); // 9 -- Going recursive
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 9, 8, 5, 2 = 72');
    expect(myobj.players[1].toString()).toBe('2: 10, 1, 7, 6, 3, 4 = 121');
    myobj.oneRoundRecursive(); // 10
    myobj.oneRoundRecursive(); // 11
    myobj.oneRoundRecursive(); // 12
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 2, 8, 1 = 23');
    expect(myobj.players[1].toString()).toBe('2: 6, 3, 4, 10, 9, 7, 5 = 166');
    myobj.oneRoundRecursive(); // 13
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 8, 1 = 17');
    expect(myobj.players[1].toString()).toBe('2: 3, 4, 10, 9, 7, 5, 6, 2 = 214');
    myobj.oneRoundRecursive(); // 14
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 1, 8, 3 = 22');
    expect(myobj.players[1].toString()).toBe('2: 4, 10, 9, 7, 5, 6, 2 = 190');
    myobj.oneRoundRecursive(); // 15
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 8, 3 = 19');
    expect(myobj.players[1].toString()).toBe('2: 10, 9, 7, 5, 6, 2, 4, 1 = 249');
    myobj.oneRoundRecursive(); // 16
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 3 = 3');
    expect(myobj.players[1].toString()).toBe('2: 9, 7, 5, 6, 2, 4, 1, 10, 8 = 265');
    myobj.oneRoundRecursive(); // 16
    expect(myobj.whoWon()).toBe(2);
    expect(myobj.players[0].toString()).toBe('1:  = 0');
    expect(myobj.players[1].toString()).toBe('2: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3 = 291');
  });

  test('Test the Game object creation from text part 2 reversed', () => {
    // 1. Create Game object from text for part2 recusive game with different cards
    const myobj = new Game(fromText(EXAMPLE_REVERSED), true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(12);
    expect(myobj.players).toHaveLength(2);
    expect(myobj.winner).toBe(NaN);
    // 3. Test methods
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 5, 8, 4, 7, 10 = 93');
    expect(myobj.players[1].toString()).toBe('2: 9, 2, 6, 3, 1 = 78');
    myobj.oneRoundRecursive(); // 1
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 8, 4, 7, 10 = 68');
    expect(myobj.players[1].toString()).toBe('2: 2, 6, 3, 1, 9, 5 = 80');
    myobj.oneRoundRecursive(); // 2
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 4, 7, 10, 8, 2 = 96');
    expect(myobj.players[1].toString()).toBe('2: 6, 3, 1, 9, 5 = 68');
    myobj.oneRoundRecursive(); // 3
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 7, 10, 8, 2 = 76');
    expect(myobj.players[1].toString()).toBe('2: 3, 1, 9, 5, 6, 4 = 90');
    myobj.oneRoundRecursive(); // 4
    myobj.oneRoundRecursive(); // 5
    myobj.oneRoundRecursive(); // 6
    myobj.oneRoundRecursive(); // 7
    myobj.oneRoundRecursive(); // 8
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 3, 10, 1, 7, 6 = 78');
    expect(myobj.players[1].toString()).toBe('2: 4, 9, 8, 5, 2 = 92');
    myobj.oneRoundRecursive(); // 9 -- Going recursive
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 10, 1, 7, 6, 3, 4 = 121');
    expect(myobj.players[1].toString()).toBe('2: 9, 8, 5, 2 = 72');
    myobj.oneRoundRecursive(); // 10
    myobj.oneRoundRecursive(); // 11
    myobj.oneRoundRecursive(); // 12
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 6, 3, 4, 10, 9, 7, 5 = 166');
    expect(myobj.players[1].toString()).toBe('2: 2, 8, 1 = 23');
    myobj.oneRoundRecursive(); // 13
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 3, 4, 10, 9, 7, 5, 6, 2 = 214');
    expect(myobj.players[1].toString()).toBe('2: 8, 1 = 17');
    myobj.oneRoundRecursive(); // 14
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 4, 10, 9, 7, 5, 6, 2 = 190');
    expect(myobj.players[1].toString()).toBe('2: 1, 8, 3 = 22');
    myobj.oneRoundRecursive(); // 15
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 10, 9, 7, 5, 6, 2, 4, 1 = 249');
    expect(myobj.players[1].toString()).toBe('2: 8, 3 = 19');
    myobj.oneRoundRecursive(); // 16
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 9, 7, 5, 6, 2, 4, 1, 10, 8 = 265');
    expect(myobj.players[1].toString()).toBe('2: 3 = 3');
    myobj.oneRoundRecursive(); // 16
    expect(myobj.whoWon()).toBe(1);
    expect(myobj.players[0].toString()).toBe('1: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3 = 291');
    expect(myobj.players[1].toString()).toBe('2:  = 0');
  });

  test('Test the Game object creation from text part 2 with recurision stopping', () => {
    // 1. Create Game object from text for part2 infinite recusive game
    const myobj = new Game(fromText(EXAMPLE_INFINITE), true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(7);
    expect(myobj.players).toHaveLength(2);
    expect(myobj.winner).toBe(NaN);
    // 3. Test methods
    expect(myobj.players[0].toString()).toBe('1: 43, 19 = 105');
    expect(myobj.players[1].toString()).toBe('2: 2, 29, 14 = 78');
    myobj.oneRoundRecursive(); // 1
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 19, 43, 2 = 145');
    expect(myobj.players[1].toString()).toBe('2: 29, 14 = 72');
    myobj.oneRoundRecursive(); // 2
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 43, 2 = 88');
    expect(myobj.players[1].toString()).toBe('2: 14, 29, 19 = 119');
    myobj.oneRoundRecursive(); // 3
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 2, 43, 14 = 106');
    expect(myobj.players[1].toString()).toBe('2: 29, 19 = 77');
    myobj.oneRoundRecursive(); // 4
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 43, 14 = 100');
    expect(myobj.players[1].toString()).toBe('2: 19, 29, 2 = 117');
    myobj.oneRoundRecursive(); // 5
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 14, 43, 19 = 147');
    expect(myobj.players[1].toString()).toBe('2: 29, 2 = 60');
    myobj.oneRoundRecursive(); // 6
    expect(myobj.whoWon()).toBe(NaN);
    expect(myobj.players[0].toString()).toBe('1: 43, 19 = 105');
    expect(myobj.players[1].toString()).toBe('2: 2, 29, 14 = 78');
    myobj.oneRoundRecursive(); // 7
    expect(myobj.whoWon()).toBe(1);
    expect(myobj.players[0].toString()).toBe('1: 43, 19 = 105');
    expect(myobj.players[1].toString()).toBe('2: 2, 29, 14 = 78');
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
// end                     g a m e . t e s t . t s                    end
// ======================================================================
