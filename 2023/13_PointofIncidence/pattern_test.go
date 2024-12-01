// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    p a t t e r n _ t e s t . g o
// ======================================================================
// Test Pattern for Advent of Code 2023 day 13, Point Of Incidence

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
	patternText = `#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
`
)

// ======================================================================
//                                                            TestPattern
// ======================================================================

// TestPatternEmptyInit ... Test the default Pattern creation
func TestPatternEmptyInit(t *testing.T) {

	// 1. Create default Pattern object
	obj, err := NewPattern(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
}

// TestPatternTextInit ... Test the Pattern object creation from text
func TestPatternTextInit(t *testing.T) {

	// 1. Create default Pattern object
	obj, err := NewPattern(false, patternText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(patternText))
}

// ======================================================================
// end                   p a t t e r n _ t e s t. g o                 end
// ======================================================================
