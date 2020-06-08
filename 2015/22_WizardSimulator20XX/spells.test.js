/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                        s p e l l s . t e s t . j s
//
// Test the spells for Advent of Code 2015 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const spells = require('./spells');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                             TestSpells
// ======================================================================

describe('Spells', () => {
  test('Test the default Spells creation', () => {
    // 1. Create default Spells object
    const myobj = new spells.Spells({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(Object.keys(myobj.book)).toHaveLength(5);
    expect(myobj.keys).toHaveLength(5);
    expect(myobj.book.MagicMissle.name).toBe('MagicMissle');
    expect(myobj.book.MagicMissle.cost).toBe(53);
    expect(myobj.book.MagicMissle.damage).toBe(4);
    expect(myobj.book.MagicMissle.health).toBe(0);
    expect(myobj.book.MagicMissle.armor).toBe(0);
    expect(myobj.book.MagicMissle.mana).toBe(0);
    expect(myobj.book.MagicMissle.turns).toBe(0);
    expect(myobj.book.Recharge.name).toBe('Recharge');
    expect(myobj.book.Recharge.cost).toBe(229);
    expect(myobj.book.Recharge.damage).toBe(0);
    expect(myobj.book.Recharge.health).toBe(0);
    expect(myobj.book.Recharge.armor).toBe(0);
    expect(myobj.book.Recharge.mana).toBe(101);
    expect(myobj.book.Recharge.turns).toBe(5);
    expect(myobj.cost('MagicMissle')).toBe(53);
    expect(myobj.cost('Recharge')).toBe(229);
    // 3. Test next
    expect(myobj.next(null)).toBe('MagicMissle');
    expect(myobj.next('MagicMissle')).toBe('Drain');
    expect(myobj.next('Poison')).toBe('Recharge');
    expect(myobj.next('Recharge')).toBe(null);
  });
});

// ======================================================================
// end                   s p e l l s . t e s t . j s                  end
// ======================================================================
