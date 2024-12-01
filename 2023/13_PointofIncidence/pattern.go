// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         p a t t e r n . g o
// ======================================================================
// Pattern for the Advent of Code 2023 Day 13 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                Pattern
// ======================================================================

// Pattern ... Object for Point Of Incidence
type Pattern struct {
	Part2 bool
	Text  string
}

// NewPattern ... Create a Pattern object
func NewPattern(part2 bool, text string) (*Pattern, error) {
	// Pattern Object for Point Of Incidence

	// 1. Set the initial values
	p := new(Pattern)
	p.Part2 = part2
	p.Text = text

	// 2. Return success
	return p, nil
}

// ======================================================================
// end                       p a t t e r n . g o                      end
// ======================================================================
