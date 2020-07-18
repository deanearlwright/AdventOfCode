// ======================================================================
// Scrambled Letters and Hash
//   Advent of Code 2016 Day 21 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p w o r d . t s
//
// A solver for the Advent of Code 2016 Day 21 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Operand = 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | 'X';
type Actions = 'swap position'
| 'swap letter'
| 'rotate left'
| 'rotate right'
| 'rotate based'
| 'reverse positions'
| 'move position';
type Instruction = {
  action: Actions,
  op1: Operand,
  op2: Operand,
};
type Instructions = Instruction[];
type Op2num = Record<Operand, number>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const UNUSED = 'X';
const START = 'abcdefgh';
const FINISH = 'fbgdceah';

const OP2NUM: Op2num = {
  a: -1,
  b: -1,
  c: -1,
  d: -1,
  e: -1,
  f: -1,
  g: -1,
  h: -1,
  0: 0,
  1: 1,
  2: 2,
  3: 3,
  4: 4,
  5: 5,
  6: 6,
  7: 7,
  8: 8,
  9: 9,
  X: -1,
};

const UNSCRAMBLE_ROTATE_BASED_5 = [1, 3, 0, 2, 4];
const UNSCRAMBLE_ROTATE_BASED_8 = [1, 1, 6, 2, 7, 3, 0, 4];
// ======================================================================
//                                                                  Pword
// ======================================================================

export class Pword {
  // Object for Scrambled Letters and Hash
  text: string[];

  part2: boolean;

  instructions: Instructions;

  start: string;

  finish: string;

  constructor(text: string[], part2 = false) {
    // Create a Pword object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.instructions = [];
    this.start = START;
    this.finish = FINISH;

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.instructions = [];
    // 2. Loop for all lines of the text
    this.text.forEach((line) => {
      // 3. Split the line up
      const parts = line.split(' ');
      // 4. Decode based on the first word
      switch (parts[0]) {
        case 'swap':
          // 4a. swap letter l1 l2 and position p1 p2
          switch (parts[1]) {
            case 'letter':
              this.instructions.push({
                action: 'swap letter',
                op1: <Operand>parts[2],
                op2: <Operand>parts[5],
              });
              break;
            case 'position':
              this.instructions.push({
                action: 'swap position',
                op1: <Operand>parts[2],
                op2: <Operand>parts[5],
              });
              break;
            default:
              console.log(`Unexpected swap instruction ${line}`);
              break;
          }
          break;
        case 'rotate':
          // 4b. rotate left n1, right n1, and based l1
          switch (parts[1]) {
            case 'left':
              this.instructions.push({
                action: 'rotate left',
                op1: <Operand>parts[2],
                op2: UNUSED,
              });
              break;
            case 'right':
              this.instructions.push({
                action: 'rotate right',
                op1: <Operand>parts[2],
                op2: UNUSED,
              });
              break;
            case 'based':
              this.instructions.push({
                action: 'rotate based',
                op1: <Operand>parts[6],
                op2: UNUSED,
              });
              break;
            default:
              console.log(`Unexpected rotate instruction ${line}`);
              break;
          }
          break;
        case 'reverse':
          // 4c. reverse positions p1 p2
          this.instructions.push({
            action: 'reverse positions',
            op1: <Operand>parts[2],
            op2: <Operand>parts[4],
          });
          break;
        case 'move':
          // 4d move positions p1 p2
          this.instructions.push({
            action: 'move position',
            op1: <Operand>parts[2],
            op2: <Operand>parts[5],
          });
          break;
        default:
          console.log(`Unexpected instruction ${line}`);
      }
    });
  }

  static execute(inst: Instruction, input: string): string {
    const result = input.split('');
    let swap = '?';
    let index1 = OP2NUM[inst.op1];
    let index2 = OP2NUM[inst.op2];
    // console.log(`execute ${index1} ${index2} ${inst.action} ${inst.op1} ${inst.op2}`);
    let subArray: string[] = [];
    switch (inst.action) {
      case 'swap position':
        swap = result[index1];
        result[index1] = result[index2];
        result[index2] = swap;
        break;
      case 'swap letter':
        index1 = result.indexOf(inst.op1);
        index2 = result.indexOf(inst.op2);
        swap = result[index1];
        result[index1] = result[index2];
        result[index2] = swap;
        break;
      case 'rotate left':
        for (let index = index1; index > 0; index -= 1) {
          result.push(<string>result.shift());
        }
        break;
      case 'rotate right':
        for (let index = index1; index > 0; index -= 1) {
          result.unshift(<string>result.pop());
        }
        break;
      case 'rotate based':
        // - rotate based on position of letter X means that the whole string
        //   should be rotated to the right based on the index of letter X
        //   (counting from 0) as determined before this instruction does any
        //   rotations. Once the index is determined, rotate the string to the
        //   right one time, plus a number of times equal to that index, plus
        //   one additional time if the index was at least 4.
        // - rotate based on position of letter b finds the index of letter b (1),
        //   then rotates the string right once plus a number of times equal to
        //   that index (2)
        //      abdec --> ecabd.
        //  - rotate based on position of letter d finds the index of letter d (4),
        //    then rotates the string right once, plus a number of times equal to
        //    that index, plus an additional time because the index was at least 4,
        //    for a total of 6 right rotations
        //      ecabd --> decab.
        index1 = result.indexOf(inst.op1);
        index1 += index1 >= 4 ? 2 : 1;
        for (let index = index1; index > 0; index -= 1) {
          result.unshift(<string>result.pop());
        }
        break;
      case 'reverse positions':
        subArray = result.slice(index1, index2 + 1);
        for (let index = index1; index <= index2; index += 1) {
          result[index] = <string>subArray.pop();
        }
        break;
      case 'move position':
        // - move position X to position Y means that the letter which is at index
        //   X should be removed from the string, then inserted such that it ends
        //   up at index Y.
        // - move position 1 to position 4 removes the letter at position 1 (c),
        //   then inserts it at position 4 (the end of the string)
        //     bcdea --> bdeac.
        // - move position 3 to position 0 removes the letter at position 3 (a),
        //   then inserts it at position 0 (the front of the string)
        //     bdeac --> abdec.
        swap = result[index1];
        if (index1 < index2) {
          for (let index = index1; index < index2; index += 1) {
            result[index] = result[index + 1];
          }
        } else if (index1 > index2) {
          for (let index = index1; index > index2; index -= 1) {
            result[index] = result[index - 1];
          }
        }
        result[index2] = swap;
        break;
      default:
        console.log(`Unable to execute instruction ${inst.action} ${inst.op1} ${inst.op2}`);
        break;
    }
    return result.join('');
  }

