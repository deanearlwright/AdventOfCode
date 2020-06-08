/* eslint-disable linebreak-style */
// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s p e l l s . j s
//
// The wizard spells for the Advent of Code 2015 Day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

const spellText = [
  'Spell:       Cost  Damage  Health  Armor  Mana  Turns',
  'MagicMissle    53     4         0      0     0      0',
  'Drain          73     2         2      0     0      0',
  'Shield        113     0         0      7     0      6',
  'Poison        173     3         0      0     0      6',
  'Recharge      229     0         0      0   101      5',
];

// ======================================================================
//                                                                 Spells
// ======================================================================

class Spells {
  // Magical Spells for the Wizard Simulator 20XX

  constructor(options) {
    // Create a Spells object, a collection of spells than can be cast

    // 1. Set the initial values
    this.text = options.text === undefined ? spellText : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.book = {};
    this.keys = [];

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.book = {};
    // 2. Loop for all line of the text
    text.forEach((line) => {
      if (line.trim().length > 0) {
        // 3. Save section name if this is a section line?
        if (line.indexOf(':') === -1) {
          const [name, cost, damage, health, armor, mana, turns] = line.split(/\s\s+/);
          const item = {
            name,
            cost: parseInt(cost, 10),
            damage: parseInt(damage, 10),
            health: parseInt(health, 10),
            armor: parseInt(armor, 10),
            mana: parseInt(mana, 10),
            turns: parseInt(turns, 10),
          };
          this.book[name] = item;
        }
      }
    });
    this.keys = Object.keys(this.book);
  }

  cost(spellName) {
    if (spellName in this.book) {
      return this.book[spellName].cost;
    }
    return null;
  }

  execute(player, boss, spellName) {
    // 1. Find the spell name in the spellbook
    if (spellName in this.book) {
      // 2. If the spell does damage to the boss, inflict it
      if (this.book[spellName].damage > 0) {
        boss.defend(this.book[spellName].damage);
      }
      // 3. Execute the player centric effects of the spell
      player.heal(this.book[spellName].health);
      player.protect(this.book[spellName].armor);
      player.recharge(this.book[spellName].mana);
    } else {
      // 4. Unknown spell, this is going to cost the player bigtime
      // eslint-disable-next-line no-console
      console.log(`Unknown spell ${spellName}`);
      player.defend(player.hitPoints + player.armor + 1);
    }
  }

  executeActive(player, boss, active) {
    const result = {};
    // 1. Remove any magic protections the player might have
    player.unprotect();
    // 2. Loop for all of the effects
    Object.keys(active).forEach((spellName) => {
      // 3. Execute the effect
      this.execute(player, boss, spellName);
      // 4. If the effect continues, remember it for next time
      if (active[spellName] > 1) {
        result[spellName] = active[spellName] - 1;
      }
    });
    // 5. Return the continuing spells
    return result;
  }

  next(previous) {
    const index = this.keys.indexOf(previous) + 1;
    if (index < this.keys.length) {
      return this.keys[index];
    }
    return null;
  }
}

module.exports.Spells = Spells;
// ======================================================================
// end                        s p e l l s . j s                       end
// ======================================================================
