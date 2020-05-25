/* eslint-disable linebreak-style */
// ======================================================================
// RPG Simulator 20XX
//   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           s h o p . j s
//
// A solver for the Advent of Code 2015 Day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const shopText = [
  'Weapons:   Cost  Damage  Armor',
  'Dagger        8     4       0',
  'Shortsword   10     5       0',
  'Warhammer    25     6       0',
  'Longsword    40     7       0',
  'Greataxe     74     8       0',
  '',
  'Armor:      Cost  Damage  Armor',
  'Leather      13     0       1',
  'Chainmail    31     0       2',
  'Splintmail   53     0       3',
  'Bandedmail   75     0       4',
  'Platemail   102     0       5',
  '',
  'Rings:      Cost  Damage  Armor',
  'Damage +1    25     1       0',
  'Damage +2    50     2       0',
  'Damage +3   100     3       0',
  'Defense +1   20     0       1',
  'Defense +2   40     0       2',
  'Defense +3   80     0       3',
];

// ======================================================================
//                                                                   Shop
// ======================================================================

class Shop {
  // Object for RPG Simulator 20XX

  constructor(options) {
    // Create a Shop object

    // 1. Set the initial values
    this.text = options.text === undefined ? shopText : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.weapons = {};
    this.armor = {};
    this.rings = {};
    this.xrings = {};

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.weapons = {};
    this.armor = {};
    this.rings = {};
    this.xrings = {};
    let section = null;
    // 2. Loop for all line of the text
    text.forEach((line) => {
      if (line.trim().length > 0) {
        // 3. Save section name if this is a section line?
        if (line.indexOf(':') !== -1) {
          [section] = line.split(':');
        } else {
          const [name, cost, damage, armor] = line.split(/\s\s+/);
          const item = {
            name,
            cost: parseInt(cost, 10),
            damage: parseInt(damage, 10),
            armor: parseInt(armor, 10),
          };
          switch (section) {
            case 'Weapons':
              this.weapons[name] = item;
              break;
            case 'Armor':
              this.armor[name] = item;
              break;
            case 'Rings':
              this.rings[name] = item;
              break;
            default:
              // eslint-disable-next-line no-console
              console.log(`Unkown type for ${name}`);
          }
        }
      }
    });
    this.expandItems();
  }

  expandItems() {
    // 1. Empty item
    const nothing = {
      name: 'none',
      cost: 0,
      damage: 0,
      armor: 0,
    };
    // 2. Add it to armor and rings (have to buy a weapon)
    this.xarmor = { ...this.armor };
    this.xarmor.nothing = nothing;
    this.xrings = { ...this.rings };
    this.xrings.nothing = nothing;
    // 3. Loop for all of the rings
    const ringKeys = Object.keys(this.rings);
    for (let i = 0; i < ringKeys.length; i += 1) {
      // 4. Loop for the remaining rings
      for (let j = i + 1; j < ringKeys.length; j += 1) {
        // 5. Combine the names and attributes
        const newRing = this.combineRings(ringKeys[i], ringKeys[j]);
        // 6. Add it to the extended rings
        this.xrings[newRing.name] = newRing;
      }
    }
  }

  combineRings(ring1, ring2) {
    // 1. Combine attributes
    const cost = this.rings[ring1].cost + this.rings[ring2].cost;
    const damage = this.rings[ring1].damage + this.rings[ring2].damage;
    const armor = this.rings[ring1].armor + this.rings[ring2].armor;
    // 2. Construct a name from the attributes
    const name = `rings d${damage} a${armor}`;
    // 3. Return combined rings
    return {
      name,
      cost,
      damage,
      armor,
    };
  }

  shopKeys() {
    // 1. Start with nothing
    const result = {};
    // 2. Add weapon keys
    result.weapons = Object.keys(this.weapons);
    // 3. and armor keys
    result.armor = Object.keys(this.armor);
    result.xarmor = Object.keys(this.xarmor);
    // 4. and lastly ring and expanded rings keys
    result.rings = Object.keys(this.rings);
    result.xrings = Object.keys(this.xrings);
    // 5. Return all those keys
    return result;
  }
}

module.exports.Shop = Shop;
// ======================================================================
// end                          s h o p . j s                         end
// ======================================================================
