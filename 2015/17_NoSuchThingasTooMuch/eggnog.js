/* eslint-disable linebreak-style */
// ======================================================================
// No Such Thing as Too Much
//   Advent of Code 2015 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// JavaScript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           e g g n o g . j s
//
// A solver for the Advent of Code 2015 Day 17 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const DEFAULT_LITERS = 150;

// ======================================================================
//                                                                 Eggnog
// ======================================================================

class Eggnog {
  // Object for No Such Thing as Too Much

  constructor(options) {
    // Create a Eggnog object

    // 1. Set the initial values
    this.text = options.text === undefined ? null : options.text;
    this.part2 = options.part2 === undefined ? false : options.part2;
    this.liters = options.liters === undefined ? DEFAULT_LITERS : options.liters;
    this.containers = [];

    // 2. Process text (if any)
    if (this.text !== null) {
      this.processText(this.text);
    }
  }

  processText(text) {
    this.containers = [];
    text.forEach((line) => {
      const size = parseInt(line, 10);
      this.containers.push(size);
    });
  }

  sumToLiters(containers) {
    let sum = 0;
    containers.forEach((size) => {
      sum += size;
    });
    return sum === this.liters;
  }

  numberSolutions() {
    // 1. Start with nothing
    let result = 0;

    function nextContainer(index, last, maximum, containers) {
      // eslint-disable-next-line no-console
      // console.log('nextContainer() index=%d, last=%d, maximum=%d', index, last, maximum);
      // 1. If we have a colution, record it
      if (maximum === 0) {
        result += 1;
      // 2. If we have more to do ...
      } else if (maximum > 0 && index < last) {
        // 3. Loop for using / not using container
        for (let use = 0; use < 2; use += 1) {
          // 4. Get more containers
          const newMax = use ? maximum - containers[index] : maximum;
          nextContainer(index + 1, last, newMax, containers);
        }
      }
    }
    // 2. Test all the containter combinations
    nextContainer(0, this.containers.length, this.liters, this.containers);
    // 3. Return the number of solutions
    return result;
  }

  minimumSolutions() {
    // 1. Start with nothing
    let result = 0;
    let minimum = this.containers.length + 1;

    function nextContainer(index, last, maximum, number, containers) {
      // eslint-disable-next-line no-console
      // console.log('nextContainer() index=%d, last=%d, maximum=%d', index, last, maximum);
      // 1. If we have a colution, record it
      if (maximum === 0) {
        if (number < minimum) {
          minimum = number;
          result = 0;
        }
        if (number === minimum) {
          result += 1;
        }
      // 2. If we have more to do ...
      } else if (maximum > 0 && index < last) {
        // 3. Loop for using / not using container
        for (let use = 0; use < 2; use += 1) {
          // 4. Get more containers
          const newMax = use ? maximum - containers[index] : maximum;
          nextContainer(index + 1, last, newMax, number + use, containers);
        }
      }
    }
    // 2. Test all the containter combinations
    nextContainer(0, this.containers.length, this.liters, 0, this.containers);
    // 3. Return the number of solutions
    return result;
  }

  partOne(options) {
    // Returns the solution for part one

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part one
    return this.numberSolutions();
  }

  partTwo(options) {
    // Returns the solution for part two

    // 0. Function arguments
    // eslint-disable-next-line no-unused-vars
    const verbose = options.verbose === undefined ? false : options.verbose;
    // eslint-disable-next-line no-unused-vars
    const limit = options.limit === undefined ? 0 : options.limit;

    // 1. Return the solution for part two
    return this.minimumSolutions();
  }
}

module.exports.Eggnog = Eggnog;
// ======================================================================
// end                        e g g n o g . j s                       end
// ======================================================================
