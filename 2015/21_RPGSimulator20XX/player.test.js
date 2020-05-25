/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p l a y e r . t e s t . j s
//
// Test the player for the Advent of Code 2015 day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc21 = require('./aoc_21');
const player = require('./player');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Hit Points: 100
Damage: 8
Armor: 2
`;

const PLAYER_TEXT = `
Hit Points: 8
Damage: 5
Armor: 5`;
const BOSS_TEXT = `
Hit Points: 12
Damage: 7
Armor: 2`;


// ======================================================================
//                                                             TestPlayer
// ======================================================================

describe('Player', () => {
  test('Test the default Player creation', () => {
    // 1. Create default Player object
    const myobj = new player.Player({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.name).toBe(null);
    expect(myobj.initialHitPoints).toBe(null);
    expect(myobj.hitPoints).toBe(0);
    expect(myobj.damage).toBe(0);
    expect(myobj.armor).toBe(0);
  });

  test('Test the Player object creation from text', () => {
    // 1. Create Player object from text
    const myobj = new player.Player({ name: 'boss', text: aoc21.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(3);
    expect(myobj.name).toBe('boss');
    expect(myobj.initialHitPoints).toBe(100);
    expect(myobj.hitPoints).toBe(100);
    expect(myobj.damage).toBe(8);
    expect(myobj.armor).toBe(2);
  });

  test('Test the Player object attack and defend', () => {
    // 1. Create Player objects from text
    //    For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that
    //    the boss has 12 hit points, 7 damage, and 2 armor:
    const thePlayer = new player.Player({ name: 'player', text: aoc21.fromText(PLAYER_TEXT) });
    const theBoss = new player.Player({ name: 'boss', text: aoc21.fromText(BOSS_TEXT) });
    // 2. Make sure they have the expected values
    expect(thePlayer.part2).toBe(false);
    expect(thePlayer.text).toHaveLength(3);
    expect(thePlayer.name).toBe('player');
    expect(thePlayer.initialHitPoints).toBe(8);
    expect(thePlayer.hitPoints).toBe(8);
    expect(thePlayer.damage).toBe(5);
    expect(thePlayer.armor).toBe(5);
    expect(theBoss.part2).toBe(false);
    expect(theBoss.text).toHaveLength(3);
    expect(theBoss.name).toBe('boss');
    expect(theBoss.initialHitPoints).toBe(12);
    expect(theBoss.hitPoints).toBe(12);
    expect(theBoss.damage).toBe(7);
    expect(theBoss.armor).toBe(2);
    // 3. Attack and defend
    //  The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
    thePlayer.attack(theBoss);
    expect(theBoss.hitPoints).toBe(9);
    //  The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
    theBoss.attack(thePlayer);
    expect(thePlayer.hitPoints).toBe(6);
    //  The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
    thePlayer.attack(theBoss);
    expect(theBoss.hitPoints).toBe(6);
    //  The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
    theBoss.attack(thePlayer);
    expect(thePlayer.hitPoints).toBe(4);
    //  The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
    thePlayer.attack(theBoss);
    expect(theBoss.hitPoints).toBe(3);
    //  The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
    theBoss.attack(thePlayer);
    expect(thePlayer.hitPoints).toBe(2);
    //  The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
    thePlayer.attack(theBoss);
    expect(theBoss.hitPoints).toBe(0);
  });
});

// ======================================================================
// end                   p l a y e r . t e s t . j s                  end
// ======================================================================
