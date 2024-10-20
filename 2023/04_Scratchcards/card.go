// ======================================================================
// Scratchcards
//   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         c a r d . g o
// ======================================================================
// A solver for the Advent of Code 2023 Day 04 puzzle

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	prefix = "Card "
	colon  = ":"
	vbar   = "|"
	numsep = " "
)

// ======================================================================
//                                                                  Card
// ======================================================================

// Object for Scratchcards

type Card struct {
	Part2   bool
	Text    string
	Number  int
	Winning []int
	Have    []int
	Matches int
	More    int
}

func NewCard(part2 bool, text string) (*Card, error) {

	// 1. Set the initial values
	p := new(Card)
	p.Part2 = part2
	p.Text = text
	p.Matches = -1
	p.More = -1

	// 2. Process text (if any)
	if len(p.Text) > 0 {
		err := p.processText(p.Text)
		if err != nil {
			return nil, err
		}
	}

	// 3. Return the new Card object
	return p, nil
}

func (p *Card) processText(text string) error {
	// Assign values from text

	// 1. Make sure the card is a card
	if !strings.HasPrefix(text, prefix) {
		return fmt.Errorf("does not start with '%s': %s", prefix, text)
	}
	if !strings.Contains(text, colon) {
		return fmt.Errorf("does not a '%s': %s", colon, text)
	}
	if !strings.Contains(text, vbar) {
		return fmt.Errorf("does not a '%s': %s", vbar, text)
	}

	// 2. Get the card number
	trimed := strings.TrimPrefix(text, prefix)
	number, numbers, _ := strings.Cut(trimed, colon)
	num, err := strconv.Atoi(strings.TrimSpace(number))
	if err != nil {
		return fmt.Errorf("unable to process card number '%s' from %s", number, text)
	}
	p.Number = num

	// 3. Split the number lists
	winning, have, _ := strings.Cut(numbers, vbar)

	// 4. Get the winning numbers
	winningints, err := stringToInts(winning)
	if err != nil {
		return fmt.Errorf("unable to process winning numbers from %s: %s", text, err)
	}
	p.Winning = winningints

	// 5. Get the numbers we have
	haveints, err := stringToInts(have)
	if err != nil {
		return fmt.Errorf("unable to process your numbers from %s: %s", text, err)
	}
	p.Have = haveints

	// 6. Return success
	return nil
}

func (p *Card) GetMatches() int {
	// Return the number of matches on the card

	// 1. If we already know it, return it
	if p.Matches >= 0 {
		return p.Matches
	}

	// 2. Start with nothing
	result := 0

	// 3. Loop for all of the numbers we have
	for _, have := range p.Have {

		// 4. If this is a winning number, increment count
		if slices.Contains(p.Winning, have) {
			result = result + 1
		}
	}

	// 5. Remember the number of matches and return same
	p.Matches = result
	return result
}

func (p *Card) GetPoints() int {
	// Return the Point value of the card
	if p.GetMatches() == 0 {
		return 0
	}
	return int(math.Pow(2, float64(p.GetMatches()-1)))
}

func (p *Card) GetMore(cards []*Card) int {
	// Return the number of addition cards

	// 1. If we already know, the number return it
	if p.More >= 0 {
		return p.More
	}

	// 2. Start with the additional cards for this card's matches
	additional := p.GetMatches()

	// 3. Loop for the number of additional cards
	for knt := 0; knt < p.GetMatches(); knt = knt + 1 {
		index := p.Number + knt

		// 4. Get may get additional cards for this one
		additional = additional + cards[index].GetMore(cards)
	}

	// 5. Remember and return the number of additional cards
	// println("Number of additinal cards for card", p.Number, "is", additional)
	p.More = additional
	return additional
}

func stringToInts(text string) ([]int, error) {
	// Convert strings seperated by spaces to array of ints

	// 1. Start with nothing
	result := make([]int, 0, 1+len(text)/2)

	// 2. Get an array of strings
	numbers := strings.Split(text, numsep)

	// 3. Loop for all the elements in the string array
	for _, number := range numbers {
		number = strings.TrimSpace(number)
		if number == "" {
			continue
		}

		// 4. Convert the string into a number and save it
		num, err := strconv.Atoi(number)
		if err != nil {
			return nil, fmt.Errorf("unable to process number '%s' from %s", number, text)
		}
		result = append(result, num)
	}

	// Return success
	return result, nil
}

// ======================================================================
// end                          c a r d . g o                         end
// ======================================================================
