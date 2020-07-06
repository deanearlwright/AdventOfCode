// ======================================================================
// Radioisotope Thermoelectric Generators
//   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           e l e v a t o r . t s
//
// A solver for the Advent of Code 2016 Day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

type ItemType = 'generator' | 'microchip';
type Item = { element: string, itype: ItemType };
type Items = Item[];
type State = { elevator: number, floors: Items[] };
type MoveType = 'up' | 'down';
type Move = { elevator: MoveType, items: Items };

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const floorWords = ['first', 'second', 'third', 'forth', 'fifth',
  'sixth', 'seventh', 'eighth', 'ninth', 'tenth'];

// ======================================================================
//                                                               Elevator
// ======================================================================

export class Elevator {
  // Object for Radioisotope Thermoelectric Generators
  text: string[];

  part2: boolean;

  state: State;

  constructor(text: string[], part2 = false) {
    // Create a Elevator object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.state = { elevator: 0, floors: [] };

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with an empty state
    this.state = { elevator: 0, floors: [] };
    // 2. Loop for all of the lines of input
    this.text.forEach((line) => {
      // 3. Break the line up into words
      const words = line.split(' ');
      // 4. Handle the elevator line
      if (words[1] === 'elevator') {
        this.state.elevator = floorWords.indexOf(words[5]);
      } else {
        // 5. Handle floor lines
        this.state.floors.push(Elevator.processFloor(words));
      }
    });
  }

  static processFloor(words: string[]): Items {
    // 1. Start with an empty floor
    const floor: Items = [];
    // 2. Loop for the items on the floor
    let index = words.indexOf('contains') + 1;
    while (index > 0 && index < words.length - 1) {
      let element = words[index];
      let microGen = words[index + 1];
      switch (element) {
        case 'nothing':
          index += 2;
          break;
        case 'and':
          index += 2;
          break;
        case 'a':
          index += 1;
          break;
        default:
          // 6. Get the Item
          if (element.indexOf('-') > -1) {
            [element] = element.split('-');
          }
          if (microGen.endsWith(',')) {
            microGen = microGen.substring(0, microGen.length - 1);
          }
          if (microGen.endsWith('.')) {
            microGen = microGen.substring(0, microGen.length - 1);
          }
          // 7. Save it
          floor.push({ element, itype: <ItemType>microGen });
          index += 2;
          break;
      }
    }
    return floor;
  }

  outputState(): void {
    // 1. Loop for each floor
    for (let floor = 0; floor < this.state.floors.length; floor += 1) {
      // 2. Output the items on this floor
      this.outputFloor(floor);
    }
    // 3. Output the locations of the elevator
    console.log(`The elevator is on the ${floorWords[this.state.elevator]} floor.`);
  }

  outputFloor(floor: number): void {
    const items = this.state.floors[floor];
    if (items.length === 0) {
      console.log(`The ${floorWords[floor]} floor contains nothing relevant.`);
    } else if (items.length === 1) {
      console.log(`The ${floorWords[floor]} floor contains ${Elevator.formatItem(items[0])}.`);
    } else if (items.length === 2) {
      console.log(`The ${floorWords[floor]} floor contains ${Elevator.formatItem(items[0])} and ${Elevator.formatItem(items[1])}.`);
    } else {
      let outItems = Elevator.formatItem(items[0]);
      for (let index = 1; index < items.length - 1; index += 1) {
        outItems += `, ${Elevator.formatItem(items[index])}`;
      }
      outItems += ` and ${Elevator.formatItem(items[items.length - 1])}`;
      console.log(`The ${floorWords[floor]} floor contains ${outItems}.`);
    }
  }

  static formatItem(item: Item): string {
    if (item.itype === 'generator') {
      return `a ${item.element} generator`;
    }
    return `a ${item.element}-compatible microchip`;
  }

  validateMove(move: Move): boolean {
    if (!this.validateElevator(move)) return false;
    if (!this.validateFrom(move)) return false;
    return this.validateTo(move);
  }

  validateElevator(move: Move): boolean {
    // 1. Not valid if elevator not on a valid flooe
    if (this.state.elevator < 0 || this.state.elevator >= this.state.floors.length) return false;
    // 2. Not valid to go down from the lowest floow
    if (this.state.elevator === 0 && move.elevator === <MoveType>'down') return false;
    // 3. Not valid to go up from the highest floor
    if (this.state.elevator === this.state.floors.length - 1 && move.elevator === <MoveType>'up') return false;
    // 4. Not valid if carrying nothing or more than two things
    if (move.items.length === 0 || move.items.length > 2) return false;
    // 5. Not valid if carrying an mismatch generator and microchip
    if (move.items.length === 2 && move.items[0].element !== move.items[1].element
      && move.items[0].itype === <ItemType>'generator' && move.items[1].itype === <ItemType>'microchip') return false;
    if (move.items.length === 2 && move.items[0].element !== move.items[1].element
      && move.items[0].itype === <ItemType>'microchip' && move.items[1].itype === <ItemType>'generator') return false;
    // 6. The items must come the current floor
    const floorItems = this.state.floors[this.state.elevator];
    if (Elevator.indexOfItem(floorItems, move.items[0]) === -1) return false;
    if (move.items.length === 2
      && Elevator.indexOfItem(floorItems, move.items[1]) === -1) return false;
    // 7. Looks good to me
    return true;
  }

