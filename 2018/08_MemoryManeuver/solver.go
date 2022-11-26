// ======================================================================
// Memory Maneuver
//   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 08 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                 Solver
// ======================================================================

// Object for Memory Maneuver

type Solver struct {
	Part2 bool
	Text  []string
	Node  *Node
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {
		p.Node, _ = NewNode(strings.Split(text[0], " "), 0)
	}

	return p
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Return the solution for part one
	return strconv.Itoa(p.Node.SumAll())
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Return the solution for part two
	return strconv.Itoa(p.Node.Value())
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
