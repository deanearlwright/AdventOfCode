// ======================================================================
// Cube Conundrum
//   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    d r a w _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 02, Cube Conundrum

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
	drawExampleText  = "1 blue, 2 green"
	drawExampleFalse = "10 blue, 20 green, 99 red"
)

// ======================================================================
//                                                               TestDraw
// ======================================================================

func TestDrawEmptyInit(t *testing.T) {
	// Test the default Draw creation

	// 1. Create default Draw object
	obj, err := NewDraw(false, "")
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Colors, 0)

	// 3. Make sure the methods returns the expected results
	assert.Equal(t, 0, obj.Count("red"))
	assert.Equal(t, 0, obj.Count("green"))
	assert.Equal(t, 0, obj.Count("blue"))
	assert.Equal(t, true, obj.IsLegal())
}

func TestDrawTextInit(t *testing.T) {
	// Test the Draw object creation from text

	// 1. Create Draw object from text
	obj, err := NewDraw(false, drawExampleText)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, 15, len(obj.Text))
	assert.Equal(t, 2, len(obj.Colors))

	// 3. Make sure the methods returns the expected results
	assert.Equal(t, 0, obj.Count("red"))
	assert.Equal(t, 2, obj.Count("green"))
	assert.Equal(t, 1, obj.Count("blue"))
	assert.Equal(t, true, obj.IsLegal())
}

func TestDrawTextFalse(t *testing.T) {
	// Test the Draw object creation from text

	// 1. Create Draw object from text
	obj, err := NewDraw(false, drawExampleFalse)
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, 25, len(obj.Text))
	assert.Equal(t, 3, len(obj.Colors))

	// 3. Make sure the methods returns the expected results
	assert.Equal(t, 99, obj.Count("red"))
	assert.Equal(t, 20, obj.Count("green"))
	assert.Equal(t, 10, obj.Count("blue"))
	assert.Equal(t, false, obj.IsLegal())
}

// ======================================================================
// end                    d r a w _ t e s t . g o                     end
// ======================================================================
