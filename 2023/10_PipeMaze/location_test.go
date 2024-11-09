// ======================================================================
// Pipe Maze
//   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    l o c a t i o n _ t e s t . g o
// ======================================================================
// Test Location for Advent of Code 2023 day 10, Pipe Maze

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
//                                                           TestLocation
// ======================================================================

// TestLocation ... Test the Location creation
func TestLocation(t *testing.T) {

	// 1. Create default Location object
	obj := NewLocation(3, 4)

	// 2. Make sure it has the default values
	assert.Equal(t, 3, obj.Row)
	assert.Equal(t, 4, obj.Col)

	// 3. Check methods
	copy := obj.Copy()
	assert.Equal(t, 3, copy.Row)
	assert.Equal(t, 4, copy.Col)
	assert.True(t, obj.Equal(copy))
	copy.Row = 2
	assert.Equal(t, 2, copy.Row)
	assert.Equal(t, 4, copy.Col)
	assert.Equal(t, 3, obj.Row)
	assert.Equal(t, 4, obj.Col)
	assert.False(t, obj.Equal(copy))
}

// ======================================================================
// end                  l o c a t i o n _ t e s t . g o               end
// ======================================================================
