// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         p a t t e r n s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 13 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
    "fmt"
    "strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
)

// ======================================================================
//                                                                  Patterns
// ======================================================================

// Patterns ... Object for Point Of Incidence
type Patterns struct {
    Part2 bool
    Text  []string
    Numbers []int
}

// NewPatterns ... Create a Patterns object
func NewPatterns(part2 bool, text []string) (*Patterns, error) {

    // 1. Set the initial values
    p := new(Patterns)
    p.Part2 = part2
    p.Text = text

    // 2. Process text (if any)
    if len(p.Text) > 0 {
        err := p.processText(p.Text)
        if err != nil {
           return nil, err
        }
    }

    // 3. Return the new Patterns object
    return p, nil
}


// processText ... Assign values from text
func (p *Patterns) processText(text []string) error {

    // 1. Loop for each line of the text
    for indx, line := range text {

        // 2. Add the number to the entries
        num, err := strconv.Atoi(line)
        if err != nil {
            return fmt.Errorf("error in line %d: %s", indx, err)
        }
        p.Numbers = append(p.Numbers, num)
    }

    // 3. Return success
    return nil
}

// PartOne ... Returns the solution for part one
func (p *Patterns) PartOne(verbose bool, limit int) string {

    // 1. Return the solution for part one
    return ""
}


// PartTwo ... Returns the solution for part two
func (p *Patterns) PartTwo(verbose bool, limit int) string {

    // 1. Return the solution for part two
    return ""
}


// ======================================================================
// end                        p a t t e r n s . g o                       end
// ======================================================================
