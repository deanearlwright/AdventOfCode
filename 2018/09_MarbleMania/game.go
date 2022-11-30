// ======================================================================
// Marble Mania
//   Advent of Code 2018 Day 09 -- Eric Wastl -- https://adventofcode.com
//
// lua implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         g a m e . g o
// ======================================================================
// Game for the Advent of Code 2018 Day 09 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"strings"
)

// ----------------------------------------------------------------------
//                                                              constants
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                   Game
// ======================================================================

type Game struct {
	numPlayers int
	numMarbles int
	players    []int
	circle     []int
	nextPlayer int
	nextMarble int
	current    int
}

func NewGame(players int, marbles int) *Game {
	// Game Object for Marble Mania

	// 1. Set the initial values
	p := new(Game)
	p.numPlayers = players
	p.numMarbles = marbles
	p.nextPlayer = 0
	p.nextMarble = 1
	p.current = 0
	p.players = make([]int, p.numPlayers)
	p.circle = make([]int, 1, p.numMarbles)

	// 2. Return Game
	return p
}

func (p *Game) Show() string {
	// Display the game

	// 1. Kludge for the start-+
	if p.nextPlayer == 0 {
		return "[----] (0)"
	}

	// 2. Start with nothing
	var result strings.Builder

	// 3. Add the player
	fmt.Fprintf(&result, "[%3d] ", p.nextPlayer)

	// 4. Loop for all the marbles in the circle
	for indx, marble := range p.circle {

		// 5. if this is the current marble use () else spaces
		if indx == p.current {
			fmt.Fprintf(&result, "(%d)", marble)
		} else {
			fmt.Fprintf(&result, " %d ", marble)
		}
	}

	// 6. Return the game information as a string
	return result.String()
}
func (p *Game) Turn() bool {
	// Do a turn, return true if the game should continue

	// 1. Get the marble
	marble := p.nextMarble
	if marble > p.numMarbles {
		return false
	}
	p.nextMarble = marble + 1

	// 2. Get the player
	player := p.nextPlayer
	p.nextPlayer = player + 1
	if p.nextPlayer >= p.numPlayers {
		p.nextPlayer = 0
	}

	// 3. Is this a special or regular turn?
	if p.IsSpecial(marble) {
		p.SpecialTurn(marble, player)
	} else {
		p.RegularTurn(marble, player)
	}

	// 4. Go again
	return true
}

func (p *Game) AllTurns() int {
	// Play the game until the end

	// 1. Lots of turns
	for p.Turn() {
	}

	// 2. Return the highest score
	return p.Highest()
}

func (p *Game) Highest() int {
	// Return the highest game score

	// 1. Start with nothing
	highest := 0

	// 2. Loop for all the players
	for _, score := range p.players {

		// 3. Keep the highest score
		if score > highest {
			highest = score
		}
	}

	// 4. Return the highest score
	return highest
}

func (p *Game) RegularTurn(marble int, player int) {
}

func (p *Game) SpecialTurn(marble int, player int) {
}

func (p *Game) Insert(index, value int) {
	// Insert a marble into the circle between the index and index + 1

	// 1. Adding to the end is easy
	if index > len(p.circle) {
		p.circle = append(p.circle, value)
	}

}

func (p *Game) Remove(slice []int, index int) int {
	// Remove a marble from the circle at the index value

	marble := 0

	// 9. Return removed marble
	return marble
}

func (p *Game) Clockwise() int {
	// Returns the index of the marble one space clockwise of the current one

	// 1. Clockwise is an increase in the index
	next := p.current + 1

	// 2. If greater than the current lenght, circle around
	if next > len(p.circle) {
		next = next - len(p.circle)
	}

	// 3. Return the index
	return next
}

func (p *Game) CounterClockwise() int {
	// Returns the index of the marble seven spaces cc of the current one

	// 1. Counter Clockwise is an decrease in the index
	next := p.current - 7

	// 2. If less than the start of the array, circle around
	if next < 0 {
		next = len(p.circle) + next
	}

	// 3. Return the index
	return next
}

func (p *Game) IsSpecial(marble int) bool {
	// Returns true if this is a special marble

	return 0 == marble%23
}

// ======================================================================
// end                          g a m e . g o                         end
// ======================================================================
