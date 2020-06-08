/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      w i z s i m . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc22 = require('./aoc_22');
const wizsim = require('./wizsim');
const player = require('./player');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `Hit Points: 71
Damage: 10
`;


const PART_ONE_13_RESULT = 226;
const PART_ONE_14_RESULT = 641;
const PART_TWO_13_RESULT = 226;
const PART_TWO_14_RESULT = null;

const WIZARD10_TEXT = `
Hit Points: 10
Damage: 0
Mana: 250
Armor: 0
`;

const BOSS13_TEXT = `
Hit Points: 13
Damage: 7
Armor: 0
`;

const BOSS14_TEXT = `
Hit Points: 14
Damage: 7
Armor: 0
`;

// ======================================================================
//                                                              TestWizsim
// ======================================================================

describe('Wizsim', () => {
  test('Test the default Wizsim creation', () => {
    // 1. Create default Wizsim object
    const myobj = new wizsim.Wizsim({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.player.name).toBe('Wizard');
    expect(myobj.player.hitPoints).toBe(50);
    expect(myobj.player.damage).toBe(0);
    expect(myobj.player.armor).toBe(0);
    expect(myobj.player.mana).toBe(500);
    expect(myobj.boss.name).toBe('Boss');
    expect(myobj.boss.hitPoints).toBe(50);
    expect(myobj.boss.damage).toBe(10);
    expect(myobj.boss.armor).toBe(0);
    expect(myobj.boss.mana).toBe(0);
  });

  test('Test the Wizsim object creation from text', () => {
    // 1. Create Wizsim object from text
    const myobj = new wizsim.Wizsim({ text: aoc22.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(2);
    expect(myobj.player.name).toBe('Wizard');
    expect(myobj.player.hitPoints).toBe(50);
    expect(myobj.player.damage).toBe(0);
    expect(myobj.player.armor).toBe(0);
    expect(myobj.player.mana).toBe(500);
    expect(myobj.boss.name).toBe(null);
    expect(myobj.boss.hitPoints).toBe(71);
    expect(myobj.boss.damage).toBe(10);
    expect(myobj.boss.armor).toBe(0);
    expect(myobj.boss.mana).toBe(0);
    expect(myobj.spells.keys).toHaveLength(5);
    expect(myobj.spells.book.MagicMissle.name).toBe('MagicMissle');
    expect(myobj.spells.book.MagicMissle.cost).toBe(53);
    expect(myobj.spells.book.MagicMissle.damage).toBe(4);
    expect(myobj.spells.book.MagicMissle.health).toBe(0);
    expect(myobj.spells.book.MagicMissle.armor).toBe(0);
    expect(myobj.spells.book.MagicMissle.mana).toBe(0);
    expect(myobj.spells.book.MagicMissle.turns).toBe(0);
  });


  test('Test part one example of Wizsim object with boss 13', () => {
    // 1. Create the wizard and boss players
    const wiz10 = new player.Player({ part2: false, text: aoc22.fromText(WIZARD10_TEXT) });
    const boss13 = new player.Player({ part2: false, text: aoc22.fromText(BOSS13_TEXT) });
    // 2. Create Wizsim object from text
    const myobj = new wizsim.Wizsim({ player: wiz10, boss: boss13 });
    // 3. Check the part one result
    expect(myobj.partOne({ verbose: false, limit: 200 })).toBe(PART_ONE_13_RESULT);
  });

  test('Test part one example of Wizsim object with boss 14', () => {
    // 1. Create the wizard and boss players
    const wiz10 = new player.Player({ part2: false, text: aoc22.fromText(WIZARD10_TEXT) });
    const boss13 = new player.Player({ part2: false, text: aoc22.fromText(BOSS14_TEXT) });
    // 2. Create Wizsim object from text
    const myobj = new wizsim.Wizsim({ player: wiz10, boss: boss13 });
    // 3. Check the part one result
    expect(myobj.partOne({ verbose: false, limit: 200 })).toBe(PART_ONE_14_RESULT);
  });

  test('Test part two example of Wizsim object with boss 13', () => {
    // 1. Create the wizard and boss players
    const wiz10 = new player.Player({ part2: true, text: aoc22.fromText(WIZARD10_TEXT) });
    const boss13 = new player.Player({ part2: true, text: aoc22.fromText(BOSS13_TEXT) });
    // 2. Create Wizsim object from text
    const myobj = new wizsim.Wizsim({ part2: true, player: wiz10, boss: boss13 });
    // 3. Check the part one result
    expect(myobj.partOne({ part2: true, verbose: false, limit: 200 })).toBe(PART_TWO_13_RESULT);
  });

  test('Test part two example of Wizsim object with boss 14', () => {
    // 1. Create the wizard and boss players
    const wiz10 = new player.Player({ part2: true, text: aoc22.fromText(WIZARD10_TEXT) });
    const boss14 = new player.Player({ part2: true, text: aoc22.fromText(BOSS14_TEXT) });
    // 2. Create Wizsim object from text
    const myobj = new wizsim.Wizsim({ part2: true, player: wiz10, boss: boss14 });
    // 3. Check the part one result
    expect(myobj.partOne({ part2: true, verbose: false, limit: 200 })).toBe(PART_TWO_14_RESULT);
  });
});

// ======================================================================
// end                   w i z s i m . t e s t . j s                  end
// ======================================================================
