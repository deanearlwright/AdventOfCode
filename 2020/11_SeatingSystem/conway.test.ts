// ======================================================================
// Seating System
//   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c o n w a y . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_11';
import { Conway } from './conway';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 37;
const PART_TWO_RESULT = 26;

// ======================================================================
//                                                              TestConway
// ======================================================================

describe('Conway', () => {
  test('Test the default Conway creation', () => {
    // 1. Create default Conway object
    const myobj = new Conway([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.seats).toHaveLength(0);
    expect(myobj.leave).toBe(4);
  });

  test('Test the Conway object creation from text', () => {
    // 1. Create Conway object from text
    const myobj = new Conway(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(10);
    expect(myobj.seats).toHaveLength(10);
    expect(myobj.leave).toBe(4);

    // 3. Check methods
    expect(myobj.countOccupied()).toBe(0);
    expect(myobj.seat(0, 0)).toBe('L');
    expect(myobj.neighbor(1, 1, [-1, -1])).toBe('L');
    expect(myobj.neighbor(0, 0, [-1, -1])).toBe(' ');
    expect(myobj.neighbors(0, 0)).toBe(0);

    expect(myobj.nextRound()).toBe(true); // 1
    expect(myobj.countOccupied()).toBe(71);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(2);

    expect(myobj.nextRound()).toBe(true); // 2
    expect(myobj.countOccupied()).toBe(20);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 3
    expect(myobj.countOccupied()).toBe(51);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 4
    expect(myobj.countOccupied()).toBe(30);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 5
    expect(myobj.countOccupied()).toBe(37);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(false); // 6
    expect(myobj.countOccupied()).toBe(37);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);
  });

  test('Test the Conway object creation from text for part 2', () => {
    // 1. Create Conway object from text
    const myobj = new Conway(fromText(EXAMPLE_TEXT), true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(10);
    expect(myobj.seats).toHaveLength(10);
    expect(myobj.leave).toBe(5);

    // 3. Check methods
    expect(myobj.countOccupied()).toBe(0);
    expect(myobj.seat(0, 0)).toBe('L');
    expect(myobj.neighbor(1, 1, [-1, -1])).toBe('L');
    expect(myobj.neighbor(0, 0, [-1, -1])).toBe(' ');
    expect(myobj.neighbors(0, 0)).toBe(0);

    expect(myobj.nextRound()).toBe(true); // 1
    expect(myobj.countOccupied()).toBe(71);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(3);

    expect(myobj.nextRound()).toBe(true); // 2
    expect(myobj.countOccupied()).toBe(7);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 3
    expect(myobj.countOccupied()).toBe(53);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 4
    expect(myobj.countOccupied()).toBe(18);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 5
    expect(myobj.countOccupied()).toBe(31);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(true); // 6
    expect(myobj.countOccupied()).toBe(26);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);

    expect(myobj.nextRound()).toBe(false); // 7
    expect(myobj.countOccupied()).toBe(26);
    expect(myobj.seat(0, 0)).toBe('#');
    expect(myobj.neighbors(0, 0)).toBe(1);
  });

  test('Test part one example of Conway object', () => {
    // 1. Create Conway object from text
    const myobj = new Conway(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Conway object', () => {
    // 1. Create Conway object from text
    const myobj = new Conway(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   c o n w a y . t e s t . t s                  end
// ======================================================================
