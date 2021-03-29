// ======================================================================
// Conway Cubes
//   Advent of Code 2020 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p o c k e t . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 17 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_17';
import { Pocket } from './pocket';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
.#.
..#
###
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 112;
const PART_TWO_RESULT = 848;

// ======================================================================
//                                                             TestPocket
// ======================================================================

describe('Pocket', () => {
  test('Test the default Pocket creation', () => {
    // 1. Create default Pocket object
    const myobj = new Pocket([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.cycle).toBe(0);

    // 3. Check methods
    expect(myobj.active()).toBe(0);
    expect(myobj.isActive('0,0,0')).toBe(false);
  });

  test('Test the Pocket object creation from text', () => {
    // 1. Create Pocket object from text
    const myobj = new Pocket(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.cycle).toBe(0);

    // 3. Check methods
    expect(myobj.active()).toBe(5);
    expect(myobj.isActive('0,0,0')).toBe(false);
    expect(myobj.isActive('0,1,0')).toBe(true);
    expect(myobj.isActive('0,2,0')).toBe(false);
    expect(myobj.isActive('1,0,0')).toBe(false);
    expect(myobj.isActive('1,1,0')).toBe(false);
    expect(myobj.isActive('1,2,0')).toBe(true);
    expect(myobj.isActive('2,0,0')).toBe(true);
    expect(myobj.isActive('2,1,0')).toBe(true);
    expect(myobj.isActive('2,2,0')).toBe(true);

    expect(myobj.neighbors('0,0,0')).toHaveLength(26);
    expect(myobj.countNearby('0,0,0')).toBe(1);
    expect(myobj.countNearby('0,1,0')).toBe(1);
    expect(myobj.countNearby('0,2,0')).toBe(2);
    expect(myobj.countNearby('1,0,0')).toBe(3);
    expect(myobj.countNearby('1,1,0')).toBe(5);
    expect(myobj.countNearby('1,2,0')).toBe(3);
    expect(myobj.countNearby('2,0,0')).toBe(1);
    expect(myobj.countNearby('2,1,0')).toBe(3);
    expect(myobj.countNearby('2,2,0')).toBe(2);
    expect(myobj.countNearby('-1,0,0')).toBe(1);

    myobj.oneCycle();
    expect(myobj.cycle).toBe(1);
    expect(myobj.active()).toBe(11);
    myobj.oneCycle();
    expect(myobj.cycle).toBe(2);
    expect(myobj.active()).toBe(21);
    myobj.oneCycle();
    expect(myobj.cycle).toBe(3);
    expect(myobj.active()).toBe(38);
    myobj.runUntil(6);
    expect(myobj.cycle).toBe(6);
    expect(myobj.active()).toBe(112);
  });

  test('Test the Pocket object creation from text part2', () => {
    // 1. Create Pocket object from text
    const myobj = new Pocket(fromText(EXAMPLE_TEXT), true);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.cycle).toBe(0);

    // 3. Check methods
    expect(myobj.active()).toBe(5);
    expect(myobj.isActive('0,0,0,0')).toBe(false);
    expect(myobj.isActive('0,1,0,0')).toBe(true);
    expect(myobj.isActive('0,2,0,0')).toBe(false);
    expect(myobj.isActive('1,0,0,0')).toBe(false);
    expect(myobj.isActive('1,1,0,0')).toBe(false);
    expect(myobj.isActive('1,2,0,0')).toBe(true);
    expect(myobj.isActive('2,0,0,0')).toBe(true);
    expect(myobj.isActive('2,1,0,0')).toBe(true);
    expect(myobj.isActive('2,2,0,0')).toBe(true);

    expect(myobj.neighbors('0,0,0,0')).toHaveLength(80);
    expect(myobj.countNearby('0,0,0,0')).toBe(1);
    expect(myobj.countNearby('0,1,0,0')).toBe(1);
    expect(myobj.countNearby('0,2,0,0')).toBe(2);
    expect(myobj.countNearby('1,0,0,0')).toBe(3);
    expect(myobj.countNearby('1,1,0,0')).toBe(5);
    expect(myobj.countNearby('1,2,0,0')).toBe(3);
    expect(myobj.countNearby('2,0,0,0')).toBe(1);
    expect(myobj.countNearby('2,1,0,0')).toBe(3);
    expect(myobj.countNearby('2,2,0,0')).toBe(2);
    expect(myobj.countNearby('-1,0,0,0')).toBe(1);

    myobj.oneCycle();
    expect(myobj.cycle).toBe(1);
    expect(myobj.active()).toBe(29);
    myobj.oneCycle();
    expect(myobj.cycle).toBe(2);
    expect(myobj.active()).toBe(60);
    myobj.runUntil(6);
    expect(myobj.cycle).toBe(6);
    expect(myobj.active()).toBe(848);
  });

  test('Test part one example of Pocket object', () => {
    // 1. Create Pocket object from text
    const myobj = new Pocket(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Pocket object', () => {
    // 1. Create Pocket object from text
    const myobj = new Pocket(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   p o c k e t . t e s t . t s                  end
// ======================================================================
