/* eslint-disable linebreak-style */
// ======================================================================
// Aunt Sue
//   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      m f c s a m . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc16 = require('./aoc_16');
const mfcsam = require('./mfcsam');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EX0 = 'children: 3';
const EX1 = 'cats: 7';
const EX2 = 'samoyeds: 2';
const EX3 = 'pomeranians: 3';
const EX4 = 'akitas: 0';
const EX5 = 'vizslas: 0';
const EX6 = 'goldfish: 5';
const EX7 = 'trees: 3';
const EX8 = 'cars: 2';
const EX9 = 'perfumes: 1';
const EXAMPLE_TEXT = `\n${EX0}\n${EX1}\n${EX2}\n${EX3}\n${EX4}\n${EX5}\n${EX6}\n${EX7}\n${EX8}\n${EX9}\n`;

// ======================================================================
//                                                             TestMfcsam
// ======================================================================

describe('Mfcsam', () => {
  test('Test the default Mfcsam creation', () => {
    // 1. Create default Mfcsam object
    const myobj = new mfcsam.Mfcsam({});
    // 2. Make sure it has the default values
    expect(myobj.text).toBe(null);
    expect(myobj.compounds).toStrictEqual({});
  });

  test('Test the Mfcsam object creation from text', () => {
    // 1. Create Mfcsam object from text
    const myobj = new mfcsam.Mfcsam({ text: aoc16.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.text).toHaveLength(10);
    expect(Object.keys(myobj.compounds)).toHaveLength(10);
    expect(myobj.compounds.children).toBe(3);
    expect(myobj.compounds.cats).toBe(7);
    expect(myobj.compounds.samoyeds).toBe(2);
    expect(myobj.compounds.pomeranians).toBe(3);
    expect(myobj.compounds.akitas).toBe(0);
    expect(myobj.compounds.vizslas).toBe(0);
    expect(myobj.compounds.goldfish).toBe(5);
    expect(myobj.compounds.trees).toBe(3);
    expect(myobj.compounds.cars).toBe(2);
    expect(myobj.compounds.perfumes).toBe(1);
  });
});

// ======================================================================
// end                   m f c s a m . t e s t . j s                  end
// ======================================================================
