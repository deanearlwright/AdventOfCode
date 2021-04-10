// ======================================================================
// Monster Messages
//   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           r u l e s . t s
//
// A solver for the Advent of Code 2020 Day 19 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
import { Rule } from './rule';

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
type Grammar = Record<number, Rule>;

// ======================================================================
//                                                                  Rules
// ======================================================================

export class Rules {
  // Object for Monster Messages
  text: string[];

  part2: boolean;

  rules: Grammar;

  messages: string[];

  constructor(text: string[], part2 = false) {
    // Create a Rules object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.rules = {};
    this.messages = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText(text);
    }
  }

  processText(text: string[]) {
    // Assign values from text -- rules then messages

    // 1. Loop for all of the lines of the text
    for (let indx = 0; indx < text.length; indx += 1) {
      const line = text[indx];

      // 2. If the line has a colon then it is a rule
      if (line.indexOf(':') !== -1) {
        const rule = new Rule(line, this.part2);
        this.rules[rule.number] = rule;
      } else {
        // 3. Otherwise it is a message to process
        this.messages.push(line);
      }
    }
  }

  tryRule(num: number, msg: string): string[] {
    // Try to match the message against the specified rule
    // Returns [] on failure or the remaining characters to match

    // 1. Get the rule in question
    const rule = this.rules[num];

    // 2. If the rule is for a letter, the message must start with that letter
    if (rule.isConstant()) {
      if (msg.length > 0 && msg.startsWith(rule.letter())) {
        return [msg.substr(1)];
      }
      return [];
    }

    // 3. Start with nothing
    const result: string[] = [];

    // 4. Try to match each (or only) alternative of the rule
    const alternatives = rule.alternatives();
    for (let aindx = 0; aindx < alternatives.length; aindx += 1) {
      const alternative = alternatives[aindx];

      // 5. Try matching and get the remainder of the message after matching
      const remaining = this.tryRules(alternative, msg);

      // 6. If match, remember what still needs to be matched
      for (let rindx = 0; rindx < remaining.length; rindx += 1) {
        result.push(remaining[rindx]);
      }
    }

    // Return the results of the matches (characters left to match) or [] if no matches
    return result;
  }

  tryRules(nums: string, msg: string): string[] {
    // Try to match a string of rules to the message
    // Returns [] on failure or list of characters remaining to match

    // 1. We want to match the entire message initially but
    //    as we match the rules we want to match against the remaining
    //    characters of the message (which different ruls may have different possibilities)
    let messages = [msg];

    // 2. Loop for each rule in the (possibly partial) rule definition
    const numbers = nums.split(' ');
    for (let indx = 0; indx < numbers.length; indx += 1) {
      const num = parseInt(numbers[indx], 10);

      // 3. Match each rule in the definition keeping track of what remains
      const remains: string[] = [];
      for (let mindx = 0; mindx < messages.length; mindx += 1) {
        const remaining = this.tryRule(num, messages[mindx]);
        for (let rindx = 0; rindx < remaining.length; rindx += 1) {
          remains.push(remaining[rindx]);
        }
      }

      // 4. If we match nothing, this defination is a bust
      if (remains.length === 0) {
        return [];
      }

      // 5. What the matching rule left behind must be matched by the next
      messages = remains;
    }

    // 6. Return what this rule definition did not match
    return messages;
  }

  matchRule(num: number, msg: string): boolean {
    // Returns true if the specified rule matches the message

    // 1. Get the the rule matches
    const matches = this.tryRule(num, msg);

    // 2. Loop for all of the matches
    for (let indx = 0; indx < matches.length; indx += 1) {
      const remains = matches[indx];

      // 3. If there an exact match, return true
      if (remains.length === 0) {
        return true;
      }
    }

    // 4. Nothing matched (or matched completely) so return false
    return false;
  }

  countZero(): number {
    // Return the number of messages that match rule 0 exactly

    // 1. Start with nothing
    let result = 0;

    // 2. Loop for all of the messages
    for (let indx = 0; indx < this.messages.length; indx += 1) {
      // 3. Increment the count if the rule 0 matches the message
      if (this.matchRule(0, this.messages[indx])) {
        result += 1;
      }
    }

    // 4. Return the count of messages that matched rule 0
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      const new8 = new Rule('8: 42 | 42 8', true);
      const new11 = new Rule('11: 42 31 | 42 11 31', true);
      this.rules[8] = new8;
      this.rules[11] = new11;
    }
    return this.countZero();
  }

  partOne(verbose = false, limit = 0): number {
    // Returns the solution for part one

    return this.solution(verbose, limit); // 124
  }

  partTwo(verbose = false, limit = 0): number {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return this.solution(verbose, limit); // 228
  }
}

// ======================================================================
// end                         r u l e s . t s                        end
// ======================================================================
