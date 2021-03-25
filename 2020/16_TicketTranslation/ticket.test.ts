// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t i c k e t . t e s t . t s
//
// Test Ticket for Advent of Code 2020 day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Ticket } from './ticket';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '7,1,14';

// ======================================================================
//                                                             TestTicket
// ======================================================================

describe('Ticket', () => {
  test('Test the default Ticket creation', () => {
    // 1. Create default Ticket object
    const myobj = new Ticket('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.numbers).toHaveLength(0);
    expect(myobj.valid).toBe(true);
  });

  test('Test the Ticket object creation from text', () => {
    // 1. Create Ticket object from text
    const myobj = new Ticket(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.numbers).toHaveLength(3);
    expect(myobj.numbers[0]).toBe(7);
    expect(myobj.numbers[1]).toBe(1);
    expect(myobj.numbers[2]).toBe(14);
    expect(myobj.valid).toBe(true);

    // 3. Check methods
    expect(myobj.length()).toBe(3);
  });
});

// ======================================================================
// end                   t i c k e t . t e s t . t s                  end
// ======================================================================
