// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t i c k e t s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_16';
import { Tickets } from './tickets';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
`;

const EXAMPLE_TWO = `
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TWO;

const PART_ONE_RESULT = 71;
const PART_TWO_RESULT = 1;

// ======================================================================
//                                                            TestTickets
// ======================================================================

describe('Tickets', () => {
  test('Test the default Tickets creation', () => {
    // 1. Create default Tickets object
    const myobj = new Tickets([]);

    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.rules.rules).toHaveLength(0);
    expect(myobj.mine.numbers).toHaveLength(0);
    expect(myobj.nearby).toHaveLength(0);
  });

  test('Test the Tickets object creation from text', () => {
    // 1. Create Tickets object from text
    const myobj = new Tickets(fromText(EXAMPLE_TEXT));

    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(10);
    expect(myobj.rules.rules).toHaveLength(3);
    expect(myobj.rules.rules[0].name).toBe('class');
    expect(myobj.rules.rules[1].name).toBe('row');
    expect(myobj.rules.rules[2].name).toBe('seat');
    expect(myobj.rules.rules[0].numbers[0]).toBe(1);
    expect(myobj.rules.rules[1].numbers[0]).toBe(6);
    expect(myobj.rules.rules[2].numbers[0]).toBe(13);
    expect(myobj.mine.numbers).toHaveLength(3);
    expect(myobj.mine.numbers[0]).toBe(7);
    expect(myobj.mine.numbers[1]).toBe(1);
    expect(myobj.mine.numbers[2]).toBe(14);
    expect(myobj.nearby).toHaveLength(4);
    expect(myobj.nearby[0].numbers[0]).toBe(7);
    expect(myobj.nearby[1].numbers[0]).toBe(40);
    expect(myobj.nearby[2].numbers[0]).toBe(55);
    expect(myobj.nearby[3].numbers[0]).toBe(38);

    // 3. Check methods
    expect(myobj.scanningErrorRate()).toBe(71);
  });

  test('Test the Tickets object creation from text part two', () => {
    // 1. Create Tickets object from text
    const myobj = new Tickets(fromText(EXAMPLE_TWO));

    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(9);
    expect(myobj.rules.rules).toHaveLength(3);
    expect(myobj.rules.rules[0].name).toBe('class');
    expect(myobj.rules.rules[1].name).toBe('row');
    expect(myobj.rules.rules[2].name).toBe('seat');
    expect(myobj.rules.rules[0].numbers[0]).toBe(0);
    expect(myobj.rules.rules[1].numbers[0]).toBe(0);
    expect(myobj.rules.rules[2].numbers[0]).toBe(0);
    expect(myobj.rules.rules[0].numbers[1]).toBe(1);
    expect(myobj.rules.rules[1].numbers[1]).toBe(5);
    expect(myobj.rules.rules[2].numbers[1]).toBe(13);
    expect(myobj.mine.numbers).toHaveLength(3);
    expect(myobj.mine.numbers[0]).toBe(11);
    expect(myobj.mine.numbers[1]).toBe(12);
    expect(myobj.mine.numbers[2]).toBe(13);
    expect(myobj.nearby).toHaveLength(3);
    expect(myobj.nearby[0].numbers[0]).toBe(3);
    expect(myobj.nearby[1].numbers[0]).toBe(15);
    expect(myobj.nearby[2].numbers[0]).toBe(5);

    // 3. Check methods
    expect(myobj.scanningErrorRate()).toBe(0);
    myobj.findFieldPositions();
    // console.log(`${myobj.rules.rules[0].name} = ${myobj.rules.rules[0].positions}`);
    // console.log(`${myobj.rules.rules[1].name} = ${myobj.rules.rules[1].positions}`);
    // console.log(`${myobj.rules.rules[2].name} = ${myobj.rules.rules[2].positions}`);
    expect(myobj.rules.rules[0].ticketIndex()).toBe(1); // class
    expect(myobj.rules.rules[1].ticketIndex()).toBe(0); // row
    expect(myobj.rules.rules[2].ticketIndex()).toBe(2); // seat
  });

  test('Test part one example of Tickets object', () => {
    // 1. Create Tickets object from text
    const myobj = new Tickets(fromText(PART_ONE_TEXT));

    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Tickets object', () => {
    // 1. Create Tickets object from text
    const myobj = new Tickets(fromText(PART_TWO_TEXT), true);

    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                  t i c k e t s . t e s t . t s                 end
// ======================================================================
