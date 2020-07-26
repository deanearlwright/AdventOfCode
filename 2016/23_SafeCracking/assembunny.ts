// ======================================================================
// Safe Cracking
//   Advent of Code 2016 Day 23 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           a s s e m b u n n y . t s
//
// A solver for the Advent of Code 2016 Day 23 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type RegisterName = 'a' | 'b' | 'c' | 'd' ;
type OpCode = 'cpy' | 'inc' | 'dec' | 'jnz' | 'tgl';
type Operand = RegisterName | number;
type Registers = Record<RegisterName, number>;
interface Instruction {
  opcode: OpCode;
  op1: Operand;
  op2?: Operand;
}
type Instructions = Instruction[];
type ProgramCounter = number;
type TGL = Record<OpCode, OpCode>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const registerLetters = 'abcd';

const tgl: TGL = {
  cpy: 'jnz',
  inc: 'dec',
  dec: 'inc',
  jnz: 'cpy',
  tgl: 'inc',
};

// ======================================================================
//                                                             Assembunny
// ======================================================================

export class Assembunny {
  // Object for Safe Cracking
  text: string[];

  part2: boolean;

  registers: Registers;

  instructions: Instructions;

  pc: ProgramCounter;

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
        return `${inst.opcode} ${inst.op1}`;
      case 'jnz':
        return `jnz ${inst.op1} ${inst.op2} (${this.getOp2(inst) + this.pc})`;
      case 'tgl':
        return `tgl ${inst.op1} (${this.getOp1(inst) + this.pc})`;
      default:
        break;
    }
    return `unknown opcode: ${inst.opcode}`;
  }

  getOp1(inst: Instruction): number {
    return (typeof inst.op1 === 'number') ? inst.op1 : this.registers[<RegisterName>inst.op1];
  }

  getOp2(inst: Instruction): number {
    return (typeof inst.op2 === 'number') ? inst.op2 : this.registers[<RegisterName>inst.op2];
  }

  step(verbose = false): boolean {
    if (verbose) console.log(this.currentState());
    if (this.pc < 0 || this.pc >= this.instructions.length) return false;
    const inst = this.instructions[this.pc];
    const op1 = this.getOp1(inst);
    let xpc = 0;
    let nextPC = this.pc + 1;
    switch (inst.opcode) {
      case 'cpy':
        if (typeof inst.op2 !== 'number') {
          this.registers[<RegisterName>inst.op2] = op1;
        }
        break;
      case 'inc':
        if (typeof inst.op1 !== 'number') {
          this.registers[<RegisterName>inst.op1] += 1;
        }
        break;
      case 'dec':
        if (typeof inst.op1 !== 'number') {
          this.registers[<RegisterName>inst.op1] -= 1;
        }
        break;
      case 'jnz':
        if (op1 !== 0) {
          nextPC = this.pc + this.getOp2(inst);
        }
        break;
      case 'tgl':
        xpc = this.pc + op1;
        if (xpc >= 0 && xpc < this.instructions.length) {
          this.instructions[xpc] = {
            opcode: tgl[this.instructions[xpc].opcode],
            op1: this.instructions[xpc].op1,
            op2: this.instructions[xpc].op2,
          };
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

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      this.run(verbose, limit);
      return this.registers.a;
    }
    this.run(verbose, limit);
    return this.registers.a;
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one
    this.registers.a = 7; // Always read and reread the instructions
    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    this.registers.a = 12; // Always read and reread the instructions
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                    a s s e m b u n n y . t s                   end
// ======================================================================
