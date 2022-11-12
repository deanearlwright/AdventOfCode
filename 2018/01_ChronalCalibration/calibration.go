// ======================================================================
// Chronal Calibration
//   Advent of Code 2018 Day 01 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c a l i b r a t i o n . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 01 puzzle

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
//                                                                  Calibration
// ======================================================================

// Object for Chronal Calibration

type Calibration struct {
    Part2 bool
    Text  []string
    Numbers []int
}

func NewCalibration(part2 bool, text []string) *Calibration {

    // 1. Set the initial values
    p := new(Calibration)
    p.Part2 = part2
    p.Text = text

    // 2. Process text (if any)
    if p.Text != nil && len(p.Text) > 0 {
       p.processText(p.Text)
    }

    return p
}


func (p *Calibration) processText(text []string) {
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

func (p *Calibration) PartOne(verbose bool, limit int) string {
    // Returns the solution for part one

    // 1. Return the solution for part one
    return ""
}


func (p *Calibration) PartTwo(verbose bool, limit int) string {
    // Returns the solution for part two

    // 1. Return the solution for part two
    return ""
}


// ======================================================================
// end                        c a l i b r a t i o n . g o                       end
// ======================================================================
