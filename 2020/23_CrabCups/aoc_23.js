"use strict";
// ======================================================================
// Crab Cups
//   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
//
// Typescript implementation by Dr. Dean Earl Wright III
// ======================================================================
exports.__esModule = true;
exports.fromText = void 0;
// ======================================================================
//                             a o c _ 2 3 . t s
//
// Solve the Advent of Code 2020 day 23 problem
// ======================================================================
// ----------------------------------------------------------------------
//                                                                 import
// ----------------------------------------------------------------------
var fs_1 = require("fs");
var process_1 = require("process");
var yargs = require("yargs");
var game_1 = require("./game");
function parseCommandLine() {
    // Parse the command line options"
    // 1. Create the command line parser
    var argv = yargs
        .command('aoc_23', 'Crab Cups - Day 23 of Advent of Code 2020', {})
        .option('verbose', {
        alias: 'v',
        "default": false,
        describe: 'Print status messages to stdout',
        type: 'boolean'
    })
        .option('part', {
        alias: 'p',
        "default": 1,
        describe: 'Puzzle Part (1 or 2)',
        type: 'number'
    })
        .option('limit', {
        alias: 'l',
        "default": 0,
        describe: 'Maximum limit (e.g., time, size, recursion) before stopping',
        type: 'number'
    })
        .option('filepath', {
        alias: 'f',
        "default": 'input.txt',
        describe: 'Location of puzzle input',
        type: 'string'
    })
        .example('$0 -p 1 input.txt', 'Solve part one of the puzzle')
        .help()
        .alias('help', 'h').argv;
    // 2. Get the options and arguments
    return argv;
}
// ----------------------------------------------------------------------
//                                                                partOne
// ----------------------------------------------------------------------
function partOne(args, inputLines) {
    // Process part one of the puzzle
    // 1. Create the puzzle solver
    var solver = new game_1.Game(inputLines, false);
    // 2. Determine the solution for part one
    var solution = solver.partOne(args.verbose, args.limit);
    if (Number.isNaN(solution)) {
        console.log('There is no solution for part one');
    }
    else {
        console.log('The solution for part one is', solution);
    }
    // 3. Return result
    return !Number.isNaN(solution);
}
// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------
function partTwo(args, inputLines) {
    // Process part two of the puzzle
    // 1. Create the puzzle solver
    var solver = new game_1.Game(inputLines, true);
    // 2. Determine the solution for part two
    var solution = solver.partTwo(args.verbose, args.limit);
    if (Number.isNaN(solution)) {
        console.log('There is no solution for part two');
    }
    else {
        console.log('The solution for part two is', solution);
    }
    // 3. Return result
    return !Number.isNaN(solution);
}
// ----------------------------------------------------------------------
//                                                              from_text
// ----------------------------------------------------------------------
function fromText(text) {
    // Break the text into trimed, non-comment lines"
    // 1. We start with no lines
    var lines = [];
    // 2. Loop for lines in the text
    text.split(/\r?\n/).forEach(function (line) {
        // 3. But ignore blank and comment lines
        var cleaned = line.trimEnd();
        if (cleaned.length > 0 && !cleaned.startsWith('!')) {
            // 4. Add the line
            lines.push(cleaned);
        }
    });
    // 5. Return a list of clean lines
    return lines;
}
exports.fromText = fromText;
// ----------------------------------------------------------------------
//                                                              from_file
// ----------------------------------------------------------------------
function fromFile(filepath) {
    // Read the file
    try {
        var data = fs_1.readFileSync(filepath, 'utf8');
        return fromText(data);
    }
    catch (e) {
        console.log('Error', e.stack); // eslint-disable-line no-console
        return [];
    }
}
// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------
function main() {
    // Read the Advent of Code problem and solve it
    var result = false;
    // 1. Get the command line options
    var argv = parseCommandLine();
    // 2. Read the puzzle file
    var inputText = fromFile(argv.filepath);
    // 3. Process the appropiate part of the puzzle
    if (argv.part === 1) {
        result = partOne(argv, inputText); // 29385746
    }
    else {
        result = partTwo(argv, inputText); // 680435423892
    }
    // 5. Set return code (0 if solution found, 2 if not)
    if (result) {
        process_1.exit(0);
    }
    process_1.exit(2);
}
// ----------------------------------------------------------------------
//                                                  module initialization
// ----------------------------------------------------------------------
if (typeof require !== 'undefined' && require.main === module) {
    main();
}
// ======================================================================
// end                         a o c _ 2 3 . t s                      end
// ======================================================================
