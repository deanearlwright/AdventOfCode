// ======================================================================
// Jurassic Jigsaw
//   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t i l e . t s
//
// Tile for the Advent of Code 2020 Day 20 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                   type
// ----------------------------------------------------------------------
type Border = string;
type Image = string[];
type Images = Image[];
type Chars = string[];
type Square = Chars[];
type Squares = Record<Border, Image>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                   Tile
// ======================================================================

export class Tile {
  // Object for Jurassic Jigsaw
  text: string[];

  part2: boolean;

  id: number;

  rows: Image;

  rotation: Square;

  flip: Square;

  alternatives: Squares;

  images: Images;

  border: Border;

  borders: Border[];

  constructor(text: string[], part2 = false) {
    // Create a Tile object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.id = 0;
    this.rows = [];
    this.rotation = [];
    this.flip = [];
    this.alternatives = {};
    this.images = [];
    this.border = '';
    this.borders = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }

    // 3. Construct alternatives
    if (this.rows.length > 0) {
      this.constructAlternatives(false);
    }
  }

  processText(text: string[]) {
    // Assign values from text

    // 1. Loop for all of the lines of text
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];

      // 2. The first row contains the number
      if (line.startsWith('Tile ')) {
        this.id = parseInt(line.substr(5, 4), 10);
      } else {
        // 3. The rest are rows of image data
        this.rows.push(line);
      }
    }
  }

  initialRotation() {
    // Convert rows of characters to rows of columns

    // 1. Start with nothing
    this.rotation = [];

    // 2. For for all of the rows
    for (let indx = 0; indx < this.rows.length; indx += 1) {
      // 3. Split the characters in the row to individual characters in an array
      const columns = this.rows[indx].split('');

      // 4. Add colutions to the rotation rows
      this.rotation.push(columns);
    }
  }

  constructAlternatives(combined: boolean) {
    // Build rotated and flipped versions of the tile

    // 1. Set initial rotation (not really rotated) and save it
    this.initialRotation();

    // 2. Add the four flips
    this.addFourFlips(combined);

    // 3. Rotate and add
    this.rotate();
    this.addFourFlips(combined);

    // 4. Rotate and add
    this.rotate();
    this.addFourFlips(combined);

    // 5. Rotate and add
    this.rotate();
    this.addFourFlips(combined);
  }

  rotate() {
    // Rotate the tile one position (clockwise?)

    // 1. Start with nothing
    const result: string[][] = [];

    // 2. loop for the columns
    for (let cindx = 0; cindx < this.rows.length; cindx += 1) {
      // 3. Start a new row
      const row: string[] = [];
      // 4. Loop for the old reversed rows
      for (let rindx = this.rows.length - 1; rindx >= 0; rindx -= 1) {
        // 5. Add a character to the new row
        row.push(this.rotation[rindx][cindx]);
      }
      // 6. Add the new row to the result
      result.push(row);
    }
    // 7. Save the new rotation
    this.rotation = result;
  }

  initialFlip() {
    // Set the flipped tiles from the current rotation

    // 1. Start with nothing
    this.flip = [];

    // 2. Loop for the rows in the rotated image
    for (let rindx = 0; rindx < this.rotation.length; rindx += 1) {
      // 3. Add to the flipped tile row
      this.flip.push(this.rotation[rindx]);
    }
  }

  flipHor() {
    // Flip the tile top to bottom

    // 1. Start with nothing
    const result: Square = [];

    // 2. Loop for all rows, bottom to top
    for (let indx = this.flip.length - 1; indx >= 0; indx -= 1) {
      // 3. Add row to result
      result.push(this.flip[indx]);
    }

    // 4. Set the new flipped tile
    this.flip = result;
  }

  flipVer() {
    // Flip the tile left to right

    // 1. Start with nothing
    const result: Square = [];

    // 2. Loop for all rows, top to bottom
    for (let rindx = 0; rindx < this.flip.length; rindx += 1) {
      // 3. Loop for all columns, right to left
      const flippedRow: string[] = [];
      for (let cindx = this.flip.length - 1; cindx >= 0; cindx -= 1) {
        flippedRow.push(this.flip[rindx][cindx]);
      }
      result.push(flippedRow);
    }

    // 5. Set the new flipped tile
    this.flip = result;
  }

  addFourFlips(combined: boolean) {
    // Add the four flips: none, hor, ver, hor & ver

    // 1. Set the initial flip
    this.initialFlip();
    // 2. Add the initial (non-flipped) version to alternates
    this.addAlternative(combined);
    // 3. Flip it top to bottom and add it
    this.flipHor();
    this.addAlternative(combined);
    // 4. Add then flip that left to right and add it
    this.flipVer();
    this.addAlternative(combined);
    // 5. Flip again top to bottom to get just the left to right flip
    this.flipHor();
    this.addAlternative(combined);
  }

  bordersAndImage(): [Border, Border, Border, Border, Image] {
    // Get the top, right, bottom, and left borders, and the internal image

    // 1. Start with nothing
    const image: Image = [];
    let top: Border = '';
    let bottom: Border = '';
    let left: Border = '';
    let right: Border = '';

    // 2. Get the image as rows of characters
    for (let rindx = 1; rindx < this.flip.length - 1; rindx += 1) {
      const row = this.flip[rindx];
      const imageRow: string[] = [];
      for (let cindx = 1; cindx < this.flip.length - 1; cindx += 1) {
        imageRow.push(row[cindx]);
      }
      image.push(imageRow.join(''));
    }

    // 3. Get the top and bottom borders
    top = this.flip[0].join('');
    bottom = this.flip[this.flip.length - 1].join('');

    // 4. Get the left and right borders
    const leftChars: Chars = [];
    const rightChars: Chars = [];
    for (let rindx = 0; rindx < this.flip.length; rindx += 1) {
      const row = this.flip[rindx];
      leftChars.push(row[0]);
      rightChars.push(row[this.flip.length - 1]);
    }
    left = leftChars.join('');
    right = rightChars.join('');

    // 5. Return the four borders clockwise from top and the internal image
    return [top, right, bottom, left, image];
  }

  addAlternative(combined: boolean) {
    // Add the alternative image

    // 1. If processing the combined image, just add it
    if (combined) {
      const image = [];
      for (let rindx = 0; rindx < this.flip.length; rindx += 1) {
        image.push(this.flip[rindx].join(''));
      }
      this.images.push(image);
    } else {
      // 2. Get the borders clockwise from top and image
      const [top, right, bottom, left, image] = this.bordersAndImage();
      this.border = [top, right, bottom, left].join();
      if (this.alternatives[this.border] === undefined) {
        // 3. Add it to the alternatives
        this.borders.push(this.border);
        this.alternatives[this.border] = image;
      }
    }
  }

  display(): string {
    // Display the tile
    return `Tile ${this.id}:\n${this.rows.join('\n')}`;
  }

  displayRotation(): string {
    // Display the rotated tile
    // 1. Start with nothing
    const result: string[] = [];
    // 2. Loop for all rows in the rotated image
    for (let indx = 0; indx < this.rotation.length; indx += 1) {
      // 3. Add that row to the result
      result.push(this.rotation[indx].join(''));
    }
    // 4. Return the rotated tile as a string
    return result.join('\n');
  }

  displayFlip(): string {
    // Display the flipped tile
    // 1. Start with nothing
    const result: string[] = [];
    // 2. Loop for all rows in the flipped image
    for (let indx = 0; indx < this.flip.length; indx += 1) {
      // 3. Add that row to the result
      result.push(this.flip[indx].join(''));
    }
    // 4. Return the rotated tile as a string
    return result.join('\n');
  }

  // eslint-disable-next-line class-methods-use-this
  getBorder(letter: string): string {
    // Get the appropiate border section
    // 1. Return a section of border based on the letter
    switch (letter) {
      case 'T':
        return this.border.substr(0, 10);
      case 'R':
        return this.border.substr(11, 10);
      case 'B':
        return this.border.substr(22, 10);
      case 'L':
        return this.border.substr(33, 10);
      default:
        return '??????????';
    }
  }

  getImage() {
    // Return the image for the current border
    return this.alternatives[this.border];
  }
}

// ======================================================================
// end                          t i l e . t s                         end
// ======================================================================
