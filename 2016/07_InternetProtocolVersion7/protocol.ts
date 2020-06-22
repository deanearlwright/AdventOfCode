// ======================================================================
// Internet Protocol Version 7
//   Advent of Code 2016 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// TypeScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p r o t o c o l . t s
//
// A solver for the Advent of Code 2016 Day 07 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                                  types
// ----------------------------------------------------------------------
interface IP7Addr {
  complete: string;
  hyperNets: string[];
  notHyperNets: string[];
  tls: boolean;
  ssl: boolean;
}

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const reHypernetSplit = /\[[a-z]+\]/;
// const reHypernetKeep = /\[([a-z]+)\]/g;

// ======================================================================
//                                                               Protocol
// ======================================================================

export class Protocol {
  // Object for Internet Protocol Version 7
  text: string[];

  part2: boolean;

  addresses: IP7Addr[];

  constructor(text: string[], part2 = false) {
    // Create a Protocol object

    // 1. Set the initial values
    this.text = text === undefined ? [] : text;
    this.part2 = part2 === undefined ? false : part2;
    this.addresses = [];

    // 2. Process text (if any)
    if (this.text.length !== 0) {
      this.processText();
    }
  }

  processText(): void {
    // 1. Start with nothing
    this.addresses = [];
    // 2. Loop for every line in the text
    this.text.forEach((line) => {
      // 3. Start with nothing
      const ip7: IP7Addr = {
        complete: line,
        hyperNets: [],
        notHyperNets: line.split(reHypernetSplit),
        tls: false,
        ssl: false,
      };

      // 4. Find the hypernets without using matchAll or exec (whose types are not working)
      let leftBracket = line.indexOf('[');
      while (leftBracket > -1) {
        const rightBracket = line.indexOf(']', leftBracket + 1);
        if (rightBracket === -1) {
          console.log(`Missing ] for [ at ${leftBracket} in ${line}`);
        } else {
          ip7.hyperNets.push(line.substring(leftBracket + 1, rightBracket));
        }
        leftBracket = line.indexOf('[', rightBracket + 1);
      }
      // 5. Compute tls and ssl
      ip7.tls = Protocol.supportTLS(ip7);
      ip7.ssl = Protocol.supportSSL(ip7);
      // 6. Add address
      this.addresses.push(ip7);
    });
  }

  static hasABBA(text: string): boolean {
    // 1. Loop for all four character groups
    for (let index = 0; index < text.length - 3; index += 1) {
      // 2. Is the grouping an abba?
      if (text[index] !== text[index + 1]
        && text[index + 1] === text[index + 2]
        && text[index] === text[index + 3]) return true;
    }
    return false;
  }

  static hasABA(text: string): boolean {
    // 1. Loop for all three character groups
    for (let index = 0; index < text.length - 2; index += 1) {
      // 2. Is the grouping an aba? If so, return true
      if (text[index] !== text[index + 1]
        && text[index] === text[index + 2]) return true;
    }
    // 3. No aba found, return false
    return false;
  }

  static allABA(text: string): string[] {
    // 1. Start with nothing
    const result = [];
    // 1. Loop for all three character groups
    for (let index = 0; index < text.length - 2; index += 1) {
      // 2. Is the grouping an aba? If so, save it
      if (text[index] !== text[index + 1]
        && text[index] === text[index + 2]) result.push(text.substring(index, index + 3));
    }
    // 3. Return all the aba's that we found
    return result;
  }

  static hasBAB(text: string, aba: string[]): boolean {
    // 1. Loop for all three character aba groups
    for (let index = 0; index < aba.length; index += 1) {
      // 2. Generate the bab from the aba
      const bab = aba[index][1] + aba[index][0] + aba[index][1];
      // 3. Does it exist in the text?
      if (text.indexOf(bab) >= 0) return true;
    }
    // 4. No matching bab found, return false
    return false;
  }

  static supportTLS(ip7: IP7Addr): boolean {
    // 1. Assume the best
    let result = false;
    // 2. Must have abba sequence in non hyperNet
    ip7.notHyperNets.forEach((text) => {
      if (Protocol.hasABBA(text)) result = true;
      // console.log(`notHyperNets ${ip7.complete}`);
    });
    // 3. Can't have abba sequence in jyperNet
    if (result) {
      ip7.hyperNets.forEach((text) => {
        if (Protocol.hasABBA(text)) result = false;
        // console.log(`hyperNets ${ip7.complete}`);
      });
    }
    return result;
  }

  numberTLS(verbose = false, limit = 0): number {
    if (verbose) console.log(`numberTLS: ${limit}`);
    // 1. Start with none
    let result = 0;
    // 2. Loop for all the addresses
    this.addresses.forEach((addr) => {
      if (addr.tls) result += 1;
    });
    // 4. Return the count
    return result;
  }

  static supportSSL(ip7: IP7Addr): boolean {
    // 1. Loop for all of the non hyperNet portions
    for (let notIndex = 0; notIndex < ip7.notHyperNets.length; notIndex += 1) {
      // 2. Get the ABAs (if any)
      const myABAs = Protocol.allABA(ip7.notHyperNets[notIndex]);
      // 3. At least one of those aba must be a bab in hyperNet
      if (myABAs.length > 0) {
        for (let hyperIndex = 0; hyperIndex < ip7.hyperNets.length; hyperIndex += 1) {
          if (Protocol.hasBAB(ip7.hyperNets[hyperIndex], myABAs)) return true;
        }
      }
    }
    // 4. Otherwise return false
    return false;
  }

  numberSSL(verbose = false, limit = 0): number {
    if (verbose) console.log(`numberSSL: ${limit}`);
    // 1. Start with none
    let result = 0;
    // 2. Loop for all the addresses
    this.addresses.forEach((addr) => {
      if (addr.ssl) result += 1;
    });
    // 4. Return the count
    return result;
  }

  solution(verbose = false, limit = 0): number {
    if (verbose) console.log(`solution: ${limit}`);
    if (this.part2) {
      return this.numberSSL();
    }
    return this.numberTLS();
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
// end                      p r o t o c o l . t s                     end
// ======================================================================
