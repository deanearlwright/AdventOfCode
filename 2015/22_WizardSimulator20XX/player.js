/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p l a y e r . j s
//
// A player for the Advent of Code 2015 Day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                 Player
// ======================================================================

class Player {
  // Player object for Wizard Simulator 20XX

  constructor(options) {
    // Create a Player object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.name = options.name === undefined ? null : options.name;
    this.hitPoints = options.hitPoints === undefined ? 0 : options.hitPoints;
    this.damage = options.damage === undefined ? 0 : options.damage;
    this.armor = options.armor === undefined ? 0 : options.armor;
    this.mana = options.mana === undefined ? 0 : options.mana;
    this.spent = options.spent === undefined ? 0 : options.spent;
    this.original = options.original === undefined ? null : options.original;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
      this.text = null;
    }

    // 3. Save initial values
    if (this.original === null) {
      this.original = {
        hitPoints: this.hitPoints,
        damage: this.damage,
        armor: this.armor,
        mana: this.mana,
      };
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.hp = 0;
    this.damage = 0;
    this.armor = 0;
    this.mana = 0;
    // 2. Loop for all line of the text
    text.forEach((line) => {
      // 3. Save section name if this is a section line?
      const [what, value] = line.split(':');
      const intValue = parseInt(value, 10);
      switch (what) {
        case 'Hit Points':
          this.hitPoints = intValue;
          break;
        case 'Damage':
          this.damage = intValue;
          break;
        case 'Armor':
          this.armor = intValue;
          break;
        case 'Mana':
          this.mana = intValue;
          break;
        default:
          // eslint-disable-next-line no-console
          console.log(`Unkown type for ${line}`);
      }
    });
  }

  reset() {
    this.hitPoints = this.original.hitPoints;
    this.damage = this.original.damage;
    this.armor = this.original.armor;
    this.mana = this.original.mana;
  }

  heal(points) {
    this.hitPoints += points;
  }

  protect(points) {
    this.armor += points;
  }

  unprotect() {
    this.armor = 0;
  }

  recharge(points) {
    this.mana += points;
  }

  cast(cost) {
    // 1. If we have tha mana for the spell ...
    if (cost < this.mana) {
      // 2. Deduct it from our pool, and record the expenditure
      this.mana -= cost;
      this.spent += cost;
    } else {
      // 3. Else, we were being very naughty and need to be chastised
      this.hitPoints = 0;
    }
  }

  defend(points) {
    let damageTaken = points - this.armor;
    if (damageTaken <= 0) {
      damageTaken = 1;
    }
    this.hitPoints -= damageTaken;
    if (this.hitPoints < 0) {
      this.hitPoints = 0;
    }
  }

  attack(other) {
    other.defend(this.damage);
  }
}

module.exports.Player = Player;
// ======================================================================
// end                       p l a y e r . j s                        end
// ======================================================================
