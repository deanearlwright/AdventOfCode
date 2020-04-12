/* eslint-disable linebreak-style */
// ======================================================================
// All in a Single Night
//   Advent of Code 2015 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      r o u t e s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 09 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc09 = require('./aoc_09');
const routes = require('./routes');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '\nLondon to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141';
const PARIS_TEXT = '\nParis to London = 344\nParis to Dublin = 781\nParis to Belfast = 855\nParis to Berlin = 878';
const BERLIN_TEXT = '\nBerlin to London = 466\nBerlin to Dublin = 1318\nBerlin to Belfast = 1294';
const EXPANDED_TEXT = EXAMPLE_TEXT + PARIS_TEXT + BERLIN_TEXT;

const EXAMPLES_PART_ONE = {
  'Dublin -> London -> Belfast': 982,
  'London -> Dublin -> Belfast': 605,
  'London -> Belfast -> Dublin': 659,
  'Dublin -> Belfast -> London': 659,
  'Belfast -> Dublin -> London': 605,
  'Belfast -> London -> Dublin': 982,
};

const EXAMPLES_PART_TWO = {};

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 605;
const PART_TWO_RESULT = 982;

// ======================================================================
//                                                             TestRoutes
// ======================================================================

describe('Routes', () => {
  test('Test the default Routes creation', () => {
    // 1. Create default Routes object
    const myobj = new routes.Routes({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(Object.keys(myobj.cities)).toHaveLength(0);
    expect(myobj.number).toBe(0);
  });

  test('Test the Routes object creation from example text', () => {
    // 1. Create Routes object from text
    const myobj = new routes.Routes({ text: aoc09.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(Object.keys(myobj.cities)).toHaveLength(3);
    expect(myobj.number).toBe(3);
    expect(myobj.cities.London.Dublin).toBe(464);
    expect(myobj.cities.Dublin.London).toBe(464);
    expect(myobj.cities.London.Belfast).toBe(518);
    expect(myobj.cities.Belfast.London).toBe(518);
    expect(myobj.cities.Dublin.Belfast).toBe(141);
    expect(myobj.cities.Belfast.Dublin).toBe(141);
    // 3. Check route distances
    expect(myobj.calculateDistance(['London', 'Dublin', 'Belfast'])).toBe(605);
    expect(myobj.calculateDistance(['London', 'Belfast', 'Dublin'])).toBe(659);
    expect(myobj.calculateDistance(['Dublin', 'London', 'Belfast'])).toBe(982);
    // 4. Find routes
    expect(myobj.findShortRoute('London')).toStrictEqual(['London', 'Dublin', 'Belfast']);
    expect(myobj.findShortRoute('Dublin')).toStrictEqual(['Dublin', 'Belfast', 'London']);
    expect(myobj.findShortRoute('Belfast')).toStrictEqual(['Belfast', 'Dublin', 'London']);
    expect(myobj.findLongRoute('London')).toStrictEqual(['London', 'Belfast', 'Dublin']);
    expect(myobj.findLongRoute('Dublin')).toStrictEqual(['Dublin', 'London', 'Belfast']);
    expect(myobj.findLongRoute('Belfast')).toStrictEqual(['Belfast', 'London', 'Dublin']);
    // 5. Find shortest route
    expect(myobj.findSortestRoute()).toStrictEqual(['London', 'Dublin', 'Belfast']);
    expect(myobj.findLongestRoute()).toStrictEqual(['Dublin', 'London', 'Belfast']);
  });

  test('Test the Routes object creation from expanded text', () => {
    // 1. Create Routes object from text
    const myobj = new routes.Routes({ text: aoc09.fromText(EXPANDED_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(10);
    expect(Object.keys(myobj.cities)).toHaveLength(5);
    expect(myobj.number).toBe(5);
    expect(myobj.cities.London.Dublin).toBe(464);
    expect(myobj.cities.Dublin.London).toBe(464);
    expect(myobj.cities.London.Belfast).toBe(518);
    expect(myobj.cities.Belfast.London).toBe(518);
    expect(myobj.cities.Dublin.Belfast).toBe(141);
    expect(myobj.cities.Belfast.Dublin).toBe(141);
    expect(myobj.cities.London.Paris).toBe(344);
    expect(myobj.cities.London.Berlin).toBe(466);
    expect(myobj.cities.Dublin.Paris).toBe(781);
    expect(myobj.cities.Dublin.Berlin).toBe(1318);
    expect(myobj.cities.Belfast.Paris).toBe(855);
    expect(myobj.cities.Belfast.Berlin).toBe(1294);
    expect(myobj.cities.Paris.Berlin).toBe(878);
    // 3. Check route distances
    expect(myobj.calculateDistance(['London', 'Dublin', 'Belfast'])).toBe(605);
    expect(myobj.calculateDistance(['London', 'Belfast', 'Dublin'])).toBe(659);
    expect(myobj.calculateDistance(['London', 'Berlin', 'Paris', 'Dublin', 'Belfast'])).toBe(2266);
    expect(myobj.calculateDistance(['Berlin', 'Paris', 'London', 'Dublin', 'Belfast'])).toBe(1827);
    expect(myobj.calculateDistance(['Dublin', 'Belfast', 'London', 'Paris', 'Berlin'])).toBe(1881);
    expect(myobj.calculateDistance(['Dublin', 'Belfast', 'London', 'Berlin', 'Paris'])).toBe(2003);
    expect(myobj.calculateDistance(['Dublin', 'Belfast', 'Paris', 'London', 'Berlin'])).toBe(1806);
    expect(myobj.calculateDistance(['Belfast', 'Dublin', 'London', 'Berlin', 'Paris'])).toBe(1949);
    expect(myobj.calculateDistance(['Belfast', 'Dublin', 'London', 'Paris', 'Berlin'])).toBe(1827);
    expect(myobj.calculateDistance(['Belfast', 'Dublin', 'Paris', 'London', 'Berlin'])).toBe(1732);
    expect(myobj.calculateDistance(['Berlin', 'Paris', 'London', 'Dublin', 'Belfast'])).toBe(1827);
    expect(myobj.calculateDistance(['Berlin', 'London', 'Paris', 'Dublin', 'Belfast'])).toBe(1732);
    expect(myobj.calculateDistance(['Paris', 'Berlin', 'London', 'Dublin', 'Belfast'])).toBe(1949);
    expect(myobj.calculateDistance(['Paris', 'London', 'Dublin', 'Belfast', 'Berlin'])).toBe(2243);
    expect(myobj.calculateDistance(['Paris', 'Dublin', 'Belfast', 'London', 'Berlin'])).toBe(1906);
    // 4. Find routes
    expect(myobj.findShortRoute('London')).toStrictEqual(['London', 'Berlin', 'Paris', 'Dublin', 'Belfast']);
    expect(myobj.findShortRoute('Dublin')).toStrictEqual(['Dublin', 'Belfast', 'Paris', 'London', 'Berlin']);
    expect(myobj.findShortRoute('Belfast')).toStrictEqual(['Belfast', 'Dublin', 'Paris', 'London', 'Berlin']);
    expect(myobj.findShortRoute('Berlin')).toStrictEqual(['Berlin', 'London', 'Paris', 'Dublin', 'Belfast']);
    expect(myobj.findShortRoute('Paris')).toStrictEqual(['Paris', 'Dublin', 'Belfast', 'London', 'Berlin']);
    // 5. Find shortest route
    expect(myobj.findSortestRoute()).toStrictEqual(['Belfast', 'Dublin', 'Paris', 'London', 'Berlin']);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    Object.keys(EXAMPLES_PART_ONE).forEach((key) => {
      // 2. Create Routes object using the key as text
      const myobj = new routes.Routes({ text: aoc09.fromText(EXAMPLE_TEXT) });
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(3);
      expect(Object.keys(myobj.cities)).toHaveLength(3);
      expect(myobj.number).toBe(3);
      expect(myobj.cities.London.Dublin).toBe(464);
      // 3. Make sure it has the expected value
      expect(myobj.verifyDistance(key)).toBe(EXAMPLES_PART_ONE[key]);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    Object.keys(EXAMPLES_PART_TWO).forEach((key) => {
      // 2. Create Routes object using the key as text
      const myobj = new routes.Routes({ part2: true, text: [key] });
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.routes(key)).toBe(EXAMPLES_PART_TWO[key]);
    });
  });

  test('Test part one example of Routes object', () => {
    // 1. Create Routes object from text
    const myobj = new routes.Routes({ text: aoc09.fromText(PART_ONE_TEXT) });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Routes object', () => {
    // 1. Create Routes object from text
    const myobj = new routes.Routes({ part2: true, text: aoc09.fromText(PART_TWO_TEXT) });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    t e s t _ r o u t e s . j s                 end
// ======================================================================
