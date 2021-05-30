// ======================================================================
// Lobby Layout
//   Advent of Code 2020 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t i l e s . t e s t . t s
//
// Test the solver for Advent of Code 2020 day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_24';
import { Tiles } from './tiles';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
`;

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 10;
const PART_TWO_RESULT = 2208;

const NEXT_DAY = [15, 12, 25, 14, 23, 28, 41, 37, 49, 37];

// ======================================================================
//                                                              TestTiles
// ======================================================================

describe('Tiles', () => {
  test('Test the default Tiles creation', () => {
    // 1. Create default Tiles object
    const myobj = new Tiles([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    // 3. Check methods
    expect(myobj.howManyBlack()).toBe(0);
  });

  test('Test the Tiles object creation from text', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(20);
    // 3. Check methods
    expect(myobj.howManyBlack()).toBe(10);
    expect(myobj.isTileBlack(10000, 10000)).toBe(true);
    expect(myobj.isTileBlack(10500, 10500)).toBe(false);
    expect(myobj.isTileBlack(10010, 9980)).toBe(true);
    const neighbors = myobj.neighbors(10000, 10000);
    expect(neighbors).toHaveLength(6);
    expect(neighbors).toStrictEqual([1000010010, 1000009990, 999510005,
      1000510005, 999509995, 1000509995]);
    expect(myobj.blackNeighbors(neighbors)).toBe(1);

    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[0]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[1]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[2]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[3]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[4]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[5]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[6]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[7]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[8]);
    expect(myobj.nextDay()).toBe(true);
    expect(myobj.howManyBlack()).toBe(NEXT_DAY[9]);
  });

  test('Test part one example of Tiles object', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Tiles object', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    t i l e s . t e s t . t s                   end
// ======================================================================
