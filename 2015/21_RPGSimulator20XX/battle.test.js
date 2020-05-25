/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b a t t l e . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc21 = require('./aoc_21');
const battle = require('./battle');
const player = require('./player');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const PLAYER_TEXT = `
Hit Points: 8
Damage: 5
Armor: 5`;
const BOSS_TEXT = `
Hit Points: 12
Damage: 7
Armor: 2`;

// ======================================================================
//                                                             TestBattle
// ======================================================================

describe('Battle', () => {
  test('Test the default Battle creation', () => {
    // 1. Create default Battle object
    const myobj = new battle.Battle({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.player).toBe(null);
    expect(myobj.boss).toBe(null);
  });

  test('Test the Battle object creation from text', () => {
    // 1. Create the player objects
    const thePlayer = new player.Player({ name: 'player', text: aoc21.fromText(PLAYER_TEXT) });
    const theBoss = new player.Player({ name: 'boss', text: aoc21.fromText(BOSS_TEXT) });
    // 2. Create Battle object using the players
    const myobj = new battle.Battle({ player: thePlayer, boss: theBoss });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.player).toBe(thePlayer);
    expect(myobj.boss).toBe(theBoss);
    // 3. Fight
    expect(myobj.simulate()).toBe(thePlayer);
    expect(thePlayer.hitPoints).toBe(2);
    expect(theBoss.hitPoints).toBe(0);
  });
});

// ======================================================================
// end                   b a t t l e . t e s t . j s                  end
// ======================================================================
