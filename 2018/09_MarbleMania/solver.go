// ======================================================================
// Marble Mania
//   Advent of Code 2018 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2018 Day 09 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"regexp"
	"strconv"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

var (
	reSolver = regexp.MustCompile("[0-9]+")
)

// ======================================================================
//                                                                  Solver
// ======================================================================

// Object for Marble Mania

type Solver struct {
	Part2 bool
	Text  []string
	Game  *Game
}

func NewSolver(part2 bool, text []string) *Solver {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if p.Text != nil && len(p.Text) > 0 {

		// 3. Get the numbers from the text
		numbers := reSolver.FindAllString(p.Text[0], -1)
		if len(numbers) != 2 {
			fmt.Printf("Unable to parse input '%s'", p.Text[0])
		}

		// 3. Create a game with those number of players and marbles
		players, _ := strconv.Atoi(numbers[0])
		marbles, _ := strconv.Atoi(numbers[1])
		p.Game = NewGame(players, marbles)
	}

	// 4. Return the new solver
	return p
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Return the solution for part one
	return strconv.Itoa(p.Game.AllTurns())
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Increase the number of marbles
	marbles := 100 * p.Game.numMarbles
	p.Game = NewGame(p.Game.numPlayers, marbles)

	// 2. Return the solution for part two
	return strconv.Itoa(p.Game.AllTurns())
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
