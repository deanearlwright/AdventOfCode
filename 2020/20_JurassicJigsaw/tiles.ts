// ======================================================================
// Jurassic Jigsaw
//   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t i l e s . t s
//
// Tiles for the Advent of Code 2020 Day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Tile } from './tile';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Grid = Tile[][];
type Image = string[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ZERO = new Tile([]);

// ======================================================================
//                                                                  Tiles
// ======================================================================

export class Tiles {
  // Object for Jurassic Jigsaw
  text: string[];

  part2: boolean;

  tiles: Tile[];

  size: number;

  grid: Grid;

  constructor(text: string[], part2 = false) {
    // Create a Tiles object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.tiles = [];
    this.size = 0;
    this.grid = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string[]) {
    // Assign values from text

    // 1. Don't know number of rows per tile -- yet
    let rows = 9999;
    let start = 9999;
    let knt = 0;

    // 1. Loop for all of the lines
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];

      // 2. If this is a tile id line, save index
      if (line.startsWith('Tile ')) {
        start = indx;
      } else {
        // 3. Else save number of rows needed and increment count
        rows = line.length;
        knt += 1;
      }

      // 4. Do we have enough rows for a tile?
      if (knt === rows) {
        // 5. Generate and save the tile
        const tile = new Tile(text.slice(start, start + rows + 1));
        this.tiles.push(tile);
        knt = 0;
      }
    }
    // 6. Determine the image size
    this.size = Math.sqrt(this.tiles.length);
  }

  corners(): number {
    // Return the product of the corner tile ids

    // 1. If we haven't built/found the grid yet, return 0
    if (this.size === 0 || this.grid.length === 0) {
      return 0;
    }

    // 2. Return the sum of the corner tile ids
    return this.grid[0][0].id * this.grid[0][this.size - 1].id
      * this.grid[this.size - 1][0].id * this.grid[this.size - 1][this.size - 1].id;
  }

  positionTiles(): boolean {
    // Position oriented tiles in a nice grid
    // 1. Create an empty grid
    this.grid = [];

    // 2. Fill it with nothing
    for (let rindx = 0; rindx < this.size; rindx += 1) {
      const row = [];
      for (let cindx = 0; cindx < this.size; cindx += 1) {
        row.push(ZERO);
      }
      this.grid.push(row);
    }
    // 3. Find (hopefully) a workable solution
    return this.determineGrid(0, 0);
  }

  determineGrid(row: number, col: number): boolean {
    // Recursively position the oriented tiles in a nice grid

    // 1. Are we done yet
    if (row >= this.size) {
      return true;
    }

    // 2. Loop for all the tiles that aren't already on the grid
    for (let tindx = 0; tindx < this.tiles.length; tindx += 1) {
      if (!this.isPlaced(tindx)) {
        // 3. Try placing the tile on the grid so that the borders line up
        const result = this.positionTile(row, col, tindx);
        if (result) {
          return true;
        }
      }
    }
    // 4. Nothing to see here
    return false;
  }

  isPlaced(tindx: number): boolean {
    // Return true if tile is already on the grid
    // 1. Loop for all the row and columns of the grid
    for (let rindx = 0; rindx < this.size; rindx += 1) {
      for (let cindx = 0; cindx < this.size; cindx += 1) {
        // 2. If the tile is at this place on the grid, return true
        if (this.grid[rindx][cindx].id === this.tiles[tindx].id) {
          return true;
        }
      }
    }
    // 3. Sorry, your tile was not found
    return false;
  }

  positionTile(row: number, col: number, tindx: number): boolean {
    // Try to orient the tile at the riw and columd of the grid
    // 1. Loop for all possible orientation of the tile
    const tile = this.tiles[tindx];
    for (let bindx = 0; bindx < tile.borders.length; bindx += 1) {
      tile.border = tile.borders[bindx];
      // 2. If placed here would the borders match
      let match = true;
      if (col > 0) {
        if (tile.getBorder('L') !== this.grid[row][col - 1].getBorder('R')) {
          match = false;
        }
      }
      if (row > 0) {
        if (tile.getBorder('T') !== this.grid[row - 1][col].getBorder('B')) {
          match = false;
        }
      }
      // 4. If the borders match, save tile in the grid;
      if (match) {
        this.grid[row][col] = tile;
        // 4. Where does the next tile go?
        let nextCol = col + 1;
        let nextRow = row;
        if (nextCol >= this.size) {
          nextCol = 0;
          nextRow += 1;
        }
        // 5. Now try to file the rest of the tiles
        const result = this.determineGrid(nextRow, nextCol);
        if (result) {
          return true;
        }
      }
      // 6. Try another orientation
    }
    // 7. Couldn't find a good orientation for the tile at this coordinate
    this.grid[row][col] = ZERO;
    return false;
  }

  image(): Image {
    // Return the combined image as rows of character
    // 1. Start with nothing
    const result: Image = [];
    const imageHeight = this.grid[0][0].getImage().length;

    // 2. Loop through all of the grid rows
    for (let rindx = 0; rindx < this.size; rindx += 1) {
      // 3. Loop for the rows of the image segment
      for (let indx = 0; indx < imageHeight; indx += 1) {
        const imageRow = [];
        // 4. Loop for the grid columns for the grid row
        for (let cindx = 0; cindx < this.size; cindx += 1) {
          // 5. Add the image for this column to the image row
          imageRow.push(this.grid[rindx][cindx].getImage()[indx]);
        }
        // 6. Add this image row to the rows of collected image
        result.push(imageRow.join(''));
      }
    }
    // 7. Return rows of the image
    return result;
  }
}

// ======================================================================
// end                         t i l e s . t s                        end
// ======================================================================
