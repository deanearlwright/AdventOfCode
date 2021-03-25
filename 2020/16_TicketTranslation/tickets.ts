// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           t i c k e t s . t s
//
// A solver for the Advent of Code 2020 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Ticket } from './ticket';
import { Rules } from './rules';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                Tickets
// ======================================================================

export class Tickets {
  // Object for Ticket Translation
  text: string[];

  part2: boolean;

  rules: Rules;

  mine: Ticket;

  nearby: Ticket[];

  constructor(text: string[], part2 = false) {
    // Create a Tickets object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rules = new Rules([], this.part2);
    this.mine = new Ticket('', this.part2);
    this.nearby = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string[]) {
    // Process the text: rules, my ticket, nearby tickets

    // 1. Start with the rules
    this.rules = new Rules(text, this.part2);

    // 2. Process the tickets
    let section = '???';
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];

      // 3. Get the type of the line
      const ltype = line.substr(0, 3);

      // 4. Process the line based on the line type
      if (ltype === 'you' || ltype === 'nea') {
        section = ltype;
      } else if (section === 'you') {
        this.mine = new Ticket(line, this.part2);
      } else if (section === 'nea') {
        this.nearby.push(new Ticket(line, this.part2));
      }
    }
  }

  scanningErrorRate(): number {
    // Return the ticket scanning error rate (sum of invalid values)

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the nearby tickets
    for (let tindx = 0; tindx < this.nearby.length; tindx += 1) {
      const tick = this.nearby[tindx];

      // 3. Loop for all of the numbers on the ticket
      for (let nindx = 0; nindx < tick.numbers.length; nindx += 1) {
        const num = tick.numbers[nindx];

        // 4. If this number is not valid, add it to the result (and mark ticket invalid)
        if (!this.rules.isValid(num)) {
          result += num;
          tick.valid = false;
        }
      }
    }

    // 5. Return the sum of invalid numbers
    return result;
  }

  departureFields(): number {
    // Return the product of the departure fields

    // 1. Mark invalid tickets as such
    this.scanningErrorRate();

    // 2. Find the field positions
    this.findFieldPositions();

    // 3. Return product of the departure fields
    return this.rules.departureFields(this.mine.numbers);
  }

  findFieldPositions() {
    // Find the position for each field

    // 1. Loop for each position of the tickets
    for (let pindx = 0; pindx < this.mine.length(); pindx += 1) {
      // 2. Get the numbers for that position from nearby valid tickers
      const numbers: number[] = [];
      for (let tindx = 0; tindx < this.nearby.length; tindx += 1) {
        const tick = this.nearby[tindx];
        if (tick.valid) {
          numbers.push(tick.numbers[pindx]);
        }
      }
      // 3. Determine the fields for those number
      this.rules.determineFields(pindx, numbers);
    }
    // 4. Resolve conflict in field assignment
    this.rules.resolveFields();
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.departureFields();
    }
    return this.scanningErrorRate();
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
// end                       t i c k e t s . t s                      end
// ======================================================================
