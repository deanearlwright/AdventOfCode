/* eslint-disable linebreak-style */
// ======================================================================
// Like a GIF For Your Yard
//   Advent of Code 2015 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      l i g h t s . t e s t . j s
//
// Test the solver for Advent of Code 2015 day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const aoc18 = require('./aoc_18');
const lights = require('./lights');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_SIZE = 6;

const EX1L1 = '.#.#.#';
const EX1L2 = '...##.';
const EX1L3 = '#....#';
const EX1L4 = '..#...';
const EX1L5 = '#.#..#';
const EX1L6 = '####..';
const EXAMPLE_TEXT = `${EX1L1}\n${EX1L2}\n${EX1L3}\n${EX1L4}\n${EX1L5}\n${EX1L6}`;
const EX2L1 = '##.#.#';
const EX2L6 = '####.#';
const EXAMPLE2_TEXT = `${EX2L1}\n${EX1L2}\n${EX1L3}\n${EX1L4}\n${EX1L5}\n${EX2L6}`;

const EXAMPLE_COUNT = 15;
const EXAMPLE_STEPS = 4;
const EXAMPLE2_COUNT = 17;
const EXAMPLE2_STEPS = 5;

const EXAMPLES_PART_ONE = [
  { text: EXAMPLE_TEXT, count: EXAMPLE_COUNT },
  { text: '..##..\n..##.#\n...##.\n......\n#.....\n#.##..', count: 11 },
  { text: '..###.\n......\n..###.\n......\n.#....\n.#....', count: 8 },
  { text: '...#..\n......\n...#..\n..##..\n......\n......', count: 4 },
  { text: '......\n......\n..##..\n..##..\n......\n......', count: 4 },
  { text: '......\n......\n..##..\n..##..\n......\n......', count: 4 },
];

const EXAMPLES_PART_TWO = [
  { text: EXAMPLE2_TEXT, count: EXAMPLE2_COUNT },
  { text: '#.##.#\n####.#\n...##.\n......\n#...#.\n#.####', count: 18 },
  { text: '#..#.#\n#....#\n.#.##.\n...##.\n.#..##\n##.###', count: 18 },
  { text: '#...##\n####.#\n..##.#\n......\n##....\n####.#', count: 18 },
  { text: '#.####\n#....#\n...#..\n.##...\n#.....\n#.#..#', count: 14 },
  { text: '##.###\n.##..#\n.##...\n.##...\n#.#...\n##...#', count: 17 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE2_TEXT;

const PART_ONE_RESULT = 4;
const PART_TWO_RESULT = 17;

// ======================================================================
//                                                             TestLights
// ======================================================================

describe('Lights', () => {
  test('Test the default Lights creation', () => {
    // 1. Create default Lights object
    const myobj = new lights.Lights({});
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toBe(null);
    expect(myobj.size).toBe(100);
    expect(myobj.steps).toBe(100);
    expect(myobj.step).toBe(0);
  });

  test('Test the Lights object creation from text', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({
      size: EXAMPLE_SIZE,
      steps: EXAMPLE_STEPS,
      text: aoc18.fromText(EXAMPLE_TEXT),
    });
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.size).toBe(EXAMPLE_SIZE);
    expect(myobj.steps).toBe(EXAMPLE_STEPS);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.step).toBe(0);
    expect(myobj.grid).toHaveLength(6);
    expect(myobj.grid[0]).toHaveLength(6);
    expect(myobj.grid[0]).toStrictEqual([0, 1, 0, 1, 0, 1]);
    // 3. Check neighbors
    expect(myobj.neighbors(0, 0)).toBe(1);
    expect(myobj.neighbors(0, 1)).toBe(0);
    expect(myobj.neighbors(0, 2)).toBe(3);
    expect(myobj.neighbors(1, 2)).toBe(3);
  });

  test('Test all of the part one examples', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({
      size: EXAMPLE_SIZE,
      steps: EXAMPLE_STEPS,
      text: aoc18.fromText(EXAMPLE_TEXT),
    });
    expect(myobj.part2).toBe(false);
    expect(myobj.size).toBe(EXAMPLE_SIZE);
    expect(myobj.steps).toBe(EXAMPLE_STEPS);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.step).toBe(0);
    expect(myobj.grid).toHaveLength(6);
    expect(myobj.grid[0]).toHaveLength(6);
    expect(myobj.grid[0]).toStrictEqual([0, 1, 0, 1, 0, 1]);
    // 2. Loop for all of the steps
    for (let step = 0; step < EXAMPLES_PART_ONE.length; step += 1) {
      // 3. Verify this step
      expect(myobj.step).toBe(step);
      const show = myobj.show();
      const count = myobj.count();
      expect(myobj.step).toBe(step);
      expect(show).toBe(EXAMPLES_PART_ONE[step].text);
      expect(count).toBe(EXAMPLES_PART_ONE[step].count);
      // 4. Advance to the next step
      myobj.next();
    }
  });

  test('Test all of the part two examples', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({
      part2: true,
      size: EXAMPLE_SIZE,
      steps: EXAMPLE2_STEPS,
      text: aoc18.fromText(EXAMPLE2_TEXT),
    });
    expect(myobj.part2).toBe(true);
    expect(myobj.size).toBe(EXAMPLE_SIZE);
    expect(myobj.steps).toBe(EXAMPLE2_STEPS);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.step).toBe(0);
    expect(myobj.grid).toHaveLength(6);
    expect(myobj.grid[0]).toHaveLength(6);
    expect(myobj.grid[0]).toStrictEqual([1, 1, 0, 1, 0, 1]);
    // 2. Loop for all of the steps
    for (let step = 0; step < EXAMPLES_PART_TWO.length; step += 1) {
      // 3. Verify this step
      expect(myobj.step).toBe(step);
      const show = myobj.show();
      const count = myobj.count();
      expect(myobj.step).toBe(step);
      expect(show).toBe(EXAMPLES_PART_TWO[step].text);
      expect(count).toBe(EXAMPLES_PART_TWO[step].count);
      // 4. Advance to the next step
      myobj.next();
    }
  });

  test('Test part one example of Lights object', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({
      size: EXAMPLE_SIZE,
      steps: EXAMPLE_STEPS,
      text: aoc18.fromText(PART_ONE_TEXT),
    });
    // 2. Check the part one result
    expect(myobj.partOne({ verbose: false })).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Lights object', () => {
    // 1. Create Lights object from text
    const myobj = new lights.Lights({
      part2: true,
      size: EXAMPLE_SIZE,
      steps: EXAMPLE2_STEPS,
      text: aoc18.fromText(PART_TWO_TEXT),
    });
    // 2. Check the part two result
    expect(myobj.partTwo({ verbose: false })).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                   l i g h t s . t e s t . j s                  end
// ======================================================================
