/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           w i z s i m . j s
//
// A solver for the Advent of Code 2015 Day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const spells = require('./spells');
const player = require('./player');
const battle = require('./battle');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const WIZARD_TEXT = ['Hit Points: 50', 'Mana: 500'];
const BOSS_TEXT = ['Hit Points: 50', 'Damage: 10'];

// ======================================================================
//                                                                 Wizsim
// ======================================================================

class Wizsim {
  // Object for Wizard Simulator 20XX

  constructor(options) {
    // Create a Wizsim object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.player = options.player === undefined ? new player.Player({
      part2: this.part2, name: 'Wizard', text: WIZARD_TEXT,
    }) : options.player;
    this.boss = options.boss === undefined ? new player.Player({
      part2: this.part2, name: 'Boss', text: BOSS_TEXT,
    }) : options.boss;
    this.spells = options.spells === undefined ? new spells.Spells({
      part2: this.part2,
    }) : options.spells;
    // 2. Process text (if any)
    if (this.text !== null) {
      this.boss = new player.Player({ text: this.text });
    }
  }

  leastMana(verbose, limit) {
    // 1. Start least mana with more than we have
    let result = 9999999999999999999;
    const original = result;
    const cast = ['Zero', null];
    let rounds = 0;
    // 2. Start a battle
    const conflict = new battle.Battle({
      part2: this.part2,
      player: this.player,
      boss: this.boss,
      spells: this.spells,
    });
    // 3. We need a brain
    function playerBrain(battleArg) {
      let name = battleArg.spells.next(cast[battleArg.round()]);
      let looking = true;
      const active = Object.keys(battleArg.active);
      while (looking) {
        if (name === null) {
          name = 'None';
          looking = false;
        } else {
          const need = battleArg.spells.cost(name);
          if (need === null) {
            name = 'Unknown';
            looking = false;
          } else if (!(name in active)) {
            if (battleArg.player.mana >= need) {
              looking = false;
            }
          }
        }
        if (looking) name = battleArg.spells.next(name);
      }
      return name;
    }
    // 4. Loop until we have exhausted the solutions
    let solving = true;
    while (solving) {
      // 5. Start a round and do the player turn
      let nextSpell = false;
      conflict.newRound();
      // eslint-disable-next-line no-console
      if (verbose) console.log(`Starting round ${conflict.round()} wizard = ${conflict.player.hitPoints}/${conflict.player.mana}  boss = ${conflict.boss.hitPoints}`);
      rounds += 1;
      if (rounds % 10000000 === 0) {
        // eslint-disable-next-line no-console
        console.log(`${rounds} rounds`);
        // eslint-disable-next-line no-console
        console.log(`Spells: ${cast.join(' - ')}`);
        // eslint-disable-next-line no-console
        console.log(`Active = ${conflict.active.join()}`);
      }
      if (limit > 0 && rounds > limit) {
        // eslint-disable-next-line no-console
        if (verbose) console.log(`Reached limit of ${limit} rounds`);
        solving = false;
      } else {
        if (conflict.player.hitPoints < 1) {
          conflict.spell = 'None';
        } else {
          conflict.playerTurn(playerBrain);
        }
        cast[conflict.round()] = conflict.spell;
        // eslint-disable-next-line no-console
        if (verbose) console.log(`Round ${conflict.round()} Player cast ${conflict.spell}`);
        // 5a. If the player is no more, redo this round
        if (conflict.player.hitPoints < 1) {
          // eslint-disable-next-line no-console
          if (verbose) console.log(`Player cast ${conflict.spell} but is no more`);
          nextSpell = true;
          // 5b. if the boss, is no more, check the result and redo this round
        } else if (conflict.boss.hitPoints < 1) {
          // eslint-disable-next-line no-console
          if (verbose) console.log(`Player cast ${conflict.spell} and the boss is no more`);
          if (conflict.player.spent < result) {
            result = conflict.player.spent;
            // eslint-disable-next-line no-console
            console.log(`Rounds: ${rounds}, Setting result to ${result}`);
            // eslint-disable-next-line no-console
            console.log(`Spells: ${cast.join(' - ')}`);
          }
          nextSpell = true;
        } else {
          // 6. Give the boss a turn
          conflict.bossTurn();
          // 6a. If the player is no more, redo this round
          if (conflict.player.hitPoints < 1) {
            // eslint-disable-next-line no-console
            if (verbose) console.log(`Player died after boss's turn in round ${conflict.round()}`);
            nextSpell = true;
            // 6b. if the boss, is no more, check the result and redo this round
          } else if (conflict.boss.hitPoints < 1) {
            // eslint-disable-next-line no-console
            if (verbose) console.log(`boss died after boss's turn in round ${conflict.round()}`);
            if (conflict.player.spent < result) {
              result = conflict.player.spent;
              // eslint-disable-next-line no-console
              console.log(`Rounds: ${rounds}, Setting result to ${result}`);
              // eslint-disable-next-line no-console
              console.log(`Spells: ${cast.join(' - ')}`);
            }
            nextSpell = true;
          }
        }
        // 7. We may have to redo this round, or even back up to the last round
        if (conflict.player.spent > result) {
          // eslint-disable-next-line no-console
          if (verbose) console.log(`Player has spent more than ${result} mana`);
          nextSpell = true;
        }
        if (nextSpell) {
          if (conflict.spell !== 'None' && conflict.spells.next(conflict.spell)) {
            // eslint-disable-next-line no-console
            if (verbose) console.log(`Redoing round ${conflict.round()}`);
            conflict.undo();
          } else {
            conflict.undo();
            cast.pop();
            // eslint-disable-next-line no-console
            if (verbose) console.log(`Backing up to round ${conflict.round()}`);
            conflict.undo();
            // 8. If we have backed up to the start, we are done
            if (conflict.round() === -1) {
              // eslint-disable-next-line no-console
              if (verbose) console.log(`That's all folks at round ${conflict.round()}`);
              solving = false;
            }
          }
        } else {
          cast.push(null);
        }
      }
    }
    // eslint-disable-next-line no-console
    if (verbose) console.log(`Result = ${result}, original = ${original}`);
    // 9. Return the least amount of mana to kill the boss(or null if we never we able to do it)
    if (result < original) {
      return result;
    }
    return null;
  }

  partOne(options) {
    // Returns the solution for part one
    // What is the least amount of mana you can spend and still win the fight?
    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.leastMana(verbose, limit);
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.leastMana(verbose, limit);
  }
}

module.exports.Wizsim = Wizsim;
// ======================================================================
// end                        w i z s i m . j s                       end
// ======================================================================
