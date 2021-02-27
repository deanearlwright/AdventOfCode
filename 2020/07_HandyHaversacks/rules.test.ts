// ======================================================================
// Handy Haversacks
//   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r u l e s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_07';
import { Rules } from './rules';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
`;

const EXAMPLE_TWO = `
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 4;
const PART_TWO_RESULT = 32;

// ======================================================================
//                                                              TestRules
// ======================================================================

describe('Rules', () => {
  test('Test the default Rules creation', () => {
    // 1. Create default Rules object
    const myobj = new Rules([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(Object.keys(myobj.rules)).toHaveLength(0);
  });

  test('Test the Rules object creation from text', () => {
    // 1. Create Rules object from text
    const myobj = new Rules(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(9);
    expect(Object.keys(myobj.rules)).toHaveLength(9);

    // 3. Test methods
    expect(Object.keys(myobj.can_hold('shiny gold'))).toHaveLength(2);
    expect(Object.keys(myobj.can_hold('faded blue'))).toHaveLength(3);
    expect(Object.keys(myobj.can_hold('puke yellow'))).toHaveLength(0);

    expect(myobj.can_contain('shiny gold')).toBe(4);
    expect(myobj.can_contain('puke yellow')).toBe(0);

    expect(myobj.required_inside('shiny gold')).toBe(32);
  });

  test('Test the Rules example two', () => {
    // 1. Create Rules object from text
    const myobj = new Rules(fromText(EXAMPLE_TWO));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(7);
    expect(Object.keys(myobj.rules)).toHaveLength(7);

    // 3. Test methods
    expect(Object.keys(myobj.can_hold('shiny gold'))).toHaveLength(0);
    expect(Object.keys(myobj.can_hold('dark blue'))).toHaveLength(1);
    expect(Object.keys(myobj.can_hold('puke yellow'))).toHaveLength(0);

    expect(myobj.can_contain('shiny gold')).toBe(0);

    expect(myobj.required_inside('shiny gold')).toBe(126);
  });

  test('Test part one example of Rules object', () => {
    // 1. Create Rules object from text
    const myobj = new Rules(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Rules object', () => {
    // 1. Create Rules object from text
    const myobj = new Rules(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   r u l e s . t e s t . t s                  end
// ======================================================================
