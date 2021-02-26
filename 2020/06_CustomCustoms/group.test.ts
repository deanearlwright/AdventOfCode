// ======================================================================
// Custom Customs
//   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      g r o u p . t e s t . t s
//
// Test Group for Advent of Code 2020 day 06 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { Group } from './group';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'abcx abcy abcz';

// ======================================================================
//                                                              TestGroup
// ======================================================================

describe('Group', () => {
  test('Test the default Group creation', () => {
    // 1. Create default Group object
    const myobj = new Group('');
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(Object.keys(myobj.answers)).toHaveLength(0);
  });

  test('Test the Group object creation from text', () => {
    // 1. Create Group object from text
    const myobj = new Group(EXAMPLE_TEXT);
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(14);
    expect(Object.keys(myobj.answers)).toHaveLength(6);

    // 3. Test methods
    expect(myobj.yes()).toBe(6);
  });
});

// ======================================================================
// end                   g r o u p . t e s t . t s                  end
// ======================================================================
