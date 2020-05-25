/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p l a y e r . j s
//
// A solver for the Advent of Code 2015 Day 21 problem
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
  // Player object for RPG Simulator 20XX

  constructor(options) {
    // Create a Player object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.name = options.name === undefined ? null : options.name;
    this.initialHitPoints = null;
    this.hitPoints = 0;
    this.damage = 0;
    this.armor = 0;

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.hp = 0;
    this.damage = 0;
    this.armor = 0;
    // 2. Loop for all line of the text
    text.forEach((line) => {
      // 3. Save section name if this is a section line?
      const [what, value] = line.split(':');
      const intValue = parseInt(value, 10);
      switch (what) {
        case 'Hit Points':
          this.hitPoints = intValue;
          this.initialHitPoints = intValue;
          break;
        case 'Damage':
          this.damage = intValue;
          break;
        case 'Armor':
          this.armor = intValue;
          break;
        default:
          // eslint-disable-next-line no-console
          console.log(`Unkown type for ${line}`);
      }
    });
  }

  reset() {
    this.hitPoints = this.initialHitPoints;
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
