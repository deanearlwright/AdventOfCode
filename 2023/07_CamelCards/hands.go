// ======================================================================
// Camel Cards
//   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         h a n d s . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 07 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"sort"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const ()

// ======================================================================
//                                                                  Hands
// ======================================================================

// Hands ... Object for Camel Cards
type Hands struct {
	Part2 bool
	Text  []string
	Hands []*Hand
}

// NewHands ... Create a Hands object
func NewHands(part2 bool, text []string) (*Hands, error) {

	// 1. Set the initial values
	p := new(Hands)
	p.Part2 = part2
	p.Text = text

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Hands object
	return p, nil
}

// processText ... Assign values from text
func (p *Hands) processText(text []string) error {

	// 1. Loop for each line of the text
	for indx, line := range text {

		// 2. Create a hand
		hand, err := NewHand(p.Part2, line)
		if err != nil {
			return fmt.Errorf("text line %d: %s", indx, err)
		}

		// 3. Add it in
		p.Hands = append(p.Hands, hand)
	}

	// 4. Return success
	return nil
}

// Sort ... Soft the hands (worst is 0)
func (p *Hands) Sort() {

	// 1. Sort the hands
	sort.Slice(p.Hands, func(i, j int) bool {
		return p.Hands[i].Less(p.Hands[j])
	})
}

// PartOne ... Returns the solution for part one
func (p *Hands) PartOne(verbose bool, limit int) string {

	// 1. Sort the hands
	p.Sort()

	// 2. Start with nothing
	winnings := 0

	// 3. Loop for all the hands
	for indx, hand := range p.Hands {

		// 4. Add to the winnings
		winnings = winnings + (indx+1)*hand.Bid
	}

	// 5. Return the solution for part one
	return fmt.Sprint(winnings)
}

// PartTwo ... Returns the solution for part two
func (p *Hands) PartTwo(verbose bool, limit int) string {

	// 1. Sort the hands
	p.Sort()

	// 2. Start with nothing
	winnings := 0

	// 3. Loop for all the hands
	for indx, hand := range p.Hands {

		// 4. Add to the winnings
		winnings = winnings + (indx+1)*hand.Bid
	}

	// 5. Return the solution for part two
	return fmt.Sprint(winnings)
}

// ======================================================================
// end                         h a n d s . g o                        end
// ======================================================================
