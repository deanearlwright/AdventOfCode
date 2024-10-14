// ======================================================================
// Cube Conundrum
//   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         g a m e . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 02 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strconv"
	"strings"
)

// ======================================================================
//                                                                   Game
// ======================================================================

// Object for Cube Conundrum

type Game struct {
	Part2 bool
	Text  string
	ID    int
	Draws Draws
}

func NewGame(part2 bool, text string) (*Game, error) {

	// 1. Set the initial values
	p := new(Game)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {

		// 3. Decode the draws
		id, draws, err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}

		// 4. Add the id and draws to the Game
		p.ID = id
		p.Draws = draws
	}

	// 5. Return the game
	return p, nil
}

func (p *Game) processText(text string) (int, Draws, error) {
	// Assign values from text
	id := 0
	draws := make(Draws, 0, 5)

	// 1. Make sure that this is a Game line
	if !strings.HasPrefix(text, "Game ") {
		return id, draws, fmt.Errorf("Game line does not begin with Game --> %s", text)
	}

	// 2. Get the game number
	number, dtexts, found := strings.Cut(text, ": ")
	if !found {
		return id, draws, fmt.Errorf("Game line does not have a colon --> %s", text)
	}
	id, err := strconv.Atoi(number[5:])
	if err != nil {
		return id, draws, fmt.Errorf("Game line does not have an id --> %s", text)
	}

	// 3. Loop for the draws
	for _, dtext := range strings.Split(dtexts, "; ") {

		// 4. Build the draw object
		draw, err := NewDraw(p.Part2, dtext)
		if err != nil {
			return id, draws, err
		}
		draws = append(draws, draw)
	}

	// 6. Return the id and draws
	return id, draws, nil
}

func (p *Game) PartOne(verbose bool, limit int) int {
	// Returns the solution for part one

	// 1. Loop for each draw
	for _, draw := range p.Draws {

		// 3. Could this draw happen?  If not, return false
		if !draw.IsLegal() {
			return 0
		}
	}

	// 3. This one is good, return the id
	return p.ID
}

func (p *Game) PartTwo(verbose bool, limit int) int {
	// Returns the solution for part two

	// 1. Start with nothing
	minimums := make(colorMap)
	for _, color := range colors {
		minimums[color] = 0
	}

	// 2. Loop for each draw
	for _, draw := range p.Draws {

		// 3. Get the mimimum number of cubes
		for _, color := range colors {
			knt := draw.Count(color)
			if knt > minimums[color] {
				minimums[color] = knt
			}
		}
	}

	// 4. Return the solution for part two (color power)
	return minimums["red"] * minimums["green"] * minimums["blue"]
}

// ======================================================================
// end                          g a m e . g o                         end
// ======================================================================
