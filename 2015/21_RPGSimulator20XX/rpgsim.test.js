/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r p g s i m . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc21 = require('./aoc_21');
const rpgsim = require('./rpgsim');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Hit Points: 100
Damage: 8
Armor: 2
`;

const EXAMPLES_PART_ONE = {};
const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 91;
const PART_TWO_RESULT = null;

// ======================================================================
//                                                             TestRPGSim
// ======================================================================

describe('RPGSim', () => {
  test('Test the default RPGSim creation', () => {
    // 1. Create default RPGSim object
    const myobj = new rpgsim.RPGSim({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the RPGSim object creation from text', () => {
    // 1. Create RPGSim object from text
    const myobj = new rpgsim.RPGSim({ text: aoc21.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.player.name).toBe('player');
    expect(myobj.player.initialHitPoints).toBe(100);
    expect(myobj.player.hitPoints).toBe(100);
    expect(myobj.player.damage).toBe(0);
    expect(myobj.player.armor).toBe(0);
    expect(myobj.boss.part2).toBe(false);
    expect(myobj.boss.text).toHaveLength(3);
    expect(myobj.boss.name).toBe('boss');
    expect(myobj.boss.initialHitPoints).toBe(100);
    expect(myobj.boss.hitPoints).toBe(100);
    expect(myobj.boss.damage).toBe(8);
    expect(myobj.boss.armor).toBe(2);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create RPGSim object using the key as text
      const myobj = new rpgsim.RPGSim({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.rpgsim(key)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create RPGSim object using the key as text
      const myobj = new rpgsim.RPGSim({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.rpgsim(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of RPGSim object', () => {
    // 1. Create RPGSim object from text
    const myobj = new rpgsim.RPGSim({ text: aoc21.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of RPGSim object', () => {
    // 1. Create RPGSim object from text
    const myobj = new rpgsim.RPGSim({ part2: true, text: aoc21.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   r p g s i m . t e s t . j s                  end
// ======================================================================