  moveToFloor(move: Move): number {
    if (move.elevator === <MoveType>'up') {
      return this.state.elevator + 1;
    }
    return this.state.elevator - 1;
  }

  validateFrom(move: Move): boolean {
    if (this.state.elevator < 0) return false;
    if (move.items.length === 0) return false;
    return true;
  }

  validateTo(move: Move): boolean {
    if (this.state.elevator < 0) return false;
    if (move.items.length === 0) return false;
    return true;
  }

  executeMove(move: Move): boolean {
    // 1. Remove the item(s) are on floor with the elevator
    if (!this.removeItem(this.state.elevator, move.items[0])) {
      console.log(`Failed remove item for ${move.items[0].element} ${move.items[0].itype} on floor ${this.state.elevator}`);
      return false;
    }
    if (move.items.length === 2
      && !this.removeItem(this.state.elevator, move.items[1])) {
      console.log(`Failed remove item for ${move.items[1].element} ${move.items[1].itype} on floor ${this.state.elevator}`);
      return false;
    }
    // 2. Move the elevator
    this.state.elevator += move.elevator === 'up' ? 1 : -1;
    // 3. Add the item(s) the elevator's new floor
    this.state.floors[this.state.elevator].push(move.items[0]);
    if (move.items.length === 2) this.state.floors[this.state.elevator].push(move.items[1]);
    // 4. Return success
    return true;
  }

  removeItem(floor: number, item: Item): boolean {
    // 1. Locate the item on the floor
    const index = Elevator.indexOfItem(this.state.floors[floor], item);
    if (index >= 0) {
      this.state.floors[floor].splice(index, 1);
      return true;
    }
    return false;
  }

  static indexOfItem(items: Items, item: Item): number {
    for (let index = 0; index < items.length; index += 1) {
      if (items[index].element === item.element
        && items[index].itype === item.itype) {
        return index;
      }
    }
    return -1;
  }

  static getMicrochips(items: Items): Items {
    // 1. Start with nothing
    const result: Items = [];
    // Loop for all of the items
    items.forEach((item) => {
      if (item.itype === 'microchip') {
        result.push(item);
      }
    });
    return result;
  }

  static getGenerators(items: Items): Items {
    // 1. Start with nothing
    const result: Items = [];
    // Loop for all of the items
    items.forEach((item) => {
      if (item.itype === 'generator') {
        result.push(item);
      }
    });
    return result;
  }

  static getUnpairMicrochips(items: Items): Items {
    const microchips = Elevator.getMicrochips(items);
    const generators = Elevator.getGenerators(items);
    const result: Items = [];
    microchips.forEach((chip) => {
      let matched = false;
      for (let index = 0; index < generators.length; index += 1) {
        if (generators[index].element === chip.element) {
          matched = true;
          break;
        }
        if (!matched) result.push(chip);
      }
    });
    return result;
  }

  static getPairs(items: Items): Items {
    const microchips = Elevator.getMicrochips(items);
    const generators = Elevator.getGenerators(items);
    const result: Items = [];
    microchips.forEach((chip) => {
      for (let index = 0; index < generators.length; index += 1) {
        if (generators[index].element === chip.element) {
          result.push(chip);
          result.push(generators[index]);
          break;
        }
      }
    });
    return result;
  }

  static getElements(items: Items, element: string): Items {
    // 1. Start with nothing
    const result: Items = [];
    // Loop for all of the items
    items.forEach((item) => {
      if (item.element === element) {
        result.push(item);
      }
    });
    return result;
  }

  static hasOther(items: Items, onePart: Item): boolean {
    // 1. Determine the other type
    let otherType = 'generator';
    if (onePart.itype === otherType) otherType = 'microchip';
    return Elevator.indexOfItem(items,
      { element: onePart.element, itype: <ItemType>otherType }) !== -1;
  }

  static isPair(items: Items): boolean {
    if (items.length !== 2) return false;
    if (items[0].element !== items[1].element) return false;
    if (items[0].itype === items[1].itype) return false;
    return true;
  }

  whatSingleItemsCanMoveOffFloor(floor: number): Items {
    // Determine which single items leaving won't screw whats left behind
    // 1. Start with nothing
    const result: Items = [];
    // 2. Get the items currently on the floor
    const items = this.state.floors[floor];
    // 3. Loop for all of the items
    items.forEach((item) => {
      // 4. If a micro chip was safe on the floor, it is save to move it
      if (item.itype === 'microchip') {
        result.push(item);
      } else {
        // 5. Generator can be moved if (a) its paired microchip is not on the floor
        //    or the paired microchip is the only other thing on the floor
      }
    });
    // 9. Return the items that can safely be moved by themselves
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return NaN;
    }
    return NaN;
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                      e l e v a t o r . t s                     end
// ======================================================================
