// ======================================================================
// Security Through Obscurity
//   Advent of Code 2016 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      e n c r y p t e d . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 04 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_04';
import { Encrypted } from './encrypted';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
`;

interface exampleTests {
  text: string;
  result: string;
}

const EXAMPLES_PART_ONE: exampleTests[] = [
  { text: 'aaaaa-bbb-z-y-x-123[abxyz]', result: 'abxyz' },
  { text: 'a-b-c-d-e-f-g-h-987[abcde]', result: 'abcde' },
  { text: 'not-a-real-room-404[oarel]', result: 'oarel' },
  { text: 'totally-real-room-200[decoy]', result: 'loart' },
  { text: 'qzmt-zixmtkozy-ivhz-343[zimth]', result: 'zimth' },
  { text: 'ghkmaihex-hucxvm-lmhktzx-267[hmxka]', result: 'hmxka' },
];
const EXAMPLES_PART_TWO: exampleTests[] = [
  { text: 'qzmt-zixmtkozy-ivhz-343[zimth]', result: 'very encrypted name' },
  { text: 'ghkmaihex-hucxvm-lmhktzx-267[hmxka]', result: 'northpole object storage' },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = `
aaaaa-bbb-z-y-x-123[abxyz]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
ghkmaihex-hucxvm-lmhktzx-267[hmxka]
a-b-c-d-e-f-g-h-987[abcde]
`;

const PART_ONE_RESULT = 1514;
const PART_TWO_RESULT = 267;

// ======================================================================
//                                                          TestEncrypted
// ======================================================================

describe('Encrypted', () => {
  test('Test the default Encrypted creation', () => {
    // 1. Create default Encrypted object
    const myobj = new Encrypted([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.rooms).toHaveLength(0);
  });

  test('Test the Encrypted object creation from text', () => {
    // 1. Create Encrypted object from text
    const myobj = new Encrypted(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(4);
    expect(myobj.rooms).toHaveLength(4);
    expect(myobj.rooms[0].text).toBe('aaaaa-bbb-z-y-x');
    expect(myobj.rooms[0].sector).toBe(123);
    expect(myobj.rooms[0].checksum).toBe('abxyz');
    expect(myobj.rooms[0].decoy).toBe(false);
    expect(myobj.rooms[3].text).toBe('totally-real-room');
    expect(myobj.rooms[3].sector).toBe(200);
    expect(myobj.rooms[3].checksum).toBe('decoy');
    expect(myobj.rooms[3].decoy).toBe(true);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Encrypted object
      const myobj = new Encrypted(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.rooms).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(Encrypted.computeChecksum(myobj.rooms[0].text)).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Encrypted object using the key as text
      const myobj = new Encrypted(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      expect(myobj.rooms[0].decoy).toBe(false);
      // 3. Make sure it has the expected value
      myobj.decryptIfReal();
      expect(myobj.rooms[0].plain).toBe(test.result);
    });
  });

  test('Test part one example of Encrypted object', () => {
    // 1. Create Encrypted object from text
    const myobj = new Encrypted(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Encrypted object', () => {
    // 1. Create Encrypted object from text
    const myobj = new Encrypted(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                e n c r y p t e d . t e s t . t s               end
// ======================================================================
