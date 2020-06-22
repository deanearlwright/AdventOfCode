// ======================================================================
// Internet Protocol Version 7
//   Advent of Code 2016 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      p r o t o c o l . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_07';
import { Protocol } from './protocol';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
ioxxoj[asdfgh]zxcvbn[bddb]aacvbn
aba[bab]xyz
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [
  { text: 'abba[mnop]qrst', result: 1 },
  { text: 'abcd[bddb]xyyx', result: 0 },
  { text: 'aaaa[qwer]tyui', result: 0 },
  { text: 'ioxxoj[asdfgh]zxcvbn', result: 1 },
  { text: 'ioxxoj[asdfgh]zxcvbn[bddb]aacvbn', result: 0 },
];
const EXAMPLES_PART_TWO: ExampleTests[] = [
  { text: 'aba[bab]xyz', result: 1 },
  { text: 'xyx[xyx]xyx', result: 0 },
  { text: 'aaa[kek]eke', result: 1 },
  { text: 'zazbz[bzb]cdb', result: 1 },
];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = `
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
`;

const PART_ONE_RESULT = 2;
const PART_TWO_RESULT = 3;

// ======================================================================
//                                                           TestProtocol
// ======================================================================

describe('Protocol', () => {
  test('Test the default Protocol creation', () => {
    // 1. Create default Protocol object
    const myobj = new Protocol([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(myobj.addresses).toHaveLength(0);
  });

  test('Test the Protocol object creation from text', () => {
    // 1. Create Protocol object from text
    const myobj = new Protocol(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(6);
    expect(myobj.addresses).toHaveLength(6);
    expect(myobj.addresses[0].complete).toBe('abba[mnop]qrst');
    expect(myobj.addresses[0].hyperNets).toStrictEqual(['mnop']);
    expect(myobj.addresses[0].notHyperNets).toStrictEqual(['abba', 'qrst']);
    expect(myobj.addresses[0].tls).toBe(true);
    expect(myobj.addresses[1].complete).toBe('abcd[bddb]xyyx');
    expect(myobj.addresses[1].hyperNets).toStrictEqual(['bddb']);
    expect(myobj.addresses[1].notHyperNets).toStrictEqual(['abcd', 'xyyx']);
    expect(myobj.addresses[1].tls).toBe(false);
    expect(myobj.addresses[2].tls).toBe(false);
    expect(myobj.addresses[3].tls).toBe(true);
    expect(myobj.addresses[4].complete).toBe('ioxxoj[asdfgh]zxcvbn[bddb]aacvbn');
    expect(myobj.addresses[4].hyperNets).toStrictEqual(['asdfgh', 'bddb']);
    expect(myobj.addresses[4].notHyperNets).toStrictEqual(['ioxxoj', 'zxcvbn', 'aacvbn']);
    expect(myobj.addresses[4].tls).toBe(false);
    expect(myobj.addresses[5].complete).toBe('aba[bab]xyz');
    expect(myobj.addresses[5].hyperNets).toStrictEqual(['bab']);
    expect(myobj.addresses[5].notHyperNets).toStrictEqual(['aba', 'xyz']);
    expect(myobj.addresses[5].tls).toBe(false);
    expect(myobj.addresses[5].ssl).toBe(true);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Protocol object
      const myobj = new Protocol(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Protocol object using the key as text
      const myobj = new Protocol(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Protocol object', () => {
    // 1. Create Protocol object from text
    const myobj = new Protocol(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(false, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Protocol object', () => {
    // 1. Create Protocol object from text
    const myobj = new Protocol(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                 p r o t o c o l . t e s t . t s                end
// ======================================================================
