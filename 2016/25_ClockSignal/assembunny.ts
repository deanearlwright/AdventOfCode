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

  nextOut: number;

  clockBits: number;

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
    this.nextOut = 0;
    this.clockBits = 0;
    if (this.part2) this.registers.c = 1;
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
    this.nextOut = 0;
    this.clockBits = 0;
    if (this.part2) this.registers.c = 1;
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

  step(verbose = false): boolean {
    let value = 0;
    if (verbose) console.log(this.currentState());
    if (this.pc < 0 || this.pc >= this.instructions.length) return false;
    const inst = this.instructions[this.pc];
    let nextPC = this.pc + 1;
    switch (inst.opcode) {
      case 'cpy':
        value = (typeof inst.op1 === 'number')
          ? <number>inst.op1
          : this.registers[<RegisterName>inst.op1];
        this.registers[<RegisterName>inst.op2] = value;
        break;
      case 'inc':
        this.registers[<RegisterName>inst.op1] += 1;
        break;
      case 'dec':
        this.registers[<RegisterName>inst.op1] -= 1;
        break;
      case 'jnz':
        value = (typeof inst.op1 === 'number')
          ? <number>inst.op1
          : this.registers[<RegisterName>inst.op1];
        if (value !== 0) {
          nextPC = this.pc + <number>inst.op2;
        }
        break;
      case 'out':
        value = (typeof inst.op1 === 'number')
          ? <number>inst.op1
          : this.registers[<RegisterName>inst.op1];
        console.log(`out: ${this.currentState()} value=${value} want=${this.nextOut} count=${this.clockBits}`);
        if (value !== this.nextOut) {
          return false;
        }
        this.nextOut = nextOut[value];
        this.clockBits += 1;
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

  runUntilWeGetClock(verbose = false, limit = 0) {
    if (verbose) console.log(`runUntilWeGetClock: ${limit}`);
    const maxA = limit === 0 ? 185 : limit;
    for (let a = 175; a < maxA; a += 1) {
      this.resetRegisters();
      this.registers.a = a;
      if (verbose) console.log(`runUntilWeGetClock a=${a}`);
      this.run(false, 99999);
      if (verbose) console.log(`a=${a} clockBits=${this.clockBits}`);
      if (this.clockBits >= 10) {
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
      return NaN;
    }
    // return this.runUntilWeGetClock(verbose, limit);
    return this.decoded(verbose, limit);
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
