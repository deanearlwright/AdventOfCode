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
	//"fmt"
	//"os"
	"regexp"
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	pairsAJ = "aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj"
	pairsKT = "kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt"
	pairsUZ = "uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz"
	pairsAZ = pairsAJ + "|" + pairsKT + "|" + pairsUZ
)

var rePairs = regexp.MustCompile(pairsAZ)

// ======================================================================
//                                                                  Solver
// ======================================================================

// Object for Alchemical Reduction

type Solver struct {
	Part2   bool
	Text    []string
	Numbers []int
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text

	return p
}

func process(text string) string {
	// Process polymer

	var newText string

	// 1. Loop forever (
	for {

		// 2. Process the porarized pairs
		newText = rePairs.ReplaceAllString(text, "")

		// 3. If no changes made, we are done
		if text == newText {
			break
		}

		// 4. This is the new polymer
		text = newText
	}

	// 5. Return the processed polymer
	return newText
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	text := process(p.Text[0])
	// 1. Return the solution for part one
	return strconv.Itoa(len(text))
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Return the solution for part two
	return ""
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
