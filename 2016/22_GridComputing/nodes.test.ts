// ======================================================================
// Grid Computing
//   Advent of Code 2016 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
//  ======================================================================

// ======================================================================
//                      n o d e s . t e s t . t s
//
// Test the solver for Advent of Code 2016 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { fromText } from './aoc_22';
import { Nodes } from './nodes';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const EXAMPLE_TEXT = `
root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     86T   73T    13T   84%
/dev/grid/node-x0-y1     88T   65T    23T   73%
/dev/grid/node-x0-y2     88T   68T    20T   77%
/dev/grid/node-x0-y3     85T   71T    14T   83%
/dev/grid/node-x1-y0     86T   69T    17T   80%
/dev/grid/node-x1-y1     94T   65T    29T   69%
/dev/grid/node-x1-y2     92T   66T    26T   71%
/dev/grid/node-x1-y3     87T   73T    14T   83%
/dev/grid/node-x2-y0     86T   64T    22T   74%
/dev/grid/node-x2-y1     92T   73T    19T   79%
/dev/grid/node-x2-y2     94T   72T    22T   76%
/dev/grid/node-x2-y3     91T   72T    19T   79%
/dev/grid/node-x3-y0     85T   25T    60T   30%
/dev/grid/node-x3-y1     90T   66T    24T   73%
/dev/grid/node-x3-y2     92T   68T    24T   73%
/dev/grid/node-x3-y3     93T   67T    26T   72%
/dev/grid/node-x4-y0     87T   65T    22T   74%
/dev/grid/node-x4-y1     85T   68T    17T   80%
/dev/grid/node-x4-y2     85T   73T    12T   85%
/dev/grid/node-x4-y3     91T   71T    20T   78%
/dev/grid/node-x5-y0     85T   64T    21T   75%
/dev/grid/node-x5-y1     90T   45T    45T   50%
/dev/grid/node-x5-y2     94T   64T    30T   68%
/dev/grid/node-x5-y3     93T   66T    27T   70%
`;

interface ExampleTests {
  text: string;
  result: number;
}

const EXAMPLES_PART_ONE: ExampleTests[] = [];
const EXAMPLES_PART_TWO: ExampleTests[] = [];

const PART_ONE_TEXT = EXAMPLE_TEXT;
const PART_TWO_TEXT = EXAMPLE_TEXT;

const PART_ONE_RESULT = 7;
const PART_TWO_RESULT = NaN;

// ======================================================================
//                                                              TestNodes
// ======================================================================

describe('Nodes', () => {
  test('Test the default Nodes creation', () => {
    // 1. Create default Nodes object
    const myobj = new Nodes([]);
    // 2. Make sure it has the default values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(0);
    expect(Object.keys(myobj.storage)).toHaveLength(0);
    expect(myobj.used).toHaveLength(0);
    expect(myobj.avail).toHaveLength(0);
    expect(myobj.corners.minX).toBe(0);
    expect(myobj.corners.minY).toBe(0);
    expect(myobj.corners.maxX).toBe(0);
    expect(myobj.corners.maxY).toBe(0);
  });

  test('Test the Nodes object creation from text', () => {
    // 1. Create Nodes object from text
    const myobj = new Nodes(fromText(EXAMPLE_TEXT));
    // 2. Make sure it has the expected values
    expect(myobj.part2).toBe(false);
    expect(myobj.text).toHaveLength(26);
    expect(Object.keys(myobj.storage)).toHaveLength(24);
    expect(myobj.used).toHaveLength(24);
    expect(myobj.avail).toHaveLength(24);
    expect(myobj.corners.minX).toBe(0);
    expect(myobj.corners.minY).toBe(0);
    expect(myobj.corners.maxX).toBe(5);
    expect(myobj.corners.maxY).toBe(3);
  });

  test('Test all of the part one examples', () => {
    // 1. Loop for all of the examples
    EXAMPLES_PART_ONE.forEach((test) => {
      // 2. Create Nodes object
      const myobj = new Nodes(fromText(test.text));
      expect(myobj.part2).toBe(false);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test all of the part two examples', () => {
    // 1. Loop for all of the examples for the second part
    EXAMPLES_PART_TWO.forEach((test) => {
      // 2. Create Nodes object using the key as text
      const myobj = new Nodes(fromText(test.text), true);
      expect(myobj.part2).toBe(true);
      expect(myobj.text).toHaveLength(1);
      // 3. Make sure it has the expected value
      expect(myobj.solution()).toBe(test.result);
    });
  });

  test('Test part one example of Nodes object', () => {
    // 1. Create Nodes object from text
    const myobj = new Nodes(fromText(PART_ONE_TEXT));
    // 2. Check the part one result
    expect(myobj.partOne(true, 0)).toBe(PART_ONE_RESULT);
  });

  test('Test part two example of Nodes object', () => {
    // 1. Create Nodes object from text
    const myobj = new Nodes(fromText(PART_TWO_TEXT), true);
    // 2. Check the part two result
    expect(myobj.partTwo(false, 0)).toBe(PART_TWO_RESULT);
  });
});

// ======================================================================
// end                    n o d e s . t e s t . t s                   end
// ======================================================================
