// ======================================================================
// Scratchcards
//   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c a r d s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 04 puzzle

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
//                                                                  Cards
// ======================================================================

// Object for Scratchcards

type Cards struct {
	Part2 bool
	Text  []string
	Cards []*Card
}

func NewCards(part2 bool, text []string) (*Cards, error) {

	// 1. Set the initial values
	p := new(Cards)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Cards object
	return p, nil
}

func (p *Cards) processText(text []string) error {
	// Assign values from text

	// 1. Start with no cards in cards
	p.Cards = make([]*Card, 0, len(text))

	// 2. Loop for each line of the text
	for indx, line := range text {

		// 2. Process the line into a card
		pCard, err := NewCard(p.Part2, line)
		if err != nil {
			return fmt.Errorf("error in line %d: %s", indx, err)
		}

		// 3. Save the card
		p.Cards = append(p.Cards, pCard)
	}

	// 4. Return success
	return nil
}

func (p *Cards) PartOne(verbose bool, limit int) string {
	// Returns the solution for part one

	// 1. Start with nothing
	result := 0

	// 2. Loop for all the cards
	for _, pCard := range p.Cards {

		// 3. Accumulate the points
		points := pCard.GetPoints()
		result = result + points
	}

	// 4. Return the solution for part one
	return fmt.Sprint(result)
}

func (p *Cards) PartTwo(verbose bool, limit int) string {
	// Returns the solution for part two

	// 1. Start with current number of cards
	result := len(p.Cards)

	// 2. Loop for all the cards
	for _, pCard := range p.Cards {

		// 3. Accumulate the additional cards
		additional := pCard.GetMore(p.Cards)
		result = result + additional
	}

	// 4. Return the solution for part two
	return fmt.Sprint(result)
}

// ======================================================================
// end                        c a r d s . g o                       end
// ======================================================================
