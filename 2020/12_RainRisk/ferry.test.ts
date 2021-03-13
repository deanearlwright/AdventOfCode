// ======================================================================
// Rain Risk
//   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      f e r r y . t e s t . t s
//
// Test Ferry for Advent of Code 2020 day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Ferry } from './ferry';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                              TestFerry
// ======================================================================

describe('Ferry', () => {
  test('Test the default Ferry creation', () => {
    // 1. Create default Ferry object
    const myobj = new Ferry();
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.start).toStrictEqual([0, 0]);
    expect(myobj.loc).toStrictEqual([0, 0]);
    expect(myobj.facing).toBe(1);
    // 3. Test methods
    expect(myobj.manhattanDistance()).toBe(0);
    myobj.execute('F10');
    expect(myobj.loc).toStrictEqual([10, 0]);
    expect(myobj.facing).toBe(1);
    myobj.execute('N3');
    expect(myobj.loc).toStrictEqual([10, -3]);
    expect(myobj.facing).toBe(1);
    myobj.execute('F7');
    expect(myobj.loc).toStrictEqual([17, -3]);
    expect(myobj.facing).toBe(1);
    myobj.execute('R90');
    expect(myobj.loc).toStrictEqual([17, -3]);
    expect(myobj.facing).toBe(2);
    myobj.execute('F11');
    expect(myobj.loc).toStrictEqual([17, 8]);
    expect(myobj.facing).toBe(2);
    expect(myobj.manhattanDistance()).toBe(25);
  });

  test('Test the default Ferry creation - part 2', () => {
    // 1. Create default Ferry object
    const myobj = new Ferry(true);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(true);
    expect(myobj.start).toStrictEqual([0, 0]);
    expect(myobj.loc).toStrictEqual([0, 0]);
    expect(myobj.facing).toBe(1);
    expect(myobj.waypoint).toStrictEqual([10, -1]);
    // 3. Test methods
    expect(myobj.manhattanDistance()).toBe(0);
    myobj.execute('F10');
    expect(myobj.loc).toStrictEqual([100, -10]);
    expect(myobj.facing).toBe(1);
    expect(myobj.waypoint).toStrictEqual([10, -1]);
    myobj.execute('N3');
    expect(myobj.loc).toStrictEqual([100, -10]);
    expect(myobj.facing).toBe(1);
    expect(myobj.waypoint).toStrictEqual([10, -4]);
    myobj.execute('F7');
    expect(myobj.loc).toStrictEqual([170, -38]);
    expect(myobj.facing).toBe(1);
    expect(myobj.waypoint).toStrictEqual([10, -4]);
    myobj.execute('R90');
    expect(myobj.loc).toStrictEqual([170, -38]);
    expect(myobj.facing).toBe(1);
    expect(myobj.waypoint).toStrictEqual([4, 10]);
    myobj.execute('F11');
    expect(myobj.loc).toStrictEqual([214, 72]);
    expect(myobj.facing).toBe(1);
    expect(myobj.waypoint).toStrictEqual([4, 10]);
    expect(myobj.manhattanDistance()).toBe(286);
  });
});

// ======================================================================
// end                    f e r r y . t e s t . t s                   end
// ======================================================================
