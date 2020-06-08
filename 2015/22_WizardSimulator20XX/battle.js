/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b a t t l e . j s
//
// A battle simulation for the Advent of Code 2015 Day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const spells = require('./spells');
const player = require('./player');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Battle
// ======================================================================

class Battle {
  // Object for Wizard Simulator 20XX

  constructor(options) {
    // Create a Battle object

    // 1. Set the initial values
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.player = options.player === undefined ? null : options.player;
    this.boss = options.boss === undefined ? null : options.boss;
    this.spells = options.spells === undefined ? new spells.Spells({}) : options.spells;
    this.timeline = [];
    this.active = {};
    this.reset();
  }

  reset() {
    // eslint-disable-next-line no-console
    // console.log(`battle.simulate(): Player ${this.player.damage},${this.player.armor}
    //  vs Boss ${ this.boss.damage }, ${ this.boss.armor }`);
    // 1. Reset the hit point counters
    if (this.player) {
      this.player.reset();
    }
    if (this.boss) {
      this.boss.reset();
    }
    const time0 = {
      player: { ...this.player },
      boss: { ...this.boss },
      spell: null,
      active: {},
    };
    this.timeline = [];
    this.timeline.push(time0);
    this.active = {};
    this.spell = null;
  }

  round() {
    return this.timeline.length - 1;
  }

  newRound() {
    const timeNew = {
      player: { ...this.player },
      boss: { ...this.boss },
      spell: this.spell,
      active: { ...this.active },
    };
    this.timeline.push(timeNew);
    if (this.part2) this.player.hitPoints -= 1;
  }

  playerTurn(playerBrain) {
    // 1. Run any current spell effects
    this.active = this.spells.executeActive(this.player, this.boss, this.active);
    // 2. Get spell to cast
    if (this.player.hitPoints > 0) {
      const spellName = playerBrain(this);
      this.spell = spellName;
      // 3. Can this spell be cast?
      if (!(spellName in this.spells.book)) {
        // eslint-disable-next-line no-console
        // console.log(`Unable to cast ${spellName}, the spell is not in the spellbook`);
        this.player.hitPoints = 0;
      } else if (this.player.mana < this.spells.book[spellName].cost) {
        // eslint-disable-next-line no-console
        // console.log(`Unable to cast ${spellName}, not enough mana`);
        this.player.hitPoints = 0;
      } else {
        // 4. Cast that spell!
        this.player.cast(this.spells.book[spellName].cost);
        this.active[spellName] = this.spells.book[spellName].turns;
      }
    }
  }

  bossTurn() {
    // 1. Run any current effects
    this.active = this.spells.executeActive(this.player, this.boss, this.active);
    // 2. Boas attacks wizard
    if (this.boss.hitPoints > 0) {
      this.boss.attack(this.player);
    }
  }

  undo() {
    // 1. Turn back the clock one round
    const timeOld = this.timeline.pop();
    this.player = new player.Player(timeOld.player);
    this.boss = new player.Player(timeOld.boss);
    this.active = { ...timeOld.active };
    this.spell = timeOld.spell;
    // const str = JSON.stringify(this.player, null, 4); // (Optional) beautiful indented output.
    // eslint-disable-next-line no-console
    // console.log(str); // Logs output to dev tools console.
  }

  toTheDeath(playerBrain) {
    // 1. Keep playing rounds until someone dies
    while (this.player.hitPoints > 0 && this.boss.hitPoints > 0) {
      // 2. Start the round
      this.newRound();
      // 3. Let the player get a chance to cast a spell
      this.playerTurn(playerBrain);
      // 4. And then let the boss do some damage
      if (this.player.hitPoints > 0 && this.boss.hitPoints > 0) {
        this.bossTurn();
      }
    }
  }
}

module.exports.Battle = Battle;
// ======================================================================
// end                        b a t t l e . j s                       end
// ======================================================================
