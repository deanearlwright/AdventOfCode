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
type ElementType = 'thulium' | 'plutonium' | 'strontium' | 'promethium' | 'ruthenium' | 'hydrogen' | 'lithium' | 'elerium' | 'dilithium';
type Item = { element: ElementType, itype: ItemType };
type Items = Item[];
type Floor = Items;
type Floors = Floor[];
type State = {
  elevator: number,
  floors: Floors,
  moves: Moves,
  steps: number,
  previous: number,
};
type States = State[];
type Dir = 'up' | 'down';
type Dirs = Dir[];
type Move = { elevator: Dir, items: Items };
type Moves = Move[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const floorWords = ['first', 'second', 'third', 'forth', 'fifth',
  'sixth', 'seventh', 'eighth', 'ninth', 'tenth'];

const itypeLetters = ['G', 'M'];
const itypeNames = ['generator', 'microchip'];
const elementLetters = ['H', 'L', 'T', 'P', 'S', 'M', 'R', 'E', 'D'];
const elementNames = ['hydrogen', 'lithium', 'thulium', 'plutonium',
  'strontium', 'promethium', 'ruthenium', 'elerium', 'dilithium'];

const initialState: State = {
  elevator: 0,
  floors: [],
  moves: [],
  steps: 0,
  previous: NaN,
};

// ======================================================================
//                                                               Elevator
// ======================================================================

export class Elevator {
  // Object for Radioisotope Thermoelectric Generators
  text: string[];

  part2: boolean;

  topFloor: number;

  state: State;

  states: States;

  constructor(text: string[], part2 = false) {
    // Create a Elevator object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.topFloor = 0;
    this.state = JSON.parse(JSON.stringify(initialState));
    this.states = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      if (part2) {
        this.text[0] += ' an elerium generator, an elerium-compatible microchip, a dilithium generator and a dilithium-compatible microchip.';
      }
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with an empty state
    this.topFloor = 0;
    this.setCurrentState(initialState);
    this.states = [];
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
    this.topFloor = this.state.floors.length - 1;
    // 5. Save the possible moves
    this.setStateMoves();
    // 6. And this is the first state in the chain
    this.saveCurrentState();
  }

  setStateMoves(): void {
    // 1. Start with nothing
    this.state.moves = [];
    // 2. Get movable items
    const moveable = this.getMovableItems();
    // 3. Get elevator directions
    const directions = this.getDirections();
    // 4. Add the moves
    moveable.forEach((items) => {
      directions.forEach((elevator) => {
        const move: Move = { elevator, items };
        if (this.validateMove(move)) {
          this.state.moves.push(move);
        }
      });
    });
  }

  setCurrentState(state: State): void {
    this.state = JSON.parse(JSON.stringify(state));
  }

  saveCurrentState(): void {
    this.states.push(JSON.parse(JSON.stringify(this.state)));
  }

  getMovableItems(): Items[] {
    // 1. Start with nothing
    const result: Items[] = [];
    // 2. Get the chips and generators on this floor
    const [microchips, generators] = this.getFloorItems(this.state.elevator);
    // 3. Add single items
    microchips.forEach((item) => {
      result.push([item]);
    });
    generators.forEach((item) => {
      result.push([item]);
    });
    // 4. Add microchips in pairs and generators in pairs
    if (microchips.length > 1) {
      for (let index1 = 0; index1 < microchips.length - 1; index1 += 1) {
        for (let index2 = index1 + 1; index2 < microchips.length; index2 += 1) {
          result.push([microchips[index1], microchips[index2]]);
        }
      }
    }
    if (generators.length > 1) {
      for (let index1 = 0; index1 < generators.length - 1; index1 += 1) {
        for (let index2 = index1 + 1; index2 < generators.length; index2 += 1) {
          result.push([generators[index1], generators[index2]]);
        }
      }
    }
    // 5. Add matched microchips and generators
    microchips.forEach((item) => {
      const generator: Item = { element: item.element, itype: 'generator' };
      if (Elevator.indexOfItem(generators, generator) >= 0) {
        result.push([item, generator]);
      }
    });
    // 6. Return the items
    return result;
  }

  getDirections(): Dirs {
    const result: Dirs = [];
    if (this.state.elevator > 0) {
      result.push(<Dir>'down');
    }
    if (this.state.elevator < this.topFloor) {
      result.push(<Dir>'up');
    }
    return result;
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
        case 'an':
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
          floor.push({
            element: <ElementType>element,
            itype: <ItemType>microGen,
          });
          index += 2;
          break;
      }
    }
    return floor;
  }

  outputDiagram(): string {
    const result = [];
    // 1. Loop for each floor starting at the top
    for (let floor = this.topFloor; floor >= 0; floor -= 1) {
      // 2. Output the items on this floor
      result.push(this.diagramFloor(floor));
    }
    // 3. Return the state as a string
    return result.join('\n');
  }

  diagramFloor(floor: number): string {
    // 1. Get the items on the floor
    const items = this.state.floors[floor];
    // 2. Start with the floor number and Elevator indicator
    const result = [`F${floor}`];
    result.push(floor === this.state.elevator ? 'E' : '.');
    // 3. Loop for all of the elements and items types
    for (let eindex = 0; eindex < elementNames.length; eindex += 1) {
      for (let index = 0; index < itypeNames.length; index += 1) {
        // 4. If that item is on the floor, output its initials otherwise a period
        const item: Item = {
          element: <ElementType>elementNames[eindex],
          itype: <ItemType>itypeNames[index],
        };
        if (Elevator.indexOfItem(items, item) >= 0) {
          result.push(`${elementLetters[eindex]}${itypeLetters[index]}`);
        } else {
          result.push('. ');
        }
      }
    }
    // 5. Return the floor diagram as a string
    return result.join(' ');
  }

  outputState(): string {
    const result = [];
    // 1. Loop for each floor
    for (let floor = 0; floor < this.state.floors.length; floor += 1) {
      // 2. Output the items on this floor
      result.push(this.outputFloor(floor));
    }
    // 3. Output the locations of the elevator
    result.push(`The elevator is on the ${floorWords[this.state.elevator]} floor.`);
    // 4. Return the state as a string
    return result.join('\n');
  }

  outputFloor(floor: number): string {
    const items = this.state.floors[floor];
    if (items.length === 0) {
      return `The ${floorWords[floor]} floor contains nothing relevant.`;
    }
    if (items.length === 1) {
      return `The ${floorWords[floor]} floor contains ${Elevator.formatItem(items[0])}.`;
    }
    if (items.length === 2) {
      return `The ${floorWords[floor]} floor contains ${Elevator.formatItem(items[0])} and ${Elevator.formatItem(items[1])}.`;
    }
    let outItems = Elevator.formatItem(items[0]);
    for (let index = 1; index < items.length - 1; index += 1) {
      outItems += `, ${Elevator.formatItem(items[index])}`;
    }
    outItems += ` and ${Elevator.formatItem(items[items.length - 1])}`;
    return `The ${floorWords[floor]} floor contains ${outItems}.`;
  }

  static formatItem(item: Item): string {
    if (item.itype === 'generator') {
      return `a ${item.element} generator`;
    }
    return `a ${item.element}-compatible microchip`;
  }

  endState(): boolean {
    for (let floor = 0; floor < this.topFloor; floor += 1) {
      if (this.state.floors[floor].length > 0) {
        return false;
      }
    }
    return true;
  }

  validateMove(move: Move): boolean {
    if (!this.validateElevator(move)) return false;
    if (!this.validateFrom(move)) return false;
    return this.validateTo(move);
  }

  validateElevator(move: Move): boolean {
    // 1. Not valid if elevator not on a valid flooe
    if (this.state.elevator < 0 || this.state.elevator > this.topFloor) return false;
    // 2. Not valid to go down from the lowest floow
    if (this.state.elevator === 0 && move.elevator === <Dir>'down') return false;
    // 3. Not valid to go up from the highest floor
    if (this.state.elevator === this.topFloor && move.elevator === <Dir>'up') return false;
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
    if (move.elevator === <Dir>'up') {
      return this.state.elevator + 1;
    }
    return this.state.elevator - 1;
  }

  validateFrom(move: Move): boolean {
    // 0. You can assume that the Elevator check has been done
    if (this.state.elevator < 0) return false;
    if (move.items.length === 0) return false;
    // 1. If removing a matched pair, all is well
    if (move.items.length === 2 && move.items[0].element === move.items[1].element) return true;
    // 2. Get the items from the floor
    const [microchips, generators] = this.getFloorItems(this.state.elevator);
    // 3. Remove item(s) in elevator
    move.items.forEach((item) => {
      if (item.itype === <ItemType>'generator') {
        const index = Elevator.indexOfItem(generators, item);
        generators.splice(index, 1);
      } else {
        const index = Elevator.indexOfItem(microchips, item);
        microchips.splice(index, 1);
      }
    });
    // 4. Checkout the remaining items
    return Elevator.checkItems(microchips, generators);
  }

  validateTo(move: Move): boolean {
    // 0. You can assume that the Elevator check has been done
    if (this.state.elevator < 0) return false;
    if (move.items.length === 0) return false;
    // 2. Get the items from the floor
    const [microchips, generators] = this.getFloorItems(this.moveToFloor(move));
    // 3. Add item(s) in elevator
    move.items.forEach((item) => {
      if (item.itype === <ItemType>'generator') {
        generators.push(item);
      } else {
        microchips.push(item);
      }
    });
    // 4. Checkout the combined items
    return Elevator.checkItems(microchips, generators);
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
    // 4. Increment the number of moves
    this.state.steps += 1;
    // 5. Return success
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
      if (item.itype === <ItemType>'microchip') {
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
      if (item.itype === <ItemType>'generator') {
        result.push(item);
      }
    });
    return result;
  }

  checkAllFloors(): boolean {
    // 1. Loop for all the floors
    for (let floor = 0; floor < this.state.floors.length; floor += 1) {
      // 2. Checkout the floor, and exit it we find a bad one
      if (!this.checkFloor(floor)) return false;
    }
    // 3. All the floors look good
    return true;
  }

  checkFloor(floor: number): boolean {
    // 1. Get the items on the floor
    const microchips = Elevator.getMicrochips(this.state.floors[floor]);
    const generators = Elevator.getGenerators(this.state.floors[floor]);
    // 2. Check the items
    return Elevator.checkItems(microchips, generators);
  }

  getFloorItems(floor: number): Items[] {
    // 1. Start with nothing
    const items: Items[] = [];
    // 2. Get microchips and generators
    items[0] = Elevator.getMicrochips(this.state.floors[floor]);
    items[1] = Elevator.getGenerators(this.state.floors[floor]);
    // 3. Return the microchips and generators
    return items;
  }

  static checkItems(microchips: Items, generators: Items): boolean {
    // 1. All is well if there are no generators or no microchips
    if (microchips.length === 0) return true;
    if (generators.length === 0) return true;
    // 2. Check that all microchips have matching generator
    let allPaired = true;
    microchips.forEach((chip) => {
      let paired = false;
      for (let gen = 0; gen < generators.length; gen += 1) {
        if (chip.element === generators[gen].element) {
          paired = true;
          break;
        }
      }
      allPaired = allPaired && paired;
    });
    // 3. Return the pairing results
    return allPaired;
  }

  minSteps(verbose = false, limit = 0): number {
    if (verbose) console.log(`minSteps: ${limit}`);
    // 1. Start with a long way to go
    let result = NaN;
    let lstate = 0;
    let kntMoves = 0;
    // 2. Loop until there are no more viable potential moves (or taking to long)
    while (!Number.isNaN(lstate)) {
      kntMoves += 1;
      if (limit !== 0 && kntMoves > limit) {
        console.log(`minSteps reached ${kntMoves} moves`);
        return result;
      }
      // 3. Get the next state with moves
      lstate = this.lowestStateWithMove(lstate, result);
      if (Number.isNaN(lstate)) {
        break;
      }
      // 4. Make the first move from this state the current state
      const move = this.states[lstate].moves.shift();
      this.setCurrentState(this.states[lstate]);
      if (!this.executeMove(<Move>move)) {
        console.log(`Unable to execute move ${JSON.stringify(move)} on state[${lstate} ${JSON.stringify(this.state)}]`);
        return NaN;
      }
      this.state.previous = lstate;
      // 5. If this is a terminal state, checked the steps
      if (this.endState()) {
        if (Number.isNaN(result) || this.state.steps < result) {
          result = this.state.steps;
          if (verbose) console.log(`State ${lstate} move=${JSON.stringify(move)} steps=${result}`);
        }
      }
      // 6. Check if this is a new state
      if (this.findPreviousState() < 0) {
        // 7. Determine the moves from this state
        this.setStateMoves();
        // 8. Save the new state
        this.saveCurrentState();
      }
    }
    // 9. Return the best number of steps we found
    return result;
  }

  findPreviousState(): number {
    // 1. Loop for all of the previous states
    for (let index = 0; index < this.states.length; index += 1) {
      // 2. Does the current state match this older one
      if (Elevator.doStatesMatch(this.state, this.states[index])) {
        // 3. Allow matching states only if the new one has fewer steps
        if (this.state.steps >= this.states[index].steps) {
          return index;
        }
        // 4. Now longer interested in older, slower state
        this.states[index].moves = [];
      }
    }
    return -1;
  }

  static doStatesMatch(state1: State, state2: State): boolean {
    // 1. Check the elevator position
    if (state1.elevator !== state2.elevator) return false;
    // 2. Check each floor
    if (state1.floors.length !== state2.floors.length) return false;
    for (let index = 0; index < state1.floors.length; index += 1) {
      if (!Elevator.doFloorsMatch(state1.floors[index], state2.floors[index])) return false;
    }
    // 3. Looks good to me
    return true;
  }

  static doFloorsMatch(floor1: Items, floor2: Items): boolean {
    // 1. Check the number of items
    if (floor1.length !== floor2.length) return false;
    // 2. Check generators
    const gen1 = Elevator.getGenerators(floor1);
    const gen2 = Elevator.getGenerators(floor2);
    if (gen1.length !== gen2.length) return false;
    // 2. Check microchips
    const mc1 = Elevator.getMicrochips(floor1);
    const mc2 = Elevator.getMicrochips(floor2);
    if (mc1.length !== mc2.length) return false;
    // 3. Looks good to me
    return true;
  }

  lowestStateWithMove(previous: number, steps: number): number {
    // 1. Loop for all the states from the last one used going forward
    for (let result = previous; result < this.states.length; result += 1) {
      // 2. If this one has an uncheck move, explore it
      if (this.states[result].moves.length > 0) {
        // 3. If it has a chance of bettering the current best path
        if (Number.isNaN(steps) || this.states[result].steps <= steps) {
          return result;
        }
      }
    }
    // 4. Everything has been explored or takes too long
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    console.log(this.outputDiagram());
    if (this.part2) {
      return this.minSteps(verbose, limit);
    }
    return this.minSteps(verbose, limit);
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
