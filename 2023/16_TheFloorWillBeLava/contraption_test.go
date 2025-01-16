// ======================================================================
// The Floor Will Be Lava
//   Advent of Code 2023 Day 16 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    c o n t r a p t i o n _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 16, The Floor Will Be Lava

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
	contraptionExampleText = `
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
`
	contraptionPartOneText = contraptionExampleText
	contraptionPartTwoText = contraptionExampleText

	contraptionPartOneResult = "46"
	contraptionPartTwoResult = "51"
)

// ======================================================================
//                                                        TestContraption
// ======================================================================

// TestContraptionEmptyInit ... Test the default Contraption creation
func TestContraptionEmptyInit(t *testing.T) {

	// 1. Create default Contraption object
	obj, err := NewContraption(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Equal(t, 0, obj.Rows)
	assert.Equal(t, 0, obj.Cols)
	assert.Len(t, obj.Tiles, 0)
	assert.Len(t, obj.Grid, 0)
}

// TestContraptionTextInit ... Test the Contraption object creation from text
func TestContraptionTextInit(t *testing.T) {

	// 1. Create Contraption object from text
	obj, err := NewContraption(false, fromText(contraptionExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Tiles, 10)
	assert.Len(t, obj.Grid, 10)

	// 3. Check methods
	obj.Beam(0, 0, EAST)
	assert.Equal(t, 46, obj.Energized())

	assert.Equal(t, 51, obj.MostTiles())
}

// TestContraptionPartOne ... Test part one example of Contraption object
func TestContraptionPartOne(t *testing.T) {

	// 1. Create Contraption object from text
	obj, err := NewContraption(false, fromText(contraptionPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Tiles, 10)
	assert.Len(t, obj.Grid, 10)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, contraptionPartOneResult, result)
}

// TestContraptionPartTwo ... Test part two example of Contraption object
func TestContraptionPartTwo(t *testing.T) {
	// Test part two example of Contraption object

	// 1. Create Contraption object from text
	obj, err := NewContraption(true, fromText(contraptionPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Equal(t, 10, obj.Rows)
	assert.Equal(t, 10, obj.Cols)
	assert.Len(t, obj.Tiles, 10)
	assert.Len(t, obj.Grid, 10)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, contraptionPartTwoResult, result)
}

// ======================================================================
// end             c o n t r a p t i o n _ t e s t . g o              end
// ======================================================================
