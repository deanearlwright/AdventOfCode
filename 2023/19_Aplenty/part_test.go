// ======================================================================
// Aplenty
//   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    p a r t _ t e s t . g o
// ======================================================================
// Test Part for Advent of Code 2023 day 19, Aplenty

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
	partText = "{x=787,m=2655,a=1222,s=2876}"
)

// ======================================================================
//                                                               TestPart
// ======================================================================

// TestPartEmptyInit ... Test the default Part creation
func TestPartEmptyInit(t *testing.T) {

	// 1. Create default Part object
	obj, err := NewPart(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Categories, 4)
	assert.Equal(t, 0, obj.Categories[0])
	assert.Equal(t, 0, obj.Categories[1])
	assert.Equal(t, 0, obj.Categories[2])
	assert.Equal(t, 0, obj.Categories[3])
}

// TestPartTextInit ... Test the Part object creation from text
func TestPartTextInit(t *testing.T) {

	// 1. Create default Part object
	obj, err := NewPart(false, partText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(partText))
	assert.Equal(t, 787, obj.Categories[0])
	assert.Equal(t, 2655, obj.Categories[1])
	assert.Equal(t, 1222, obj.Categories[2])
	assert.Equal(t, 2876, obj.Categories[3])

	// 3. Check methods
	assert.Equal(t, 7540, obj.Rating())
	assert.Equal(t, 0, obj.GetValue("?"))
	assert.Equal(t, 787, obj.GetValue("x"))
	assert.Equal(t, 2655, obj.GetValue("m"))
	assert.Equal(t, 1222, obj.GetValue("a"))
	assert.Equal(t, 2876, obj.GetValue("s"))
}

// ======================================================================
// end                      p a r t _ t e s t. g o                    end
// ======================================================================
