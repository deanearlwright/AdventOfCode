// ======================================================================
// Jurassic Jigsaw
//   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      t i l e . t e s t . t s
//
// Test Tile for Advent of Code 2020 day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { fromText } from './aoc_20';
import { Tile } from './tile';

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
`;

const EXAMPLE_BORDERS = '#..##.#...,.#..#.##..,.#..#####.,###..###..';

const EXAMPLE_IMAGE = `#.###.#.
.#.##...
#...#...
..##.##.
....#.##
..#.##..
##...#..
#.####.#`;

const EXAMPLE_DISPLAY = `Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###`;

const EXAMPLE_INITIAL = `..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###`;

const EXAMPLE_ROTATED = `.#..#####.
.#.####.#.
###...#..#
#..#.##..#
#....#.##.
...##.##.#
.#...#....
#.#.##....
##.###.#.#
#..##.#...`;

const EXAMPLE_FLIP_HOR = `#..##.#...
##.###.#.#
#.#.##....
.#...#....
...##.##.#
#....#.##.
#..#.##..#
###...#..#
.#.####.#.
.#..#####.`;

const EXAMPLE_FLIP_VER = `...#.##..#
#.#.###.##
....##.#.#
....#...#.
#.##.##...
.##.#....#
#..##.#..#
#..#...###
.#.####.#.
.#####..#.`;

const EXAMPLE_BORDERS_SV = '...#.##..#,###..###..,.#####..#.,.#..#.##..';

const COMBINED_IMAGE = [
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

const MONSTER_IMAGE = `.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#`;

// ======================================================================
//                                                               TestTile
// ======================================================================

describe('Tile', () => {
  test('Test the default Tile creation', () => {
    // 1. Create default Tile object
    const myobj = new Tile([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.id).toBe(0);
    expect(myobj.rows).toHaveLength(0);
    expect(myobj.rotation).toHaveLength(0);
    expect(myobj.flip).toHaveLength(0);
    expect(myobj.images).toHaveLength(0);
    expect(myobj.borders).toHaveLength(0);
  });

  test('Test the Tile object creation from text', () => {
    // 1. Create Tile object from text
    const myobj = new Tile(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(11);
    expect(myobj.id).toBe(2311);
    expect(myobj.rows).toHaveLength(10);
    expect(myobj.rotation).toHaveLength(10);
    expect(myobj.flip).toHaveLength(10);
    expect(myobj.images).toHaveLength(0);
    expect(myobj.rows[0]).toBe('..##.#..#.');
    expect(myobj.rows[9]).toBe('..###..###');
    expect(myobj.alternatives[EXAMPLE_BORDERS].join('\n')).toBe(EXAMPLE_IMAGE);
    expect(myobj.borders).toHaveLength(8);

    // 3. Check Methods
    expect(myobj.display()).toBe(EXAMPLE_DISPLAY);
    myobj.initialRotation();
    expect(myobj.displayRotation()).toBe(EXAMPLE_INITIAL);
    myobj.rotate();
    expect(myobj.displayRotation()).toBe(EXAMPLE_ROTATED);
    myobj.initialFlip();
    expect(myobj.displayFlip()).toBe(EXAMPLE_ROTATED);
    myobj.flipHor();
    expect(myobj.displayFlip()).toBe(EXAMPLE_FLIP_HOR);
    let [top, right, bottom, left, image] = myobj.bordersAndImage();
    let border = [top, right, bottom, left].join();
    expect(border).toBe(EXAMPLE_BORDERS);
    expect(image.join('\n')).toBe(EXAMPLE_IMAGE);
    myobj.border = border;
    expect(myobj.getBorder('T')).toBe(top);
    expect(myobj.getBorder('R')).toBe(right);
    expect(myobj.getBorder('B')).toBe(bottom);
    expect(myobj.getBorder('L')).toBe(left);
    expect(myobj.getImage().join('\n')).toBe(EXAMPLE_IMAGE);
    myobj.flipVer();
    expect(myobj.displayFlip()).toBe(EXAMPLE_FLIP_VER);
    [top, right, bottom, left, image] = myobj.bordersAndImage();
    border = [top, right, bottom, left].join();
    expect(border).toBe(EXAMPLE_BORDERS_SV);
    myobj.border = border;
    expect(myobj.getBorder('T')).toBe(top);
    expect(myobj.getBorder('R')).toBe(right);
    expect(myobj.getBorder('B')).toBe(bottom);
    expect(myobj.getBorder('L')).toBe(left);
  });

  test('Test the big image manipulation', () => {
    // Test the big image manipulation
    // 1. Create default Tile object
    const myobj = new Tile([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.id).toBe(0);
    expect(myobj.rows).toHaveLength(0);
    expect(myobj.rotation).toHaveLength(0);
    expect(myobj.flip).toHaveLength(0);
    expect(myobj.images).toHaveLength(0);
    // 3. Set the image
    myobj.id = 9999;
    myobj.rows = COMBINED_IMAGE;
    // 4. Check methods
    myobj.constructAlternatives(true);
    expect(myobj.images).toHaveLength(16);
    let found = false;
    for (let indx = 0; indx < myobj.images.length; indx += 1) {
      if (myobj.images[indx].join('\n') === MONSTER_IMAGE) {
        found = true;
      }
    }
    expect(found).toBe(true);
  });
});

// ======================================================================
// end                     t i l e . t e s t . t s                    end
// ======================================================================
