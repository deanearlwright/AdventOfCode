// ======================================================================
// Rain Risk
//   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                             a o c _ 1 2 . t s
//
// Solve the Advent of Code 2020 day 12 problem
// ======================================================================

// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------

import { readFileSync } from 'fs';

import { exit } from 'process';

import * as yargs from 'yargs';

import { Navigation } from './navigation';

// ----------------------------------------------------------------------
//                                                        parseCommndLine
// ----------------------------------------------------------------------

interface Arguments {
  verbose: boolean;
  part: number;
  limit: number;
  filepath: string;
}

function parseCommandLine(): Arguments {
  // Parse the command line options"

  // 1. Create the command line parser
  const { argv } = yargs
    .command('aoc_12', 'Rain Risk - Day 12 of Advent of Code 2020', { })
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

function partOne(args: Arguments, inputLines: string[]): boolean {
  // Process part one of the puzzle

  // 1. Create the puzzle solver
  const solver = new Navigation(inputLines, false);

  // 2. Determine the solution for part one
  const solution = solver.partOne(args.verbose, args.limit);
  if (Number.isNaN(solution)) {
    console.log('There is no solution for part one');
  } else {
    console.log('The solution for part one is', solution);
  }

  // 3. Return result
  return !Number.isNaN(solution);
}

// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------

function partTwo(args: Arguments, inputLines: string[]): boolean {
  // Process part two of the puzzle

  // 1. Create the puzzle solver
  const solver = new Navigation(inputLines, true);

  // 2. Determine the solution for part two
  const solution = solver.partTwo(args.verbose, args.limit);
  if (Number.isNaN(solution)) {
    console.log('There is no solution for part two');
  } else {
    console.log('The solution for part two is', solution);
  }

  // 3. Return result
  return !Number.isNaN(solution);
}

// ----------------------------------------------------------------------
//                                                              from_text
// ----------------------------------------------------------------------

export function fromText(text: string): string[] {
  // Break the text into trimed, non-comment lines"

  // 1. We start with no lines
  const lines: string[] = [];

  // 2. Loop for lines in the text
  text.split(/\r?\n/).forEach((line) => {
    // 3. But ignore blank and comment lines
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

function fromFile(filepath: string): string[] {
  // Read the file
  try {
    const data = readFileSync(filepath, 'utf8');
    return fromText(data);
  } catch (e) {
    console.log('Error', e.stack); // eslint-disable-line no-console
    return [];
  }
}

// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------

function main() {
  // Read the Advent of Code problem and solve it
  let result = false;

  // 1. Get the command line options
  const argv: Arguments = parseCommandLine();

  // 2. Read the puzzle file
  const inputText: string[] = fromFile(argv.filepath);

  // 3. Process the appropiate part of the puzzle
  if (argv.part === 1) {
    result = partOne(argv, inputText);
  } else {
    result = partTwo(argv, inputText);
  }

  // 5. Set return code (0 if solution found, 2 if not)
  if (result) {
    exit(0);
  }
  exit(2);
}

// ----------------------------------------------------------------------
//                                                  module initialization
// ----------------------------------------------------------------------
if (typeof require !== 'undefined' && require.main === module) {
  main();
}

// ======================================================================
// end                         a o c _ 1 2 . t s                      end
// ======================================================================
