// ======================================================================
// Combo Breaker
//   Advent of Code 2020 Day 25 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      h a n d s h a k e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 25 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_25';
import { Handshake } from './handshake';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
5764801
17807724
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 14897079;
const PART_TWO_RESULT = NaN;

// ======================================================================
//                                                          TestHandshake
// ======================================================================

describe('Handshake', () => {
  test('Test the default Handshake creation', () => {
    // 1. Create default Handshake object
    const myobj = new Handshake([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.cardPublic).toBe(NaN);
    expect(myobj.cardPrivate).toBe(NaN);
    expect(myobj.doorPublic).toBe(NaN);
    expect(myobj.doorPrivate).toBe(NaN);
  });

  test('Test the Handshake object creation from text', () => {
    // 1. Create Handshake object from text
    const myobj = new Handshake(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.cardPublic).toBe(5764801);
    expect(myobj.cardPrivate).toBe(NaN);
    expect(myobj.doorPublic).toBe(17807724);
    expect(myobj.doorPrivate).toBe(NaN);
    // 3. Check methods
    expect(myobj.transformNumber(17807724, 8)).toBe(14897079);
    expect(myobj.transformNumber(5764801, 11)).toBe(14897079);
    expect(myobj.guessPrivate(17807724)).toBe(11);
    expect(myobj.guessPrivate(5764801)).toBe(8);
    expect(myobj.guessEncryptionKey()).toBe(14897079);
  });

  test('Test part one example of Handshake object', () => {
    // 1. Create Handshake object from text
    const myobj = new Handshake(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Handshake object', () => {
    // 1. Create Handshake object from text
    const myobj = new Handshake(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                h a n d s h a k e . t e s t . t s               end
// ======================================================================
