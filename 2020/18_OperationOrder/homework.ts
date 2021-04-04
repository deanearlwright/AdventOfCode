// ======================================================================
// Operation Order
//   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           h o m e w o r k . t s
//
// A solver for the Advent of Code 2020 Day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Expression } from './expression';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Homework
// ======================================================================

export class Homework {
  // Object for Operation Order
  text: string[];

  part2: boolean;

  expressions: Expression[];

  constructor(text: string[], part2 = false) {
    // Create a Homework object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.expressions = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      for (let indx = 0; indx < this.text.length; indx += 1) {
        this.expressions.push(new Expression(this.text[indx], this.part2));
      }
    }
  }

  evaluateAll(): number {
    // Returns the sum of evaluatin all of the expressions
    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all the expressions
    for (let indx = 0; indx < this.expressions.length; indx += 1) {
      const expression = this.expressions[indx];

      // 3. Evaluate the expression
      const value = expression.evaluate();

      // 4. Accumulate the value of the expressions
      result += value;
    }

    // 5. Return the sum of the evaluated expressions
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    return this.evaluateAll();
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
// end                      h o m e w o r k . t s                     end
// ======================================================================
