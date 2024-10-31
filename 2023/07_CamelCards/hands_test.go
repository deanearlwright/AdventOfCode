// ======================================================================
// Camel Cards
//   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    h a n d s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 07, Camel Cards

package main

// ----------------------------------------------------------------------
//                                                                imports
// ----------------------------------------------------------------------
import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// ----------------------------------------------------------------------
//
//	constants
//
// ----------------------------------------------------------------------
const (
	handsExampleText = `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
`
	handsPartOneText = handsExampleText
	handsPartTwoText = handsExampleText

	handsPartOneResult = "6440"
	handsPartTwoResult = "5905"
)

// ======================================================================
//                                                              TestHands
// ======================================================================

// TestHandsEmptyInit ... Test the default Hands creation
func TestHandsEmptyInit(t *testing.T) {

	// 1. Create default Hands object
	obj, err := NewHands(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Hands, 0)
}

// TestHandsTextInit ... Test the Hands object creation from text
func TestHandsTextInit(t *testing.T) {

	// 1. Create Hands object from text
	obj, err := NewHands(false, fromText(handsExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Hands, 5)

	// 3. Check methods
	obj.Sort()
	assert.Len(t, obj.Hands, 5)
	assert.Equal(t, obj.Hands[0].Bid, 765)
	assert.Equal(t, obj.Hands[1].Bid, 220)
	assert.Equal(t, obj.Hands[2].Bid, 28)
	assert.Equal(t, obj.Hands[3].Bid, 684)
	assert.Equal(t, obj.Hands[4].Bid, 483)
}

// TestHandsPartOne ... Test part one example of Hands object
func TestHandsPartOne(t *testing.T) {

	// 1. Create Hands object from text
	obj, err := NewHands(false, fromText(handsPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Hands, 5)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, handsPartOneResult, result)
}

// TestHandsPartTwo ... Test part two example of Hands object
func TestHandsPartTwo(t *testing.T) {
	// Test part two example of Hands object

	// 1. Create Hands object from text
	obj, err := NewHands(true, fromText(handsPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Len(t, obj.Hands, 5)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, handsPartTwoResult, result)
}

// ======================================================================
// end                   h a n d s _ t e s t . g o                    end
// ======================================================================
