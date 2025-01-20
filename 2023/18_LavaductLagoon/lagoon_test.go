// ======================================================================
// Lavaduct Lagoon
//   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    l a g o o n _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 18, Lavaduct Lagoon

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
	lagoonExampleText = `
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
`
	lagoonPartOneText = lagoonExampleText
	lagoonPartTwoText = lagoonExampleText

	lagoonPartOneResult = "62"
	lagoonPartTwoResult = "952408144115"
)

// ======================================================================
//                                                             TestLagoon
// ======================================================================

// TestLagoonEmptyInit ... Test the default Lagoon creation
func TestLagoonEmptyInit(t *testing.T) {

	// 1. Create default Lagoon object
	obj, err := NewLagoon(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Corners, 0)
	assert.Equal(t, 0, obj.Trench)

	// 3. Check methods
	row, col := nextLoc(0, 0, 'R', 6)
	assert.Equal(t, 0, row)
	assert.Equal(t, 6, col)
	row, col = nextLoc(0, 6, 'D', 5)
	assert.Equal(t, 5, row)
	assert.Equal(t, 6, col)

	assert.Equal(t, 0, obj.ShoelaceArea())
	assert.Equal(t, 1, obj.LagoonArea())

	// Example from https://en.wikipedia.org/wiki/Shoelace_formula
	obj.Corners = [][]int{
		{1, 6},
		{3, 1},
		{7, 2},
		{4, 4},
		{8, 5},
	}
	assert.Equal(t, 16, obj.ShoelaceArea())
}

// TestLagoonTextInit ... Test the Lagoon object creation from text
func TestLagoonTextInit(t *testing.T) {

	// 1. Create Lagoon object from text
	obj, err := NewLagoon(false, fromText(lagoonExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 14)
	assert.Len(t, obj.Corners, 15)
	assert.Equal(t, 38, obj.Trench)

	// 3. Check Methods
	assert.Equal(t, 42, obj.ShoelaceArea())
	assert.Equal(t, 62, obj.LagoonArea())
}

// TestLagoonPartOne ... Test part one example of Lagoon object
func TestLagoonPartOne(t *testing.T) {

	// 1. Create Lagoon object from text
	obj, err := NewLagoon(false, fromText(lagoonPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 14)
	assert.Len(t, obj.Corners, 15)
	assert.Equal(t, 38, obj.Trench)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, lagoonPartOneResult, result)
}

// TestLagoonPartTwo ... Test part two example of Lagoon object
func TestLagoonPartTwo(t *testing.T) {
	// Test part two example of Lagoon object

	// 1. Create Lagoon object from text
	obj, err := NewLagoon(true, fromText(lagoonPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 14)
	assert.Len(t, obj.Corners, 15)
	assert.Equal(t, 6405262, obj.Trench)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, lagoonPartTwoResult, result)
}

// ======================================================================
// end                  l a g o o n _ t e s t . g o                   end
// ======================================================================
