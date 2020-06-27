// ======================================================================
// Balance Bots
//   Advent of Code 2016 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           b o t s . t s
//
// A solver for the Advent of Code 2016 Day 10 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------

interface GoesType {
  value: number;
  bot: number;
}

interface WhichType {
  which: string;
  num: number;
}

interface GivesDataType {
  low: WhichType;
  high: WhichType;
}

interface CompareType {
  low: number;
  high: number;
}

type HasType = number[];

type BotType = Record<number, HasType>;

type OutType = Record<number, HasType>;

type GivesType = Record<number, GivesDataType>;

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                   Bots
// ======================================================================

export class Bots {
  // Object for Balance Bots
  text: string[];

  part2: boolean;

  bots: BotType;

  outs: OutType;

  goes: GoesType[];

  gives: GivesType;

  hasTwo: HasType;

  constructor(text: string[], part2 = false) {
    // Create a Bot object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.bots = {};
    this.outs = {};
    this.goes = [];
    this.gives = {};
    this.hasTwo = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.goes = [];
    this.gives = {};
    // 2. Loop for all lines of text
    this.text.forEach((line) => {
      // 3. Divide the line into parts
      const parts = line.split(' ');
      // 4. Store goes and gives instructions
      //    value 5 goes to bot 2
      //    bot 2 gives low to bot 1 and high to bot 0
      if (parts[0] === 'value') {
        this.goes.push({ value: parseInt(parts[1], 10), bot: parseInt(parts[5], 10) });
      } else {
        this.gives[parseInt(parts[1], 10)] = {
          low: { which: parts[5], num: parseInt(parts[6], 10) },
          high: { which: parts[10], num: parseInt(parts[11], 10) },
        };
      }
    });
  }

  initialDistribution(): void {
    // 1. Reset the values
    this.bots = {};
    this.outs = {};
    this.hasTwo = [];
    // 2. Loop for all the initial distributions
    this.goes.forEach((goes) => {
      // 3. Add the value to the selected bot
      this.giveBot(goes.bot, goes.value);
    });
  }

  giveBot(bot: number, value: number): void {
    if (bot in this.bots) {
      this.bots[bot].push(value);
      if (this.bots[bot].length === 2) {
        this.hasTwo.push(bot);
      }
    } else {
      this.bots[bot] = [value];
    }
  }

  giveOut(out: number, value: number): void {
    if (out in this.outs) {
      this.outs[out].push(value);
    } else {
      this.outs[out] = [value];
    }
  }

  giveToBotOrOut(where: WhichType, value: number): void {
    if (where.which === 'output') {
      this.giveOut(where.num, value);
    } else {
      this.giveBot(where.num, value);
    }
  }

  distribute(bot: number, compare: CompareType): boolean {
    // 0. Precondition
    if (!(bot in this.bots) || !(bot in this.gives) || this.bots[bot].length !== 2) console.log(`Bad distribution bot=${bot}`);
    // 1. Get high and low values
    const high = Math.max(...this.bots[bot]);
    const low = Math.min(...this.bots[bot]);
    // 2. Distribute the high and low values
    this.giveToBotOrOut(this.gives[bot].high, high);
    this.giveToBotOrOut(this.gives[bot].low, low);
    // 3. Now the bot has none
    this.bots[bot] = [];
    // 4. Is this the comparison we were looking for?
    let result = false;
    if (high === compare.high && low === compare.low) result = true;
    return result;
  }

  whoCompares(value1: number, value2: number, verbose = false, limit = 0): number {
    if (verbose) console.log(`whoCompares: (${value1}, ${value2}) ${limit}`);
    // 1. Assume the worst
    let result = NaN;
    // 2. Set the desired value
    const compare: CompareType = {
      high: Math.max(value1, value2),
      low: Math.min(value1, value2),
    };
    // 3. Distribute initial values
    this.initialDistribution();
    // 3. Loop there is nothing to do
    while (this.hasTwo.length > 0) {
      // 4. Distribute from the first bot on the list
      const bot = this.hasTwo.shift() || 0;
      if (this.distribute(bot, compare)) {
        result = bot;
      }
    }
    // 5. Return which bot did the comparison (if any)
    return result;
  }

  multiplyOutputs(verbose = false, limit = 0): number {
    if (verbose) console.log(`multipleOutputs: ${limit}`);
    // 1. Assume the worst
    let result = NaN;
    // 2. Run the bots
    this.whoCompares(99, 99);
    // 3. Check the outputs
    if (0 in this.outs && 1 in this.outs && 2 in this.outs
      && this.outs[0].length === 1 && this.outs[1].length === 1 && this.outs[2].length === 1) {
      result = this.outs[0][0] * this.outs[1][0] * this.outs[2][0];
    }
    // 4. Return the product or NaN
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.multiplyOutputs(verbose, limit);
    }
    return this.whoCompares(61, 17, verbose, limit);
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
// end                          b o t s . t s                         end
// ======================================================================
