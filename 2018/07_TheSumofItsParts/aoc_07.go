// ======================================================================
// The Sum of Its Parts
//   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                           a o c _ 0 7 . g o
// ======================================================================
// Solve the puzzles for Advent of Code 2018 day 07

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "flag"
    "fmt"
    "os"
    "regexp"
    "strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
     SAVE_BLANK_LINES = false
)

// ----------------------------------------------------------------------
//                                                                globals
// ----------------------------------------------------------------------
var aocVerbose bool
var aocPart int
var aocLimit int
var aocInput string = "";

// ----------------------------------------------------------------------
//                                                          initialzation
// ----------------------------------------------------------------------

func init() {
  // Parse the command line options

  // 1. Create the command line parser
  flag.IntVar(&aocPart, "part", 1, "Part 1 or 2 of the puzzle")
  flag.IntVar(&aocPart, "p", 1, "Part 1 or 2 of the puzzle")
  flag.IntVar(&aocLimit, "limit", 0, "Optional execution limit")
  flag.IntVar(&aocLimit, "l", 0, "Optional execution limit")
  flag.BoolVar(&aocVerbose, "verbose", false, "Optional extra messages")
  flag.BoolVar(&aocVerbose, "v", false, "Optional extra messages")
  flag.StringVar(&aocInput, "input", "", "Input file name")
  flag.StringVar(&aocInput, "i", "", "Input file name")
}

// ----------------------------------------------------------------------
//                                                       parseCommandLine
// ----------------------------------------------------------------------

func parseCommandLine() {

    // 1. Parse the command line to aocXXXX variables
    flag.Parse()

    // 2. Verify that part is 1 or 2
    if aocPart != 1 && aocPart != 2 {
        fmt.Println("part (-p) must be 1 or 2")
        os.Exit(1)
    }

    // 3. If input file name not specified, get from unprocessed arguments
    if aocInput == "" {
        if flag.NArg() == 0 {
            fmt.Println("Input file name (-i) not specified")
            os.Exit(1)
        }
        aocInput = flag.Arg(0)
    }
}

// ----------------------------------------------------------------------
//                                                                partOne
// ----------------------------------------------------------------------

func partOne(verbose bool, limit int, input_lines []string) string {
    // Process part one of the puzzle

    // 1. Create the puzzle solver
    solver := NewSolver(false, input_lines)

    // 2. Determine the solution for part one
    solution := solver.PartOne(verbose, limit)
    if solution == "" {
        fmt.Println("There is no solution")
    } else {
        fmt.Println("The solution for part one is " + solution)
    }

    // 3. Return result
    return solution
}

// ----------------------------------------------------------------------
//                                                                partTwo
// ----------------------------------------------------------------------

func partTwo(verbose bool, limit int, input_lines []string) string {
    // Process part two of the puzzle

    // 1. Create the puzzle solver
    solver := NewSolver(true, input_lines)

    // 2. Determine the solution for part two
    solution := solver.PartTwo(verbose, limit)
    if solution == "" {
        fmt.Println("There is no solution")
    } else {
        fmt.Println("The solution for part two is " + solution)
    }

    // 3. Return result
    return solution
}

// ----------------------------------------------------------------------
//                                                               fromFile
// ----------------------------------------------------------------------

func fromFile(filepath string) []string {
    // 1. Read the file
    b, err := os.ReadFile(filepath)
    if err != nil {
        fmt.Print(err)
        os.Exit(2)
    }

    // 2. Return the contents as a string
    return fromText(string(b))
}

// ----------------------------------------------------------------------
//                                                               fromText
// ----------------------------------------------------------------------

func fromText(text string) []string {
    // Break the text into trimed, non-comment lines

    // 1. We start with no lines
    var result []string

    // 2. Break up the text into lines
    lines := regexp.MustCompile("\\r?\\n").Split(text, -1)

    // 3. Loop for lines in the text
    for _, line := range lines {

        // 4. Ignore comment lines and maybe blank lines
        if len(line) > 0 {
            if !strings.HasPrefix(line, "!") {
                result = append(result, line)
            }
        } else if SAVE_BLANK_LINES {
            result = append(result, "")
        }
    }

    // 5. Return a table of cleaned text lines
    return result
}

// ----------------------------------------------------------------------
//                                                                   main
// ----------------------------------------------------------------------

func main() {
    // Read the Advent of Code problem and solve it

    // 1. Get the command line options
    parseCommandLine()

    // 2. Read the puzzle file
    input_text := fromFile(aocInput)

    // 3. Process the appropiate part of the puzzle
    var result string
    if aocPart == 1 {
        result = partOne(aocVerbose, aocLimit, input_text)
    } else {
        result = partTwo(aocVerbose, aocLimit, input_text)
    }

    // 5. Set return code (0 if solution found, 2 if not)
    if len(result) > 0 {
        os.Exit(0)
    }
    os.Exit(2)
}

// ======================================================================
// end                         a o c _ 0 7 . g o                      end
// ======================================================================
