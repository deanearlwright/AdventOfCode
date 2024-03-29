// ======================================================================
// Jurassic Jigsaw
//   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      i m a g e . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_20';
import { Image } from './image';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 20899048083289;
const PART_TWO_RESULT = 273;

const EXAMPLE_IMAGE = `.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###`;

const IMAGE_ROWS = [
  '.#.#..#.##...#.##..#####',
  '###....#.#....#..#......',
  '##.##.###.#.#..######...',
  '###.#####...#.#####.#..#',
  '##.#....#.##.####...#.##',
  '...########.#....#####.#',
  '....#..#...##..#.#.###..',
  '.####...#..#.....#......',
  '#..#.##..#..###.#.##....',
  '#.####..#.####.#.#.###..',
  '###.#.#...#.######.#..##',
  '#.####....##..########.#',
  '##..##.#...#...#.#.#.#..',
  '...#..#..#.#.##..###.###',
  '.#.#....#.##.#...###.##.',
  '###.#...#..#.##.######..',
  '.#.#.###.##.##.#..#.##..',
  '.####.###.#...###.#..#.#',
  '..#.#..#..#.#.#.####.###',
  '#..####...#.#.#.###.###.',
  '#####..#####...###....##',
  '#.##..#..#...#..####...#',
  '.#.###..##..##..####.##.',
  '...###...##...#...#..###',
];

const MONSTER_ROWS = [
  '.####...#####..#...###..',
  '#####..#..#.#.####..#.#.',
  '.#.#...#.###...#.##.##..',
  '#.#.##.###.#.##.##.#####',
  '..##.###.####..#.####.##',
  '...#.#..##.##...#..#..##',
  '#.##.#..#.#..#..##.#.#..',
  '.###.##.....#...###.#...',
  '#.####.#.#....##.#..#.#.',
  '##...#..#....#..#...####',
  '..#.##...###..#.#####..#',
  '....#.##.#.#####....#...',
  '..##.##.###.....#.##..#.',
  '#...#...###..####....##.',
  '.#.##...#.##.#.#.###...#',
  '#.###.#..####...##..#...',
  '#.###...#.##...#.######.',
  '.###.###.#######..#####.',
  '..##.#..#..#.#######.###',
  '#.#..##.########..#..##.',
  '#.#####..#.#...##..#....',
  '#....##..#.#########..##',
  '#...#.....#..##...###.##',
  '#..###....##.#...##.##.#',
];

// ======================================================================
//                                                              TestImage
// ======================================================================

describe('Image', () => {
  test('Test the default Image creation', () => {
    // 1. Create default Image object
    const myobj = new Image([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.tiles.tiles).toHaveLength(0);
    expect(myobj.image).toHaveLength(0);
  });

  test('Test the Image object creation from text', () => {
    // 1. Create Image object from text
    const myobj = new Image(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(11 * 9);
    expect(myobj.tiles.tiles).toHaveLength(9);
    expect(myobj.image).toHaveLength(0);

    // 3. Check methods
    expect(myobj.corners()).toBe(PART_ONE_RESULT);
    expect(myobj.countPoundSigns(EXAMPLE_IMAGE.split('\n'))).toBe(303);
    expect(myobj.countPoundSigns(IMAGE_ROWS)).toBe(303);
    expect(myobj.countPoundSigns(MONSTER_ROWS)).toBe(303);
    expect(myobj.countMonsters(MONSTER_ROWS)).toBe(2);
  });

  test('Test part one example of Image object', () => {
    // 1. Create Image object from text
    const myobj = new Image(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Image object', () => {
    // 1. Create Image object from text
    const myobj = new Image(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    i m a g e . t e s t . t s                   end
// ======================================================================
