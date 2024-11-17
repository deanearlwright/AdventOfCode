// ======================================================================
// HotSprings
//   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s e e n _ t e s t . g o
// ======================================================================
// Test Seen for Advent of Code 2023 day 12, HotSprings

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
//                                                               TestSeen
// ======================================================================

// TestSeenEmptyInit ... Test the default Seen creation
func TestSeenEmptyInit(t *testing.T) {

	// 1. Create default Seen object
	obj, err := NewSeen(false)
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Observations, 17)

	// 3. Check methods
	assert.Equal(t, 1, obj.FindObservation("? 1"))
	assert.Equal(t, 2, obj.FindObservation("?? 1"))
	assert.Equal(t, -1, obj.FindObservation("?????? 1"))
	assert.NoError(t, obj.AddObservation("?? 1", 2))
	assert.ErrorContains(t, obj.AddObservation("?? 1", 3), "different values")
}

// ======================================================================
// end                      s e e n _ t e s t. g o                    end
// ======================================================================
