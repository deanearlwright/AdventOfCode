/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b a t t l e . j s
//
// A battle simulation for the Advent of Code 2015 Day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Battle
// ======================================================================

class Battle {
  // Object for RPG Simulator 20XX

  constructor(options) {
    // Create a Battle object

    // 1. Set the initial values
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.player = options.player === undefined ? null : options.player;
    this.boss = options.boss === undefined ? null : options.boss;
  }

  simulate() {
    // eslint-disable-next-line no-console
    // console.log(`battle.simulate(): Player ${this.player.damage},${this.player.armor} vs Boss ${this.boss.damage},${this.boss.armor}`);
    // 1. Reset the hit point counters
    this.player.reset();
    this.boss.reset();

    // 2. Loop until one of the other is dead
    while (this.player.hitPoints > 0 && this.boss.hitPoints > 0) {
      // 3. Do player attack followed by boss.attack
      if (this.player.hitPoints > 0) {
        this.player.attack(this.boss);
      }
      if (this.boss.hitPoints > 0) {
        this.boss.attack(this.player);
      }
    }
    // 4. Return the victor
    return this.player.hitPoints > 0 ? this.player : this.boss;
  }
}

module.exports.Battle = Battle;
// ======================================================================
// end                        b a t t l e . j s                       end
// ======================================================================
