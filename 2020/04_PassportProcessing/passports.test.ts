// ======================================================================
// Passport Processing
//   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p a s s p o r t s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_04';
import { Passports } from './passports';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 2;
const PART_TWO_RESULT = 2;

// ======================================================================
//                                                          TestPassports
// ======================================================================

describe('Passports', () => {
  test('Test the default Passports creation', () => {
    // 1. Create default Passports object
    const myobj = new Passports([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.passports).toHaveLength(0);
  });

  test('Test the Passports object creation from text', () => {
    // 1. Create Passports object from text
    const myobj = new Passports(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(15);
    expect(myobj.passports).toHaveLength(4);
    // 3. Check methods
    expect(myobj.count_valid()).toBe(2);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Passports object
      const myobj = new Passports(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Passports object using the key as text
      const myobj = new Passports(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Passports object', () => {
    // 1. Create Passports object from text
    const myobj = new Passports(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Passports object', () => {
    // 1. Create Passports object from text
    const myobj = new Passports(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                p a s s p o r t s . t e s t . t s               end
// ======================================================================
