// ======================================================================
// Handheld Halting
//   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           i n s t r u c t i o n . t s
//
// Instruction for the Advent of Code 2020 Day 08 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_OP = /[a-z][a-z][a-z]/;
const RE_ARG = /[-+0-9]+/;

// ======================================================================
//                                                            Instruction
// ======================================================================

export class Instruction {
  // Object for Handheld Halting
  text: string;

  part2: boolean;

  operation: string;

  argument: number;

  visited: boolean;

  constructor(text: string, part2 = false) {
    // Create a Instruction object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.operation = '';
    this.argument = 0;
    this.visited = false;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      let ok = this.text.match(RE_OP);
      if (ok) {
        [this.operation] = ok;
      } else {
        console.log(`'Unable to parse operation from ${this.text}`);
      }
      ok = this.text.match(RE_ARG);
      if (ok) {
        this.argument = parseInt(ok[0], 10);
      } else {
        console.log(`'Unable to parse operation from ${this.text}`);
      }
    }
  }

  execute(acc: number): number[] {
    // Execute the instruction and return the new accumulator and pc delta
    let delta = 1;
    let accumulator = acc;

    // 1. Mark instruction as visited
    this.visited = true;

    // 2. Switch based on the operation
    switch (this.operation) {
      case 'acc':
        accumulator += this.argument;
        break;
      case 'jmp':
        delta = this.argument;
        break;
      case 'nop':
        break;
      default:
        console.log(`Unimplemented operation ${this.operation}`);
    }

    // 3. Return the new accumulator and change to PC
    return [accumulator, delta];
  }

  is_visited(): boolean {
    // Returns true if this instruction has been visited before
    return this.visited;
  }

  reset() {
    // Reset the visited flag
    this.visited = false;
  }
}

// ======================================================================
// end                   i n s t r u c t i o n . t s                  end
// ======================================================================
