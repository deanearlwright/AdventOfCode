/* eslint-disable linebreak-style */
// ======================================================================
// Knights of the Dinner Table
//   Advent of Code 2015 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      s e a t i n g . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc13 = require('./aoc_13');
const seating = require('./seating');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
`;

const EXAMPLES_PART_ONE = {
  'Alice,David': -2 + 46,
  'Bob,Alice': 83 + 54,
  'Carol,Bob': 60 - 7,
  'Carol,David': 55 + 41,
};
const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 330;
const PART_TWO_RESULT = 286;

// ======================================================================
//                                                            TestSeating
// ======================================================================

describe('Seating', () => {
  test('Test the default Seating creation', () => {
    // 1. Create default Seating object
    const myobj = new seating.Seating({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.number).toBe(0);
    expect(Object.keys(myobj.attendees)).toHaveLength(0);
  });

  test('Test the Seating object creation from text', () => {
    // 1. Create Seating object from text
    const myobj = new seating.Seating({ text: aoc13.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(12);
    expect(myobj.number).toBe(4);
    expect(Object.keys(myobj.attendees)).toHaveLength(4);
    expect(myobj.totalHappiness(['Alice', 'Bob', 'Carol', 'David'])).toBe(330);
    const maximum = myobj.maximizeHappiness();
    expect(maximum).toHaveLength(4);
    expect(myobj.totalHappiness(maximum)).toBe(330);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Seating object using the key as text
      const myobj = new seating.Seating({ text: aoc13.fromText(EXAMPLE_TEXT) });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(12);
      expect(Object.keys(myobj.attendees)).toHaveLength(4);
      // 3. Make sure it has the expected value
      const persons = key.split(',');
      expect(myobj.nextTo(persons[0], persons[1])).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test the part 2 Seating object creation from text', () => {
    // 1. Create Seating object from text
    const myobj = new seating.Seating({ part2: true, text: aoc13.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(12);
    expect(myobj.number).toBe(5);
    expect(Object.keys(myobj.attendees)).toHaveLength(4);
    expect(myobj.totalHappiness(['yourself', 'Alice', 'Bob', 'Carol', 'David'])).toBe(286);
    const maximum = myobj.maximizeHappiness();
    expect(maximum).toHaveLength(5);
    expect(myobj.totalHappiness(maximum)).toBe(286);
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Seating object using the key as text
      const myobj = new seating.Seating({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.seating(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Seating object', () => {
    // 1. Create Seating object from text
    const myobj = new seating.Seating({ text: aoc13.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Seating object', () => {
    // 1. Create Seating object from text
    const myobj = new seating.Seating({ part2: true, text: aoc13.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  t e s t _ s e a t i n g . j s                 end
// ======================================================================
