// ======================================================================
// Ticket Translation
//   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r u l e s . t s
//
// Rules for the Advent of Code 2020 Day 16 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Rule } from './rule';

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                                  Rules
// ======================================================================

export class Rules {
  // Object for Ticket Translation
  text: string[];

  part2: boolean;

  rules: Rule[];

  constructor(text: string[], part2 = false) {
    // Create a Rules object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rules = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(this.text);
    }
  }

  processText(text: string[]) {
    // Process the text: rules, my ticket, nearby tickets

    // 1. Loop fpr all of the text
    let section = 'rul';
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];

      // 2. Get the type of the line
      const ltype = line.substr(0, 3);

      // 3. Check for the end of the rules
      if (ltype === 'you' || ltype === 'nea') {
        section = ltype;
        break;
      }

      // 4. If still in the rules, save rule
      if (section === 'rul') {
        this.rules.push(new Rule(line, this.part2));
      }
    }
  }

  isValid(num: number): boolean {
    // Return true if the number matches any rule

    // 1. Loop for all the rules
    for (let indx = 0; indx < this.rules.length; indx += 1) {
      const rule = this.rules[indx];

      // 2. If this number is in the range for this rule, return true
      if (rule.isValid(num)) {
        return true;
      }
    }

    // 3. The number was not in the range of any rule, return false
    return false;
  }

  allValid(nums: number[]): boolean {
    // Return true if all of the number match some rule

    // 1. Loop for all the numbers
    for (let indx = 0; indx < nums.length; indx += 1) {
      const num = nums[indx];

      // 2. If this number is not in the range any rule, return false
      if (!this.isValid(num)) {
        return false;
      }
    }

    // 3. All number were in the range of some rule, return true
    return true;
  }

  determineFields(position: number, numbers: number[]) {
    // Determine which rules match all of these numbers
    // console.log(`determineFields(${position},${numbers})`);

    // 1. Loop for all of the rules
    for (let rindx = 0; rindx < this.rules.length; rindx += 1) {
      const rul = this.rules[rindx];

      // 2. If all of the numbers are valid for this rule, remember the position
      if (rul.allValid(numbers)) {
        rul.positions.push(position);
        // console.log(`dF: adding position ${position} to rule ${rul.name}`);
      }
    }
  }

  departureFields(nums: number[]): number {
    // Return the product of the departure fields

    // 1. Start with nothing
    let result = 1;

    // 2. Loop for all of the rules
    for (let rindx = 0; rindx < this.rules.length; rindx += 1) {
      const rul = this.rules[rindx];

      // 3. Only want departure fields
      if (rul.name.substr(0, 9) === 'departure') {
        // 4. Multiple the product by this field
        const nindx = rul.ticketIndex();
        if (nindx >= 0) {
          result *= nums[nindx];
        } else {
          console.log(`Unable to resolve field ${rul.name}`);
        }
      }
    }
    // 5. Return the product of the departure fields
    return result;
  }

  areFieldsResolved() {
    // Test is we need to continue rule resolution

    // 1. Loop for all of the rules
    for (let indx = 0; indx < this.rules.length; indx += 1) {
      const rul = this.rules[indx];

      // 2. If this rule is not resolved return false
      if (!rul.resolved()) {
        return false;
      }
    }

    // 3. All rules resolved, return true
    return true;
  }

  resolveFields() {
    // There can be only one

    // 1. Keep looping until every settles out
    while (!this.areFieldsResolved()) {
      // console.log('resolveFields loop');
      // 2. Loop for all of the rules
      for (let rindx = 0; rindx < this.rules.length; rindx += 1) {
        // 3. Get rules that could apply to this position (rule number == position number)
        const where = [];
        for (let r2indx = 0; r2indx < this.rules.length; r2indx += 1) {
          const rul = this.rules[r2indx];
          for (let indx = 0; indx < rul.positions.length; indx += 1) {
            const number = rul.positions[indx];
            if (number === rindx) {
              where.push(rul);
            }
          }
        }
        // 4. If there is only position for this rule, save it and remove from all other positions
        if (where.length === 1) {
          where[0].positions = [rindx];
          this.removePosition(rindx);
        }
      }
    }
  }

  removePosition(rnum: number) {
    // Remove the singleton rule from other rule positions

    // 1. Loop for all of the rules
    for (let rindx = 0; rindx < this.rules.length; rindx += 1) {
      const rul = this.rules[rindx];

      // 2. Don't mess with singleton rule
      if (rul.ticketIndex() !== rnum) {
        // 3. Remove the number from the non-singleton rule (if it is there)
        rul.remove(rnum);
      }
    }
  }
}

// ======================================================================
// end                         r u l e s . t s                        end
// ======================================================================
