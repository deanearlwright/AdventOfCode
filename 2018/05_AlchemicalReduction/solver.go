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
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const (
	pairsAJ = "aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj"
	pairsKT = "kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt"
	pairsUZ = "uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz"
	pairsAZ = pairsAJ + "|" + pairsKT + "|" + pairsUZ
	letters = "abcdefghijklmnopqrstuvwxyz"
)

var rePairs = regexp.MustCompile(pairsAZ)

// ======================================================================
//                                                                  Solver
// ======================================================================

// Object for Alchemical Reduction

type Solver struct {
	Part2 bool
	Text  []string
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text

	return p
}

func oneIteration(text string) string {
	// Run one iteration of the polizared pairs

	return rePairs.ReplaceAllString(text, "")
}

func multipleIterations(text string) string {
	// Process polymer

	var newText string

	// 1. Loop forever (
	for {

		// 2. Process the porarized pairs
		newText = oneIteration(text)

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

func removePolymer(text string, polymer string) string {
	// Remove both polarities of the polymer

	return strings.ReplaceAll(strings.ReplaceAll(text, strings.ToUpper(polymer), ""), strings.ToLower(polymer), "")
}

func removePolymers(text string) string {
	// Find the smallest string after polymer removal and processing

	// 1. Start with nothing
	bestString := text
	bestLength := len(text) + 1

	// 2. Loop for all letters
	for _, letter := range letters {

		// 3. Remove a letter from the polymer test
		eliminated := removePolymer(text, string(letter))

		// 4. Process the shorter polymer string
		newText := multipleIterations(eliminated)

		// 5. If this processed string is shorter, save it
		if len(newText) < bestLength {
			bestString = newText
			bestLength = len(newText)
		}
	}

	// 6. Return the shortest string
	return bestString
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Process the text for multiple iterations
	text := multipleIterations(p.Text[0])

	// 2. Return the solution for part one
	return strconv.Itoa(len(text))
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Get the shortest string after eliminating a polymer
	shortest := removePolymers(p.Text[0])

	// 1. Return the solution for part two
	return strconv.Itoa(len(shortest))
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
