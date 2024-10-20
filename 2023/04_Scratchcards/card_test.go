// ======================================================================
// Scratchcards
//   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c a r d _ t e s t . g o
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
	cardExampleText = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
)

// ======================================================================
//                                                              TestCard
// ======================================================================

func TestCardEmptyInit(t *testing.T) {
	// Test the default Card creation

	// 1. Create default Card object
	obj, err := NewCard(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Number)
	assert.Len(t, obj.Winning, 0)
	assert.Len(t, obj.Have, 0)
	assert.Equal(t, -1, obj.Matches)
}

func TestCardTextInit(t *testing.T) {
	// Test the Card object creation from text

	// 1. Create Card object from text
	obj, err := NewCard(false, cardExampleText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, 48, len(obj.Text))
	assert.Equal(t, 1, obj.Number)
	assert.Len(t, obj.Winning, 5)
	assert.Len(t, obj.Have, 8)
	assert.Equal(t, -1, obj.Matches)

	// 3. Check the methods
	assert.Equal(t, 4, obj.GetMatches())
	assert.Equal(t, 4, obj.GetMatches())
	assert.Equal(t, 8, obj.GetPoints())
}

// ======================================================================
// end                  c a r d _ t e s t . g o                   end
// ======================================================================
