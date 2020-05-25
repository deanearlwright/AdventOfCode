/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                        s h o p . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc21 = require('./aoc_21');
const shop = require('./shop');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = '';

// ======================================================================
//                                                             TestShop
// ======================================================================

describe('Shop', () => {
  test('Test the default Shop creation', () => {
    // 1. Create default Shop object
    const myobj = new shop.Shop({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(21);
    expect(Object.keys(myobj.weapons)).toHaveLength(5);
    expect(Object.keys(myobj.armor)).toHaveLength(5);
    expect(Object.keys(myobj.rings)).toHaveLength(6);
    expect(myobj.weapons.Warhammer.name).toBe('Warhammer');
    expect(myobj.weapons.Warhammer.cost).toBe(25);
    expect(myobj.weapons.Warhammer.damage).toBe(6);
    expect(myobj.weapons.Warhammer.armor).toBe(0);
    expect(myobj.armor.Chainmail.name).toBe('Chainmail');
    expect(myobj.armor.Chainmail.cost).toBe(31);
    expect(myobj.armor.Chainmail.damage).toBe(0);
    expect(myobj.armor.Chainmail.armor).toBe(2);
    expect(myobj.rings['Damage +1'].name).toBe('Damage +1');
    expect(myobj.rings['Damage +1'].cost).toBe(25);
    expect(myobj.rings['Damage +1'].damage).toBe(1);
    expect(myobj.rings['Damage +1'].armor).toBe(0);
    // 3. Check out the expanded rings
    expect(Object.keys(myobj.xrings)).toHaveLength(22);
    expect(myobj.xrings['Damage +1'].name).toBe('Damage +1');
    expect(myobj.xrings['Damage +1'].cost).toBe(25);
    expect(myobj.xrings['Damage +1'].damage).toBe(1);
    expect(myobj.xrings['Damage +1'].armor).toBe(0);
    expect(myobj.xrings['rings d1 a2'].name).toBe('rings d1 a2');
    expect(myobj.xrings['rings d1 a2'].cost).toBe(65);
    expect(myobj.xrings['rings d1 a2'].damage).toBe(1);
    expect(myobj.xrings['rings d1 a2'].armor).toBe(2);
    // 4. Checkout out the keys
    const shopKeys = myobj.shopKeys();
    expect(Object.keys(shopKeys)).toHaveLength(5);
    expect(shopKeys.weapons).toHaveLength(5);
    expect(shopKeys.armor).toHaveLength(5);
    expect(shopKeys.xarmor).toHaveLength(6);
    expect(shopKeys.rings).toHaveLength(6);
    expect(shopKeys.xrings).toHaveLength(22);
  });

  test('Test the Shop object creation from text', () => {
    // 1. Create Shop object from text
    const myobj = new shop.Shop({ text: aoc21.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
  });
});

// ======================================================================
// end                     s h o p . t e s t . j s                    end
// ======================================================================
