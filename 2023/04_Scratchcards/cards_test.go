// ======================================================================
// Scratchcards
//   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c a r d s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 04, Scratchcards

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
	cardsExampleText = `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
`
	cardsPartOneText = cardsExampleText
	cardsPartTwoText = cardsExampleText

	cardsPartOneResult = "13"
	cardsPartTwoResult = "30"
)

// ======================================================================
//                                                              TestCards
// ======================================================================

func TestCardsEmptyInit(t *testing.T) {
	// Test the default Cards creation

	// 1. Create default Cards object
	obj, err := NewCards(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Cards, 0)
}

func TestCardsTextInit(t *testing.T) {
	// Test the Cards object creation from text

	// 1. Create Cards object from text
	obj, err := NewCards(false, fromText(cardsExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 6)
	assert.Len(t, obj.Cards, 6)
}

func TestCardsPartOne(t *testing.T) {
	// Test part one example of Cards object

	// 1. Create Cards object from text
	obj, err := NewCards(false, fromText(cardsPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 6)
	assert.Len(t, obj.Cards, 6)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, cardsPartOneResult, result)
}

func TestCardsPartTwo(t *testing.T) {
	// Test part two example of Cards object

	// 1. Create Cards object from text
	obj, err := NewCards(true, fromText(cardsPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 6)
	assert.Len(t, obj.Cards, 6)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, cardsPartTwoResult, result)
}

// ======================================================================
// end                  c a r d s _ t e s t . g o                   end
// ======================================================================
