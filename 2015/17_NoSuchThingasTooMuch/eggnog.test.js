/* eslint-disable linebreak-style */
// ======================================================================
// No Such Thing as Too Much
//   Advent of Code 2015 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      e g g n o g . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 17 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc17 = require('./aoc_17');
const eggnog = require('./eggnog');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\n20\n15\n10\n5\n5';
const EXAMPLE_LITERS = 25;

const EXAMPLES_PART_ONE = {
  '15\n10': true,
  '20\n5': true,
  '15\n5\n5': true,
  '': false,
  '15\n': false,
  // eslint-disable-next-line quote-props
  '25\n': true,
  '5\n5\n5\n5': false,
  '5\n5\n5\n5\n5': true,
  '5\n5\n5\n5\n5\n5': false,
};
const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 4;
const PART_TWO_RESULT = 3;

// ======================================================================
//                                                             TestEggnog
// ======================================================================

describe('Eggnog', () => {
  test('Test the default Eggnog creation', () => {
    // 1. Create default Eggnog object
    const myobj = new eggnog.Eggnog({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.liters).toBe(150);
    expect(myobj.containers).toStrictEqual([]);
  });

  test('Test the Eggnog object creation from text', () => {
    // 1. Create Eggnog object from text
    const myobj = new eggnog.Eggnog({
      liters: EXAMPLE_LITERS,
      text: aoc17.fromText(EXAMPLE_TEXT),
    });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(5);
    expect(myobj.liters).toBe(25);
    expect(myobj.containers).toHaveLength(5);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Eggnog object using the key as text
      const myobj = new eggnog.Eggnog({
        liters: EXAMPLE_LITERS,
        text: aoc17.fromText(key),
      });
      expect(myobj.part2).toBe(false);
      // 3. Make sure it has the expected value
      expect(myobj.sumToLiters(myobj.containers)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Eggnog object using the key as text
      const myobj = new eggnog.Eggnog({ part2: true, text: aoc17.fromText(key) });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.eggnog(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Eggnog object', () => {
    // 1. Create Eggnog object from text
    const myobj = new eggnog.Eggnog({
      liters: EXAMPLE_LITERS,
      text: aoc17.fromText(PART_ONE_TEXT),
    });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Eggnog object', () => {
    // 1. Create Eggnog object from text
    const myobj = new eggnog.Eggnog({
      part2: true,
      liters: EXAMPLE_LITERS,
      text: aoc17.fromText(PART_TWO_TEXT),
    });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   e g g n o g . t e s t . j s                  end
// ======================================================================
