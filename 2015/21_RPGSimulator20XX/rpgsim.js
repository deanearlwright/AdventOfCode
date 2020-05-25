/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r p g s i m . j s
//
// A solver for the Advent of Code 2015 Day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const aoc21 = require('./aoc_21');
const shop = require('./shop');
const player = require('./player');
const battle = require('./battle');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const standardShop = new shop.Shop({});
const standardPlayer = new player.Player({
  name: 'player',
  text: aoc21.fromText('Hit Points: 100\nDamage: 0\nArmor: 0'),
});
const maximumCost = 113;

// ======================================================================
//                                                                 RPGSim
// ======================================================================

class RPGSim {
  // Object for RPG Simulator 20XX

  constructor(options) {
    // Create a RPGSim object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.shop = options.shop === undefined ? standardShop : options.shop;
    this.boss = options.boss === undefined ? null : options.boss;
    this.player = options.player === undefined ? standardPlayer : options.player;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.boss = new player.Player({ part2: this.part2, name: 'boss', text: this.text });
    }

    // 3. Set up for the conflict
    this.battle = new battle.Battle({ part2: this.part2, player: this.player, boss: this.boss });
  }

  findCheapestVictory() {
    // 1. Start with a known (or assumed) value that is too high
    let bestCost = maximumCost;
    // 2. Get the keys to the weapons, armor, and rings
    const allKeys = this.shop.shopKeys();
    // 3. Loop for all of the weapons
    for (let windex = 0; windex < allKeys.weapons.length; windex += 1) {
      const wname = allKeys.weapons[windex];
      const weapon = this.shop.weapons[wname];
      // eslint-disable-next-line no-console
      // console.log(`weapon: ${wname} cost = ${weapon.cost} ${typeof weapon.cost}`);
      if (weapon.cost < bestCost) {
        // 4. Loop for all armor choices (including no armor)
        for (let aindex = 0; aindex < allKeys.xarmor.length; aindex += 1) {
          const aname = allKeys.xarmor[aindex];
          const armor = this.shop.xarmor[aname];
          // eslint-disable-next-line no-console
          // console.log(`armor: ${aname} cost = ${armor.cost}`);
          if ((weapon.cost + armor.cost) < bestCost) {
            // 5. Loop for all the ring choices (include none, one, or two)
            for (let rindex = 0; rindex < allKeys.xrings.length; rindex += 1) {
              const rname = allKeys.xrings[rindex];
              const rings = this.shop.xrings[rname];
              // eslint-disable-next-line no-console
              // console.log(`rings: ${rname} cost = ${rings.cost}`);
              const totalCost = weapon.cost + armor.cost + rings.cost;
              if (totalCost < bestCost) {
                // 6. Set the damage and armor attributes of the player
                this.player.damage = weapon.damage + armor.damage + rings.damage;
                this.player.armor = weapon.armor + armor.armor + rings.armor;
                // 7. Send the player into battle
                const victor = this.battle.simulate();
                // 8. Did he win?
                if (victor.name === this.player.name) {
                  bestCost = totalCost;
                  // eslint-disable-next-line no-console
                  // console.log(`New best cost of ${bestCost}: w:${weapon.name}, a:${armor.name}, r:${rings.name}, hp=${victor.hitPoints}`);
                }
              }
            }
          }
        }
      }
    }
    // 9. Return the best cost
    return bestCost;
  }

  findCostliestDefeat() {
    // 1. Start with a known to bee too low
    let bestCost = -1;
    // 2. Get the keys to the weapons, armor, and rings
    const allKeys = this.shop.shopKeys();
    // 3. Loop for all of the weapons
    for (let windex = 0; windex < allKeys.weapons.length; windex += 1) {
      const wname = allKeys.weapons[windex];
      const weapon = this.shop.weapons[wname];
      // eslint-disable-next-line no-console
      // console.log(`weapon: ${wname} cost = ${weapon.cost} ${typeof weapon.cost}`);
      // 4. Loop for all armor choices (including no armor)
      for (let aindex = 0; aindex < allKeys.xarmor.length; aindex += 1) {
        const aname = allKeys.xarmor[aindex];
        const armor = this.shop.xarmor[aname];
        // eslint-disable-next-line no-console
        // console.log(`armor: ${aname} cost = ${armor.cost}`);
        // 5. Loop for all the ring choices (include none, one, or two)
        for (let rindex = 0; rindex < allKeys.xrings.length; rindex += 1) {
          const rname = allKeys.xrings[rindex];
          const rings = this.shop.xrings[rname];
          // eslint-disable-next-line no-console
          // console.log(`rings: ${rname} cost = ${rings.cost}`);
          const totalCost = weapon.cost + armor.cost + rings.cost;
          if (totalCost > bestCost) {
            // 6. Set the damage and armor attributes of the player
            this.player.damage = weapon.damage + armor.damage + rings.damage;
            this.player.armor = weapon.armor + armor.armor + rings.armor;
            // 7. Send the player into battle
            const victor = this.battle.simulate();
            // 8. Did he win and was it cheaper?
            if (victor.name !== this.player.name) {
              bestCost = totalCost;
              // eslint-disable-next-line no-console
              console.log(`New higher cost of ${bestCost}: w:${weapon.name}, a:${armor.name}, r:${rings.name}, hp=${victor.hitPoints}`);
            }
          }
        }
      }
    }
    // 9. Return the best cost
    return bestCost;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.findCheapestVictory();
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.findCostliestDefeat();
  }
}

module.exports.RPGSim = RPGSim;
// ======================================================================
// end                        r p g s i m . j s                       end
// ======================================================================
