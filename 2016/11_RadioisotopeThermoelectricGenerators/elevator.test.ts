// ======================================================================
// Radioisotope Thermoelectric Generators
//   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      e l e v a t o r . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 11 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_11';
import { Elevator } from './elevator';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
interface ExampleTests {
  text: string;
  result: number;
}
interface CheckAllFloorsTests {
  text: string;
  result: boolean;
  microchips: number;
  generators: number;
}

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
The elevator is on the first floor.
`;

const CHECK_ALL_FLOORS: CheckAllFloorsTests[] = [
  {
    text: 'The first floor contains nothing relevant.',
    result: true,
    microchips: 0,
    generators: 0,
  },
  {
    text: 'The first floor contains a hydrogen generator.',
    result: true,
    microchips: 0,
    generators: 1,
  },
  {
    text: 'The first floor contains a hydrogen-compatible microchip.',
    result: true,
    microchips: 1,
    generators: 0,
  },
  {
    text: 'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
    result: true,
    microchips: 2,
    generators: 0,
  },
  {
    text: 'The first floor contains a hydrogen generator and a lithium generator.',
    result: true,
    microchips: 0,
    generators: 2,
  },
  {
    text: 'The first floor contains a hydrogen generator and a hydrogen-compatible microchip.',
    result: true,
    microchips: 1,
    generators: 1,
  },
  {
    text: 'The first floor contains a hydrogen generator and a lithium-compatible microchip.',
    result: false,
    microchips: 1,
    generators: 1,
  },
  {
    text: 'The first floor contains a hydrogen generator, a hydrogen-compatible microchip and a lithium-campatible microchip.',
    result: false,
    microchips: 2,
    generators: 1,
  },
  {
    text: 'The first floor contains a hydrogen generator, a hydrogen-compatible microchip and a lithium generator.',
    result: true,
    microchips: 1,
    generators: 2,
  },
];

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 11;
const PART_TWO_RESULT = 35;

// ======================================================================
//                                                           TestElevator
// ======================================================================

describe('Elevator', () => {
  test('Test the default Elevator creation', () => {
    // 1. Create default Elevator object
    const myobj = new Elevator([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.state.steps).toBe(0);
    expect(myobj.state.elevator).toBe(0);
    expect(myobj.checkAllFloors()).toBe(true);
    expect(myobj.states).toHaveLength(0);
  });

  test('Test the Elevator object creation from text', () => {
    // 1. Create Elevator object from text
    const myobj = new Elevator(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(5);
    expect(myobj.state.steps).toBe(0);
    expect(myobj.state.elevator).toBe(0);
    expect(myobj.state.floors).toHaveLength(4);
    expect(myobj.state.floors[0]).toHaveLength(2);
    expect(myobj.state.floors[1]).toHaveLength(1);
    expect(myobj.state.floors[2]).toHaveLength(1);
    expect(myobj.state.floors[3]).toHaveLength(0);
    expect(myobj.state.floors[0][0]).toStrictEqual({ element: 'hydrogen', itype: 'microchip' });
    expect(myobj.state.floors[0][1]).toStrictEqual({ element: 'lithium', itype: 'microchip' });
    expect(myobj.state.floors[1][0]).toStrictEqual({ element: 'hydrogen', itype: 'generator' });
    expect(myobj.state.floors[2][0]).toStrictEqual({ element: 'lithium', itype: 'generator' });
    expect(myobj.topFloor).toBe(3);
    expect(myobj.checkAllFloors()).toBe(true);
    expect(myobj.getDirections()).toStrictEqual(['up']);
    expect(myobj.getMovableItems()).toStrictEqual(
      [[{ element: 'hydrogen', itype: 'microchip' }],
        [{ element: 'lithium', itype: 'microchip' }],
        [{ element: 'hydrogen', itype: 'microchip' }, { element: 'lithium', itype: 'microchip' }]],
    );
    expect(myobj.state.moves).toStrictEqual(
      [{ elevator: 'up', items: [{ element: 'hydrogen', itype: 'microchip' }] }],
    );
    expect(myobj.states).toHaveLength(1);
    expect(myobj.states[0].steps).toBe(0);
    expect(myobj.states[0].elevator).toBe(0);
    expect(myobj.states[0].floors).toHaveLength(4);
    expect(myobj.states[0].floors[0]).toHaveLength(2);
    expect(myobj.states[0].floors[1]).toHaveLength(1);
    expect(myobj.states[0].floors[2]).toHaveLength(1);
    expect(myobj.states[0].floors[3]).toHaveLength(0);
    expect(myobj.states[0].floors[0][0]).toStrictEqual({ element: 'hydrogen', itype: 'microchip' });
    expect(myobj.states[0].floors[0][1]).toStrictEqual({ element: 'lithium', itype: 'microchip' });
    expect(myobj.states[0].floors[1][0]).toStrictEqual({ element: 'hydrogen', itype: 'generator' });
    expect(myobj.states[0].floors[2][0]).toStrictEqual({ element: 'lithium', itype: 'generator' });
    expect(myobj.lowestStateWithMove(0, NaN)).toBe(0);
    // 3. Let's try following the example
    // 3.1 Bring the Hydrogen-compatible Microchip to the second floor, which is
    //     safe because it can get power from the Hydrogen Generator
    expect(myobj.getDirections()).toStrictEqual(['up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [{ element: 'hydrogen', itype: 'microchip' }],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [{
        element: 'hydrogen',
        itype: 'microchip',
      }],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.2 Bring both Hydrogen-related items to the third floor, which is safe
    //     because the Hydrogen-compatible microchip is getting power from its generator
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'hydrogen', itype: 'generator' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'hydrogen', itype: 'generator' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.3 Leave the Hydrogen Generator on floor three, but bring the Hydrogen-
    //     compatible Microchip back down with you so you can still use the elevator
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'down',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'down',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.4 At the first floor, grab the Lithium-compatible Microchip, which is
    //    safe because Microchips don't affect each other
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'down',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'down',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    expect(myobj.state.elevator).toBe(0);
    // 3.5 Bring both Microchips up one floor, where there is nothing to fry them
    expect(myobj.getDirections()).toStrictEqual(['up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.6 Bring both Microchips up again to floor three, where they can be
    //     temporarily connected to their corresponding generators while the
    //     elevator recharges, preventing either of them from being fried
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.7 Bring both Microchips to the fourth floor
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    expect(myobj.state.elevator).toBe(3);
    // 3.8 Leave the Lithium-compatible microchip on the fourth floor, but bring
    //     the Hydrogen-compatible one so you can still use the elevator; this is
    //     safe because although the Lithium Generator is on the destination
    //     floor, you can connect Hydrogen-compatible microchip to the Hydrogen
    //     Generator there
    expect(myobj.getDirections()).toStrictEqual(['down']);
    expect(myobj.validateMove({
      elevator: 'down',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'down',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.9 Bring both Generators up to the fourth floor, which is safe because
    //     you can connect the Lithium-compatible Microchip to the Lithium
    //     Generator upon arrival
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'generator' },
        { element: 'lithium', itype: 'generator' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'generator' },
        { element: 'lithium', itype: 'generator' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    expect(myobj.state.elevator).toBe(3);
    // 3.10 Bring the Lithium Microchip with you to the third floor so you can use
    //      the elevator
    expect(myobj.getDirections()).toStrictEqual(['down']);
    expect(myobj.validateMove({
      elevator: 'down',
      items: [
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'down',
      items: [
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 3.11 Bring both Microchips to the fourth floor
    expect(myobj.getDirections()).toStrictEqual(['down', 'up']);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.executeMove({
      elevator: 'up',
      items: [
        { element: 'hydrogen', itype: 'microchip' },
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.checkAllFloors()).toBe(true);
    // 4. And that is all
    expect(myobj.endState()).toBe(true);
    expect(myobj.state.steps).toBe(11);
    // 5. Try to do something stupid
    expect(myobj.getDirections()).toStrictEqual(['down']);
    expect(myobj.validateTo({
      elevator: 'down',
      items: [
        { element: 'lithium', itype: 'generator' },
      ],
    })).toBe(true);
    expect(myobj.validateFrom({
      elevator: 'down',
      items: [
        { element: 'lithium', itype: 'generator' },
      ],
    })).toBe(false);
    expect(myobj.validateMove({
      elevator: 'down',
      items: [
        { element: 'lithium', itype: 'generator' },
      ],
    })).toBe(false);
    expect(myobj.validateMove({
      elevator: 'down',
      items: [
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(true);
    expect(myobj.validateMove({
      elevator: 'up',
      items: [
        { element: 'lithium', itype: 'microchip' },
      ],
    })).toBe(false);
  });

  test('Test checkAllFloors examples', () => {
    // 1. Loop for all of the examples
    CHECK_ALL_FLOORS.forEach((test) => {
      // 2. Create Elevator object
      const myobj = new Elevator(fromText(`\n${test.text}`));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // console.log(myobj.text);
      expect(myobj.state.floors).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(Elevator.getMicrochips(myobj.state.floors[0])).toHaveLength(test.microchips);
      expect(Elevator.getGenerators(myobj.state.floors[0])).toHaveLength(test.generators);
      expect(myobj.checkAllFloors()).toBe(test.result);
    });
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Elevator object
      const myobj = new Elevator(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Elevator object using the key as text
      const myobj = new Elevator(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Elevator object', () => {
    // 1. Create Elevator object from text
    const myobj = new Elevator(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 999)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Elevator object', () => {
    // 1. Create Elevator object from text
    const myobj = new Elevator(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 999999)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 e l e v a t o r . t e s t . t s                end
// ======================================================================
