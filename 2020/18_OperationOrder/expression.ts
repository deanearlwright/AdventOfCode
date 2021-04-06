// ======================================================================
// Operation Order
//   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           e x p r e s s i o n . t s
//
// Expression for the Advent of Code 2020 Day 18 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Token = string;
type Tokens = Token[];

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const RE_LEFT = /\(/g;
const RE_RIGHT = /\)/g;
const RE_SPACES = / +/g;

// ======================================================================
//                                                             Expression
// ======================================================================

export class Expression {
  // Object for Operation Order
  text: string;

  part2: boolean;

  tokens: Tokens;

  constructor(text: string, part2 = false) {
    // Create a Expression object

    // 1. Set the initial values
    this.text = text === undefined ? '' : text;
    this.part2 = part2 === undefined ? false : part2;
    this.tokens = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(text);
    }
  }

  processText(text: string) {
    // Assign values from text

    // 1. Add space around parens to ease splitting
    const spaced = text.replace(RE_LEFT, ' ( ').replace(RE_RIGHT, ' ) ').replace(RE_SPACES, ' ').trim();

    // 2. Split on spaces to get tokens
    this.tokens = spaced.split(' ');
  }

  evaluate(): number {
    // Returns the result of evaluating the entire expression
    return this.evaluateTokens(this.tokens);
  }

  evaluateTokens(tokens: Tokens): number {
    // Evaluate the tokens

    // 1. Get the left operand
    const [leftTokens, opTokens] = this.getOperand(tokens, '+');
    let leftValue = 0;
    if (leftTokens.length === 1) {
      leftValue = parseInt(leftTokens[0], 10);
    } else {
      leftValue = this.evaluateTokens(leftTokens);
    }
    if (opTokens.length === 0) {
      return leftValue;
    }

    // 2. Get the operation
    const operation = opTokens[0];

    // 3. Get the right operand
    const [rightTokens, moreTokens] = this.getOperand(opTokens.slice(1), operation);
    let rightValue = 0;
    if (rightTokens.length === 1) {
      rightValue = parseInt(rightTokens[0], 10);
    } else {
      rightValue = this.evaluateTokens(rightTokens);
    }

    // 4. Execute the operation
    let result = 0;
    switch (operation) {
      case '+':
        result = leftValue + rightValue;
        break;
      case '*':
        result = leftValue * rightValue;
        break;
      default:
        console.log(`Illegal operation: ${operation}`);
    }

    // 5. If no more tokens we are done
    if (moreTokens.length === 0) {
      return result;
    }

    // 6. Still more work to do
    moreTokens.splice(0, 0, `${result}`);
    return this.evaluateTokens(moreTokens);
  }

  getOperand(tokens: Tokens, lastOP: Token): [Tokens, Tokens] {
    // Returns the tokens for the next operand and the rest of the tokens

    // 1. Easy to handle a single token
    if (tokens.length === 1) {
      return [tokens, []];
    }

    // 2. Get operand tokens()
    if (this.part2 && lastOP === '*') {
      return [[`${this.evaluateTokens(tokens)}`], []];
    }
    if (tokens[0] === '(') {
      return this.getParen(tokens.slice(1));
    }
    return [[tokens[0]], tokens.slice(1)];
  }

  // eslint-disable-next-line class-methods-use-this
  getParen(tokens: Tokens): [Tokens, Tokens] {
    // Returns the parenthetical expression (minus parens) and the remaining tokens
    // 1. Start with nothing
    let depth = 0;

    // 2. Loop until we run out of tokens
    for (let indx = 0; indx < tokens.length; indx += 1) {
      // 3. Get the next token
      const token = tokens[indx];

      // 4. If this is the closing paren, return the collected within and remaining tokens
      if (token === ')' && depth === 0) {
        return [tokens.slice(0, indx), tokens.slice(indx + 1)];
      }

      // 5. If this is a closing paren, but not THE closing paren, decrease paren depth
      if (token === ')') {
        depth -= 1;
        if (depth < 0) {
          console.log('Too many closing parens');
          return [[], []];
        }
        // 6. If another opening paren, increase paren depth
      } else if (token === '(') {
        depth += 1;
      }
    }
    // 7. No closing paren
    console.log('Missing closing paren');
    return [[], []];
  }
}

// ======================================================================
// end                    e x p r e s s i o n . t s                   end
// ======================================================================
