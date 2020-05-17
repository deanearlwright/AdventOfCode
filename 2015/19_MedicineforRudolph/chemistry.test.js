/* eslint-disable linebreak-style */
// ======================================================================
// Medicine for Rudolph
//   Advent of Code 2015 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      c h e m i s t r y . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc19 = require('./aoc_19');
const chemistry = require('./chemistry');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'H => HO\nH => OH\nO => HH\n\nHOH\n';

const EXAMPLES_PART_ONE = {
  H: 2,
  O: 1,
  X: 0,
};
const EXAMPLES_PART_TWO = {
  H: 1,
  O: 1,
  HO: 2,
  OH: 2,
  HH: 2,
  HOH: 3,
  HHH: 3,
  HHHH: 4,
  HOHO: 4,
  HOHH: 4,
  HOHOH: 5,
  HOHOHO: 6,
};

const PART_ONE_TEXT = 'H => HO\nH => OH\nO => HH\n\nHOHOHO\n';
const PART_TWO_TEXT = 'e => H\ne => O\nH => HO\nH => OH\nO => HH\n\nHOHOHO\n';

const PART_ONE_RESULT = 7;
const PART_TWO_RESULT = 6;

// ======================================================================
//                                                          TestChemistry
// ======================================================================

describe('Chemistry', () => {
  test('Test the default Chemistry creation', () => {
    // 1. Create default Chemistry object
    const myobj = new chemistry.Chemistry({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.replacements).toStrictEqual({});
    expect(myobj.molecule).toBe('');
    expect(myobj.kntRep).toBe(0);
  });

  test('Test the Chemistry object creation from text', () => {
    // 1. Create Chemistry object from text
    const myobj = new chemistry.Chemistry({ text: aoc19.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.replacements).toStrictEqual({
      H: ['HO', 'OH'],
      O: ['HH'],
    });
    expect(myobj.molecule).toBe('HOH');
    expect(myobj.kntRep).toBe(2);
    // 3. Try out the calibration function
    expect(myobj.oneOff('HOH')).toStrictEqual({
      HOOH: true,
      HOHO: true,
      OHOH: true,
      HHHH: true,
    });
    expect(myobj.calibrate()).toBe(4);
  });

  test('Test all of the part one examples', () => {
    // 1. Create Chemistry object from text
    const myobj = new chemistry.Chemistry({ text: aoc19.fromText(PART_ONE_TEXT) });
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.replacements).toStrictEqual({
      H: ['HO', 'OH'],
      O: ['HH'],
    });
    expect(myobj.molecule).toBe('HOHOHO');
    expect(myobj.kntRep).toBe(2);
    // 2. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 3. Set  Chemistry object molecule to the text
      myobj.molecule = key;
      // 3. Make sure it has the expected value
      expect(myobj.calibrate()).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Create Chemistry object from text
    const myobj = new chemistry.Chemistry({ part2: true, text: aoc19.fromText(PART_TWO_TEXT) });
    expect(myobj.part2).toBe(true);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.replacements).toStrictEqual({
      e: ['H', 'O'],
      H: ['HO', 'OH'],
      O: ['HH'],
    });
    expect(myobj.molecule).toBe('HOHOHO');
    expect(myobj.kntRep).toBe(3);
    // 2. Loop for all of the examples
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 3. Set  Chemistry object molecule to the text
      myobj.molecule = key;
      // 3. Make sure it has the expected value
      expect(myobj.medicine()).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Chemistry object', () => {
    // 1. Create Chemistry object from text
    const myobj = new chemistry.Chemistry({ text: aoc19.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Chemistry object', () => {
    // 1. Create Chemistry object from text
    const myobj = new chemistry.Chemistry({ part2: true, text: aoc19.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.medicine({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                c h e m i s t r y . t e s t . j s               end
// ======================================================================
