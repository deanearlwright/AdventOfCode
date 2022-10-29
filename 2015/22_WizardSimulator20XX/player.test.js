/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p l a y e r . t e s t . j s
//
// Test the player for the Advent of Code 2015 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc22 = require('./aoc_22');
const player = require('./player');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Hit Points: 71
Damage: 10
`;

const PLAYER_TEXT = `
Hit Points: 10
Damage: 0
Mana: 250
Armor: 0
`;
const BOSS_TEXT = `
Hit Points: 13
Damage: 7
Armor: 0
`;

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
    expect(myobj.hitPoints).toBe(0);
    expect(myobj.damage).toBe(0);
    expect(myobj.armor).toBe(0);
    expect(myobj.mana).toBe(0);
    expect(myobj.original.hitPoints).toBe(0);
    expect(myobj.original.damage).toBe(0);
    expect(myobj.original.armor).toBe(0);
    expect(myobj.original.mana).toBe(0);
  });

  test('Test the Player object creation from text', () => {
    // 1. Create Player object from text
    const myobj = new player.Player({ name: 'boss', text: aoc22.fromText(EXAMPLE_TEXT) });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.name).toBe('boss');
    expect(myobj.hitPoints).toBe(71);
    expect(myobj.damage).toBe(10);
    expect(myobj.armor).toBe(0);
    expect(myobj.mana).toBe(0);
    expect(myobj.original.hitPoints).toBe(71);
    expect(myobj.original.damage).toBe(10);
    expect(myobj.original.armor).toBe(0);
    expect(myobj.original.mana).toBe(0);
  });

  test('Test the Player object attack and defend', () => {
    // 1. Create Player objects from text
    //    For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that
    //    the boss has 12 hit points, 7 damage, and 2 armor:
    const thePlayer = new player.Player({ name: 'player', text: aoc22.fromText(PLAYER_TEXT) });
    const theBoss = new player.Player({ name: 'boss', text: aoc22.fromText(BOSS_TEXT) });
    // 2. Make sure they have the expected values
    expect(thePlayer.part2).toBe(false);
    expect(thePlayer.text).toBe(null);
    expect(thePlayer.name).toBe('player');
    expect(thePlayer.hitPoints).toBe(10);
    expect(thePlayer.damage).toBe(0);
    expect(thePlayer.armor).toBe(0);
    expect(thePlayer.mana).toBe(250);
    expect(thePlayer.original.hitPoints).toBe(10);
    expect(thePlayer.original.damage).toBe(0);
    expect(thePlayer.original.armor).toBe(0);
    expect(thePlayer.original.mana).toBe(250);
    expect(theBoss.part2).toBe(false);
    expect(theBoss.text).toBe(null);
    expect(theBoss.name).toBe('boss');
    expect(theBoss.hitPoints).toBe(13);
    expect(theBoss.damage).toBe(7);
    expect(theBoss.armor).toBe(0);
    expect(theBoss.mana).toBe(0);
    expect(theBoss.original.hitPoints).toBe(13);
    expect(theBoss.original.damage).toBe(7);
    expect(theBoss.original.armor).toBe(0);
    expect(theBoss.original.mana).toBe(0);
    // 3. Attack and defend
    // 3a. Initial state
    //     Player has 10 hit points, 0 armor, 250 mana
    //     Boss has 13 hit points
    expect(thePlayer.hitPoints).toBe(10);
    expect(thePlayer.mana).toBe(250);
    expect(theBoss.hitPoints).toBe(13);
    // 3a. Turns 1 and 2
    //     Player casts Poision
    //     Boss attacks
    theBoss.defend(3); // poison
    theBoss.attack(thePlayer);
    // 3b. After turn 2
    expect(thePlayer.hitPoints).toBe(3);
    expect(thePlayer.armor).toBe(0);
    expect(theBoss.hitPoints).toBe(10);
    theBoss.defend(3); // poison
    // 3c. Turns 3 and 4
    //     Player casts Magic Missle
    theBoss.defend(4); // magic missle
    theBoss.defend(3); // poison
    expect(theBoss.hitPoints).toBe(0);
    // 4. Reset the player and boss's values
    thePlayer.reset();
    theBoss.reset();
    expect(thePlayer.hitPoints).toBe(10);
    expect(thePlayer.damage).toBe(0);
    expect(thePlayer.armor).toBe(0);
    expect(thePlayer.mana).toBe(250);
    expect(theBoss.hitPoints).toBe(13);
    expect(theBoss.damage).toBe(7);
    expect(theBoss.armor).toBe(0);
    expect(theBoss.mana).toBe(0);
  });
});

// ======================================================================
// end                   p l a y e r . t e s t . j s                  end
// ======================================================================
