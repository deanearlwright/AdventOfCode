// ======================================================================
// Cube Conundrum
//   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         s o l v e r . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 02 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                 Solver
// ======================================================================

// Object for Cube Conundrum

type Solver struct {
	Part2 bool
	Text  []string
	Games []*Game
}

func NewSolver(part2 bool, text []string) (*Solver, error) {

	// 1. Set the initial values
	p := new(Solver)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		games, err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
		p.Games = games
	}

	// 3. Return the object (and no errors)
	return p, nil
}

func (p *Solver) processText(text []string) ([]*Game, error) {
	// Assign values from text

	// 1. Loop for each line of the text
	games := make([]*Game, 0, 10)
	for indx, line := range text {

		// 2. Create a game from the text
		agame, err := NewGame(p.Part2, line)
		if err != nil {
			return nil, fmt.Errorf("error in line %d %s", indx, err)
		}
		games = append(games, agame)
	}
	return games, nil
}

func (p *Solver) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the games
	for _, game := range p.Games {

		// 3. Get the index of this game or zero if invalid
		value := game.PartOne(false, 0)

		// 4. Accumulate the result
		result = result + value
	}

	// 5. Return the solution for part one
	return fmt.Sprintf("%d", result)
}

func (p *Solver) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Start with nothing
	result := 0

	// 2. Loop for all of the games
	for _, game := range p.Games {

		// 3. Get the color power for this game
		value := game.PartTwo(false, 0)

		// 4. Accumulate the result
		result = result + value
	}

	// 5. Return the solution for part two
	return fmt.Sprintf("%d", result)
}

// ======================================================================
// end                        s o l v e r . g o                       end
// ======================================================================
