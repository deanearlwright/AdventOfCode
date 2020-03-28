/* eslint-disable linebreak-style */
// ======================================================================
// Does not He Have Intern Elves For This
//   Advent of Code 2015 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      n a u g h t y . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 05 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc05 = require('./aoc_05');
const naughty = require('./naughty');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\nugknbfddgicrmopn\naaa\njchzalrnumimnmhp\n';

const EXAMPLES_PART_ONE = {
  ugknbfddgicrmopn: false,
  aaa: false,
  jchzalrnumimnmhp: true,
  haegwjzuvuyypxyu: true,
  dvszwmarrgswjxmb: true,
};

const EXAMPLES_PART_TWO = {
  qjhvhtzxzqqjkmpb: false,
  xxyxx: false,
  xxyyxx: true,
  uurcxstgmygtbstg: true,
  ieodomkazucvgmuy: true,
};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = '\nqjhvhtzxzqqjkmpb\nxxyxx\nuurcxstgmygtbstg\nieodomkazucvgmuy';

const PART_ONE_RESULT = 2;
const PART_TWO_RESULT = 2;

// ======================================================================
//                                                            TestNaughty
// ======================================================================

describe('Naughty', () => {
  test('Test the default Naughty creation', () => {
    // 1. Create default Naughty object
    const myobj = new naughty.Naughty({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
  });

  test('Test the Naughty object creation from text', () => {
    // 1. Create Naughty object from text
    const myobj = new naughty.Naughty({ text: aoc05.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
  });


  test('Test the Naughty word checks', () => {
    // 1. Check itHasThreeVowels
    expect(naughty.Naughty.itHasThreeVowels('aei')).toBe(true);
    expect(naughty.Naughty.itHasThreeVowels('xazegov')).toBe(true);
    expect(naughty.Naughty.itHasThreeVowels('aeiouaeiouaeiou')).toBe(true);
    expect(naughty.Naughty.itHasThreeVowels('dvszwmarrgswjxmb')).toBe(false);
    // 2. Check itHasDoubleLette
    expect(naughty.Naughty.itHasDoubleLetter('xx')).toBe(true);
    expect(naughty.Naughty.itHasDoubleLetter('abcdde')).toBe(true);
    expect(naughty.Naughty.itHasDoubleLetter('aabbccdd')).toBe(true);
    expect(naughty.Naughty.itHasDoubleLetter('jchzalrnumimnmhp')).toBe(false);
    // 3. Check itHasBadSequence
    expect(naughty.Naughty.itHasBadSequence('aaa')).toBe(false);
    expect(naughty.Naughty.itHasBadSequence('abdefghi')).toBe(true);
    expect(naughty.Naughty.itHasBadSequence('wxyz')).toBe(true);
    expect(naughty.Naughty.itHasBadSequence('haegwjzuvuyypxyu')).toBe(true);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Santa object using the key at text
      const myobj = new naughty.Naughty({ text: [key] });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Check out naughty or nice
      expect(myobj.isItNaughty(key)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Santa object using the key at text
      const myobj = new naughty.Naughty({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Check out naughty or nice
      expect(myobj.isItNaughty(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Naughty object', () => {
    // 1. Create Naughty object from text
    const myobj = new naughty.Naughty({ text: aoc05.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Naughty object', () => {
    // 1. Create Naughty object from text
    const myobj = new naughty.Naughty({ part2: true, text: aoc05.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   t e s t _ n a u g h t y . j s                end
// ======================================================================
