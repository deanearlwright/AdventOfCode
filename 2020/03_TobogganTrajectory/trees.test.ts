// ======================================================================
// Toboggan Trajectory
//   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t r e e s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 03 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_03';
import { Trees } from './trees';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 7;
const PART_TWO_RESULT = 336;

// ======================================================================
//                                                              TestTrees
// ======================================================================

describe('Trees', () => {
  test('Test the default Trees creation', () => {
    // 1. Create default Trees object
    const myobj = new Trees([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.rows).toBe(0);
    expect(myobj.cols).toBe(0);
  });

  test('Test the Trees object creation from text', () => {
    // 1. Create Trees object from text
    const myobj = new Trees(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(11);
    expect(myobj.rows).toBe(11);
    expect(myobj.cols).toBe(11);
    // 3. Check methods
    expect(myobj.is_below(0)).toBe(false);
    expect(myobj.is_below(5)).toBe(false);
    expect(myobj.is_below(9)).toBe(false);
    expect(myobj.is_below(10)).toBe(false);
    expect(myobj.is_below(11)).toBe(true);
    expect(myobj.is_below(12)).toBe(true);

    expect(myobj.is_tree(0, 0)).toBe(false);
    expect(myobj.is_tree(3, 1)).toBe(false);
    expect(myobj.is_tree(6, 2)).toBe(true);
    expect(myobj.is_tree(9, 3)).toBe(false);
    expect(myobj.is_tree(12, 4)).toBe(true);
    expect(myobj.is_tree(15, 5)).toBe(true);
    expect(myobj.is_tree(18, 6)).toBe(false);
    expect(myobj.is_tree(21, 7)).toBe(true);
    expect(myobj.is_tree(24, 8)).toBe(true);
    expect(myobj.is_tree(27, 9)).toBe(true);
    expect(myobj.is_tree(30, 10)).toBe(true);
    expect(myobj.is_tree(33, 11)).toBe(false);
    expect(myobj.is_tree(38, 12)).toBe(false);

    expect(myobj.count_trees(3, 1)).toBe(7);
    expect(myobj.count_trees(1, 1)).toBe(2);
    expect(myobj.count_trees(5, 1)).toBe(3);
    expect(myobj.count_trees(7, 1)).toBe(4);
    expect(myobj.count_trees(1, 2)).toBe(2);
  });

  test('Test part one example of Trees object', () => {
    // 1. Create Trees object from text
    const myobj = new Trees(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Trees object', () => {
    // 1. Create Trees object from text
    const myobj = new Trees(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   t r e e s . t e s t . t s                  end
// ======================================================================
