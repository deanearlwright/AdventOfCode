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

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                   Game
// ======================================================================

// Object for Cube Conundrum

type Colors struct {
	Red   int
	Green int
	Blue  int
}

type Game struct {
	Part2 bool
	Text  string
	ID    int
	Draws []Colors
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

func (p *Game) processText(text string) (int, []Colors, error) {
	// Assign values from text
	id := 0
	draws := make([]Colors, 0, 5)

	// 1. Make sure that this is a Game line
	if !strings.HasPrefix(text, "Game ") {
		return id, draws, fmt.Errorf("Game line does not begin with Game --> %s", text)
	}

	// 2. Get the game number
	number, xdraws, found := strings.Cut(text, ": ")
	if !found {
		return id, draws, fmt.Errorf("Game line does not have a colon --> %s", text)
	}
	id, err := strconv.Atoi(number[5:])
	if err != nil {
		return id, draws, fmt.Errorf("Game line does not have an id --> %s", text)
	}

	// 3. Loop for the draws
	for _, draw := range strings.Split(xdraws, "; ") {
		colors := Colors{}

		// 4. Loop for the colors in the draw
		for _, kntcolor := range strings.Split(draw, ", ") {

			// 5. Get the count and color
			knt, color, found := strings.Cut(kntcolor, " ")
			if !found {
				return id, draws, fmt.Errorf("unable to get count and color from --> %s", kntcolor)
			}
			count, err := strconv.Atoi(knt)
			if err != nil {
				return id, draws, fmt.Errorf("invalid count for --> %s", kntcolor)
			}
			switch color {
			case "red":
				colors.Red = count
			case "green":
				colors.Green = count
			case "blue":
				colors.Blue = count
			default:
				return id, draws, fmt.Errorf("invalid color for --> %s", kntcolor)
			}
		}
		draws = append(draws, colors)
	}

	// 6. Return the id and draws
	return id, draws, nil
}

func (p *Game) PartOne(verbose bool, limit int) int {
	// Returns the solution for part one

	// 1. Loop for each draw
	for _, draw := range p.Draws {

		// 3. Could this draw happen?
		if draw.Red > 12 {
			return 0
		}
		if draw.Green > 13 {
			return 0
		}
		if draw.Blue > 14 {
			return 0
		}
	}

	// 2. This one is good, return the id
	return p.ID
}

func (p *Game) PartTwo(verbose bool, limit int) int {
	// Returns the solution for part two

	// 1. Start with nothing
	colors := Colors{}

	// 2. Loop for each draw
	for _, draw := range p.Draws {

		// 3. Get the mimimum number of cubes
		if draw.Red > colors.Red {
			colors.Red = draw.Red
		}
		if draw.Green > colors.Green {
			colors.Green = draw.Green
		}
		if draw.Blue > colors.Blue {
			colors.Blue = draw.Blue
		}
	}

	// 4. Return the solution for part two (color power)
	return colors.Red * colors.Green * colors.Blue
}

// ======================================================================
// end                          g a m e . g o                         end
// ======================================================================
