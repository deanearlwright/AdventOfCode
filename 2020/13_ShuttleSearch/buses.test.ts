// ======================================================================
// Shuttle Search
//   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b u s e s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 13 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_13';
import { Buses } from './buses';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
939
7,13,x,x,59,x,31,19
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: '17,x,13,19', result: 3417 },
  { text: '67,7,59,61', result: 754018 },
  { text: '67,x,7,59,61', result: 779210 },
  { text: '67,7,x,59,61', result: 1261476 },
  { text: '1789,37,47,1889', result: 1202161486 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 295;
const PART_TWO_RESULT = 1068781;

// ======================================================================
//                                                              TestBuses
// ======================================================================

describe('Buses', () => {
  test('Test the default Buses creation', () => {
    // 1. Create default Buses object
    const myobj = new Buses([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.earliest).toBe(0);
    expect(myobj.buses).toHaveLength(0);
  });

  test('Test the Buses object creation from text', () => {
    // 1. Create Buses object from text
    const myobj = new Buses(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.earliest).toBe(939);
    expect(myobj.buses).toHaveLength(5);
    // 3. Test methods
    expect(myobj.waiting()).toBe(295);
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Bitmask object using the key as text
      const theText: string[] = ['123', test.text];
      const myobj = new Buses(theText, true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(2);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Buses object', () => {
    // 1. Create Buses object from text
    const myobj = new Buses(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Buses object', () => {
    // 1. Create Buses object from text
    const myobj = new Buses(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   b u s e s . t e s t . t s                  end
// ======================================================================
