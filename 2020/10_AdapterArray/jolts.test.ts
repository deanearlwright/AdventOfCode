// ======================================================================
// Adapter Array
//   Advent of Code 2020 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      j o l t s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 10 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_10';
import { Jolts } from './jolts';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
16
10
15
5
1
11
7
19
6
12
4
`;

const EXAMPLE_TWO = `
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 35;
const PART_TWO_RESULT = 8;

// ======================================================================
//                                                              TestJolts
// ======================================================================

describe('Jolts', () => {
  test('Test the default Jolts creation', () => {
    // 1. Create default Jolts object
    const myobj = new Jolts([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.numbers).toHaveLength(0);
    expect(myobj.device).toBe(0);
  });

  test('Test the Jolts object creation from text', () => {
    // 1. Create Jolts object from text
    const myobj = new Jolts(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(11);
    expect(myobj.numbers).toHaveLength(11);
    expect(myobj.device).toBe(22);

    // 3. Check methods
    expect(myobj.count_diff()).toStrictEqual([7, 5]);
    expect(myobj.count_arrangements()).toBe(8);
  });

  test('Test the Jolts object creation from text using second example', () => {
    // 1. Create Jolts object from text
    const myobj = new Jolts(fromText(EXAMPLE_TWO));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(31);
    expect(myobj.numbers).toHaveLength(31);
    expect(myobj.device).toBe(52);

    // 3. Check methods
    expect(myobj.count_diff()).toStrictEqual([22, 10]);
    expect(myobj.count_arrangements()).toBe(19208);
  });

  test('Test part one example of Jolts object', () => {
    // 1. Create Jolts object from text
    const myobj = new Jolts(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Jolts object', () => {
    // 1. Create Jolts object from text
    const myobj = new Jolts(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   j o l t s . t e s t . t s                  end
// ======================================================================
