// ======================================================================
// Clumsy Crucible
//   Advent of Code 2023 Day 17 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c r u c i b l e s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 17, Clumsy Crucible

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
	cruciblesExampleText = `
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
`
	cruciblesExampleTwo = `
111111111111
999999999991
999999999991
999999999991
999999999991
`
	cruciblesPartOneText = cruciblesExampleText
	cruciblesPartTwoText = cruciblesExampleText

	cruciblesPartOneResult = "102"
	cruciblesPartTwoResult = "94"
)

// ======================================================================
//                                                          TestCrucibles
// ======================================================================

// TestCruciblesEmptyInit ... Test the default Crucibles creation
func TestCruciblesEmptyInit(t *testing.T) {

	// 1. Create default Crucibles object
	obj, err := NewCrucibles(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Rows)
	assert.Equal(t, 0, obj.Cols)
	assert.Len(t, obj.Loss, 0)

	// 3. Check methods
	state := heatEncode(1, 6, 'E', 2, 7)
	assert.Equal(t, 7023001006, state)
	row, col, dir, str, heat := heatDecode(state)
	assert.Equal(t, 1, row)
	assert.Equal(t, 6, col)
	assert.Equal(t, 'E', dir)
	assert.Equal(t, 2, str)
	assert.Equal(t, 7, heat)
	assert.Equal(t, state, heatEncode(row, col, dir, str, heat))

	state = heatEncode(12, 34, 'E', 56, 78)
	assert.Equal(t, 78563012034, state)
	row, col, dir, str, heat = heatDecode(state)
	assert.Equal(t, 12, row)
	assert.Equal(t, 34, col)
	assert.Equal(t, 'E', dir)
	assert.Equal(t, 56, str)
	assert.Equal(t, 78, heat)
	assert.Equal(t, state, heatEncode(row, col, dir, str, heat))

	nextRow, nextCol := nextLoc(5, 8, 'E')
	assert.True(t, equalLoc(nextRow, nextCol, []int{5, 9}))
	nextRow, nextCol = nextLoc(5, 8, 'W')
	assert.True(t, equalLoc(nextRow, nextCol, []int{5, 7}))
	nextRow, nextCol = nextLoc(5, 8, 'N')
	assert.True(t, equalLoc(nextRow, nextCol, []int{4, 8}))
	nextRow, nextCol = nextLoc(5, 8, 'S')
	assert.True(t, equalLoc(nextRow, nextCol, []int{6, 8}))
}

// TestCruciblesTextInit ... Test the Crucibles object creation from text
func TestCruciblesTextInit(t *testing.T) {

	// 1. Create Crucibles object from text
	obj, err := NewCrucibles(false, fromText(cruciblesExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 13)
	assert.Equal(t, 13, obj.Rows)
	assert.Equal(t, 13, obj.Cols)
	assert.Len(t, obj.Loss, 13)

	// 3. Check Methods
	assert.Equal(t, 2, obj.HeatDelta(0, 0))
	assert.Equal(t, 5, obj.HeatDelta(1, 3))
	assert.Equal(t, 3, obj.HeatDelta(12, 12))
	assert.Equal(t, -1, obj.HeatDelta(12, 14))

	assert.Equal(t, []rune{'E'}, obj.NextDirections('E', false, false))
	assert.Equal(t, []rune{}, obj.NextDirections('E', false, true))
	assert.Equal(t, []rune{'E', 'N', 'S'}, obj.NextDirections('E', true, false))
	assert.Equal(t, []rune{'N', 'S'}, obj.NextDirections('E', true, true))

	assert.Equal(t, 102, obj.MinHeatLoss())
}

// TestCruciblesTextTwo ... Test the Crucibles object creation from text
func TestCruciblesTextTwo(t *testing.T) {

	// 1. Create Crucibles object from text
	obj, err := NewCrucibles(true, fromText(cruciblesExampleTwo))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 5)
	assert.Equal(t, 5, obj.Rows)
	assert.Equal(t, 12, obj.Cols)
	assert.Len(t, obj.Loss, 5)

	// 3. Check Methods
	assert.Equal(t, 71, obj.MinHeatLoss())
}

// TestCruciblesPartOne ... Test part one example of Crucibles object
func TestCruciblesPartOne(t *testing.T) {

	// 1. Create Crucibles object from text
	obj, err := NewCrucibles(false, fromText(cruciblesPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 13)
	assert.Equal(t, 13, obj.Rows)
	assert.Equal(t, 13, obj.Cols)
	assert.Len(t, obj.Loss, 13)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, cruciblesPartOneResult, result)
}

// TestCruciblesPartTwo ... Test part two example of Crucibles object
func TestCruciblesPartTwo(t *testing.T) {
	// Test part two example of Crucibles object

	// 1. Create Crucibles object from text
	obj, err := NewCrucibles(true, fromText(cruciblesPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 13)
	assert.Equal(t, 13, obj.Rows)
	assert.Equal(t, 13, obj.Cols)
	assert.Len(t, obj.Loss, 13)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, cruciblesPartTwoResult, result)
}

// ======================================================================
// end               c r u c i b l e s _ t e s t . g o                end
// ======================================================================
