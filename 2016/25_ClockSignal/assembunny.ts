// ======================================================================
// Clock Signal
//   Advent of Code 2016 Day 25 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           a s s e m b u n n y . t s
//
// A solver for the Advent of Code 2016 Day 25 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type RegisterName = 'a' | 'b' | 'c' | 'd' ;
type OpCode = 'cpy' | 'inc' | 'dec' | 'jnz' | 'out';
type Operand = RegisterName | number;
type Registers = Record<RegisterName, number>;
interface Instruction {
  opcode: OpCode;
  op1: Operand;
  op2?: Operand;
}
type Instructions = Instruction[];
type ProgramCounter = number;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const registerLetters = 'abcd';

const nextOut = [1, 0];

// ======================================================================
//                                                             Assembunny
// ======================================================================

export class Assembunny {
  // Object for Clock Signal
  text: string[];

  part2: boolean;

  registers: Registers;

  instructions: Instructions;

  pc: ProgramCounter;

  output: number[];

  constructor(text: string[], part2 = false) {
    // Create a Assembunny object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.registers = {
      a: 0,
      b: 0,
      c: 0,
      d: 0,
    };
    this.output = [];
    this.instructions = [];
    this.pc = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.instructions = [];
    // 2. Loop for each line of text
    this.text.forEach((line) => {
      // 3. Break the line into parts
      const [opcode, op1, op2] = line.split(' ');
      const xop1 = registerLetters.indexOf(op1) >= 0 ? op1 : parseInt(op1, 10);
      if (op2 && !op2.startsWith('#')) {
        const xop2 = registerLetters.indexOf(op2) >= 0 ? op2 : parseInt(op2, 10);
        this.instructions.push({
          opcode: <OpCode>opcode,
          op1: <Operand>xop1,
          op2: <Operand>xop2,
        });
      } else {
        this.instructions.push({
          opcode: <OpCode>opcode,
          op1: <Operand>xop1,
        });
      }
    });
  }

  resetRegisters(): void {
    this.registers = {
      a: 0,
      b: 0,
      c: 0,
      d: 0,
    };
    this.output = [];
    this.pc = 0;
  }

  currentState(): string {
    return `${this.pc}: ${this.currentRegisters()} ${this.currentInstruction()}`;
  }

  currentRegisters(): string {
    return `${this.registers.a} ${this.registers.b} ${this.registers.c} ${this.registers.d}`;
  }

  currentInstruction(): string {
    if (this.pc < 0 || this.pc >= this.instructions.length) return '';
    const inst = this.instructions[this.pc];
    switch (inst.opcode) {
      case 'cpy':
        return `cpy ${inst.op1} ${inst.op2}`;
      case 'inc':
      case 'dec':
      case 'out':
        return `${inst.opcode} ${inst.op1}`;
      case 'jnz':
        return `jnz ${inst.op1} ${inst.op2} (${<number>inst.op2 + this.pc})`;
      default:
        break;
    }
    return `unknown opcode: ${inst.opcode}`;
  }

  getOp1(inst: Instruction): number {
    return (typeof inst.op1 === 'number') ? inst.op1 : this.registers[<RegisterName>inst.op1];
  }

  step(verbose = false, stopOnOut = false): boolean {
    if (verbose) console.log(this.currentState());
    if (this.pc < 0 || this.pc >= this.instructions.length) return false;
    const inst = this.instructions[this.pc];
    const op1 = this.getOp1(inst);
    let nextPC = this.pc + 1;
    switch (inst.opcode) {
      case 'cpy':
        this.registers[<RegisterName>inst.op2] = op1;
        break;
      case 'inc':
        this.registers[<RegisterName>inst.op1] += 1;
        break;
      case 'dec':
        this.registers[<RegisterName>inst.op1] -= 1;
        break;
      case 'jnz':
        if (op1 !== 0) {
          nextPC = this.pc + <number>inst.op2;
        }
        break;
      case 'out':
        this.output.push(op1);
        if (stopOnOut) {
          return false;
        }
        break;
      default:
        console.log(`??? ${this.currentState()}`);
        return false;
    }
    this.pc = nextPC;
    return true;
  }

  run(verbose = false, limit = 0) {
    let steps = 0;
    while (this.step(verbose) && (limit === 0 || steps < limit)) {
      steps += 1;
    }
  }

  tryClockValue(a: number, verbose = false, limit = 0): boolean {
    if (verbose) console.log(`tryClockValue: a=${a} limit=${limit}`);
    const numBits = 10;
    let want = 0;
    let lastLength = 0;
    const maxSteps = limit > 0 ? limit : 9999;
    let steps = 0;
    this.resetRegisters();
    this.registers.a = a;
    while (this.output.length < numBits) {
      while (this.step(false, true) && steps < maxSteps);
      if (lastLength !== this.output.length - 1) {
        if (verbose) console.log(`tryClockValue: stopped at ${this.currentState()}`);
        return false;
      }
      if (this.output[lastLength] !== want) {
        if (verbose) console.log(`tryClockValue: wanted ${want} at ${this.currentState()}`);
        return false;
      }
      want = nextOut[want];
      lastLength += 1;
      this.pc += 1;
      steps += 1;
    }
    if (verbose) console.log(`tryClockValue: returning true at ${this.currentState()}`);
    return true;
  }

  findValueForClock(verbose = false, limit = 0) {
    if (verbose) console.log(`findValueForClock: ${limit}`);
    const maxA = limit === 0 ? 999 : limit;
    for (let a = 0; a < maxA; a += 1) {
      if (verbose) console.log(`findValueForClock a=${a}`);
      if (this.tryClockValue(a, verbose)) {
        return a;
      }
    }
    return NaN;
  }

  decoded(verbose = false, limit = 0) {
    if (verbose) console.log(`decoded: ${limit}`);
    const maxA = limit === 0 ? 200 : limit;
    for (let a = 0; a < maxA; a += 1) {
      const value = a + <number> this.instructions[1].op1 * <number> this.instructions[2].op1;
      const binary = value.toString(2).split('').reverse().join('');
      if (binary.length % 2 === 0 && binary[0] === '0') {
        if (verbose) console.log(`${a} ${value} ${binary}`);
        let need = '0';
        let ok = true;
        for (let index = 0; index < binary.length; index += 1) {
          if (binary[index] === need) {
            need = need === '0' ? '1' : '0';
          } else {
            ok = false;
          }
        }
        if (ok) {
          return a;
        }
      }
    }
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.decoded(verbose, limit);
    }
    return this.findValueForClock(verbose, limit);
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                    a s s e m b u n n y . t s                   end
// ======================================================================
