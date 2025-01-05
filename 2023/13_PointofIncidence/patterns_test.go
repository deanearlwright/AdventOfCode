// ======================================================================
// Point Of Incidence
//   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
//
// go implementation by Dr. Dean Earl Wright III
// ======================================================================

// ======================================================================
//                    p a t t e r n s _ t e s t . g o
// ======================================================================
// Test solver for Advent of Code 2023 day 13, Point Of Incidence

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
	patternsExampleText = `
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
`
	patternsPartOneText = patternsExampleText
	patternsPartTwoText = patternsExampleText

	patternsPartOneResult = "405"
	patternsPartTwoResult = "400"
)

// ======================================================================
//                                                           TestPatterns
// ======================================================================

// TestPatternsEmptyInit ... Test the default Patterns creation
func TestPatternsEmptyInit(t *testing.T) {

	// 1. Create default Patterns object
	obj, err := NewPatterns(false, fromText(""))
	assert.NoError(t, err)

	// 2. Make sure it has the default values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 1)
	assert.Len(t, obj.Patterns, 0)
}

// TestPatternsTextInit ... Test the Patterns object creation from text
func TestPatternsTextInit(t *testing.T) {

	// 1. Create Patterns object from text
	obj, err := NewPatterns(false, fromText(patternsExampleText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 17)
	assert.Len(t, obj.Patterns, 2)
}

// TestPatternsPartOne ... Test part one example of Patterns object
func TestPatternsPartOne(t *testing.T) {

	// 1. Create Patterns object from text
	obj, err := NewPatterns(false, fromText(patternsPartOneText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.False(t, obj.Part2)
	assert.Len(t, obj.Text, 17)
	assert.Len(t, obj.Patterns, 2)

	// 3. Make sure it returns the expected solution
	result := obj.PartOne(false, 0)
	assert.Equal(t, patternsPartOneResult, result)
}

// TestPatternsPartTwo ... Test part two example of Patterns object
func TestPatternsPartTwo(t *testing.T) {
	// Test part two example of Patterns object

	// 1. Create Patterns object from text
	obj, err := NewPatterns(true, fromText(patternsPartTwoText))
	assert.NoError(t, err)

	// 2. Make sure it has the expected values
	assert.True(t, obj.Part2)
	assert.Len(t, obj.Text, 17)
	assert.Len(t, obj.Patterns, 2)

	// 3. Make sure it returns the expected solution
	result := obj.PartTwo(false, 0)
	assert.Equal(t, patternsPartTwoResult, result)
}

// ======================================================================
// end                p a t t e r n s _ t e s t . g o                 end
// ======================================================================
