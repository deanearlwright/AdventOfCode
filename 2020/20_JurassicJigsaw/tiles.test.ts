// ======================================================================
// Jurassic Jigsaw
//   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t i l e s . t e s t . t s
//
// Test Tiles for Advent of Code 2020 day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { fromText } from './aoc_20';
import { Tiles } from './tiles';

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

const IMAGE = `.#.#..#.##...#.##..#####
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
    expect(myobj.tiles).toHaveLength(0);
    expect(myobj.size).toBe(0);
    expect(myobj.grid).toHaveLength(0);
  });

  test('Test the Tiles object creation from text', () => {
    // 1. Create Tiles object from text
    const myobj = new Tiles(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(11 * 9);
    expect(myobj.tiles).toHaveLength(9);
    expect(myobj.size).toBe(3);
    expect(myobj.grid).toHaveLength(0);
    expect(myobj.tiles[0].id).toBe(2311);
    expect(myobj.tiles[1].id).toBe(1951);
    expect(myobj.tiles[2].id).toBe(1171);
    expect(myobj.tiles[3].id).toBe(1427);
    expect(myobj.tiles[4].id).toBe(1489);
    expect(myobj.tiles[5].id).toBe(2473);
    expect(myobj.tiles[6].id).toBe(2971);
    expect(myobj.tiles[7].id).toBe(2729);
    expect(myobj.tiles[8].id).toBe(3079);

    // 3. Test methods
    expect(myobj.positionTiles()).toBe(true);
    expect(myobj.grid).toHaveLength(3);
    expect(myobj.grid[0][0].id).toBe(1951);
    expect(myobj.grid[0][1].id).toBe(2311);
    expect(myobj.grid[0][2].id).toBe(3079);
    expect(myobj.grid[1][0].id).toBe(2729);
    expect(myobj.grid[1][1].id).toBe(1427);
    expect(myobj.grid[1][2].id).toBe(2473);
    expect(myobj.grid[2][0].id).toBe(2971);
    expect(myobj.grid[2][1].id).toBe(1489);
    expect(myobj.grid[2][2].id).toBe(1171);
    expect(myobj.corners()).toBe(20899048083289);
    expect(myobj.grid[0][0].getBorder('T')).toBe('#...##.#..');
    expect(myobj.grid[0][1].getBorder('T')).toBe('..###..###');
    expect(myobj.grid[0][2].getBorder('T')).toBe('#.#.#####.');
    expect(myobj.grid[1][0].getBorder('T')).toBe('#.##...##.');
    expect(myobj.grid[1][1].getBorder('T')).toBe('..##.#..#.');
    expect(myobj.grid[1][2].getBorder('T')).toBe('..#.###...');
    expect(myobj.grid[2][0].getBorder('T')).toBe('...#.#.#.#');
    expect(myobj.grid[2][1].getBorder('T')).toBe('###.##.#..');
    expect(myobj.grid[2][2].getBorder('T')).toBe('.##...####');
    expect(myobj.image().join('\n')).toBe(IMAGE);
  });
});

// ======================================================================
// end                    t i l e s . t e s t . t s                   end
// ======================================================================
