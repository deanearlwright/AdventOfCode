// ======================================================================
// Radioisotope Thermoelectric Generators
//   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      e l e v a t o r . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_11';
import { Elevator } from './elevator';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
interface ExampleTests {
  text: string;
  result: Number;
}

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
The elevator is on the first floor.
`;

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 11;
const PART_TWO_RESULT = NaN;

// ======================================================================
//                                                           TestElevator
// ======================================================================

describe('Elevator', () => {
  test('Test the default Elevator creation', () => {
    // 1. Create default Elevator object
    const myobj = new Elevator([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.state.elevator).toBe(0);
  });

  test('Test the Elevator object creation from text', () => {
    // 1. Create Elevator object from text
    const myobj = new Elevator(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(5);
    expect(myobj.state.elevator).toBe(0);
    expect(myobj.state.floors).toHaveLength(4);
    expect(myobj.state.floors[0]).toHaveLength(2);
    expect(myobj.state.floors[1]).toHaveLength(1);
    expect(myobj.state.floors[2]).toHaveLength(1);
    expect(myobj.state.floors[3]).toHaveLength(0);
    expect(myobj.state.floors[0][0]).toStrictEqual({ element: 'hydrogen', itype: 'microchip' });
    expect(myobj.state.floors[0][1]).toStrictEqual({ element: 'lithium', itype: 'microchip' });
    expect(myobj.state.floors[1][0]).toStrictEqual({ element: 'hydrogen', itype: 'generator' });
    expect(myobj.state.floors[2][0]).toStrictEqual({ element: 'lithium', itype: 'generator' });
    // 3. Let's try a move
    myobj.outputState();
    expect(myobj.validateElevator({ elevator: 'up', items: [{ element: 'hydrogen', itype: 'microchip' }] })).toBe(true);
    expect(myobj.executeMove({ elevator: 'up', items: [{ element: 'hydrogen', itype: 'microchip' }] })).toBe(true);
    myobj.outputState();
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Elevator object
      const myobj = new Elevator(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Elevator object using the key as text
      const myobj = new Elevator(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Elevator object', () => {
    // 1. Create Elevator object from text
    const myobj = new Elevator(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Elevator object', () => {
    // 1. Create Elevator object from text
    const myobj = new Elevator(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 e l e v a t o r . t e s t . t s                end
// ======================================================================
