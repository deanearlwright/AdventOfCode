// ======================================================================
// Jurassic Jigsaw
//   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           i m a g e . t s
//
// A solver for the Advent of Code 2020 Day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Tile } from './tile';
import { Tiles } from './tiles';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
// const MONSTER_PATTERN1 = '..................#.';
const MONSTER_PATTERN2 = '#....##....##....###';
const MONSTER_PATTERN3 = '.#..#..#..#..#..#...';

const MONSTER_POUNDS = 1 + 8 + 6;
const pound = /#/g;
const RE_MP2 = new RegExp(MONSTER_PATTERN2);
const RE_MP3 = new RegExp(MONSTER_PATTERN3);

// ======================================================================
//                                                                  Image
// ======================================================================

export class Image {
  // Object for Jurassic Jigsaw
  text: string[];

  part2: boolean;

  tiles: Tiles;

  image: string[];

  constructor(text: string[], part2 = false) {
    // Create a Image object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.tiles = new Tiles([]);
    this.image = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.tiles = new Tiles(this.text, this.part2);
    }
  }

  corners(): number {
    // Return the product of the ids of the corner tiles
    this.tiles.positionTiles();
    return this.tiles.corners();
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      this.tiles.positionTiles();
      return this.roughSeas();
    }
    return this.corners();
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  // eslint-disable-next-line class-methods-use-this
  countPoundSigns(text: string[]): number {
    // Return the number of pound signs in the text
    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the row of the text
    for (let indx = 0; indx < text.length; indx += 1) {
      // 3. Get the number of pound signs in the row
      const count = (text[indx].match(pound) || []).length;
      // 4. Increment the count
      result += count;
    }
    // 5. Return the total number of pound signs found
    return result;
  }

  roughSeas(): number {
    // Returns the rough the waters are in the sea monsters' habitat
    // 1. Get the combined image
    if (this.tiles.tiles.length === 0) {
      return 0;
    }
    const image = this.tiles.image();

    // 2. Get the total number of pound signs
    const totalRough = this.countPoundSigns(image);

    // 3. Create a single tile with the combined image
    const tile = new Tile([]);
    tile.rows = image;

    // 4. Create the alternative images
    tile.constructAlternatives(true);

    // 5. Loop through the alternative images
    let mostMonsters = 0;
    for (let indx = 0; indx < tile.images.length; indx += 1) {
      const tileImage = tile.images[indx];
      // 6. Count the monsters in the image
      const monsters = this.countMonsters(tileImage);

      // 7. Keep track of the most monsters found
      if (monsters > mostMonsters) {
        mostMonsters = monsters;
      }
    }

    // 8. Return the roughness of the seas minus the monsters
    return totalRough - mostMonsters * MONSTER_POUNDS;
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }

  // eslint-disable-next-line class-methods-use-this
  countMonsters(image: string[]): number {
    // 1. Start with nothing
    let result = 0;
    // 2. Loop for all of the rows
    for (let rindx = 0; rindx < image.length; rindx += 1) {
      // 3. Only look at rows three or higher
      if (rindx > 2) {
        // 4. Find the pattern starts
        const start2 = this.findAllStarts(RE_MP2, image[rindx - 1]);
        const start3 = this.findAllStarts(RE_MP3, image[rindx]);
        // console.log(`result=${result} rindx=${rindx} start2 = ${start2} start3 = ${start3}`);
        // 5. Loop for all of the possible sightings
        for (let indx3 = 0; indx3 < start3.length; indx3 += 1) {
          for (let indx2 = 0; indx2 < start2.length; indx2 += 1) {
            // 6. If confirmed, increment count
            if (start2[indx2] === start3[indx3]) {
              result += 1;
            }
          }
        }
      }
    }
    // 7. Return the number of confirmed sightings
    return result;
  }

  // eslint-disable-next-line class-methods-use-this
  findAllStarts(pattern: RegExp, image: string): number[] {
    // Find all (could be overlapping) starting locations of the pattern

    // 1. Start with nothing
    const result = [];

    // 2. Loop for all possible possitions
    for (let pos = 0; pos < image.length; pos += 1) {
      // 3. Look for the pattern
      const at = image.substring(pos).search(pattern);
      // 4. If not found, we are done here
      if (at === -1) {
        return result;
      }
      pos += at;
      result.push(pos);
    }
    // 5. We should not get here, but if we do return the starting positions
    return result;
  }
}

// ======================================================================
// end                         i m a g e . t s                        end
// ======================================================================
