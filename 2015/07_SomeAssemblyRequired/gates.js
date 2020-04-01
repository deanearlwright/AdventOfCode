/* eslint-disable linebreak-style */
// ======================================================================
// Some Assembly Required
//   Advent of Code 2015 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           g a t e s . j s
//
// A solver for the Advent of Code 2015 Day 07 problem
// ======================================================================

// TODO -- Need to be able to defer instructions until arguments available

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const MASK = 65535;
// ======================================================================
//                                                                  Gates
// ======================================================================

class Gates {
  // Object for Some Assembly Required

  constructor(options) {
    // Create a Gates object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.wires = {};
    this.instructions = {};

    // 2. Process text (if any)
    if (this.text !== null) {
      this.text.forEach((line) => this.processInstruction(line));
    }
  }

  processInstruction(line) {
    const pattern = /([a-z0-9]+ AND [a-z0-9]+|[a-z0-9]+ OR [a-z0-9]+|NOT [a-z0-9]+|[a-z0-9]+ LSHIFT [0-9]+|[a-z0-9]+ RSHIFT [0-9]+|[0-9a-z]+) -> ([a-z]+)/;
    const inst = pattern.exec(line);
    if (inst === null) {
      // eslint-disable-next-line no-console
      console.log('Unable to parse', line);
      return;
    }
    const what = inst[1];
    const parts = what.split(' ');
    const where = inst[2];
    if (what.search('AND') !== -1) {
      this.instructions[where] = ['AND', parts[0], parts[2]];
    } else if (what.search('OR') !== -1) {
      this.instructions[where] = ['OR', parts[0], parts[2]];
    } else if (what.search('NOT') !== -1) {
      this.instructions[where] = ['NOT', parts[1], parts[1]];
    } else if (what.search('LSHIFT') !== -1) {
      this.instructions[where] = ['LSHIFT', parts[0], parts[2]];
    } else if (what.search('RSHIFT') !== -1) {
      this.instructions[where] = ['RSHIFT', parts[0], parts[2]];
    } else {
      this.instructions[where] = ['ASSIGN', parts[0], parts[0]];
      if (this.getValue(parts[0]) !== undefined) {
        this.wires[where] = this.getValue(parts[0]);
      }
    }
  }

  evaluate(where) {
    // eslint-disable-next-line no-console
    console.log('evaluate', where);
    if (this.wires[where] !== undefined) {
      return this.wires[where];
    }
    this.evaluateInstruction(where);
    if (this.wires[where] !== undefined) {
      return this.wires[where];
    }
    return undefined;
  }

  evaluateInstruction(where) {
    // eslint-disable-next-line no-console
    console.log('evaluateInstruction', where);
    const [inst, op1, op2] = this.instructions[where];
    let value1 = this.getValue(op1);
    if (value1 === undefined) {
      value1 = this.evaluate(op1);
    }
    let value2 = this.getValue(op2);
    if (value2 === undefined) {
      value2 = this.evaluate(op2);
    }
    if (value1 === undefined || value2 === undefined) {
      // eslint-disable-next-line no-console
      console.log('Unable to evaluate', where);
      return;
    }
    switch (inst) {
      case 'AND':
        // eslint-disable-next-line no-bitwise
        this.wires[where] = value1 & value2;
        break;
      case 'OR':
        // eslint-disable-next-line no-bitwise
        this.wires[where] = value1 | value2;
        break;
      case 'NOT':
        // eslint-disable-next-line no-bitwise
        this.wires[where] = MASK & (~value1);
        break;
      case 'LSHIFT':
        // eslint-disable-next-line no-bitwise
        this.wires[where] = value1 << value2;
        break;
      case 'RSHIFT':
        // eslint-disable-next-line no-bitwise
        this.wires[where] = MASK & (value1 >>> value2);
        break;
      case 'ASSIGN':
        this.wires[where] = value1;
        break;
      default:
        // eslint-disable-next-line no-console
        console.log('Unexpected instruction', inst, 'for', where);
    }
  }

  executeInstruction(line) {
    const pattern = /([a-z0-9]+ AND [a-z0-9]+|[a-z0-9]+ OR [a-z0-9]+|NOT [a-z0-9]+|[a-z0-9]+ LSHIFT [0-9]+|[a-z0-9]+ RSHIFT [0-9]+|[0-9a-z]+) -> ([a-z]+)/;
    const inst = pattern.exec(line);
    if (inst === null) {
      // eslint-disable-next-line no-console
      console.log('Unable to parse', line);
      return;
    }
    const what = inst[1];
    const parts = what.split(' ');
    const where = inst[2];
    if (what.search('AND') !== -1) {
      // eslint-disable-next-line no-bitwise
      this.wires[where] = this.getValue(parts[0]) & this.getValue(parts[2]);
    } else if (what.search('OR') !== -1) {
      // eslint-disable-next-line no-bitwise
      this.wires[where] = this.getValue(parts[0]) | this.getValue(parts[2]);
    } else if (what.search('NOT') !== -1) {
      // eslint-disable-next-line no-bitwise
      this.wires[where] = MASK & (~this.getValue(parts[1]));
    } else if (what.search('LSHIFT') !== -1) {
      // eslint-disable-next-line no-bitwise
      this.wires[where] = this.getValue(parts[0]) << this.getValue(parts[2]);
    } else if (what.search('RSHIFT') !== -1) {
      // eslint-disable-next-line no-bitwise
      this.wires[where] = MASK & (this.getValue(parts[0]) >>> this.getValue(parts[2]));
    } else {
      this.wires[where] = this.getValue(parts[0]);
    }
  }

  getValue(operand) {
    // eslint-disable-next-line no-restricted-globals
    const number = parseInt(operand, 10);
    // eslint-disable-next-line no-restricted-globals
    if (isNaN(number)) {
      return this.wires[operand];
    }
    return number;
  }


  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    const result = this.evaluate('a');
    if (result === undefined) {
      return null;
    }
    return result;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Find the solution for part one
    const part1a = this.evaluate('a');

    // 2. Override wire b with that signal and reset the other wires
    this.wires = {};
    this.wires.b = part1a;

    // 3. Return the solution for part two
    const result = this.evaluate('a');
    if (result === undefined) {
      return null;
    }
    return result;
  }
}

module.exports.Gates = Gates;
// ======================================================================
// end                         g a t e s . j s                        end
// ======================================================================
