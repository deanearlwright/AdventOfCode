/* eslint-disable linebreak-style */

// ======================================================================
// Wizard Simulator 20XX
//   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
//
// Javascript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                             a o c _ 2 2 . j s
//
// Solve the Advent of Code 2015 day 22 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

const yargs = require('yargs');
const fs = require('fs');
const process = require('process');

const wizsim = require('./wizsim');

// ----------------------------------------------------------------------
//                                                        parseCommndLine
// ----------------------------------------------------------------------

function parseCommandLine() {
  // Parse the command line options"

  // 1. Create the command line parser
  const { argv } = yargs
    .command('aoc_22', 'Wizard Simulator 20XX - Day 22 of Advent of Code 2015', { })
    .option('verbose', {
      alias: 'v',
      default: false,
      describe: 'Print status messages to stdout',
      type: 'boolean',
    })
    .option('part', {
      alias: 'p',
      default: 1,
      describe: 'Puzzle Part (1 or 2)',
      type: 'number',
    })
    .option('limit', {
      alias: 'l',
      default: 0,
      describe: 'Maximum limit (e.g., time, size, recursion) before stopping',
      type: 'number',
    })
    .option('filepath', {
      alias: 'f',
      default: 'input.txt',
      describe: 'Location of puzzle input',
      type: 'string',
    })
    .example('$0 -p 1 input.txt', 'Solve part one of the puzzle')
    .help()
    .alias('help', 'h');

  // 2. Get the options and arguments
  return argv;
}

// ----------------------------------------------------------------------
//                                                                partOne
// ----------------------------------------------------------------------

function partOne(args, inputLines) {
  // Process part one of the puzzle

  // 1. Create the puzzle solver
  const solver = new wizsim.Wizsim({ part2: false, text: inputLines });

  // 2. Determine the solution for part two
  const solution = solver.partOne({ verbose: args.verbose, limit: args.limit });
  if (solution == null) {
    console.log('There is no solution for part one'); // eslint-disable-line no-console
  } else {
    console.log('The solution for part one is', solution); // eslint-disable-line no-console
  }

  // 3. Return result
  return solution != null;
}

// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------

function partTwo(args, inputLines) {
  // Process part two of the puzzle

  // 1. Create the puzzle solver
  const solver = new wizsim.Wizsim({ part2: true, text: inputLines });

  // 2. Determine the solution for part two
  const solution = solver.partTwo({ verbose: args.verbose, limit: args.limit });
  if (solution == null) {
    console.log('There is no solution for part two'); // eslint-disable-line no-console
  } else {
    console.log('The solution for part two is', solution); // eslint-disable-line no-console
  }

  // 3. Return result
  return solution != null;
}

// ----------------------------------------------------------------------
//                                                              from_text
// ----------------------------------------------------------------------

function fromText(text) {
  // Break the text into trimed, non-comment lines"

  // 1. We start with no lines
  const lines = [];

  // 2. Loop for lines in the text
  text.split(/\r?\n/).forEach((line) => {
    // 3. But ignore blank and non-claim lines
    const cleaned = line.trimEnd();
    if (cleaned.length > 0 && !cleaned.startsWith('!')) {
      // 4. Add the line
      lines.push(cleaned);
    }
  });

  // 5. Return a list of clean lines
  return lines;
}

// ----------------------------------------------------------------------
//                                                              from_file
// ----------------------------------------------------------------------

function fromFile(filepath) {
  // Read the file
  try {
    const data = fs.readFileSync(filepath, 'utf8');
    return fromText(data);
  } catch (e) {
    console.log('Error', e.stack); // eslint-disable-line no-console
    return '';
  }
}

// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------

function main() {
  // Read the Advent of Code problem and solve it
  let result = null;

  // 1. Get the command line options
  const argv = parseCommandLine();

  // 2. Read the puzzle file
  const inputText = fromFile(argv.filepath);

  // 3. Process the appropiate part of the puzzle
  if (argv.part === 1) {
    result = partOne(argv, inputText);
  } else {
    result = partTwo(argv, inputText);
  }

  // 5. Set return code (0 if solution found, 2 if not)
  if (result != null) {
    process.exit(0);
  }
  process.exit(2);
}

// ----------------------------------------------------------------------
//                                                  module initialization
// ----------------------------------------------------------------------
if (typeof require !== 'undefined' && require.main === module) {
  main();
}

// ----------------------------------------------------------------------
//                                                                 export
// ----------------------------------------------------------------------

module.exports.fromText = fromText;

// ======================================================================
// end                         a o c _ 2 2 . j s                      end
// ======================================================================
