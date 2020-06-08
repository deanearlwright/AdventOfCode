/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      b a t t l e . t e s t . j s
//
// Test the combat simulation for Advent of Code 2015 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc22 = require('./aoc_22');
const player = require('./player');
const battle = require('./battle');


// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const PLAYER_TEXT = `
Hit Points: 10
Damage: 0
Mana: 250
Armor: 0
`;

const BOSS_TEXT = `
Hit Points: 14
Damage: 8
Armor: 0
`;

const SPELL_ORDER = ['None', 'Recharge', 'Shield', 'Drain', 'Poison', 'MagicMissle'];

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
    expect(myobj.timeline).toHaveLength(1);
    expect(Object.keys(myobj.active)).toHaveLength(0);
  });

  test('Test the Battle object creation from text', () => {
    // 1. Create the player objects
    // const spellbook = new spells.Spells({}).spells;
    const thePlayer = new player.Player({ name: 'player', text: aoc22.fromText(PLAYER_TEXT) });
    const theBoss = new player.Player({ name: 'boss', text: aoc22.fromText(BOSS_TEXT) });
    // 2. Create Battle object using the players
    const myobj = new battle.Battle({ player: thePlayer, boss: theBoss });
    // 3. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.player).toBe(thePlayer);
    expect(myobj.boss).toBe(theBoss);
    expect(myobj.timeline).toHaveLength(1);
    expect(Object.keys(myobj.active)).toHaveLength(0);
  });

  test('Test the Battle object in a scripted combat', () => {
    // 1. Create the player objects
    const wizard = new player.Player({ name: 'player', text: aoc22.fromText(PLAYER_TEXT) });
    const theBoss = new player.Player({ name: 'boss', text: aoc22.fromText(BOSS_TEXT) });
    // 2. Create Battle object using the players
    const myobj = new battle.Battle({ player: wizard, boss: theBoss });
    // 3. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.player).toBe(wizard);
    expect(myobj.boss).toBe(theBoss);
    expect(myobj.timeline).toHaveLength(1);
    expect(Object.keys(myobj.active)).toHaveLength(0);
    // 4. Create a function to supply the spell to use
    function playerBrain(battleArg) {
      const spellName = SPELL_ORDER[battleArg.round()];
      // eslint-disable-next-line no-console
      // console.log(`playerBrain round=${round} spellName=${spellName}`);
      return spellName;
    }
    // 5. Round 1
    expect(myobj.round()).toBe(0);
    myobj.newRound();
    expect(myobj.timeline).toHaveLength(2);
    expect(myobj.round()).toBe(1);
    // 5a. Player turn (1)
    //    Player has 10 hit points, 0 armor, 250 mana
    expect(myobj.player.hitPoints).toBe(10);
    expect(myobj.player.mana).toBe(250);
    //    Boss has 14 hit points
    expect(myobj.boss.hitPoints).toBe(14);
    //    Player casts Recharge.
    myobj.playerTurn(playerBrain);
    expect(Object.keys(myobj.active)).toHaveLength(1);
    expect(myobj.active.Recharge).toBe(5);
    // 5b. Boss turn (1)
    //    Player has 10 hit points, 0 armor, 21 mana
    expect(myobj.player.hitPoints).toBe(10);
    expect(myobj.player.mana).toBe(21);
    //    Boss has 14 hit points
    expect(myobj.boss.hitPoints).toBe(14);
    //    Boss attacks for 8 damage!
    myobj.bossTurn();
    expect(myobj.boss.hitPoints).toBe(14);
    //    Recharge provides 101 mana; its timer is now 4.
    expect(Object.keys(myobj.active)).toHaveLength(1);
    expect(myobj.active.Recharge).toBe(4);
    // 6. Round 2
    myobj.newRound();
    expect(myobj.timeline).toHaveLength(3);
    expect(myobj.round()).toBe(2);
    // 6a. Player turn (2)
    //    Player has 2 hit points, 0 armor, 122 mana
    expect(myobj.player.hitPoints).toBe(2);
    expect(myobj.player.armor).toBe(0);
    expect(myobj.player.mana).toBe(122);
    //     Boss has 14 hit points
    expect(myobj.boss.hitPoints).toBe(14);
    //     Player casts Shield, increasing armor by 7.
    myobj.playerTurn(playerBrain);
    //    Recharge provides 101 mana; its timer is now 3.
    expect(Object.keys(myobj.active)).toHaveLength(2);
    expect(myobj.active.Recharge).toBe(3);
    expect(myobj.active.Shield).toBe(6);
    // 6b. Boss turn (2)
    //     Player has 2 hit points, 7 armor, 110 mana
    expect(myobj.player.hitPoints).toBe(2);
    expect(myobj.player.armor).toBe(0); // Will be 7 very soon
    expect(myobj.player.mana).toBe(110);
    //    Boss has 14 hit points
    expect(myobj.boss.hitPoints).toBe(14);
    //    Boss attacks for 8 - 7 = 1 damage!
    myobj.bossTurn();
    //    Shield's timer is now 5.
    //    Recharge provides 101 mana; its timer is now 2.
    expect(Object.keys(myobj.active)).toHaveLength(2);
    expect(myobj.active.Recharge).toBe(2);
    expect(myobj.active.Shield).toBe(5);
    // 7. Round 3
    myobj.newRound();
    expect(myobj.timeline).toHaveLength(4);
    expect(myobj.round()).toBe(3);
    // 7a. Player turn (3)
    //    Player has 1 hit point, 7 armor, 211 mana
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(211);
    //    Boss has 14 hit points
    expect(myobj.boss.hitPoints).toBe(14);
    //    Player casts Drain, dealing 2 damage, and healing 2 hit points.
    myobj.playerTurn(playerBrain);
    //    Shield's timer is now 4.
    //    Recharge provides 101 mana; its timer is now 1.
    expect(Object.keys(myobj.active)).toHaveLength(3);
    expect(myobj.active.Recharge).toBe(1);
    expect(myobj.active.Shield).toBe(4);
    expect(myobj.active.Drain).toBe(0);
    // 7b. Boss turn (3)
    //    Player has 1 (soon to be 3) hit points, 7 armor, 239 mana
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(239);
    //    Boss has 14 (soon to be 12) hit points
    expect(myobj.boss.hitPoints).toBe(14);
    //    Boss attacks for 8 - 7 = 1 damage!
    myobj.bossTurn();
    //    Shield's timer is now 3.
    //    Recharge provides 101 mana; its timer is now 0.
    //    Recharge wears off.
    expect(Object.keys(myobj.active)).toHaveLength(1);
    expect(myobj.active.Shield).toBe(3);
    // 8. Round 4
    myobj.newRound();
    expect(myobj.timeline).toHaveLength(5);
    expect(myobj.round()).toBe(4);
    // 8a. Player turn (4)
    //    Player has 2 hit points, 7 armor, 340 mana
    expect(myobj.player.hitPoints).toBe(2);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(340);
    //    Boss has 12 hit points
    expect(myobj.boss.hitPoints).toBe(12);
    //    Player casts Poison.
    myobj.playerTurn(playerBrain);
    //    Shield's timer is now 2.
    expect(Object.keys(myobj.active)).toHaveLength(2);
    expect(myobj.active.Shield).toBe(2);
    expect(myobj.active.Poison).toBe(6);
    // 8b. Boss turn (4)
    //    Player has 2 hit points, 7 armor, 167 mana
    expect(myobj.player.hitPoints).toBe(2);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(167);
    //    Boss has 12 hit points
    expect(myobj.boss.hitPoints).toBe(12);
    //    Boss attacks for 8 - 7 = 1 damage!
    myobj.bossTurn();
    //    Shield's timer is now 1.
    //    Poison deals 3 damage; its timer is now 5.
    expect(Object.keys(myobj.active)).toHaveLength(2);
    expect(myobj.active.Shield).toBe(1);
    expect(myobj.active.Poison).toBe(5);
    // 9. Round 5
    myobj.newRound();
    expect(myobj.timeline).toHaveLength(6);
    expect(myobj.round()).toBe(5);
    // 9a. Player turn (5)
    //     Player has 1 hit point, 7 armor, 167 mana
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(167);
    //     Boss has 9 hit points
    expect(myobj.boss.hitPoints).toBe(9);
    // Player casts Magic Missile, dealing 4 damage.
    myobj.playerTurn(playerBrain);
    //     Shield's timer is now 0.
    //     Shield wears off, decreasing armor by 7.
    //     Poison deals 3 damage; its timer is now 4.
    expect(Object.keys(myobj.active)).toHaveLength(2);
    expect(myobj.active.Poison).toBe(4);
    expect(myobj.active.MagicMissle).toBe(0);
    // 9b. Boss turn (5)
    //     Player has 1 hit point, 7 (soon to be 0) armor, 114 mana
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(114);
    //     Boss has 6 hit points, soon to be 0 due to MagicMissle (-4) and Poison (-2)
    expect(myobj.boss.hitPoints).toBe(6);
    //     Poison deals 3 damage. This kills the boss, and the player wins.
    myobj.bossTurn();
    expect(myobj.boss.hitPoints).toBe(0);
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(0);
    expect(myobj.player.mana).toBe(114);
    // 10. Undo the last two turns
    myobj.undo();
    expect(myobj.timeline).toHaveLength(5);
    expect(myobj.round()).toBe(4);
    //     Player has 1 hit point, 7 armor, 167 mana
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(167);
    //     Boss has 9 hit points
    expect(myobj.boss.hitPoints).toBe(9);
    //    Shield's timer is now 1.
    //    Poison deals 3 damage; its timer is now 5.
    expect(Object.keys(myobj.active)).toHaveLength(2);
    expect(myobj.active.Poison).toBe(5);
    expect(myobj.active.Shield).toBe(1);
    myobj.undo();
    expect(myobj.timeline).toHaveLength(4);
    expect(myobj.round()).toBe(3);
    //    Player has 2 hit points, 7 armor, 340 mana
    expect(myobj.player.hitPoints).toBe(2);
    expect(myobj.player.armor).toBe(7);
    expect(myobj.player.mana).toBe(340);
    //    Boss has 12 hit points
    expect(myobj.boss.hitPoints).toBe(12);
    //    Shield's timer is now 3.
    //    Recharge provides 101 mana; its timer is now 0.
    //    Recharge wears off.
    expect(Object.keys(myobj.active)).toHaveLength(1);
    expect(myobj.active.Shield).toBe(3);
    // 11. Replay the last turns
    myobj.toTheDeath(playerBrain);
    expect(myobj.boss.hitPoints).toBe(0);
    expect(myobj.player.hitPoints).toBe(1);
    expect(myobj.player.armor).toBe(0);
    expect(myobj.player.mana).toBe(114);
  });
});

// ======================================================================
// end                   b a t t l e . t e s t . j s                  end
// ======================================================================
