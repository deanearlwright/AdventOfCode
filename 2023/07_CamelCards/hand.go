// ======================================================================
// Camel Cards
//   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                         h a n d . g o
// ======================================================================
// Hand for the Advent of Code 2023 Day 07 puzzle

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
const (
	handFive   = "Five of a kind"
	handFour   = "Four of a kind"
	handFull   = "Full house"
	handThree  = "Three of a kind"
	handTwo    = "Two pair"
	handOne    = "One pair"
	handHigh   = "High card"
	handNone   = "No cards"
	cardOrder1 = "AKQJT98765432"
	cardOrder2 = "AKQT98765432J"
	joker      = "J"
)

var (
	handType = map[string]int{
		handFive:  6,
		handFour:  5,
		handFull:  4,
		handThree: 3,
		handTwo:   2,
		handOne:   1,
		handHigh:  0,
		handNone:  0,
	}
)

// ======================================================================
//                                                                   Hand
// ======================================================================

// Hand ... Object for Camel Cards
type Hand struct {
	Part2 bool
	Text  string
	Cards string
	Bid   int
	Type  int
}

// NewHand ... Create a Hand object
func NewHand(part2 bool, text string) (*Hand, error) {
	// Hand Object for Camel Cards

	// 1. Set the initial values
	p := new(Hand)
	p.Part2 = part2
	p.Text = strings.TrimSpace(text)

	// 2. Set the Cards and Bid
	if len(p.Text) > 0 {
		fields := strings.Fields(p.Text)
		if len(fields) != 2 {
			return nil, fmt.Errorf("hand '%s' should have two values not %d", p.Text, len(fields))
		}
		p.Cards = fields[0]
		bid, err := strconv.Atoi(fields[1])
		if err != nil {
			return nil, fmt.Errorf("invalid bid value '%s' for hand '%s", fields[2], p.Text)
		}
		p.Bid = bid
	}

	// 3. Determine the type of the hand
	p.Type = p.HandType()

	// 4. Return success
	return p, nil
}

// HandType ... Returns the numerical hand type
func (p *Hand) HandType() int {

	// 1. Determine the type of hand
	hType := p.HandType1()
	if p.Part2 {
		hType = p.HandType2()
	}

	// 2. Return the numeric type
	return handType[hType]
}

// HandType1 ... Returns the hand type (No Jokers)
func (p *Hand) HandType1() string {

	// 1. Really should have some cards
	if len(p.Cards) == 0 {
		return handNone
	}

	// 2. Get the count of the cards and the counts of the counts
	countCards := p.CountCards()
	countCounts := CountCounts(countCards)

	// 3. Do we have Five of a kind?
	if countCounts[5] > 0 {
		return handFive
	}

	// 4. Do we have Four of a kind?
	if countCounts[4] > 0 {
		return handFour
	}

	// 5. Do we have a Full house?
	if countCounts[3] > 0 && countCounts[2] > 0 {
		return handFull
	}

	// 6. Do we have Three of a kind?
	if countCounts[3] > 0 {
		return handThree
	}

	// 7. Do we have Two pair?
	if countCounts[2] > 1 {
		return handTwo
	}

	// 8. Do we have One pair?
	if countCounts[2] > 0 {
		return handOne
	}

	// 9. Else it is High card
	return handHigh
}

// HandType2 ... Returns the hand type (With Jokers)
func (p *Hand) HandType2() string {

	// 1. If no Jokers, just use the regular handtype
	if !strings.Contains(p.Cards, joker) {
		return p.HandType1()
	}

	// 2. Start with a low hand
	result := handHigh
	originalCards := p.Cards

	// 3. Loop for the possible replacements for the Joker
	for _, card := range cardOrder1 {
		replacement := string(card)
		if replacement == joker {
			continue
		}

		// 4. Replace the jokers
		p.Cards = strings.ReplaceAll(originalCards, joker, replacement)

		// 5. Get the type of this modified hand
		jokerType := p.HandType1()

		// 6. If this better than what we had, save it
		if handType[jokerType] > handType[result] {
			result = jokerType
		}
	}

	// 7. Return the best hand type using Jokers
	p.Cards = originalCards
	return result
}

// CountCards ... Returns the number of each card
func (p *Hand) CountCards() map[string]int {

	// 1. Start a map for the cards
	counts := make(map[string]int, len(cardOrder1))
	for indx := 0; indx < len(cardOrder1); indx = indx + 1 {
		card := string(cardOrder1[indx])
		counts[card] = 0
	}

	// 2. Loop for all the cards in the hand
	for indx := 0; indx < len(p.Cards); indx = indx + 1 {
		card := string(p.Cards[indx])

		// 3. Increment the count of the card
		counts[card] = counts[card] + 1
	}

	// 4. Return the counts of each of the cards
	return counts
}

// Less ... Returns true of p's hand is less than o's
func (p *Hand) Less(o *Hand) bool {

	// 1. Compare the rank of the hand types
	if p.Type < o.Type {
		return true
	}
	if p.Type > o.Type {
		return false
	}

	// 2. Compare the hands card by card
	for indx := 0; indx < len(p.Cards); indx = indx + 1 {

		// 3. If the cards are not equal, return true or false
		if p.CardLess(o, indx) {
			return true
		}
		if o.CardLess(p, indx) {
			return false
		}
	}

	// 3. Should never reach error
	fmt.Printf("unexpected equality between '%s' %d and '%s' %d\n", p.Cards, p.Type, o.Cards, o.Type)
	return true
}

// CardLess ... Return true if the indx'th card of p is less than the one from o
func (p *Hand) CardLess(o *Hand, indx int) bool {

	// 1. Return true if bad indx
	if indx < 0 || indx >= len(p.Cards) || indx >= len(o.Cards) {
		fmt.Printf("unexpected index %d for '%s' and '%s'\n", indx, p.Cards, o.Cards)
		return true
	}

	// 2. What are we using to rank the cards?
	order := cardOrder1
	if p.Part2 {
		order = cardOrder2
	}

	// 3. Get the order of the cards
	oCard := string(o.Cards[indx])
	oOrder := strings.Index(order, oCard)
	if oOrder == -1 {
		fmt.Printf("unexpected card '%s' at index %d of '%s', not in '%s'", oCard, indx, o.Cards, order)
		return true
	}
	pCard := string(p.Cards[indx])
	pOrder := strings.Index(order, pCard)
	if pOrder == -1 {
		fmt.Printf("unexpected card '%s' at index %d of '%s', not in '%s'", pCard, indx, p.Cards, order)
		return true
	}

	// 4. Return difference pCard to oCard (note order string is reversed)
	return pOrder > oOrder
}

// CountCounts ... Return the count of counts
func CountCounts(countCards map[string]int) map[int]int {

	// 1. Start all zeroes
	counts := make(map[int]int, 6)
	for indx := 0; indx < 6; indx = indx + 1 {
		counts[indx] = 0
	}

	// 2. Loop for the count of each card
	for indx := 0; indx < len(cardOrder1); indx = indx + 1 {
		card := string(cardOrder1[indx])
		count := countCards[card]

		// 3. Increment the count of the counts
		counts[count] = counts[count] + 1
	}

	// 4. Return the count of the counts
	return counts
}

// ======================================================================
// end                          h a n d . g o                         end
// ======================================================================
