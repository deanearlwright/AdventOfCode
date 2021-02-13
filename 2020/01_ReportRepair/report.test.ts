// ======================================================================
// Report Repair
//   Advent of Code 2020 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r e p o r t . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 01 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_01';
import { Report } from './report';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
1721
979
366
299
675
1456
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 514579;
const PART_TWO_RESULT = 241861950;

// ======================================================================
//                                                             TestReport
// ======================================================================

describe('Report', () => {
  test('Test the default Report creation', () => {
    // 1. Create default Report object
    const myobj = new Report([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.numbers).toHaveLength(0);
  });

  test('Test the Report object creation from text', () => {
    // 1. Create Report object from text
    const myobj = new Report(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.numbers).toHaveLength(6);
    expect(myobj.numbers[0]).toBe(1721);
    expect(myobj.numbers[5]).toBe(1456);
    expect(myobj.two_entries(true)).toBe(514579);
    expect(myobj.three_entries(true)).toBe(241861950);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Report object
      const myobj = new Report(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Report object using the key as text
      const myobj = new Report(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Report object', () => {
    // 1. Create Report object from text
    const myobj = new Report(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Report object', () => {
    // 1. Create Report object from text
    const myobj = new Report(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   r e p o r t . t e s t . t s                  end
// ======================================================================
