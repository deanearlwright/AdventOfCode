// ======================================================================
// Gear Ratios
//   Advent of Code 2023 Day 03 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    s c h e m a t i c _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 03, Gear Ratios

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
	schematicExampleText = `467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
`
	schematicPartOneText = schematicExampleText
	schematicPartTwoText = schematicExampleText

	schematicPartOneResult = "4361"
	schematicPartTwoResult = "467835"
)

// ======================================================================
//                                                          TestSchematic
// ======================================================================

func TestSchematicEmptyInit(t *testing.T) {
	// Test the default Schematic creation

	// 1. Create default Schematic object
	obj, err := NewSchematic(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 0)
	assert.Len(t, obj.Numbers, 0)
}

func TestSchematicTextInit(t *testing.T) {
	// Test the Schematic object creation from text

	// 1. Create Schematic object from text
	obj, err := NewSchematic(false, fromText(schematicExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 10)
	assert.Len(t, obj.Numbers, 10)
	assert.Len(t, obj.Symbols, 6)
}

func TestSchematicPartOne(t *testing.T) {
	// Test part one example of Schematic object

	// 1. Create Schematic object from text
	obj, err := NewSchematic(false, fromText(schematicPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(obj.Numbers))

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, schematicPartOneResult, result)
}

func TestSchematicPartTwo(t *testing.T) {
	// Test part two example of Schematic object

	// 1. Create Schematic object from text
	obj, err := NewSchematic(true, fromText(schematicPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Equal(t, len(obj.Text), len(obj.Numbers))

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, schematicPartTwoResult, result)
}

// ======================================================================
// end                  s c h e m a t i c _ t e s t . g o                   end
// ======================================================================
