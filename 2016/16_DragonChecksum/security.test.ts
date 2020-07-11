// ======================================================================
// Dragon Checksum
//   Advent of Code 2016 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      s e c u r i t y . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_16';
import { Security } from './security';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
10000
`;
const EXAMPLE_LENGTH = 20;

interface StringStringTests {
  text: string;
  result: string;
}

interface ExampleTests {
  text: string;
  result: number;
}

const REVERSE_EXAMPLES: StringStringTests[] = [
  { text: '1', result: '1' },
  { text: '0', result: '0' },
  { text: '11111', result: '11111' },
  { text: '111100001010', result: '010100001111' },
];

const FLIP_EXAMPLES: StringStringTests[] = [
  { text: '0', result: '1' },
  { text: '1', result: '0' },
  { text: '11111', result: '00000' },
  { text: '111100001010', result: '000011110101' },
];

const ONE_DRAGON_EXAMPLES: StringStringTests[] = [
  { text: '1', result: '100' },
  { text: '0', result: '001' },
  { text: '11111', result: '11111000000' },
  { text: '111100001010', result: '1111000010100101011110000' },
];

const PAIRS_EXAMPLES: StringStringTests[] = [
  { text: '110010110100', result: '110101' },
  { text: '110101', result: '100' },
  { text: '10000011110010000111', result: '0111110101' },
  { text: '0111110101', result: '01100' },
];

const CHECKSUM_EXAMPLES: StringStringTests[] = [
  { text: '110010110100', result: '100' },
  { text: '10000011110010000111', result: '01100' },
];

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = '01100';
const PART_TWO_RESULT = '';

// ======================================================================
//                                                           TestSecurity
// ======================================================================

describe('Security', () => {
  test('Test the default Security creation', () => {
    // 1. Create default Security object
    const myobj = new Security([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.initial).toHaveLength(0);
    expect(myobj.diskSize).toBe(272);
  });

  test('Test the Security object creation from text', () => {
    // 1. Create Security object from text
    const myobj = new Security(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.initial).toHaveLength(5);
    expect(myobj.initial).toBe('10000');
    expect(myobj.diskSize).toBe(272);
    // 3. Check long dragon
    myobj.diskSize = EXAMPLE_LENGTH;
    const fullDisk = myobj.longDragon();
    expect(fullDisk).toBe('10000011110010000111');
  });

  test('Test stringFlip()', () => {
    // 1. Loop for all of the examples
    FLIP_EXAMPLES.forEach((test) => {
      // 2. Make sure it has the expected value
      expect(Security.stringFlip(test.text)).toBe(test.result);
    });
  });

  test('Test stringReverse()', () => {
    // 1. Loop for all of the examples
    REVERSE_EXAMPLES.forEach((test) => {
      // 2. Make sure it has the expected value
      expect(Security.stringReverse(test.text)).toBe(test.result);
    });
  });

  test('Test oneDragon()', () => {
    // 1. Loop for all of the examples
    ONE_DRAGON_EXAMPLES.forEach((test) => {
      // 2. Make sure it has the expected value
      expect(Security.oneDragon(test.text)).toBe(test.result);
    });
  });

  test('Test pairs()', () => {
    // 1. Loop for all of the examples
    PAIRS_EXAMPLES.forEach((test) => {
      // 2. Make sure it has the expected value
      expect(Security.pairs(test.text)).toBe(test.result);
    });
  });

  test('Test checksum()', () => {
    // 1. Loop for all of the examples
    CHECKSUM_EXAMPLES.forEach((test) => {
      // 2. Make sure it has the expected value
      expect(Security.checksum(test.text)).toBe(test.result);
    });
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Security object
      const myobj = new Security(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Security object using the key as text
      const myobj = new Security(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Security object', () => {
    // 1. Create Security object from text
    const myobj = new Security(fromText(PART_ONE_TEXT));
    myobj.diskSize = 20;
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Security object', () => {
    // 1. Create Security object from text
    const myobj = new Security(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 s e c u r i t y . t e s t . t s                end
// ======================================================================
