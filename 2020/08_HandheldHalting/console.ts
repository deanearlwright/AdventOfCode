// ======================================================================
// Handheld Halting
//   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           c o n s o l e . t s
//
// A solver for the Advent of Code 2020 Day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Instruction } from './instruction';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type PC = number;
type ACC = number;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Console
// ======================================================================

export class Console {
  // Object for Handheld Halting
  text: string[];

  part2: boolean;

  instructions: Instruction[];

  pc: PC;

  acc: ACC;

  constructor(text: string[], part2 = false) {
    // Create a Console object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.instructions = [];
    this.pc = 1;
    this.acc = 0;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.instructions.push(new Instruction('nop +0'));
      for (let indx = 0; indx < this.text.length; indx += 1) {
        this.instructions.push(new Instruction(this.text[indx]));
      }
    }
  }

  infinite_loop(): number {
    // Return the accumulator before the program would run an instruction a second time

    // 1. Reset the console
    this.pc = 1;
    this.acc = 0;

    // 2. Loop until stopped
    while (this.pc > 0 && this.pc < this.instructions.length) {
      // console.log(`infinite_loop ${this.pc} ${this.acc}`);
      // 3. Exit with the accumulator value if we have seen this instruction before
      const inst = this.instructions[this.pc];
      if (inst.is_visited()) {
        return this.acc;
      }
      // 4. Execute the instruction
      const [acc, delta] = inst.execute(this.acc);
      this.acc = acc;
      this.pc += delta;
    }
    // 5. I guess the loop wasn't so infinate after all
    return NaN;
  }

  reset_visited() {
    // Reset the visited flag in all of the instructions

    // 1. Loop for all of the instructions
    for (let indx = 0; indx < this.instructions.length; indx += 1) {
      const inst = this.instructions[indx];
      // 2. Reset the visited flag on this instruction
      inst.reset();
    }
  }

  fix_the_program(): number {
    // Return the value of the accumulator after the fixed program terminates

    // 1. Loop for every instruction
    for (let indx = 1; indx < this.instructions.length; indx += 1) {
      const inst = this.instructions[indx];
      // 2. Ignore acc instructions
      if (inst.operation !== 'acc') {
        // 3. Replace jmp with nop and nop with jmp
        const original = inst.operation;
        // console.log(`fix_the_program ${indx} ${original}`);
        if (original === 'jmp') {
          inst.operation = 'nop';
        } else {
          inst.operation = 'jmp';
        }
        // 4. Execute the new program
        const result = this.infinite_loop();
        // 5. If we corrected the program, return the accumulator
        if (Number.isNaN(result)) {
          return this.acc;
        }
        // 6. Reset the instruction operation back to the way it was originally
        inst.operation = original;
        // 7. Reset all of the visited flags
        this.reset_visited();
      }
    }
    // 8. We tried to fixed every instruction but nothing worked
    return NaN;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.fix_the_program();
    }
    return this.infinite_loop();
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
// end                       c o n s o l e . t s                      end
// ======================================================================