  scramble(verbose = false, limit = 0): string {
    if (verbose) console.log(`scramble of ${this.start}, limit=${limit}`);
    // 1. Start at the start
    let result = this.start;
    // 2. Loop for all of the instructions
    this.instructions.forEach((inst) => {
      // 3. Execute the instruction
      const next = Pword.execute(inst, result);
      if (verbose) console.log(`scramble ${result} --> ${next} inst ${inst.action} ${inst.op1} ${inst.op2}`);
      // 4. The scrample is now the result
      result = next;
    });
    // 5. Return the final scrambled result
    return result;
  }

  static reverse(inst: Instruction, input: string): string {
    const result = input.split('');
    let swap = '?';
    let index1 = OP2NUM[inst.op1];
    let index2 = OP2NUM[inst.op2];
    // console.log(`reverse ${index1} ${index2} ${inst.action} ${inst.op1} ${inst.op2}`);
    let subArray: string[] = [];
    switch (inst.action) {
      case 'swap position': // reverse is same as execute
        swap = result[index1];
        result[index1] = result[index2];
        result[index2] = swap;
        break;
      case 'swap letter': // reverse is same as execute
        index1 = result.indexOf(inst.op1);
        index2 = result.indexOf(inst.op2);
        swap = result[index1];
        result[index1] = result[index2];
        result[index2] = swap;
        break;
      case 'rotate left': // reverse is rotate right
        for (let index = index1; index > 0; index -= 1) {
          result.unshift(<string>result.pop());
        }
        break;
      case 'rotate right': // reverse if rotate left
        for (let index = index1; index > 0; index -= 1) {
          result.push(<string>result.shift());
        }
        break;
      case 'rotate based':
        // reverse has left rotate instead of right
        // but count determined empirically
        index1 = result.indexOf(inst.op1);
        index1 = result.length === 8 ? UNSCRAMBLE_ROTATE_BASED_8[index1]
          : UNSCRAMBLE_ROTATE_BASED_5[index1];
        for (let index = index1; index > 0; index -= 1) {
          result.push(<string>result.shift());
        }
        break;
      case 'reverse positions': // reverse is same as execute
        subArray = result.slice(index1, index2 + 1);
        for (let index = index1; index <= index2; index += 1) {
          result[index] = <string>subArray.pop();
        }
        break;
      case 'move position': // reverse swaps the indexes
        // - move position X to position Y means that the letter which is at index
        //   X should be removed from the string, then inserted such that it ends
        //   up at index Y.
        // - move position 1 to position 4 removes the letter at position 1 (c),
        //   then inserts it at position 4 (the end of the string)
        //     bcdea --> bdeac.
        // - move position 3 to position 0 removes the letter at position 3 (a),
        //   then inserts it at position 0 (the front of the string)
        //     bdeac --> abdec.
        index2 = OP2NUM[inst.op1];
        index1 = OP2NUM[inst.op2];
        swap = result[index1];
        if (index1 < index2) {
          for (let index = index1; index < index2; index += 1) {
            result[index] = result[index + 1];
          }
        } else if (index1 > index2) {
          for (let index = index1; index > index2; index -= 1) {
            result[index] = result[index - 1];
          }
        }
        result[index2] = swap;
        break;
      default:
        console.log(`Unable to execute instruction ${inst.action} ${inst.op1} ${inst.op2}`);
        break;
    }
    return result.join('');
  }

  unscramble(verbose = false, limit = 0): string {
    if (verbose) console.log(`unscramble of ${this.finish}, limit=${limit}`);
    // 1. Start at the end
    let result = this.finish;
    // 2. Loop for all of the instructions (in reverse)
    for (let index = this.instructions.length - 1; index >= 0; index -= 1) {
      const inst = this.instructions[index];
      // 3. Execute the instruction
      const next = Pword.reverse(inst, result);
      if (verbose) console.log(`unscramble ${result} --> ${next} inst ${inst.action} ${inst.op1} ${inst.op2}`);
      // 4. The scrample is now the result
      result = next;
    }
    // 5. Return the final scrambled result
    return result;
  }

  solution(verbose = false, limit = 0): string {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.unscramble(verbose, limit);
    }
    return this.scramble(verbose, limit);
  }

  partOne(verbose = false, limit = 0): string {
    // Returns the solution for part one

    return this.solution(verbose, limit);
  }

  partTwo(verbose = false, limit = 0): string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

// ======================================================================
// end                         p w o r d . t s                        end
// ======================================================================
