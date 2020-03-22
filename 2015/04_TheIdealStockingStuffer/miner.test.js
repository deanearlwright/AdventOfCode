/* eslint-disable linebreak-style */
// ======================================================================
// The Ideal Stocking Stuffer
//   Advent of Code 2015 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      m i n e r . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc04 = require('./aoc_04');
const miner = require('./miner');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\nabcdef\n';

const EXAMPLES_PART_ONE = {
  abcdef: 609043,
  pqrstuv: 1048970,
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 609043;
const PART_TWO_RESULT = 6742839;

// ======================================================================
//                                                              TestMiner
// ======================================================================

describe('Miner', () => {
  test('Test the default Miner creation', () => {
    // 1. Create default Miner object
    const myobj = new miner.Miner({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.base).toBe('');
  });

  test('Test the Miner object creation from text', () => {
    // 1. Create Miner object from text
    const myobj = new miner.Miner({ text: aoc04.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.base).toBe('abcdef');
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Santa object using the key at text
      const myobj = new miner.Miner({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.base).toBe(key);
      // 3. Create an Advent Coin
      const coin = myobj.findAdventCoin();
      expect(coin).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test part one example of Miner object', () => {
    // 1. Create Miner object from text
    const myobj = new miner.Miner({ text: aoc04.fromText(PART_ONE_TEXT) });
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.base).toBe('abcdef');
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Miner object', () => {
    // 1. Create Miner object from text
    const myobj = new miner.Miner({ part2: true, text: aoc04.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                     t e s t _ m i n e r . j s                  end
// ======================================================================
