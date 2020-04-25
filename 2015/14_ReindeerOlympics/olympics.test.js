/* eslint-disable linebreak-style */
// ======================================================================
// Reindeer Olympics
//   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      o l y m p i c s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc14 = require('./aoc_14');
const olympics = require('./olympics');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const COMET = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.';
const DANCER = 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.';
const EXAMPLE_TEXT = `\n${COMET}\n${DANCER}\n`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;
const PART_ONE_RESULT = 2660;
const PART_TWO_RESULT = 1564;

// ======================================================================
//                                                           TestOlympics
// ======================================================================

describe('Olympics', () => {
  test('Test the default Olympics creation', () => {
    // 1. Create default Olympics object
    const myobj = new olympics.Olympics({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.reindeer).toHaveLength(0);
  });

  test('Test the Olympics object creation from text', () => {
    // 1. Create Olympics object from text
    const myobj = new olympics.Olympics({ text: aoc14.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.reindeer).toHaveLength(2);
    expect(myobj.reindeer[0].name).toBe('Comet');
    expect(myobj.reindeer[1].name).toBe('Dancer');
    expect(myobj.reindeer[0].atTick).toBe(0);
    expect(myobj.reindeer[1].atTick).toBe(0);
    expect(myobj.reindeer[0].distance).toBe(0);
    expect(myobj.reindeer[1].distance).toBe(0);
    // 3. Race for 1,000 seconds
    const winner = myobj.race(1000);
    expect(winner.name).toBe('Comet');
    expect(myobj.reindeer[0].atTick).toBe(1000);
    expect(myobj.reindeer[1].atTick).toBe(1000);
    expect(myobj.reindeer[0].distance).toBe(1120);
    expect(myobj.reindeer[1].distance).toBe(1056);
    // 4. Race for 1,000 seconds
    const winner2 = myobj.race2(1000);
    expect(myobj.reindeer[0].atTick).toBe(1000);
    expect(myobj.reindeer[1].atTick).toBe(1000);
    expect(myobj.reindeer[0].points).toBe(312);
    expect(myobj.reindeer[1].points).toBe(689);
    expect(winner2.name).toBe('Dancer');
  });

  test('Test part one example of Olympics object', () => {
    // 1. Create Olympics object from text
    const myobj = new olympics.Olympics({ text: aoc14.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Olympics object', () => {
    // 1. Create Olympics object from text
    const myobj = new olympics.Olympics({ part2: true, text: aoc14.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  t e s t _ o l y m p i c s . j s               end
// ======================================================================
