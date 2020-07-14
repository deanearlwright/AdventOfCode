// ======================================================================
// Like a Rogue
//   Advent of Code 2016 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t i l e s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_18';
import { Tiles } from './tiles';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
.^^.^.^^^^
`;

interface ExampleTests {
  text: string;
  result: number;
}

interface NextRowTests {
  text: string;
  result: string;
}

const NEXT_ROW_PART_ONE: NextRowTests[] = [
  { text: '..^^.', result: '.^^^^' },
  { text: '.^^^^', result: '^^..^' },
];

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_ROWS = 10;
const PART_ONE_RESULT = 38;
const PART_TWO_RESULT = 38;

// ======================================================================
//                                                              TestTiles
// ======================================================================

describe('Tiles', () => {
  test('Test the default Tiles creation', () => {
    // 1. Create default Tiles object
    const myobj = new Tiles([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });

  test('Test the Tiles object creation from text', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Tiles object
      const myobj = new Tiles(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test next rows from part one examples', () => {
    // 1. Loop for all of the examples
    NEXT_ROW_PART_ONE.forEach((test) => {
      // 2. Make sure it has the expected value
      expect(Tiles.nextRow(test.text)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Tiles object using the key as text
      const myobj = new Tiles(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Tiles object', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(PART_ONE_TEXT));
    myobj.numRows = PART_ONE_ROWS;
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Tiles object', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(PART_TWO_TEXT), true);
    myobj.numRows = PART_ONE_ROWS;
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    t i l e s . t e s t . t s                   end
// ======================================================================
