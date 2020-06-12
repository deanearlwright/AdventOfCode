/* eslint-disable linebreak-style */
// ======================================================================
// It Hangs in the Balance
//   Advent of Code 2015 Day 24 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           p a c k a g e s . j s
//
// A solver for the Advent of Code 2015 Day 24 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
const comb = require('js-combinatorics');

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------

// ======================================================================
//                                                               Packages
// ======================================================================

class Packages {
  // Object for It Hangs in the Balance

  constructor(options) {
    // Create a Packages object

    // 1. Set the initial values
    this.text = options.text === undefined ? [] : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.weights = [];
    this.compartments = this.part2 ? 4 : 3;
    this.target = this.weights.reduce((pv, cv) => pv + cv, 0) / this.compartments;

    // 2. Process text (if any)
    if (this.text.length > 0) {
      this.processText(this.text);
      this.target = this.weights.reduce((pv, cv) => pv + cv, 0) / this.compartments;
    }
  }

  processText(text) {
    // 1. Start with nothing
    this.weights = [];
    // 2. Loop for all of the lines of text
    text.forEach((line) => {
      // 3. Get the weight
      const weight = parseInt(line, 10);
      this.weights.push(weight);
    });
  }


  solution(verbose, limit) {
    // 1. Start with nothing
    const packings = [];
    let n = 1;
    // 1. Work from the smallest number of packages to the largest
    while (packings.length === 0 && (limit === 0 || n < limit) && n <= this.weights.length) {
      // 2. Loop for all of the permutations of that number of weights
      // eslint-disable-next-line no-console
      if (verbose) console.log(`Trying groups of ${n} packages to reach ${this.target}`);
      comb.permutation(this.weights, n).forEach((packages) => {
        // 3. If the packages weight one third, save that package combimation
        if (packages.reduce((pv, cv) => pv + cv, 0) === this.target) packings.push(packages);
      });
      // 4. Try with more packages
      n += 1;
    }
    // eslint-disable-next-line no-console
    if (verbose) console.log(`Found ${packings.length} combinations of ${n - 1} packages with a combined weight of ${this.target}`);
    // 5. Get the smallest quantum entanglement of the packing with the best legroom
    let entanglement = 999999999999999999;
    packings.forEach((pack) => {
      const qe = pack.reduce((pv, cv) => pv * cv, 1);
      if (qe < entanglement) entanglement = qe;
    });
    // 4. Return smallest quantum entanglement
    // eslint-disable-next-line no-console
    if (verbose) console.log(`Lowest entanglement is ${entanglement}`);
    return entanglement;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.solution(verbose, limit);
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.solution(verbose, limit);
  }
}

module.exports.Packages = Packages;
// ======================================================================
// end                      p a c k a g e s . j s                     end
// ======================================================================
