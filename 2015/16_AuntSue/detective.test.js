/* eslint-disable linebreak-style */
// ======================================================================
// Aunt Sue
//   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                       d e t e c t i v e . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc16 = require('./aoc_16');
const detective = require('./detective');
const sue = require('./sue');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const sue1 = 'Sue 1: children: 1, cars: 8, vizslas: 7';
const sue2 = 'Sue 2: akitas: 10, perfumes: 10, children: 5';
const sue3 = 'Sue 3: cars: 5, pomeranians: 4, vizslas: 1';
const sue4 = 'Sue 4: goldfish: 5, children: 3, perfumes: 1';
const sue5 = 'Sue 5: vizslas: 2, akitas: 7, perfumes: 6';
const sue6 = 'Sue 6: vizslas: 0, akitas: 1, perfumes: 2';
const sue7 = 'Sue 7: perfumes: 8, cars: 4, goldfish: 10';
const sue8 = 'Sue 8: perfumes: 7, children: 2, cats: 1';
const sue9 = 'Sue 9: pomeranians: 3, goldfish: 10, trees: 10';
const EXAMPLE_TEXT = `\n${sue1}\n${sue2}\n${sue3}\n${sue4}\n${sue5}\n${sue6}\n${sue7}\n${sue8}\n${sue9}`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 4;
const PART_TWO_RESULT = null;

// ======================================================================
//                                                          TestDetective
// ======================================================================

describe('Detective', () => {
  test('Test the default Dective creation', () => {
    // 1. Create default Mfcsam object
    const myobj = new detective.Detective({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.aunts).toHaveLength(0);
    expect(myobj.number).toBe(0);
    expect(Object.keys(myobj.CSI.compounds)).toHaveLength(10);
    expect(myobj.CSI.compounds.children).toBe(3);
    expect(myobj.CSI.compounds.cats).toBe(7);
    expect(myobj.CSI.compounds.samoyeds).toBe(2);
    expect(myobj.CSI.compounds.pomeranians).toBe(3);
    expect(myobj.CSI.compounds.akitas).toBe(0);
    expect(myobj.CSI.compounds.vizslas).toBe(0);
    expect(myobj.CSI.compounds.goldfish).toBe(5);
    expect(myobj.CSI.compounds.trees).toBe(3);
    expect(myobj.CSI.compounds.cars).toBe(2);
    expect(myobj.CSI.compounds.perfumes).toBe(1);
  });

  test('Test the Detective object creation from text', () => {
    // 1. Create Mfcsam object from text
    const myobj = new detective.Detective({ text: aoc16.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(9);
    expect(Object.keys(myobj.CSI.compounds)).toHaveLength(10);
    expect(myobj.CSI.compounds.children).toBe(3);
    expect(myobj.CSI.compounds.cats).toBe(7);
    expect(myobj.CSI.compounds.samoyeds).toBe(2);
    expect(myobj.CSI.compounds.pomeranians).toBe(3);
    expect(myobj.CSI.compounds.akitas).toBe(0);
    expect(myobj.CSI.compounds.vizslas).toBe(0);
    expect(myobj.CSI.compounds.goldfish).toBe(5);
    expect(myobj.CSI.compounds.trees).toBe(3);
    expect(myobj.CSI.compounds.cars).toBe(2);
    expect(myobj.CSI.compounds.perfumes).toBe(1);
    // 3. Check each of the aunts
    expect(myobj.checkAunt(new sue.Sue({ text: sue1 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue2 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue3 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue4 }))).toBe(true);
    expect(myobj.checkAunt(new sue.Sue({ text: sue5 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue6 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue7 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue8 }))).toBe(false);
    expect(myobj.checkAunt(new sue.Sue({ text: sue9 }))).toBe(false);
  });


  test('Test part one example of Detective object', () => {
    // 1. Create Mfcsam object from text
    const myobj = new detective.Detective({ text: aoc16.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Detective object', () => {
    // 1. Create Mfcsam object from text
    const myobj = new detective.Detective({ part2: true, text: aoc16.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                d e t e c t i v e . t e s t . j s               end
// ======================================================================
