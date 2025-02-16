// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    r a n g e s _ t e s t . g o
// ======================================================================
// Test Ranges for Advent of Code 2023 day 19, Aplenty

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
const ()

// ======================================================================
//                                                             TestRanges
// ======================================================================

// TestRangesEmptyInit ... Test the default Ranges creation
func TestRangesEmptyInit(t *testing.T) {

	// 1. Create default Ranges object
	obj, err := NewRanges(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Categories, 4)
	assert.Equal(t, obj.Categories[0].Min, 1)
	assert.Equal(t, obj.Categories[0].Max, 4000)
	assert.Equal(t, obj.Categories[1].Min, 1)
	assert.Equal(t, obj.Categories[1].Max, 4000)
	assert.Equal(t, obj.Categories[2].Min, 1)
	assert.Equal(t, obj.Categories[2].Max, 4000)
	assert.Equal(t, obj.Categories[3].Min, 1)
	assert.Equal(t, obj.Categories[3].Max, 4000)
}

// ======================================================================
// end                    r a n g e s _ t e s t. g o                  end
// ======================================================================
