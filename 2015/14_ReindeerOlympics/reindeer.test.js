/* eslint-disable linebreak-style */
// ======================================================================
// Reindeer Olympics
//   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      o l y m p i c s . t e s t . j s
//
// Test the reindeer object for Advent of Code 2015 day 14 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const reindeer = require('./reindeer');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.';

// ======================================================================
//                                                           TestReindeer
// ======================================================================

describe('Reindeer', () => {
  test('Test the default Reindeer creation', () => {
    // 1. Create default Reindeer object
    const myobj = new reindeer.Reindeer({});
    // 2. Make sure it has the default values
    expect(myobj.name).toBe(null);
    expect(myobj.speed).toBe(null);
    expect(myobj.fly).toBe(null);
    expect(myobj.rest).toBe(null);
    expect(myobj.text).toBe(null);
    expect(myobj.distance).toBe(0);
    expect(myobj.atTick).toBe(0);
    expect(myobj.flyUntil).toBe(null);
    expect(myobj.restUntil).toBe(null);
    expect(myobj.points).toBe(0);
    // 3. Play with points and rewards
    expect(myobj.points).toBe(0);
    myobj.reward();
    expect(myobj.points).toBe(1);
    myobj.reward();
    expect(myobj.points).toBe(2);
  });

  test('Test the Reindeer object creation from text', () => {
    // 1. Create Reindeer object from text
    const myobj = new reindeer.Reindeer({ text: EXAMPLE_TEXT });
    // 2. Make sure it has the expected values
    expect(myobj.name).toBe('Comet');
    expect(myobj.speed).toBe(14);
    expect(myobj.fly).toBe(10);
    expect(myobj.rest).toBe(127);
    expect(myobj.text).toBe(EXAMPLE_TEXT);
    expect(myobj.distance).toBe(0);
    expect(myobj.atTick).toBe(0);
    expect(myobj.flyUntil).toBe(null);
    expect(myobj.restUntil).toBe(null);
    expect(myobj.points).toBe(0);
    // 3. Start flying
    myobj.start();
    expect(myobj.atTick).toBe(0);
    expect(myobj.distance).toBe(0);
    expect(myobj.flyUntil).toBe(10);
    expect(myobj.restUntil).toBe(null);
    // 4. And watch it fly
    myobj.tick();
    expect(myobj.atTick).toBe(1);
    expect(myobj.distance).toBe(14);
    expect(myobj.flyUntil).toBe(10);
    expect(myobj.restUntil).toBe(null);
    myobj.tick();
    expect(myobj.atTick).toBe(2);
    expect(myobj.distance).toBe(28);
    expect(myobj.flyUntil).toBe(10);
    expect(myobj.restUntil).toBe(null);
    myobj.tick();
    expect(myobj.atTick).toBe(3);
    expect(myobj.distance).toBe(42);
    expect(myobj.flyUntil).toBe(10);
    expect(myobj.restUntil).toBe(null);
    myobj.goto(10);
    expect(myobj.atTick).toBe(10);
    expect(myobj.distance).toBe(140);
    expect(myobj.flyUntil).toBe(null);
    expect(myobj.restUntil).toBe(137);
    myobj.goto(12);
    expect(myobj.atTick).toBe(12);
    expect(myobj.distance).toBe(140);
    expect(myobj.flyUntil).toBe(null);
    expect(myobj.restUntil).toBe(137);
    myobj.goto(138);
    expect(myobj.atTick).toBe(138);
    expect(myobj.distance).toBe(154);
    expect(myobj.flyUntil).toBe(147);
    expect(myobj.restUntil).toBe(null);
    myobj.goto(1000);
    expect(myobj.atTick).toBe(1000);
    expect(myobj.distance).toBe(1120);
    expect(myobj.flyUntil).toBe(null);
    expect(myobj.restUntil).toBe(1096);
  });
});

// ======================================================================
// end                  r e i n d e e r . t e s t . j s               end
// ======================================================================
