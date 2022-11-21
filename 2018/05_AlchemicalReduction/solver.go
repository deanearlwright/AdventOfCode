// ======================================================================
// Alchemical Reduction
//   Advent of Code 2018 Day 05 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 05 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "fmt"
    "os"
    "strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
)

// ======================================================================
//                                                                  Solver
// ======================================================================

// Object for Alchemical Reduction

type Solver struct {
    Part2 bool
    Text  []string
    Numbers []int
}

func NewSolver(part2 bool, text []string) *Solver {

    // 1. Set the initial values
    p := new(Solver)
    p.Part2 = part2
    p.Text = text

    // 2. Process text (if any)
    if p.Text != nil && len(p.Text) > 0 {
       p.processText(p.Text)
    }

    return p
}


func (p *Solver) processText(text []string) {
    // Assign values from text

    // 1. Loop for each line of the text
    for indx, line := range text {

        // 2. Add the number to the entries
        num, err := strconv.Atoi(line)
        if err != nil {
            fmt.Printf("Error %s in line %d: '%s'\n", err.Error(), indx, line)
            os.Exit(1)
        }
        p.Numbers = append(p.Numbers, num)
    }
}

func (p *Solver) PartOne(verbose bool, limit int) string {
    // Returns the solution for part one

    // 1. Return the solution for part one
    return ""
}


func (p *Solver) PartTwo(verbose bool, limit int) string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return ""
}


// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
