// ======================================================================
// Two Steps Forward
//   Advent of Code 2016 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      d o o r s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 17 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_17';
import { Doors } from './doors';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
ihgpwlah
`;

interface ExampleTests {
  text: string;
  result: String;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: 'hijkl', result: '' },
  { text: 'ihgpwlah', result: 'DDRRRD' },
  { text: 'kglvqrro', result: 'DDUDRLRRUDRD' },
  { text: 'ulqzkmiv', result: 'DRURDRUDDLLDLUURRDULRLDUUDDDRR' },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: 'ihgpwlah', result: '370' },
  { text: 'kglvqrro', result: '492' },
  { text: 'ulqzkmiv', result: '830' },

];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 'DDRRRD';
const PART_TWO_RESULT = '370';

// ======================================================================
//                                                              TestDoors
// ======================================================================

describe('Doors', () => {
  test('Test the default Doors creation', () => {
    // 1. Create default Doors object
    const myobj = new Doors([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.salt).toHaveLength(0);
    expect(myobj.start).toBe(11);
    expect(myobj.vault).toBe(44);
    expect(Object.keys(myobj.grid)).toHaveLength(1);
    expect(myobj.start in myobj.grid).toBe(true);
  });

  test('Test the Doors object creation from text', () => {
    // 1. Create Doors object from text
    const myobj = new Doors(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(1);
    expect(myobj.salt).toBe('ihgpwlah');
    expect(myobj.start).toBe(11);
    expect(myobj.vault).toBe(44);
    expect(Object.keys(myobj.grid)).toHaveLength(1);
    expect(myobj.start in myobj.grid).toBe(true);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Doors object
      const myobj = new Doors(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution(false)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Doors object using the key as text
      const myobj = new Doors(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution(false)).toBe(test.result);
    });
  });

  test('Test part one example of Doors object', () => {
    // 1. Create Doors object from text
    const myobj = new Doors(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Doors object', () => {
    // 1. Create Doors object from text
    const myobj = new Doors(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    d o o r s . t e s t . t s                   end
// ======================================================================
