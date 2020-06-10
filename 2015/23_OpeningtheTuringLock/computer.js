/* eslint-disable linebreak-style */
// ======================================================================
// Opening the Turing Lock
//   Advent of Code 2015 Day 23 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           c o m p u t e r . j s
//
// A solver for the Advent of Code 2015 Day 23 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

const INSTRUCTIONS = {
  hlf: 'r',
  tpl: 'r',
  inc: 'r',
  jmp: 'o',
  jie: 'ro',
  jio: 'ro',
};

// ======================================================================
//                                                               Computer
// ======================================================================

class Computer {
  // Object for Opening the Turing Lock

  constructor(options) {
    // Create a Computer object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.registers = { a: 0, b: 0, pc: 0 };
    this.instructions = [];

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  reset() {
    this.registers = { a: 0, b: 0, pc: 0 };
  }

  processText(text) {
    // 1. Reset the instructions
    this.instructions = [];
    let pc = 0;
    // 2. Loop for all of the lines of text
    text.forEach((line) => {
      // 3. Split out instruction and operands
      let badInst = null;
      let [opcode, op1, op2] = line.split(' ');
      if (opcode) opcode = opcode.trim();
      if (op1) op1 = op1.trim();
      if (op1 && op1[op1.length - 1] === ',') op1 = op1.substring(0, op1.length - 1);
      if (op2) op2 = op2.trim();
      // 4. Check the instruction and operands
      if (!(opcode in INSTRUCTIONS)) {
        badInst = `Unkown opcode ${pc} ${line}`;
      } else {
        const ops = INSTRUCTIONS[opcode];
        if (ops[0] === 'r' && op1 !== 'a' && op1 !== 'b') {
          badInst = `Invalid register operand ${pc} ${line}`;
        } else if (ops[0] === 'o' && Computer.badOffset(op1)) {
          badInst = `Invalid jump offset ${pc} ${line}`;
        } else if (ops.length === 2 && Computer.badOffset(op2)) {
          badInst = `Invalid conditional jump offset ${pc} ${line}`;
        }
        if (badInst === null) {
          if (ops[0] === 'o') op1 = parseInt(op1, 10);
          if (ops.length === 2) op2 = parseInt(op2, 10);
        }
      }
      // 5. Report any problems
      if (badInst !== null) {
        // eslint-disable-next-line no-console
        console.log(badInst);
      } else {
        this.instructions.push({ opcode, op1, op2 });
        pc += 1;
      }
    });
  }

  static badOffset(operand) {
    if (typeof operand !== 'string') return true;
    if (operand.length < 2) return true;
    if (operand[0] !== '+' && operand[0] !== '-') return true;
    if (operand[1] < '0' || operand[1] > '9') return true;
    return false;
  }

  step() {
    // 1. Check the program counter, halt if out of range
    const { a, b, pc } = this.registers;
    if (pc < 0 || pc >= this.instructions.length) return true;
    // 2. Execute the instruction
    const { opcode, op1, op2 } = this.instructions[pc];
    switch (opcode) {
      case 'hlf':
        this.registers[op1] = Math.floor(this.registers[op1] / 2);
        this.registers.pc += 1;
        break;
      case 'tpl':
        this.registers[op1] *= 3;
        this.registers.pc += 1;
        break;
      case 'inc':
        this.registers[op1] += 1;
        this.registers.pc += 1;
        break;
      case 'jmp':
        this.registers.pc += op1;
        break;
      case 'jie':
        this.registers.pc += this.registers[op1] % 2 === 0 ? op2 : 1;
        break;
      case 'jio':
        this.registers.pc += this.registers[op1] === 1 ? op2 : 1;
        break;
      default:
        // eslint-disable-next-line no-console
        console.log(`pc=${pc} invalid opcode ${opcode}`);
        return true;
    }
    return false;
  }

  run(options) {
    // 1. Get the optional arguments
    const verbose = options.verbose === undefined ? false : options.verbose;
    const limit = options.limit === undefined ? 0 : options.limit;
    // eslint-disable-next-line no-console
    // 2. Loop until the program stops;
    let halt = false;
    let knt = 0;
    while (!halt && (limit === 0 || knt < limit)) {
      if (verbose) {
        const { a, b, pc } = this.registers;
        if (pc >= 0 && pc < this.instructions.length) {
          const { opcode, op1, op2 } = this.instructions[pc];
          // eslint-disable-next-line no-console
          console.log(`${pc}: ${opcode} ${op1} ${op2} a = ${a} b = ${b}`);
        }
      }
      halt = this.step();
      knt += 1;
    }
    if (verbose) {
      const { a, b, pc } = this.registers;
      if (halt) {
        // eslint-disable-next-line no-console
        console.log(`${pc}: Halted a = ${a} b = ${b}`);
      } else {
        // eslint-disable-next-line no-console
        console.log(`${pc}: Limit ${limit} a = ${a} b = ${b}`);
      }
    }
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Run the computer
    this.run({ verbose, limit });
    // 2. Return the solution for part one
    return this.registers.b;
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;
    this.todo = 'TODO';

    // 1. Run the computer
    this.registers.a = 1;
    this.run({ verbose, limit });
    // 2. Return the solution for part one
    return this.registers.b;
  }
}

module.exports.Computer = Computer;
// ======================================================================
// end                      c o m p u t e r . j s                     end
// ======================================================================
